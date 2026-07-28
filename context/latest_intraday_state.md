# Intraday State

- Generated at: `2026-07-29T00:55:05+08:00`
- Market time ET: `2026-07-28T12:55:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'watch_only': 10, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1, 'below_vwap': 2, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 679.14 |  | 673.6574 | 0.8138 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 496.265 |  | 489.7177 | 1.337 | 497.64 | 485.42 | 0.0544 | watch_only | none |
| SMH | semiconductor_index | 533.715 |  | 527.0007 | 1.2741 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.515 |  | 739.0997 | 0.4621 | 739.42 | 736.57 | 0.0215 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.97 |  | 195.7369 | 1.1409 | 195.4 | 193.65 | 0.0758 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 533.715 |  | 527.0007 | 1.2741 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.515 |  | 739.0997 | 0.4621 | 739.42 | 736.57 | 0.0215 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 679.14 |  | 673.6574 | 0.8138 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1587.39 |  | 1576.4538 | 0.6937 | 1586.01 | 1565.95 | 0.0712 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 334.16 |  | 329.4525 | 1.4289 | 330.21 | 324.97 | 0.2963 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.52 |  | 292.1291 | 0.4761 | 293.26 | 291.55 | 0.017 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.5 |  | 60.9515 | 2.5405 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1587.39 |  | 1576.4538 | 0.6937 | 1586.01 | 1565.95 | 0.0712 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.52 |  | 292.1291 | 0.4761 | 293.26 | 291.55 | 0.017 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.515 |  | 739.0997 | 0.4621 | 739.42 | 736.57 | 0.0215 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 339.83 |  | 338.8422 | 0.2915 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 5 | SMH | semiconductor_index | 533.715 |  | 527.0007 | 1.2741 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 679.14 |  | 673.6574 | 0.8138 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 398.6 |  | 396.0397 | 0.6465 | 400.09 | 392.355 | 0.0276 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 231.71 |  | 230.1937 | 0.6587 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 9 | NVDA | ai_accelerator | 197.97 |  | 195.7369 | 1.1409 | 195.4 | 193.65 | 0.0758 | buy_precheck_manual_confirm | none |
| 10 | MU | memory_hbm_storage | 826.045 |  | 814.5819 | 1.4072 | 846.4 | 813.91 | 0.0484 | watch_only | none |
| 11 | SOXX | semiconductor_index | 496.265 |  | 489.7177 | 1.337 | 497.64 | 485.42 | 0.0544 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 334.16 |  | 329.4525 | 1.4289 | 330.21 | 324.97 | 0.2963 | buy_precheck_manual_confirm | none |
| 13 | COHU | semiconductor_test_packaging | 42.52 |  | 42.5158 | 0.0098 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | HPE | ai_server_oem | 44.95 |  | 44.4385 | 1.1511 | 46.19 | 44.33 | 0.0445 | watch_only | none |
| 15 | LIN | industrial_gases | 518.685 |  | 518.5672 | 0.0227 | 518.6 | 511.495 | 4.3437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | APLD | high_beta_ai_infrastructure | 26.86 |  | 26.538 | 1.2134 | 27 | 25.42 | 0.1489 | watch_only | none |
| 17 | TT | data_center_power_cooling | 468.07 |  | 464.7858 | 0.7066 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | META | cloud_ai_capex | 595 |  | 593.8332 | 0.1965 | 600.765 | 594.21 | 1.0319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ENTG | semiconductor_materials | 120.12 |  | 119.4369 | 0.572 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMAT | semiconductor_equipment | 479.73 |  | 476.9741 | 0.5778 | 494.87 | 477.03 | 1.1381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.97 |  | 195.7369 | 1.1409 | 195.4 | 193.65 | 0.0758 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 533.715 |  | 527.0007 | 1.2741 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.515 |  | 739.0997 | 0.4621 | 739.42 | 736.57 | 0.0215 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 679.14 |  | 673.6574 | 0.8138 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1587.39 |  | 1576.4538 | 0.6937 | 1586.01 | 1565.95 | 0.0712 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 334.16 |  | 329.4525 | 1.4289 | 330.21 | 324.97 | 0.2963 | buy_precheck_manual_confirm | none |
| 7 | IWM | market_regime | 293.52 |  | 292.1291 | 0.4761 | 293.26 | 291.55 | 0.017 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.5 |  | 60.9515 | 2.5405 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 392.855 |  | 387.0814 | 1.4916 | 390.46 | 382.495 | 2.6473 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | AVGO | custom_silicon_networking | 383.85 |  | 378.2193 | 1.4887 | 378.64 | 371.57 | 3.3763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ANET | ai_networking_optical | 168.49 |  | 163.8822 | 2.8117 | 165.975 | 160.51 | 4.024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ETN | data_center_power_cooling | 386.33 |  | 380.2253 | 1.6055 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | LIN | industrial_gases | 518.685 |  | 518.5672 | 0.0227 | 518.6 | 511.495 | 4.3437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 121.2 |  | 117.7993 | 2.8869 | 117.17 | 115.25 | 0.6683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MU | memory_hbm_storage | 826.045 |  | 814.5819 | 1.4072 | 846.4 | 813.91 | 0.0484 | watch_only | none |
| 16 | SOXX | semiconductor_index | 496.265 |  | 489.7177 | 1.337 | 497.64 | 485.42 | 0.0544 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 398.6 |  | 396.0397 | 0.6465 | 400.09 | 392.355 | 0.0276 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.71 |  | 230.1937 | 0.6587 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.95 |  | 44.4385 | 1.1511 | 46.19 | 44.33 | 0.0445 | watch_only | none |
| 20 | SMCI | ai_server_oem | 28.58 |  | 27.9124 | 2.3919 | 28.86 | 27.59 | 0.035 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 679.14 |  | 673.6574 | 0.8138 | 677.3 | 670.84 | 0.0309 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.5 |  | 60.9515 | 2.5405 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.97 |  | 195.7369 | 1.1409 | 195.4 | 193.65 | 0.0758 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.6 |  | 396.0397 | 0.6465 | 400.09 | 392.355 | 0.0276 | watch_only | none |
| AAPL | mega_cap_platform | 339.83 |  | 338.8422 | 0.2915 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.16 |  | 329.4525 | 1.4289 | 330.21 | 324.97 | 0.2963 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 462.34 |  | 455.017 | 1.6094 | 472.485 | 453.76 | 3.8673 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.855 |  | 387.0814 | 1.4916 | 390.46 | 382.495 | 2.6473 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 496.265 |  | 489.7177 | 1.337 | 497.64 | 485.42 | 0.0544 | watch_only | none |
| SMH | semiconductor_index | 533.715 |  | 527.0007 | 1.2741 | 533.01 | 523.325 | 0.0618 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 383.85 |  | 378.2193 | 1.4887 | 378.64 | 371.57 | 3.3763 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 826.045 |  | 814.5819 | 1.4072 | 846.4 | 813.91 | 0.0484 | watch_only | none |
| MRVL | custom_silicon_networking | 178.71 |  | 173.866 | 2.7861 | 181.24 | 172.395 | 1.8689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 386.47 |  | 374.1912 | 3.2814 | 402 | 374.02 | 0.8099 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.95 |  | 44.4385 | 1.1511 | 46.19 | 44.33 | 0.0445 | watch_only | none |
| SMCI | ai_server_oem | 28.58 |  | 27.9124 | 2.3919 | 28.86 | 27.59 | 0.035 | watch_only | none |
| SPY | market_regime | 742.515 |  | 739.0997 | 0.4621 | 739.42 | 736.57 | 0.0215 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.52 |  | 292.1291 | 0.4761 | 293.26 | 291.55 | 0.017 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 121.2 |  | 117.7993 | 2.8869 | 117.17 | 115.25 | 0.6683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67.8 |  | 66.125 | 2.5331 | 68.995 | 65.635 | 4.4248 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.285 |  | 266.1822 | 1.1657 | 273.86 | 266.04 | 0.4011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.33 |  | 380.2253 | 1.6055 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 587.74 |  | 581.3481 | 1.0995 | 603.25 | 584.69 | 5.0567 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 949.27 |  | 936.907 | 1.3196 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.07 |  | 464.7858 | 0.7066 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.75 |  | 138.2451 | 1.0886 | 139.755 | 137.31 | 3.542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 168.49 |  | 163.8822 | 2.8117 | 165.975 | 160.51 | 4.024 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 243.36 |  | 236.3427 | 2.9691 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 654.61 |  | 629.4722 | 3.9935 | 673.65 | 624.91 | 1.4986 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 344.91 |  | 336.7381 | 2.4268 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 89.18 |  | 85.5569 | 4.2347 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.87 |  | 258.611 | 2.8069 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1587.39 |  | 1576.4538 | 0.6937 | 1586.01 | 1565.95 | 0.0712 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 479.73 |  | 476.9741 | 0.5778 | 494.87 | 477.03 | 1.1381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 271.22 |  | 266.064 | 1.9379 | 276.85 | 267.14 | 3.676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.155 |  | 190.5686 | 1.3572 | 194.96 | 189.48 | 1.636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 313.88 |  | 307.7724 | 1.9845 | 315.21 | 304.11 | 0.4492 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 237.62 |  | 236.4864 | 0.4794 | 248.8 | 236.42 | 4.4399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.16 |  | 46.8268 | -1.4239 | 51.64 | 47.435 | 0.325 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.52 |  | 42.5158 | 0.0098 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 120.12 |  | 119.4369 | 0.572 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 287.23 |  | 282.1475 | 1.8014 | 296.8 | 283.22 | 0.4491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 518.685 |  | 518.5672 | 0.0227 | 518.6 | 511.495 | 4.3437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.86 |  | 295.9065 | -0.0157 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.86 |  | 26.538 | 1.2134 | 27 | 25.42 | 0.1489 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.43 |  | 33.6868 | 2.2063 | 35.08 | 33.52 | 0.029 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.37 |  | 20.0048 | 1.8258 | 20.97 | 19.755 | 0.0491 | watch_only | none |
| SNDK | memory_hbm_storage | 1107.17 |  | 1102.7001 | 0.4054 | 1185.19 | 1114.57 | 1.885 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 460.37 |  | 437.1478 | 5.3122 | 465.04 | 435.22 | 4.8874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 751.3 |  | 725.6118 | 3.5402 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.71 |  | 230.1937 | 0.6587 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 595 |  | 593.8332 | 0.1965 | 600.765 | 594.21 | 1.0319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 248.9 |  | 245.2062 | 1.5064 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.715 |  | 131.5991 | 1.6078 | 136.45 | 131.735 | 0.3814 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
