# Intraday State

- Generated at: `2026-07-28T22:56:34+08:00`
- Market time ET: `2026-07-28T10:56:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 16, 'manual_confirm_candidate': 4, 'below_opening_15m_low': 14, 'price_stale_or_missing': 1, 'below_vwap': 2, 'spread_too_wide_or_missing': 19}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 674.255 |  | 671.5623 | 0.401 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| SOXX | semiconductor_index | 490.27 |  | 488.4001 | 0.3829 | 497.64 | 485.42 | 0.0714 | watch_only | none |
| SMH | semiconductor_index | 528.52 |  | 525.3214 | 0.6089 | 533.01 | 523.325 | 0.0454 | watch_only | none |
| SPY | market_regime | 739.715 |  | 737.7935 | 0.2604 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.235 |  | 194.508 | 1.402 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.41 |  | 375.748 | 0.9746 | 378.64 | 371.57 | 0.1977 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 739.715 |  | 737.7935 | 0.2604 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 118.52 |  | 115.943 | 2.2227 | 117.17 | 115.25 | 0.1097 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 739.715 |  | 737.7935 | 0.2604 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 292.11 |  | 291.6314 | 0.1641 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| 3 | KLAC | semiconductor_equipment | 190.31 |  | 189.9763 | 0.1756 | 194.96 | 189.48 | 0.1629 | watch_only | none |
| 4 | SMH | semiconductor_index | 528.52 |  | 525.3214 | 0.6089 | 533.01 | 523.325 | 0.0454 | watch_only | none |
| 5 | SOXX | semiconductor_index | 490.27 |  | 488.4001 | 0.3829 | 497.64 | 485.42 | 0.0714 | watch_only | none |
| 6 | QQQ | market_regime | 674.255 |  | 671.5623 | 0.401 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 328.97 |  | 327.3587 | 0.4922 | 330.21 | 324.97 | 0.0395 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 396.53 |  | 394.8889 | 0.4156 | 400.09 | 392.355 | 0.0454 | watch_only | none |
| 9 | HPE | ai_server_oem | 44.455 |  | 44.1211 | 0.7567 | 46.19 | 44.33 | 0.09 | watch_only | none |
| 10 | TSM | foundry | 386.57 |  | 384.715 | 0.4822 | 390.46 | 382.495 | 0.3234 | watch_only | none |
| 11 | MU | memory_hbm_storage | 817.63 |  | 811.5603 | 0.7479 | 846.4 | 813.91 | 0.1737 | watch_only | none |
| 12 | TT | data_center_power_cooling | 466.615 |  | 464.066 | 0.5493 | 477.73 | 460.77 | 0.1886 | watch_only | none |
| 13 | AVGO | custom_silicon_networking | 379.41 |  | 375.748 | 0.9746 | 378.64 | 371.57 | 0.1977 | buy_precheck_manual_confirm | none |
| 14 | NVDA | ai_accelerator | 197.235 |  | 194.508 | 1.402 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 15 | JCI | data_center_power_cooling | 138.17 |  | 137.8084 | 0.2624 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ARM | ai_accelerator | 245.17 |  | 244.6147 | 0.227 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | COHU | semiconductor_test_packaging | 42.72 |  | 42.6573 | 0.147 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SMCI | ai_server_oem | 27.93 |  | 27.6792 | 0.9061 | 28.86 | 27.59 | 0.0358 | watch_only | none |
| 19 | LIN | industrial_gases | 518.825 |  | 518.6774 | 0.0285 | 518.6 | 511.495 | 4.2384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CORZ | high_beta_ai_infrastructure | 20.175 |  | 19.9509 | 1.1234 | 20.97 | 19.755 | 0.0991 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.235 |  | 194.508 | 1.402 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.41 |  | 375.748 | 0.9746 | 378.64 | 371.57 | 0.1977 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 739.715 |  | 737.7935 | 0.2604 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 118.52 |  | 115.943 | 2.2227 | 117.17 | 115.25 | 0.1097 | buy_precheck_manual_confirm | none |
| 5 | LIN | industrial_gases | 518.825 |  | 518.6774 | 0.0285 | 518.6 | 511.495 | 4.2384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | TSM | foundry | 386.57 |  | 384.715 | 0.4822 | 390.46 | 382.495 | 0.3234 | watch_only | none |
| 7 | MU | memory_hbm_storage | 817.63 |  | 811.5603 | 0.7479 | 846.4 | 813.91 | 0.1737 | watch_only | none |
| 8 | SMH | semiconductor_index | 528.52 |  | 525.3214 | 0.6089 | 533.01 | 523.325 | 0.0454 | watch_only | none |
| 9 | SOXX | semiconductor_index | 490.27 |  | 488.4001 | 0.3829 | 497.64 | 485.42 | 0.0714 | watch_only | none |
| 10 | QQQ | market_regime | 674.255 |  | 671.5623 | 0.401 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| 11 | TT | data_center_power_cooling | 466.615 |  | 464.066 | 0.5493 | 477.73 | 460.77 | 0.1886 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 328.97 |  | 327.3587 | 0.4922 | 330.21 | 324.97 | 0.0395 | watch_only | none |
| 13 | IWM | market_regime | 292.11 |  | 291.6314 | 0.1641 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| 14 | KLAC | semiconductor_equipment | 190.31 |  | 189.9763 | 0.1756 | 194.96 | 189.48 | 0.1629 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 396.53 |  | 394.8889 | 0.4156 | 400.09 | 392.355 | 0.0454 | watch_only | none |
| 16 | HPE | ai_server_oem | 44.455 |  | 44.1211 | 0.7567 | 46.19 | 44.33 | 0.09 | watch_only | none |
| 17 | MRVL | custom_silicon_networking | 174.96 |  | 171.8954 | 1.7828 | 181.24 | 172.395 | 0.2915 | watch_only | none |
| 18 | SMCI | ai_server_oem | 27.93 |  | 27.6792 | 0.9061 | 28.86 | 27.59 | 0.0358 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34.03 |  | 33.3123 | 2.1543 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| 20 | CORZ | high_beta_ai_infrastructure | 20.175 |  | 19.9509 | 1.1234 | 20.97 | 19.755 | 0.0991 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 674.255 |  | 671.5623 | 0.401 | 677.3 | 670.84 | 0.0104 | watch_only | none |
| TQQQ | leveraged_tool | 61.12 |  | 60.4475 | 1.1125 | 62.01 | 60.23 | 0.0164 | watch_only | none |
| NVDA | ai_accelerator | 197.235 |  | 194.508 | 1.402 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.53 |  | 394.8889 | 0.4156 | 400.09 | 392.355 | 0.0454 | watch_only | none |
| AAPL | mega_cap_platform | 337.24 |  | 338.5365 | -0.383 | 342.87 | 337.78 | 0.0178 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 328.97 |  | 327.3587 | 0.4922 | 330.21 | 324.97 | 0.0395 | watch_only | none |
| AMD | ai_accelerator | 453.32 |  | 452.9188 | 0.0886 | 472.485 | 453.76 | 0.0882 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 386.57 |  | 384.715 | 0.4822 | 390.46 | 382.495 | 0.3234 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.27 |  | 488.4001 | 0.3829 | 497.64 | 485.42 | 0.0714 | watch_only | none |
| SMH | semiconductor_index | 528.52 |  | 525.3214 | 0.6089 | 533.01 | 523.325 | 0.0454 | watch_only | none |
| AVGO | custom_silicon_networking | 379.41 |  | 375.748 | 0.9746 | 378.64 | 371.57 | 0.1977 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 817.63 |  | 811.5603 | 0.7479 | 846.4 | 813.91 | 0.1737 | watch_only | none |
| MRVL | custom_silicon_networking | 174.96 |  | 171.8954 | 1.7828 | 181.24 | 172.395 | 0.2915 | watch_only | none |
| DELL | ai_server_oem | 376.11 |  | 371.023 | 1.3711 | 402 | 374.02 | 4.177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.455 |  | 44.1211 | 0.7567 | 46.19 | 44.33 | 0.09 | watch_only | none |
| SMCI | ai_server_oem | 27.93 |  | 27.6792 | 0.9061 | 28.86 | 27.59 | 0.0358 | watch_only | none |
| SPY | market_regime | 739.715 |  | 737.7935 | 0.2604 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.11 |  | 291.6314 | 0.1641 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| ORCL | cloud_ai_capex | 118.52 |  | 115.943 | 2.2227 | 117.17 | 115.25 | 0.1097 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.54 |  | 65.8796 | 1.0024 | 68.995 | 65.635 | 2.4346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.655 |  | 265.5944 | 0.0228 | 273.86 | 266.04 | 0.5458 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ETN | data_center_power_cooling | 380.66 |  | 378.601 | 0.5438 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 579.04 |  | 578.8214 | 0.0378 | 603.25 | 584.69 | 4.732 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 934.95 |  | 933.0822 | 0.2002 | 955.825 | 935.665 | 4.7158 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 466.615 |  | 464.066 | 0.5493 | 477.73 | 460.77 | 0.1886 | watch_only | none |
| JCI | data_center_power_cooling | 138.17 |  | 137.8084 | 0.2624 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 162.945 |  | 161.839 | 0.6834 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 237.55 |  | 235.654 | 0.8046 | 256.145 | 236.73 | 4.2012 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 635.03 |  | 623.8296 | 1.7954 | 673.65 | 624.91 | 0.9433 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 337.88 |  | 335.4959 | 0.7106 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 86.82 |  | 84.7909 | 2.3931 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 256.68 |  | 255.312 | 0.5358 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1575.94 |  | 1571.7071 | 0.2693 | 1586.01 | 1565.95 | 0.3979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 476.71 |  | 477.2825 | -0.12 | 494.87 | 477.03 | 4.6317 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 266.07 |  | 265.7092 | 0.1358 | 276.85 | 267.14 | 1.5034 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 190.31 |  | 189.9763 | 0.1756 | 194.96 | 189.48 | 0.1629 | watch_only | none |
| TER | semiconductor_test_packaging | 307.53 |  | 305.39 | 0.7007 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 235.05 |  | 237.7626 | -1.1409 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 47.28 |  | 47.2313 | 0.1031 | 51.64 | 47.435 | 2.39 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.72 |  | 42.6573 | 0.147 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 120.85 |  | 119.1497 | 1.4271 | 121 | 117.72 | 0.4799 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 281.43 |  | 281.942 | -0.1816 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.825 |  | 518.6774 | 0.0285 | 518.6 | 511.495 | 4.2384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.65 |  | 296.4246 | -0.2613 | 297.25 | 293.555 | 1.7216 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.525 |  | 26.3119 | 0.8098 | 27 | 25.42 | 3.6569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.03 |  | 33.3123 | 2.1543 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.175 |  | 19.9509 | 1.1234 | 20.97 | 19.755 | 0.0991 | watch_only | none |
| SNDK | memory_hbm_storage | 1106.2 |  | 1103.6717 | 0.2291 | 1185.19 | 1114.57 | 3.7679 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 438.27 |  | 433.4333 | 1.1159 | 465.04 | 435.22 | 0.9195 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 730.34 |  | 722.096 | 1.1417 | 774.805 | 719.02 | 4.6061 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 228.86 |  | 229.981 | -0.4874 | 233.05 | 229.7 | 0.0175 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 591.33 |  | 594.4592 | -0.5264 | 600.765 | 594.21 | 1.0671 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 245.17 |  | 244.6147 | 0.227 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.7 |  | 131.4214 | 0.9729 | 136.45 | 131.735 | 1.7935 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
