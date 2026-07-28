# Intraday State

- Generated at: `2026-07-29T00:39:44+08:00`
- Market time ET: `2026-07-28T12:39:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 6, 'watch_only': 15, 'price_stale_or_missing': 1, 'below_vwap': 3, 'spread_too_wide_or_missing': 27, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.47 |  | 673.5613 | 0.5803 | 677.3 | 670.84 | 0.0089 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 493.37 |  | 489.57 | 0.7762 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| SMH | semiconductor_index | 530.86 |  | 526.9068 | 0.7503 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| SPY | market_regime | 741.625 |  | 738.9959 | 0.3558 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.25 |  | 195.6659 | 0.8096 | 195.4 | 193.65 | 0.1521 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.37 |  | 386.9407 | 1.1447 | 390.46 | 382.495 | 0.1226 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.625 |  | 738.9959 | 0.3558 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 677.47 |  | 673.5613 | 0.5803 | 677.3 | 670.84 | 0.0089 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.64 |  | 329.2867 | 1.322 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 62.1 |  | 60.8888 | 1.9891 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.625 |  | 738.9959 | 0.3558 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 677.47 |  | 673.5613 | 0.5803 | 677.3 | 670.84 | 0.0089 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 293 |  | 292.0832 | 0.3139 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | META | cloud_ai_capex | 595.48 |  | 593.8052 | 0.282 | 600.765 | 594.21 | 0.0571 | watch_only | none |
| 5 | SMH | semiconductor_index | 530.86 |  | 526.9068 | 0.7503 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| 6 | SOXX | semiconductor_index | 493.37 |  | 489.57 | 0.7762 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| 7 | TSM | foundry | 391.37 |  | 386.9407 | 1.1447 | 390.46 | 382.495 | 0.1226 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 398.55 |  | 395.9744 | 0.6504 | 400.09 | 392.355 | 0.0527 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 231.325 |  | 230.1454 | 0.5126 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 10 | AAPL | mega_cap_platform | 340.06 |  | 338.8046 | 0.3705 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 11 | PWR | data_center_power_cooling | 585.5 |  | 581.2152 | 0.7372 | 603.25 | 584.69 | 0.2664 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 333.64 |  | 329.2867 | 1.322 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 26.65 |  | 26.534 | 0.4373 | 27 | 25.42 | 0.2251 | watch_only | none |
| 14 | LIN | industrial_gases | 519.31 |  | 518.5538 | 0.1458 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ASML | semiconductor_equipment | 1578.72 |  | 1576.0905 | 0.1668 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | NVDA | ai_accelerator | 197.25 |  | 195.6659 | 0.8096 | 195.4 | 193.65 | 0.1521 | buy_precheck_manual_confirm | none |
| 17 | MU | memory_hbm_storage | 821.01 |  | 814.1688 | 0.8403 | 846.4 | 813.91 | 0.1474 | watch_only | none |
| 18 | ARM | ai_accelerator | 245.98 |  | 245.1252 | 0.3487 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | APD | industrial_gases | 296.04 |  | 295.9097 | 0.044 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 460.99 |  | 454.8768 | 1.3439 | 472.485 | 453.76 | 0.115 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.25 |  | 195.6659 | 0.8096 | 195.4 | 193.65 | 0.1521 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.37 |  | 386.9407 | 1.1447 | 390.46 | 382.495 | 0.1226 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.625 |  | 738.9959 | 0.3558 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 677.47 |  | 673.5613 | 0.5803 | 677.3 | 670.84 | 0.0089 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.64 |  | 329.2867 | 1.322 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 62.1 |  | 60.8888 | 1.9891 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 381.61 |  | 378.0382 | 0.9448 | 378.64 | 371.57 | 2.7201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 167.07 |  | 163.7514 | 2.0266 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 385.2 |  | 379.9839 | 1.3727 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | LIN | industrial_gases | 519.31 |  | 518.5538 | 0.1458 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ORCL | cloud_ai_capex | 120.68 |  | 117.6775 | 2.5515 | 117.17 | 115.25 | 1.0689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | MU | memory_hbm_storage | 821.01 |  | 814.1688 | 0.8403 | 846.4 | 813.91 | 0.1474 | watch_only | none |
| 13 | SMH | semiconductor_index | 530.86 |  | 526.9068 | 0.7503 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| 14 | SOXX | semiconductor_index | 493.37 |  | 489.57 | 0.7762 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 585.5 |  | 581.2152 | 0.7372 | 603.25 | 584.69 | 0.2664 | watch_only | none |
| 16 | IWM | market_regime | 293 |  | 292.0832 | 0.3139 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 17 | AMD | ai_accelerator | 460.99 |  | 454.8768 | 1.3439 | 472.485 | 453.76 | 0.115 | watch_only | none |
| 18 | META | cloud_ai_capex | 595.48 |  | 593.8052 | 0.282 | 600.765 | 594.21 | 0.0571 | watch_only | none |
| 19 | MSFT | cloud_ai_capex | 398.55 |  | 395.9744 | 0.6504 | 400.09 | 392.355 | 0.0527 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 231.325 |  | 230.1454 | 0.5126 | 233.05 | 229.7 | 0.0173 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.47 |  | 673.5613 | 0.5803 | 677.3 | 670.84 | 0.0089 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.1 |  | 60.8888 | 1.9891 | 62.01 | 60.23 | 0.0322 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.25 |  | 195.6659 | 0.8096 | 195.4 | 193.65 | 0.1521 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.55 |  | 395.9744 | 0.6504 | 400.09 | 392.355 | 0.0527 | watch_only | none |
| AAPL | mega_cap_platform | 340.06 |  | 338.8046 | 0.3705 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.64 |  | 329.2867 | 1.322 | 330.21 | 324.97 | 0.021 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 460.99 |  | 454.8768 | 1.3439 | 472.485 | 453.76 | 0.115 | watch_only | none |
| TSM | foundry | 391.37 |  | 386.9407 | 1.1447 | 390.46 | 382.495 | 0.1226 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.37 |  | 489.57 | 0.7762 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| SMH | semiconductor_index | 530.86 |  | 526.9068 | 0.7503 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| AVGO | custom_silicon_networking | 381.61 |  | 378.0382 | 0.9448 | 378.64 | 371.57 | 2.7201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 821.01 |  | 814.1688 | 0.8403 | 846.4 | 813.91 | 0.1474 | watch_only | none |
| MRVL | custom_silicon_networking | 177.29 |  | 173.7565 | 2.0336 | 181.24 | 172.395 | 1.2014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 384.57 |  | 374.0327 | 2.8172 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.905 |  | 44.4208 | 1.0901 | 46.19 | 44.33 | 0.1113 | watch_only | none |
| SMCI | ai_server_oem | 28.31 |  | 27.8976 | 1.4781 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.625 |  | 738.9959 | 0.3558 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293 |  | 292.0832 | 0.3139 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.68 |  | 117.6775 | 2.5515 | 117.17 | 115.25 | 1.0689 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.72 |  | 66.0778 | 0.9719 | 68.995 | 65.635 | 2.7128 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.16 |  | 266.1373 | 0.3843 | 273.86 | 266.04 | 0.7411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.2 |  | 379.9839 | 1.3727 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.5 |  | 581.2152 | 0.7372 | 603.25 | 584.69 | 0.2664 | watch_only | none |
| GEV | data_center_power_cooling | 944.89 |  | 936.6806 | 0.8764 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 467.33 |  | 464.6965 | 0.5667 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.09 |  | 138.1991 | 0.6446 | 139.755 | 137.31 | 3.9327 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.07 |  | 163.7514 | 2.0266 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.035 |  | 236.1864 | 1.6295 | 256.145 | 236.73 | 4.4702 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 646.62 |  | 628.3679 | 2.9047 | 673.65 | 624.91 | 2.3244 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.57 |  | 336.6477 | 1.1651 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.78 |  | 85.4569 | 2.7185 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.02 |  | 258.5168 | 2.5156 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1578.72 |  | 1576.0905 | 0.1668 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.67 |  | 476.979 | -0.2744 | 494.87 | 477.03 | 2.5438 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 267.81 |  | 265.9201 | 0.7107 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 191.2 |  | 190.5213 | 0.3563 | 194.96 | 189.48 | 0.5962 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 311.11 |  | 307.583 | 1.1467 | 315.21 | 304.11 | 1.1411 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 235.49 |  | 236.4421 | -0.4027 | 248.8 | 236.42 | 4.858 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 45.87 |  | 46.8406 | -2.0721 | 51.64 | 47.435 | 4.5128 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.03 |  | 42.5236 | -1.1607 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.91 |  | 119.432 | -0.4371 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 284.47 |  | 282.0108 | 0.872 | 296.8 | 283.22 | 0.5168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 519.31 |  | 518.5538 | 0.1458 | 518.6 | 511.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.04 |  | 295.9097 | 0.044 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.65 |  | 26.534 | 0.4373 | 27 | 25.42 | 0.2251 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.12 |  | 33.6705 | 1.3349 | 35.08 | 33.52 | 0.0293 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.285 |  | 19.9967 | 1.4419 | 20.97 | 19.755 | 0.0493 | watch_only | none |
| SNDK | memory_hbm_storage | 1100.76 |  | 1102.6442 | -0.1709 | 1185.19 | 1114.57 | 1.181 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 455.245 |  | 436.5513 | 4.2821 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 744.04 |  | 725.0726 | 2.6159 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.325 |  | 230.1454 | 0.5126 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 595.48 |  | 593.8052 | 0.282 | 600.765 | 594.21 | 0.0571 | watch_only | none |
| ARM | ai_accelerator | 245.98 |  | 245.1252 | 0.3487 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.35 |  | 131.5709 | 0.5921 | 136.45 | 131.735 | 0.4005 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
