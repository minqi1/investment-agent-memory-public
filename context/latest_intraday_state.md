# Intraday State

- Generated at: `2026-07-28T22:44:45+08:00`
- Market time ET: `2026-07-28T10:44:46-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 11, 'manual_confirm_candidate': 1, 'below_vwap': 10, 'below_opening_15m_low': 25, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 672.34 |  | 671.217 | 0.1673 | 677.3 | 670.84 | 0.0863 | watch_only | none |
| SOXX | semiconductor_index | 487.62 |  | 488.0339 | -0.0848 | 497.64 | 485.42 | 0.1025 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.02 |  | 524.8542 | 0.2221 | 533.01 | 523.325 | 0.1065 | watch_only | none |
| SPY | market_regime | 738.42 |  | 737.5827 | 0.1135 | 739.42 | 736.57 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196 |  | 194.1918 | 0.9311 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 526.02 |  | 524.8542 | 0.2221 | 533.01 | 523.325 | 0.1065 | watch_only | none |
| 2 | SPY | market_regime | 738.42 |  | 737.5827 | 0.1135 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 3 | QQQ | market_regime | 672.34 |  | 671.217 | 0.1673 | 677.3 | 670.84 | 0.0863 | watch_only | none |
| 4 | KLAC | semiconductor_equipment | 190.26 |  | 189.8388 | 0.2219 | 194.96 | 189.48 | 0.1156 | watch_only | none |
| 5 | STX | memory_hbm_storage | 723.02 |  | 721.707 | 0.1819 | 774.805 | 719.02 | 0.2711 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 327.855 |  | 327.1726 | 0.2086 | 330.21 | 324.97 | 0.2166 | watch_only | none |
| 7 | NVDA | ai_accelerator | 196 |  | 194.1918 | 0.9311 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 377.215 |  | 375.38 | 0.4888 | 378.64 | 371.57 | 0.1697 | watch_only | none |
| 9 | SMCI | ai_server_oem | 27.74 |  | 27.6419 | 0.3549 | 28.86 | 27.59 | 0.0721 | watch_only | none |
| 10 | SKHY | memory_hbm_storage | 132.26 |  | 131.2564 | 0.7646 | 136.45 | 131.735 | 0.1512 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 396.21 |  | 394.7032 | 0.3818 | 400.09 | 392.355 | 0.1893 | watch_only | none |
| 12 | LIN | industrial_gases | 519.19 |  | 518.694 | 0.0956 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ANET | ai_networking_optical | 162.08 |  | 161.7167 | 0.2247 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AAOI | ai_networking_optical | 84.75 |  | 84.6927 | 0.0677 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 119.12 |  | 119.0683 | 0.0434 | 121 | 117.72 | 0.6632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | APLD | high_beta_ai_infrastructure | 26.32 |  | 26.2975 | 0.0854 | 27 | 25.42 | 2.8116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ASML | semiconductor_equipment | 1576.09 |  | 1570.3001 | 0.3687 | 1586.01 | 1565.95 | 0.6097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ORCL | cloud_ai_capex | 116.42 |  | 115.7141 | 0.61 | 117.17 | 115.25 | 3.0407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TER | semiconductor_test_packaging | 306.865 |  | 305.0795 | 0.5853 | 315.21 | 304.11 | 1.4925 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | HPE | ai_server_oem | 44.11 |  | 44.0209 | 0.2025 | 46.19 | 44.33 | 0.1134 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196 |  | 194.1918 | 0.9311 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 519.19 |  | 518.694 | 0.0956 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | SMH | semiconductor_index | 526.02 |  | 524.8542 | 0.2221 | 533.01 | 523.325 | 0.1065 | watch_only | none |
| 4 | AVGO | custom_silicon_networking | 377.215 |  | 375.38 | 0.4888 | 378.64 | 371.57 | 0.1697 | watch_only | none |
| 5 | SPY | market_regime | 738.42 |  | 737.5827 | 0.1135 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 6 | QQQ | market_regime | 672.34 |  | 671.217 | 0.1673 | 677.3 | 670.84 | 0.0863 | watch_only | none |
| 7 | STX | memory_hbm_storage | 723.02 |  | 721.707 | 0.1819 | 774.805 | 719.02 | 0.2711 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 327.855 |  | 327.1726 | 0.2086 | 330.21 | 324.97 | 0.2166 | watch_only | none |
| 9 | SKHY | memory_hbm_storage | 132.26 |  | 131.2564 | 0.7646 | 136.45 | 131.735 | 0.1512 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 190.26 |  | 189.8388 | 0.2219 | 194.96 | 189.48 | 0.1156 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 396.21 |  | 394.7032 | 0.3818 | 400.09 | 392.355 | 0.1893 | watch_only | none |
| 12 | SMCI | ai_server_oem | 27.74 |  | 27.6419 | 0.3549 | 28.86 | 27.59 | 0.0721 | watch_only | none |
| 13 | TQQQ | leveraged_tool | 60.6 |  | 60.3816 | 0.3618 | 62.01 | 60.23 | 0.033 | watch_only | none |
| 14 | TSM | foundry | 383.86 |  | 384.5828 | -0.1879 | 390.46 | 382.495 | 1.7637 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 487.62 |  | 488.0339 | -0.0848 | 497.64 | 485.42 | 0.1025 | below_vwap | below_vwap |
| 16 | TT | data_center_power_cooling | 462.3 |  | 464.0209 | -0.3709 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 137.49 |  | 137.7648 | -0.1994 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 377.76 |  | 378.5191 | -0.2006 | 384.565 | 377.43 | 3.7564 | below_vwap | below_vwap,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | APD | industrial_gases | 296.41 |  | 296.4594 | -0.0167 | 297.25 | 293.555 | 4.2475 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 672.34 |  | 671.217 | 0.1673 | 677.3 | 670.84 | 0.0863 | watch_only | none |
| TQQQ | leveraged_tool | 60.6 |  | 60.3816 | 0.3618 | 62.01 | 60.23 | 0.033 | watch_only | none |
| NVDA | ai_accelerator | 196 |  | 194.1918 | 0.9311 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.21 |  | 394.7032 | 0.3818 | 400.09 | 392.355 | 0.1893 | watch_only | none |
| AAPL | mega_cap_platform | 337.92 |  | 338.6248 | -0.2081 | 342.87 | 337.78 | 0.0237 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 327.855 |  | 327.1726 | 0.2086 | 330.21 | 324.97 | 0.2166 | watch_only | none |
| AMD | ai_accelerator | 450.33 |  | 453.1031 | -0.612 | 472.485 | 453.76 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 383.86 |  | 384.5828 | -0.1879 | 390.46 | 382.495 | 1.7637 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 487.62 |  | 488.0339 | -0.0848 | 497.64 | 485.42 | 0.1025 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.02 |  | 524.8542 | 0.2221 | 533.01 | 523.325 | 0.1065 | watch_only | none |
| AVGO | custom_silicon_networking | 377.215 |  | 375.38 | 0.4888 | 378.64 | 371.57 | 0.1697 | watch_only | none |
| MU | memory_hbm_storage | 812.5 |  | 811.1384 | 0.1679 | 846.4 | 813.91 | 0.4825 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 172.01 |  | 171.5414 | 0.2732 | 181.24 | 172.395 | 2.0115 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| DELL | ai_server_oem | 371.805 |  | 370.5809 | 0.3303 | 402 | 374.02 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| HPE | ai_server_oem | 44.11 |  | 44.0209 | 0.2025 | 46.19 | 44.33 | 0.1134 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.74 |  | 27.6419 | 0.3549 | 28.86 | 27.59 | 0.0721 | watch_only | none |
| SPY | market_regime | 738.42 |  | 737.5827 | 0.1135 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| IWM | market_regime | 291.2 |  | 291.6228 | -0.145 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 116.42 |  | 115.7141 | 0.61 | 117.17 | 115.25 | 3.0407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 65.22 |  | 65.8846 | -1.0087 | 68.995 | 65.635 | 4.4312 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 262.21 |  | 265.7859 | -1.3454 | 273.86 | 266.04 | 0.3585 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 377.76 |  | 378.5191 | -0.2006 | 384.565 | 377.43 | 3.7564 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 575.37 |  | 578.9036 | -0.6104 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 928.01 |  | 933.1701 | -0.553 | 955.825 | 935.665 | 0.1455 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 462.3 |  | 464.0209 | -0.3709 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 137.49 |  | 137.7648 | -0.1994 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 162.08 |  | 161.7167 | 0.2247 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 233.1 |  | 235.7159 | -1.1098 | 256.145 | 236.73 | 4.1956 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 621.39 |  | 623.2274 | -0.2948 | 673.65 | 624.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 333.945 |  | 335.4518 | -0.4492 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 84.75 |  | 84.6927 | 0.0677 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 252.63 |  | 255.2578 | -1.0295 | 268.265 | 253.05 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1576.09 |  | 1570.3001 | 0.3687 | 1586.01 | 1565.95 | 0.6097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 474.33 |  | 477.5318 | -0.6705 | 494.87 | 477.03 | 0.4512 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 263.88 |  | 265.7483 | -0.703 | 276.85 | 267.14 | 0.8261 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 190.26 |  | 189.8388 | 0.2219 | 194.96 | 189.48 | 0.1156 | watch_only | none |
| TER | semiconductor_test_packaging | 306.865 |  | 305.0795 | 0.5853 | 315.21 | 304.11 | 1.4925 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 232.57 |  | 237.8213 | -2.2081 | 248.8 | 236.42 | 4.5148 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 46.76 |  | 47.2461 | -1.029 | 51.64 | 47.435 | 1.3259 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.24 |  | 42.6523 | -0.9667 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.12 |  | 119.0683 | 0.0434 | 121 | 117.72 | 0.6632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 278.95 |  | 282.204 | -1.1531 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 519.19 |  | 518.694 | 0.0956 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.41 |  | 296.4594 | -0.0167 | 297.25 | 293.555 | 4.2475 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.32 |  | 26.2975 | 0.0854 | 27 | 25.42 | 2.8116 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.44 |  | 33.2534 | 0.561 | 35.08 | 33.52 | 0.0299 | below_opening_15m_low | below_opening_15m_low |
| CORZ | high_beta_ai_infrastructure | 19.84 |  | 19.9386 | -0.4945 | 20.97 | 19.755 | 0.0504 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1101.07 |  | 1103.4055 | -0.2117 | 1185.19 | 1114.57 | 1.4886 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 431.23 |  | 433.3205 | -0.4824 | 465.04 | 435.22 | 1.8204 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 723.02 |  | 721.707 | 0.1819 | 774.805 | 719.02 | 0.2711 | watch_only | none |
| AMZN | cloud_ai_capex | 228.66 |  | 230.0765 | -0.6157 | 233.05 | 229.7 | 0.0262 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 592.61 |  | 594.6876 | -0.3494 | 600.765 | 594.21 | 4.7924 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 243.6 |  | 244.5984 | -0.4082 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 132.26 |  | 131.2564 | 0.7646 | 136.45 | 131.735 | 0.1512 | watch_only | none |
