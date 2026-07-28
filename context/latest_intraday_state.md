# Intraday State

- Generated at: `2026-07-28T22:48:39+08:00`
- Market time ET: `2026-07-28T10:48:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 11, 'manual_confirm_candidate': 1, 'below_vwap': 13, 'below_opening_15m_low': 22, 'spread_too_wide_or_missing': 8, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 672.82 |  | 671.2866 | 0.2284 | 677.3 | 670.84 | 0.0149 | watch_only | none |
| SOXX | semiconductor_index | 487.82 |  | 488.0062 | -0.0382 | 497.64 | 485.42 | 0.0943 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.46 |  | 524.8878 | 0.2995 | 533.01 | 523.325 | 0.0532 | watch_only | none |
| SPY | market_regime | 738.72 |  | 737.6176 | 0.1495 | 739.42 | 736.57 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.675 |  | 194.2893 | 1.2279 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 526.46 |  | 524.8878 | 0.2995 | 533.01 | 523.325 | 0.0532 | watch_only | none |
| 2 | SPY | market_regime | 738.72 |  | 737.6176 | 0.1495 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 3 | QQQ | market_regime | 672.82 |  | 671.2866 | 0.2284 | 677.3 | 670.84 | 0.0149 | watch_only | none |
| 4 | ANET | ai_networking_optical | 161.975 |  | 161.7159 | 0.1602 | 165.975 | 160.51 | 0.1358 | watch_only | none |
| 5 | KLAC | semiconductor_equipment | 190.45 |  | 189.8543 | 0.3138 | 194.96 | 189.48 | 0.2783 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 377.325 |  | 375.4537 | 0.4984 | 378.64 | 371.57 | 0.0451 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 328.86 |  | 327.2214 | 0.5008 | 330.21 | 324.97 | 0.0334 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 397.27 |  | 394.7587 | 0.6362 | 400.09 | 392.355 | 0.1485 | watch_only | none |
| 9 | NVDA | ai_accelerator | 196.675 |  | 194.2893 | 1.2279 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 27.865 |  | 27.645 | 0.796 | 28.86 | 27.59 | 0.0718 | watch_only | none |
| 11 | IREN | high_beta_ai_infrastructure | 33.63 |  | 33.2613 | 1.1084 | 35.08 | 33.52 | 0.0297 | watch_only | none |
| 12 | LIN | industrial_gases | 518.84 |  | 518.695 | 0.028 | 518.6 | 511.495 | 4.3096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 385.05 |  | 384.562 | 0.1269 | 390.46 | 382.495 | 1.3635 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ASML | semiconductor_equipment | 1574.635 |  | 1570.3683 | 0.2717 | 1586.01 | 1565.95 | 0.6008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 307.1 |  | 305.1236 | 0.6477 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | HPE | ai_server_oem | 44.18 |  | 44.0266 | 0.3485 | 46.19 | 44.33 | 0.1132 | below_opening_15m_low | below_opening_15m_low |
| 17 | ENTG | semiconductor_materials | 119.63 |  | 119.073 | 0.4678 | 121 | 117.72 | 4.004 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AAOI | ai_networking_optical | 85.545 |  | 84.6951 | 1.0035 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SOXX | semiconductor_index | 487.82 |  | 488.0062 | -0.0382 | 497.64 | 485.42 | 0.0943 | below_vwap | below_vwap |
| 20 | MU | memory_hbm_storage | 813.28 |  | 811.0931 | 0.2696 | 846.4 | 813.91 | 3.6888 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.675 |  | 194.2893 | 1.2279 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 518.84 |  | 518.695 | 0.028 | 518.6 | 511.495 | 4.3096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | SMH | semiconductor_index | 526.46 |  | 524.8878 | 0.2995 | 533.01 | 523.325 | 0.0532 | watch_only | none |
| 4 | AVGO | custom_silicon_networking | 377.325 |  | 375.4537 | 0.4984 | 378.64 | 371.57 | 0.0451 | watch_only | none |
| 5 | SPY | market_regime | 738.72 |  | 737.6176 | 0.1495 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| 6 | QQQ | market_regime | 672.82 |  | 671.2866 | 0.2284 | 677.3 | 670.84 | 0.0149 | watch_only | none |
| 7 | ANET | ai_networking_optical | 161.975 |  | 161.7159 | 0.1602 | 165.975 | 160.51 | 0.1358 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 328.86 |  | 327.2214 | 0.5008 | 330.21 | 324.97 | 0.0334 | watch_only | none |
| 9 | KLAC | semiconductor_equipment | 190.45 |  | 189.8543 | 0.3138 | 194.96 | 189.48 | 0.2783 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 397.27 |  | 394.7587 | 0.6362 | 400.09 | 392.355 | 0.1485 | watch_only | none |
| 11 | SMCI | ai_server_oem | 27.865 |  | 27.645 | 0.796 | 28.86 | 27.59 | 0.0718 | watch_only | none |
| 12 | IREN | high_beta_ai_infrastructure | 33.63 |  | 33.2613 | 1.1084 | 35.08 | 33.52 | 0.0297 | watch_only | none |
| 13 | TQQQ | leveraged_tool | 60.78 |  | 60.3873 | 0.6503 | 62.01 | 60.23 | 0.0329 | watch_only | none |
| 14 | SOXX | semiconductor_index | 487.82 |  | 488.0062 | -0.0382 | 497.64 | 485.42 | 0.0943 | below_vwap | below_vwap |
| 15 | TT | data_center_power_cooling | 463.26 |  | 464.0103 | -0.1617 | 477.73 | 460.77 | 0.1727 | below_vwap | below_vwap |
| 16 | STX | memory_hbm_storage | 719.42 |  | 721.7039 | -0.3165 | 774.805 | 719.02 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 137.68 |  | 137.763 | -0.0603 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 377.775 |  | 378.4925 | -0.1896 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ALAB | ai_networking_optical | 255.08 |  | 255.2457 | -0.0649 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 672.82 |  | 671.2866 | 0.2284 | 677.3 | 670.84 | 0.0149 | watch_only | none |
| TQQQ | leveraged_tool | 60.78 |  | 60.3873 | 0.6503 | 62.01 | 60.23 | 0.0329 | watch_only | none |
| NVDA | ai_accelerator | 196.675 |  | 194.2893 | 1.2279 | 195.4 | 193.65 | 0.0203 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.27 |  | 394.7587 | 0.6362 | 400.09 | 392.355 | 0.1485 | watch_only | none |
| AAPL | mega_cap_platform | 338.165 |  | 338.6024 | -0.1292 | 342.87 | 337.78 | 0.0769 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 328.86 |  | 327.2214 | 0.5008 | 330.21 | 324.97 | 0.0334 | watch_only | none |
| AMD | ai_accelerator | 450 |  | 452.8976 | -0.6398 | 472.485 | 453.76 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TSM | foundry | 385.05 |  | 384.562 | 0.1269 | 390.46 | 382.495 | 1.3635 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 487.82 |  | 488.0062 | -0.0382 | 497.64 | 485.42 | 0.0943 | below_vwap | below_vwap |
| SMH | semiconductor_index | 526.46 |  | 524.8878 | 0.2995 | 533.01 | 523.325 | 0.0532 | watch_only | none |
| AVGO | custom_silicon_networking | 377.325 |  | 375.4537 | 0.4984 | 378.64 | 371.57 | 0.0451 | watch_only | none |
| MU | memory_hbm_storage | 813.28 |  | 811.0931 | 0.2696 | 846.4 | 813.91 | 3.6888 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 172.235 |  | 171.5598 | 0.3936 | 181.24 | 172.395 | 2.903 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| DELL | ai_server_oem | 371.66 |  | 370.5786 | 0.2918 | 402 | 374.02 | 3.3633 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 44.18 |  | 44.0266 | 0.3485 | 46.19 | 44.33 | 0.1132 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.865 |  | 27.645 | 0.796 | 28.86 | 27.59 | 0.0718 | watch_only | none |
| SPY | market_regime | 738.72 |  | 737.6176 | 0.1495 | 739.42 | 736.57 | 0.0054 | watch_only | none |
| IWM | market_regime | 291.52 |  | 291.6123 | -0.0316 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 116.88 |  | 115.7332 | 0.9909 | 117.17 | 115.25 | 2.4298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 65.34 |  | 65.8642 | -0.7958 | 68.995 | 65.635 | 3.6731 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 262.23 |  | 265.7198 | -1.3133 | 273.86 | 266.04 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 377.775 |  | 378.4925 | -0.1896 | 384.565 | 377.43 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 576.47 |  | 578.7903 | -0.4009 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 931.55 |  | 933.0062 | -0.1561 | 955.825 | 935.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 463.26 |  | 464.0103 | -0.1617 | 477.73 | 460.77 | 0.1727 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 137.68 |  | 137.763 | -0.0603 | 139.755 | 137.31 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 161.975 |  | 161.7159 | 0.1602 | 165.975 | 160.51 | 0.1358 | watch_only | none |
| COHR | ai_networking_optical | 234.16 |  | 235.5961 | -0.6095 | 256.145 | 236.73 | 3.3908 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 622.75 |  | 623.1652 | -0.0666 | 673.65 | 624.91 | 3.6403 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 333.71 |  | 335.4056 | -0.5055 | 354.09 | 338.14 | 4.399 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 85.545 |  | 84.6951 | 1.0035 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 255.08 |  | 255.2457 | -0.0649 | 268.265 | 253.05 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1574.635 |  | 1570.3683 | 0.2717 | 1586.01 | 1565.95 | 0.6008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 473.32 |  | 477.4064 | -0.856 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 263.185 |  | 265.7149 | -0.9521 | 276.85 | 267.14 | 2.409 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 190.45 |  | 189.8543 | 0.3138 | 194.96 | 189.48 | 0.2783 | watch_only | none |
| TER | semiconductor_test_packaging | 307.1 |  | 305.1236 | 0.6477 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 233.3 |  | 237.7793 | -1.8838 | 248.8 | 236.42 | 4.0163 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 46.925 |  | 47.2258 | -0.6369 | 51.64 | 47.435 | 0.2344 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.385 |  | 42.6487 | -0.6183 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.63 |  | 119.073 | 0.4678 | 121 | 117.72 | 4.004 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 278.69 |  | 281.9887 | -1.1698 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.84 |  | 518.695 | 0.028 | 518.6 | 511.495 | 4.3096 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.08 |  | 296.4571 | -0.1272 | 297.25 | 293.555 | 1.9218 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.28 |  | 26.292 | -0.0455 | 27 | 25.42 | 0.1522 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.63 |  | 33.2613 | 1.1084 | 35.08 | 33.52 | 0.0297 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 19.83 |  | 19.9334 | -0.5185 | 20.97 | 19.755 | 0.0504 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1095.14 |  | 1103.2281 | -0.7331 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 432.36 |  | 433.2753 | -0.2113 | 465.04 | 435.22 | 1.5057 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 719.42 |  | 721.7039 | -0.3165 | 774.805 | 719.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 228.855 |  | 230.0393 | -0.5148 | 233.05 | 229.7 | 0.035 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 593.14 |  | 594.6079 | -0.2469 | 600.765 | 594.21 | 1.4381 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 243.99 |  | 244.577 | -0.24 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 132.49 |  | 131.2774 | 0.9237 | 136.45 | 131.735 | 3.3889 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
