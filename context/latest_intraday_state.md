# Intraday State

- Generated at: `2026-07-28T23:17:10+08:00`
- Market time ET: `2026-07-28T11:17:12-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 12, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 9, 'below_opening_15m_low': 18, 'price_stale_or_missing': 2, 'below_vwap': 11}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 674.05 |  | 671.7784 | 0.3381 | 677.3 | 670.84 | 0.0771 | watch_only | none |
| SOXX | semiconductor_index | 488.125 |  | 488.3993 | -0.0562 | 497.64 | 485.42 | 0.1127 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.7 |  | 525.5046 | 0.2275 | 533.01 | 523.325 | 0.0759 | watch_only | none |
| SPY | market_regime | 739.44 |  | 737.9597 | 0.2006 | 739.42 | 736.57 | 0.0081 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.6 |  | 194.7853 | 0.9316 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 378.94 |  | 376.1154 | 0.751 | 378.64 | 371.57 | 0.0818 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 739.44 |  | 737.9597 | 0.2006 | 739.42 | 736.57 | 0.0081 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 519.2 |  | 518.6707 | 0.102 | 518.6 | 511.495 | 0.0828 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 739.44 |  | 737.9597 | 0.2006 | 739.42 | 736.57 | 0.0081 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 519.2 |  | 518.6707 | 0.102 | 518.6 | 511.495 | 0.0828 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 378.94 |  | 376.1154 | 0.751 | 378.64 | 371.57 | 0.0818 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 385.9 |  | 384.8469 | 0.2736 | 390.46 | 382.495 | 0.1477 | watch_only | none |
| 5 | SMH | semiconductor_index | 526.7 |  | 525.5046 | 0.2275 | 533.01 | 523.325 | 0.0759 | watch_only | none |
| 6 | QQQ | market_regime | 674.05 |  | 671.7784 | 0.3381 | 677.3 | 670.84 | 0.0771 | watch_only | none |
| 7 | IWM | market_regime | 292.125 |  | 291.6644 | 0.1579 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 339.17 |  | 338.5021 | 0.1973 | 342.87 | 337.78 | 0.0914 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 398.115 |  | 395.0834 | 0.7673 | 400.09 | 392.355 | 0.1457 | watch_only | none |
| 10 | NVDA | ai_accelerator | 196.6 |  | 194.7853 | 0.9316 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 27.84 |  | 27.6919 | 0.5349 | 28.86 | 27.59 | 0.0718 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 33.59 |  | 33.3597 | 0.6903 | 35.08 | 33.52 | 0.0893 | watch_only | none |
| 13 | APLD | high_beta_ai_infrastructure | 26.49 |  | 26.3582 | 0.4999 | 27 | 25.42 | 0.1133 | watch_only | none |
| 14 | HPE | ai_server_oem | 44.35 |  | 44.1813 | 0.3818 | 46.19 | 44.33 | 0.1578 | watch_only | none |
| 15 | TT | data_center_power_cooling | 465.66 |  | 464.1896 | 0.3168 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 138.145 |  | 137.836 | 0.2242 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | TER | semiconductor_test_packaging | 306.16 |  | 305.5859 | 0.1879 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 380.235 |  | 378.7865 | 0.3824 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AAOI | ai_networking_optical | 85.49 |  | 84.928 | 0.6618 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 436.92 |  | 433.7086 | 0.7404 | 465.04 | 435.22 | 3.3187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.6 |  | 194.7853 | 0.9316 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 378.94 |  | 376.1154 | 0.751 | 378.64 | 371.57 | 0.0818 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 739.44 |  | 737.9597 | 0.2006 | 739.42 | 736.57 | 0.0081 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 519.2 |  | 518.6707 | 0.102 | 518.6 | 511.495 | 0.0828 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 330.54 |  | 327.6319 | 0.8876 | 330.21 | 324.97 | 1.0649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ORCL | cloud_ai_capex | 117.93 |  | 116.245 | 1.4495 | 117.17 | 115.25 | 0.8395 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | TSM | foundry | 385.9 |  | 384.8469 | 0.2736 | 390.46 | 382.495 | 0.1477 | watch_only | none |
| 8 | SMH | semiconductor_index | 526.7 |  | 525.5046 | 0.2275 | 533.01 | 523.325 | 0.0759 | watch_only | none |
| 9 | QQQ | market_regime | 674.05 |  | 671.7784 | 0.3381 | 677.3 | 670.84 | 0.0771 | watch_only | none |
| 10 | IWM | market_regime | 292.125 |  | 291.6644 | 0.1579 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 398.115 |  | 395.0834 | 0.7673 | 400.09 | 392.355 | 0.1457 | watch_only | none |
| 12 | HPE | ai_server_oem | 44.35 |  | 44.1813 | 0.3818 | 46.19 | 44.33 | 0.1578 | watch_only | none |
| 13 | MRVL | custom_silicon_networking | 175.44 |  | 172.4703 | 1.7219 | 181.24 | 172.395 | 0.1938 | watch_only | none |
| 14 | SMCI | ai_server_oem | 27.84 |  | 27.6919 | 0.5349 | 28.86 | 27.59 | 0.0718 | watch_only | none |
| 15 | IREN | high_beta_ai_infrastructure | 33.59 |  | 33.3597 | 0.6903 | 35.08 | 33.52 | 0.0893 | watch_only | none |
| 16 | AAPL | mega_cap_platform | 339.17 |  | 338.5021 | 0.1973 | 342.87 | 337.78 | 0.0914 | watch_only | none |
| 17 | APLD | high_beta_ai_infrastructure | 26.49 |  | 26.3582 | 0.4999 | 27 | 25.42 | 0.1133 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 61.01 |  | 60.4961 | 0.8495 | 62.01 | 60.23 | 0.0328 | watch_only | none |
| 19 | SOXX | semiconductor_index | 488.125 |  | 488.3993 | -0.0562 | 497.64 | 485.42 | 0.1127 | below_vwap | below_vwap |
| 20 | ASML | semiconductor_equipment | 1566.7 |  | 1571.1894 | -0.2857 | 1586.01 | 1565.95 | 0.6906 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 674.05 |  | 671.7784 | 0.3381 | 677.3 | 670.84 | 0.0771 | watch_only | none |
| TQQQ | leveraged_tool | 61.01 |  | 60.4961 | 0.8495 | 62.01 | 60.23 | 0.0328 | watch_only | none |
| NVDA | ai_accelerator | 196.6 |  | 194.7853 | 0.9316 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.115 |  | 395.0834 | 0.7673 | 400.09 | 392.355 | 0.1457 | watch_only | none |
| AAPL | mega_cap_platform | 339.17 |  | 338.5021 | 0.1973 | 342.87 | 337.78 | 0.0914 | watch_only | none |
| GOOGL | cloud_ai_capex | 330.54 |  | 327.6319 | 0.8876 | 330.21 | 324.97 | 1.0649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 452.12 |  | 452.7753 | -0.1447 | 472.485 | 453.76 | 2.391 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 385.9 |  | 384.8469 | 0.2736 | 390.46 | 382.495 | 0.1477 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 488.125 |  | 488.3993 | -0.0562 | 497.64 | 485.42 | 0.1127 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.7 |  | 525.5046 | 0.2275 | 533.01 | 523.325 | 0.0759 | watch_only | none |
| AVGO | custom_silicon_networking | 378.94 |  | 376.1154 | 0.751 | 378.64 | 371.57 | 0.0818 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 811.92 |  | 811.7967 | 0.0152 | 846.4 | 813.91 | 0.1687 | below_opening_15m_low | below_opening_15m_low |
| MRVL | custom_silicon_networking | 175.44 |  | 172.4703 | 1.7219 | 181.24 | 172.395 | 0.1938 | watch_only | none |
| DELL | ai_server_oem | 373.29 |  | 371.6977 | 0.4284 | 402 | 374.02 | 0.3081 | below_opening_15m_low | below_opening_15m_low |
| HPE | ai_server_oem | 44.35 |  | 44.1813 | 0.3818 | 46.19 | 44.33 | 0.1578 | watch_only | none |
| SMCI | ai_server_oem | 27.84 |  | 27.6919 | 0.5349 | 28.86 | 27.59 | 0.0718 | watch_only | none |
| SPY | market_regime | 739.44 |  | 737.9597 | 0.2006 | 739.42 | 736.57 | 0.0081 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.125 |  | 291.6644 | 0.1579 | 293.26 | 291.55 | 0.0103 | watch_only | none |
| ORCL | cloud_ai_capex | 117.93 |  | 116.245 | 1.4495 | 117.17 | 115.25 | 0.8395 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 65.64 |  | 65.8788 | -0.3624 | 68.995 | 65.635 | 3.4887 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 264.68 |  | 265.5488 | -0.3272 | 273.86 | 266.04 | 2.044 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 380.235 |  | 378.7865 | 0.3824 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 579.42 |  | 578.8187 | 0.1039 | 603.25 | 584.69 | 0.6593 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 932.995 |  | 932.9827 | 0.0013 | 955.825 | 935.665 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 465.66 |  | 464.1896 | 0.3168 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 138.145 |  | 137.836 | 0.2242 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.01 |  | 162.0486 | 1.2104 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 233.88 |  | 235.7115 | -0.777 | 256.145 | 236.73 | 2.8262 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 624.67 |  | 624.4549 | 0.0344 | 673.65 | 624.91 | 0.6163 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 336.815 |  | 335.8174 | 0.2971 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 85.49 |  | 84.928 | 0.6618 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 255.185 |  | 255.296 | -0.0435 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1566.7 |  | 1571.1894 | -0.2857 | 1586.01 | 1565.95 | 0.6906 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 472.31 |  | 476.8599 | -0.9541 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 263.02 |  | 265.555 | -0.9546 | 276.85 | 267.14 | 0.2053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| KLAC | semiconductor_equipment | 189.09 |  | 189.8956 | -0.4242 | 194.96 | 189.48 | 0.1216 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 306.16 |  | 305.5859 | 0.1879 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 232.72 |  | 237.4163 | -1.9781 | 248.8 | 236.42 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| AMKR | semiconductor_test_packaging | 46.05 |  | 47.1629 | -2.3597 | 51.64 | 47.435 | 0.2389 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.12 |  | 42.6095 | -1.1487 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119 |  | 119.2816 | -0.236 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 278.19 |  | 281.5943 | -1.2089 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 519.2 |  | 518.6707 | 0.102 | 518.6 | 511.495 | 0.0828 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 295.545 |  | 296.3688 | -0.278 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.49 |  | 26.3582 | 0.4999 | 27 | 25.42 | 0.1133 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.59 |  | 33.3597 | 0.6903 | 35.08 | 33.52 | 0.0893 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 19.785 |  | 19.9154 | -0.6547 | 20.97 | 19.755 | 0.0505 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1087.77 |  | 1102.3429 | -1.322 | 1185.19 | 1114.57 | 3.0337 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 436.92 |  | 433.7086 | 0.7404 | 465.04 | 435.22 | 3.3187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 719.605 |  | 722.5453 | -0.4069 | 774.805 | 719.02 | 3.6409 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 229.78 |  | 229.8489 | -0.03 | 233.05 | 229.7 | 0.0218 | below_vwap | below_vwap |
| META | cloud_ai_capex | 591.67 |  | 593.1064 | -0.2422 | 600.765 | 594.21 | 1.7577 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 243.67 |  | 244.6204 | -0.3885 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.14 |  | 131.2738 | -0.8637 | 136.45 | 131.735 | 0.5148 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
