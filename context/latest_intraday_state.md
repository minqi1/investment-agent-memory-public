# Intraday State

- Generated at: `2026-07-29T00:28:07+08:00`
- Market time ET: `2026-07-28T12:28:08-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'watch_only': 17, 'price_stale_or_missing': 1, 'below_vwap': 5, 'spread_too_wide_or_missing': 22, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.43 |  | 673.4437 | 0.5919 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 493.19 |  | 489.5499 | 0.7436 | 497.64 | 485.42 | 0.075 | watch_only | none |
| SMH | semiconductor_index | 530.95 |  | 526.87 | 0.7744 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| SPY | market_regime | 741.54 |  | 738.9457 | 0.3511 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.43 |  | 195.6223 | 0.9241 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.305 |  | 386.8503 | 1.1515 | 390.46 | 382.495 | 0.092 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 381.775 |  | 377.9425 | 1.014 | 378.64 | 371.57 | 0.0655 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.54 |  | 738.9457 | 0.3511 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 677.43 |  | 673.4437 | 0.5919 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 333.71 |  | 329.1648 | 1.3808 | 330.21 | 324.97 | 0.024 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.06 |  | 60.8536 | 1.9824 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.54 |  | 738.9457 | 0.3511 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 677.43 |  | 673.4437 | 0.5919 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 293.03 |  | 292.0572 | 0.3331 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 4 | KLAC | semiconductor_equipment | 191.12 |  | 190.5143 | 0.318 | 194.96 | 189.48 | 0.0209 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 339.92 |  | 338.7378 | 0.349 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 6 | MU | memory_hbm_storage | 820.22 |  | 813.9493 | 0.7704 | 846.4 | 813.91 | 0.0841 | watch_only | none |
| 7 | SMH | semiconductor_index | 530.95 |  | 526.87 | 0.7744 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| 8 | SOXX | semiconductor_index | 493.19 |  | 489.5499 | 0.7436 | 497.64 | 485.42 | 0.075 | watch_only | none |
| 9 | TSM | foundry | 391.305 |  | 386.8503 | 1.1515 | 390.46 | 382.495 | 0.092 | buy_precheck_manual_confirm | none |
| 10 | META | cloud_ai_capex | 596.84 |  | 593.665 | 0.5348 | 600.765 | 594.21 | 0.057 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 398.44 |  | 395.9046 | 0.6404 | 400.09 | 392.355 | 0.0376 | watch_only | none |
| 12 | AMZN | cloud_ai_capex | 231.52 |  | 230.1021 | 0.6162 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 13 | HPE | ai_server_oem | 44.77 |  | 44.4158 | 0.7974 | 46.19 | 44.33 | 0.0893 | watch_only | none |
| 14 | ARM | ai_accelerator | 246.19 |  | 245.1218 | 0.4358 | 253.38 | 243.72 | 0.3087 | watch_only | none |
| 15 | NVDA | ai_accelerator | 197.43 |  | 195.6223 | 0.9241 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 16 | AVGO | custom_silicon_networking | 381.775 |  | 377.9425 | 1.014 | 378.64 | 371.57 | 0.0655 | buy_precheck_manual_confirm | none |
| 17 | GOOGL | cloud_ai_capex | 333.71 |  | 329.1648 | 1.3808 | 330.21 | 324.97 | 0.024 | buy_precheck_manual_confirm | none |
| 18 | ASML | semiconductor_equipment | 1578.965 |  | 1576.0924 | 0.1823 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | IREN | high_beta_ai_infrastructure | 34.07 |  | 33.6592 | 1.2205 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| 20 | CORZ | high_beta_ai_infrastructure | 20.28 |  | 19.9919 | 1.4412 | 20.97 | 19.755 | 0.0493 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.43 |  | 195.6223 | 0.9241 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.305 |  | 386.8503 | 1.1515 | 390.46 | 382.495 | 0.092 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 381.775 |  | 377.9425 | 1.014 | 378.64 | 371.57 | 0.0655 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 741.54 |  | 738.9457 | 0.3511 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 677.43 |  | 673.4437 | 0.5919 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 333.71 |  | 329.1648 | 1.3808 | 330.21 | 324.97 | 0.024 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 62.06 |  | 60.8536 | 1.9824 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 166.935 |  | 163.6607 | 2.0007 | 165.975 | 160.51 | 1.9049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ETN | data_center_power_cooling | 386.39 |  | 379.8755 | 1.7149 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ORCL | cloud_ai_capex | 120.78 |  | 117.6053 | 2.6994 | 117.17 | 115.25 | 1.2171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | MU | memory_hbm_storage | 820.22 |  | 813.9493 | 0.7704 | 846.4 | 813.91 | 0.0841 | watch_only | none |
| 12 | SMH | semiconductor_index | 530.95 |  | 526.87 | 0.7744 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| 13 | SOXX | semiconductor_index | 493.19 |  | 489.5499 | 0.7436 | 497.64 | 485.42 | 0.075 | watch_only | none |
| 14 | IWM | market_regime | 293.03 |  | 292.0572 | 0.3331 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 15 | AMD | ai_accelerator | 460.415 |  | 454.7309 | 1.25 | 472.485 | 453.76 | 0.2215 | watch_only | none |
| 16 | KLAC | semiconductor_equipment | 191.12 |  | 190.5143 | 0.318 | 194.96 | 189.48 | 0.0209 | watch_only | none |
| 17 | ARM | ai_accelerator | 246.19 |  | 245.1218 | 0.4358 | 253.38 | 243.72 | 0.3087 | watch_only | none |
| 18 | META | cloud_ai_capex | 596.84 |  | 593.665 | 0.5348 | 600.765 | 594.21 | 0.057 | watch_only | none |
| 19 | TER | semiconductor_test_packaging | 310.74 |  | 307.4516 | 1.0696 | 315.21 | 304.11 | 0.2864 | watch_only | none |
| 20 | MSFT | cloud_ai_capex | 398.44 |  | 395.9046 | 0.6404 | 400.09 | 392.355 | 0.0376 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.43 |  | 673.4437 | 0.5919 | 677.3 | 670.84 | 0.0118 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.06 |  | 60.8536 | 1.9824 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.43 |  | 195.6223 | 0.9241 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.44 |  | 395.9046 | 0.6404 | 400.09 | 392.355 | 0.0376 | watch_only | none |
| AAPL | mega_cap_platform | 339.92 |  | 338.7378 | 0.349 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.71 |  | 329.1648 | 1.3808 | 330.21 | 324.97 | 0.024 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 460.415 |  | 454.7309 | 1.25 | 472.485 | 453.76 | 0.2215 | watch_only | none |
| TSM | foundry | 391.305 |  | 386.8503 | 1.1515 | 390.46 | 382.495 | 0.092 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.19 |  | 489.5499 | 0.7436 | 497.64 | 485.42 | 0.075 | watch_only | none |
| SMH | semiconductor_index | 530.95 |  | 526.87 | 0.7744 | 533.01 | 523.325 | 0.0264 | watch_only | none |
| AVGO | custom_silicon_networking | 381.775 |  | 377.9425 | 1.014 | 378.64 | 371.57 | 0.0655 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 820.22 |  | 813.9493 | 0.7704 | 846.4 | 813.91 | 0.0841 | watch_only | none |
| MRVL | custom_silicon_networking | 176.975 |  | 173.697 | 1.8872 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 383.86 |  | 373.9119 | 2.6606 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.77 |  | 44.4158 | 0.7974 | 46.19 | 44.33 | 0.0893 | watch_only | none |
| SMCI | ai_server_oem | 28.315 |  | 27.8812 | 1.5558 | 28.86 | 27.59 | 0.0706 | watch_only | none |
| SPY | market_regime | 741.54 |  | 738.9457 | 0.3511 | 739.42 | 736.57 | 0.0135 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.03 |  | 292.0572 | 0.3331 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.78 |  | 117.6053 | 2.6994 | 117.17 | 115.25 | 1.2171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.76 |  | 66.0661 | 1.0503 | 68.995 | 65.635 | 4.7184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.57 |  | 266.1241 | 0.5433 | 273.86 | 266.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 386.39 |  | 379.8755 | 1.7149 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 586.99 |  | 581.1013 | 1.0134 | 603.25 | 584.69 | 2.1619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 943.26 |  | 936.5007 | 0.7218 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 467.295 |  | 464.5731 | 0.5859 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.21 |  | 138.1216 | 0.788 | 139.755 | 137.31 | 3.8359 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 166.935 |  | 163.6607 | 2.0007 | 165.975 | 160.51 | 1.9049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 239.49 |  | 236.1467 | 1.4158 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 643.79 |  | 628.0924 | 2.4992 | 673.65 | 624.91 | 1.3918 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.765 |  | 336.5647 | 1.248 | 354.09 | 338.14 | 4.7041 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.33 |  | 85.4022 | 2.2573 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 264.54 |  | 258.2912 | 2.4193 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1578.965 |  | 1576.0924 | 0.1823 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.72 |  | 477.2054 | -0.3113 | 494.87 | 477.03 | 1.133 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 268.12 |  | 265.8996 | 0.8351 | 276.85 | 267.14 | 2.6331 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.12 |  | 190.5143 | 0.318 | 194.96 | 189.48 | 0.0209 | watch_only | none |
| TER | semiconductor_test_packaging | 310.74 |  | 307.4516 | 1.0696 | 315.21 | 304.11 | 0.2864 | watch_only | none |
| ONTO | semiconductor_test_packaging | 235.83 |  | 236.449 | -0.2618 | 248.8 | 236.42 | 5.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 45.69 |  | 46.8848 | -2.5483 | 51.64 | 47.435 | 0.2408 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.245 |  | 42.5388 | -0.6907 | 44.155 | 41.78 | 0.8285 | below_vwap | below_vwap,spread_too_wide |
| ENTG | semiconductor_materials | 119.37 |  | 119.4506 | -0.0675 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 284.42 |  | 281.9489 | 0.8764 | 296.8 | 283.22 | 0.6786 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 518.5 |  | 518.5247 | -0.0048 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.54 |  | 295.908 | -0.1244 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.805 |  | 26.5302 | 1.0358 | 27 | 25.42 | 0.0373 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.07 |  | 33.6592 | 1.2205 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.28 |  | 19.9919 | 1.4412 | 20.97 | 19.755 | 0.0493 | watch_only | none |
| SNDK | memory_hbm_storage | 1098.68 |  | 1102.8118 | -0.3747 | 1185.19 | 1114.57 | 3.1856 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 453.81 |  | 436.2409 | 4.0274 | 465.04 | 435.22 | 1.0952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 741.945 |  | 724.7719 | 2.3694 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.52 |  | 230.1021 | 0.6162 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 596.84 |  | 593.665 | 0.5348 | 600.765 | 594.21 | 0.057 | watch_only | none |
| ARM | ai_accelerator | 246.19 |  | 245.1218 | 0.4358 | 253.38 | 243.72 | 0.3087 | watch_only | none |
| SKHY | memory_hbm_storage | 132.04 |  | 131.5613 | 0.3639 | 136.45 | 131.735 | 2.2645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
