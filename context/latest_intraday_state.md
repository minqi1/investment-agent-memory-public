# Intraday State

- Generated at: `2026-07-29T00:04:55+08:00`
- Market time ET: `2026-07-28T12:04:56-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'watch_only': 12, 'spread_too_wide_or_missing': 32, 'price_stale_or_missing': 1, 'below_vwap': 3, 'below_opening_15m_low': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.81 |  | 673.1885 | 0.8351 | 677.3 | 670.84 | 0.0088 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 497.37 |  | 489.3894 | 1.6307 | 497.64 | 485.42 | 0.0925 | watch_only | none |
| SMH | semiconductor_index | 534.73 |  | 526.7386 | 1.5171 | 533.01 | 523.325 | 0.0916 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.125 |  | 738.6974 | 0.464 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.3 |  | 195.432 | 1.4675 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.48 |  | 386.5226 | 1.8 | 390.46 | 382.495 | 0.0686 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 534.73 |  | 526.7386 | 1.5171 | 533.01 | 523.325 | 0.0916 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 742.125 |  | 738.6974 | 0.464 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 678.81 |  | 673.1885 | 0.8351 | 677.3 | 670.84 | 0.0088 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 333.04 |  | 328.8556 | 1.2724 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.44 |  | 60.7812 | 2.7292 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 742.125 |  | 738.6974 | 0.464 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.61 |  | 395.7707 | 0.2121 | 400.09 | 392.355 | 0.0429 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 339.69 |  | 338.641 | 0.3098 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 4 | QQQ | market_regime | 678.81 |  | 673.1885 | 0.8351 | 677.3 | 670.84 | 0.0088 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.14 |  | 292.0116 | 0.3864 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 231.33 |  | 230.0083 | 0.5746 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 7 | NVDA | ai_accelerator | 198.3 |  | 195.432 | 1.4675 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 333.04 |  | 328.8556 | 1.2724 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| 9 | SMH | semiconductor_index | 534.73 |  | 526.7386 | 1.5171 | 533.01 | 523.325 | 0.0916 | buy_precheck_manual_confirm | none |
| 10 | TSM | foundry | 393.48 |  | 386.5226 | 1.8 | 390.46 | 382.495 | 0.0686 | buy_precheck_manual_confirm | none |
| 11 | COHU | semiconductor_test_packaging | 42.6 |  | 42.5533 | 0.1099 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 588.93 |  | 580.3463 | 1.4791 | 603.25 | 584.69 | 0.1647 | watch_only | none |
| 13 | TT | data_center_power_cooling | 467.96 |  | 464.4882 | 0.7475 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ARM | ai_accelerator | 246.68 |  | 245.0421 | 0.6684 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ONTO | semiconductor_test_packaging | 238.04 |  | 236.4521 | 0.6715 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MU | memory_hbm_storage | 829.32 |  | 813.433 | 1.9531 | 846.4 | 813.91 | 0.0856 | watch_only | none |
| 17 | SOXX | semiconductor_index | 497.37 |  | 489.3894 | 1.6307 | 497.64 | 485.42 | 0.0925 | watch_only | none |
| 18 | HPE | ai_server_oem | 45.075 |  | 44.3705 | 1.5878 | 46.19 | 44.33 | 0.0666 | watch_only | none |
| 19 | AMAT | semiconductor_equipment | 480.68 |  | 477.1811 | 0.7332 | 494.87 | 477.03 | 0.5742 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SMCI | ai_server_oem | 28.55 |  | 27.8567 | 2.4888 | 28.86 | 27.59 | 0.035 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.3 |  | 195.432 | 1.4675 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.48 |  | 386.5226 | 1.8 | 390.46 | 382.495 | 0.0686 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 534.73 |  | 526.7386 | 1.5171 | 533.01 | 523.325 | 0.0916 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 742.125 |  | 738.6974 | 0.464 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 678.81 |  | 673.1885 | 0.8351 | 677.3 | 670.84 | 0.0088 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 333.04 |  | 328.8556 | 1.2724 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.44 |  | 60.7812 | 2.7292 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 384.07 |  | 377.6048 | 1.7122 | 378.64 | 371.57 | 4.1581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1592.78 |  | 1575.1886 | 1.1168 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ANET | ai_networking_optical | 167.72 |  | 163.4519 | 2.6112 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ETN | data_center_power_cooling | 386.525 |  | 379.5384 | 1.8408 | 384.565 | 377.43 | 3.0891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ORCL | cloud_ai_capex | 120.32 |  | 117.2189 | 2.6455 | 117.17 | 115.25 | 1.4461 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | MU | memory_hbm_storage | 829.32 |  | 813.433 | 1.9531 | 846.4 | 813.91 | 0.0856 | watch_only | none |
| 14 | SOXX | semiconductor_index | 497.37 |  | 489.3894 | 1.6307 | 497.64 | 485.42 | 0.0925 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 588.93 |  | 580.3463 | 1.4791 | 603.25 | 584.69 | 0.1647 | watch_only | none |
| 16 | GEV | data_center_power_cooling | 953.005 |  | 935.0225 | 1.9232 | 955.825 | 935.665 | 0.2686 | watch_only | none |
| 17 | IWM | market_regime | 293.14 |  | 292.0116 | 0.3864 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 18 | APLD | high_beta_ai_infrastructure | 27.16 |  | 26.5021 | 2.4825 | 27 | 25.42 | 3.4242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MSFT | cloud_ai_capex | 396.61 |  | 395.7707 | 0.2121 | 400.09 | 392.355 | 0.0429 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 231.33 |  | 230.0083 | 0.5746 | 233.05 | 229.7 | 0.013 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.81 |  | 673.1885 | 0.8351 | 677.3 | 670.84 | 0.0088 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.44 |  | 60.7812 | 2.7292 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 198.3 |  | 195.432 | 1.4675 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.61 |  | 395.7707 | 0.2121 | 400.09 | 392.355 | 0.0429 | watch_only | none |
| AAPL | mega_cap_platform | 339.69 |  | 338.641 | 0.3098 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.04 |  | 328.8556 | 1.2724 | 330.21 | 324.97 | 0.027 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 464.6 |  | 454.269 | 2.2742 | 472.485 | 453.76 | 4.7288 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.48 |  | 386.5226 | 1.8 | 390.46 | 382.495 | 0.0686 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 497.37 |  | 489.3894 | 1.6307 | 497.64 | 485.42 | 0.0925 | watch_only | none |
| SMH | semiconductor_index | 534.73 |  | 526.7386 | 1.5171 | 533.01 | 523.325 | 0.0916 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 384.07 |  | 377.6048 | 1.7122 | 378.64 | 371.57 | 4.1581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 829.32 |  | 813.433 | 1.9531 | 846.4 | 813.91 | 0.0856 | watch_only | none |
| MRVL | custom_silicon_networking | 179.21 |  | 173.4092 | 3.3451 | 181.24 | 172.395 | 3.8112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 387.155 |  | 373.1599 | 3.7504 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.075 |  | 44.3705 | 1.5878 | 46.19 | 44.33 | 0.0666 | watch_only | none |
| SMCI | ai_server_oem | 28.55 |  | 27.8567 | 2.4888 | 28.86 | 27.59 | 0.035 | watch_only | none |
| SPY | market_regime | 742.125 |  | 738.6974 | 0.464 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.14 |  | 292.0116 | 0.3864 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.32 |  | 117.2189 | 2.6455 | 117.17 | 115.25 | 1.4461 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67.39 |  | 66.0046 | 2.099 | 68.995 | 65.635 | 1.2168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.15 |  | 266.0028 | 1.1831 | 273.86 | 266.04 | 1.3153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.525 |  | 379.5384 | 1.8408 | 384.565 | 377.43 | 3.0891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 588.93 |  | 580.3463 | 1.4791 | 603.25 | 584.69 | 0.1647 | watch_only | none |
| GEV | data_center_power_cooling | 953.005 |  | 935.0225 | 1.9232 | 955.825 | 935.665 | 0.2686 | watch_only | none |
| TT | data_center_power_cooling | 467.96 |  | 464.4882 | 0.7475 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.395 |  | 138.0313 | 0.9879 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.72 |  | 163.4519 | 2.6112 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 241.085 |  | 236.0533 | 2.1316 | 256.145 | 236.73 | 2.4763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 646.69 |  | 626.7103 | 3.188 | 673.65 | 624.91 | 2.6752 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 345.25 |  | 336.2696 | 2.6706 | 354.09 | 338.14 | 4.7386 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.35 |  | 85.293 | 3.5841 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.145 |  | 257.677 | 2.8982 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1592.78 |  | 1575.1886 | 1.1168 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 480.68 |  | 477.1811 | 0.7332 | 494.87 | 477.03 | 0.5742 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 269.965 |  | 265.7854 | 1.5725 | 276.85 | 267.14 | 3.9005 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.47 |  | 190.3515 | 1.6383 | 194.96 | 189.48 | 1.5868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 313.92 |  | 306.7214 | 2.347 | 315.21 | 304.11 | 0.5861 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 238.04 |  | 236.4521 | 0.6715 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.65 |  | 47.039 | -0.8269 | 51.64 | 47.435 | 0.4073 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.6 |  | 42.5533 | 0.1099 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 120.32 |  | 119.4452 | 0.7324 | 121 | 117.72 | 3.9727 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 286.61 |  | 281.7571 | 1.7224 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 518.26 |  | 518.5309 | -0.0522 | 518.6 | 511.495 | 4.4476 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.895 |  | 295.941 | -0.3534 | 297.25 | 293.555 | 4.4863 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.16 |  | 26.5021 | 2.4825 | 27 | 25.42 | 3.4242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.81 |  | 33.5809 | 3.66 | 35.08 | 33.52 | 0.0575 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.52 |  | 19.9769 | 2.7188 | 20.97 | 19.755 | 0.0487 | watch_only | none |
| SNDK | memory_hbm_storage | 1118.77 |  | 1102.5993 | 1.4666 | 1185.19 | 1114.57 | 4.5586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 455.73 |  | 435.4732 | 4.6517 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 751.62 |  | 724.1399 | 3.7949 | 774.805 | 719.02 | 0.7544 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.33 |  | 230.0083 | 0.5746 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 596.67 |  | 593.4735 | 0.5386 | 600.765 | 594.21 | 0.8464 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 246.68 |  | 245.0421 | 0.6684 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.835 |  | 131.4876 | 1.7853 | 136.45 | 131.735 | 0.5828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
