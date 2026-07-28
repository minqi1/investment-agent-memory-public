# Intraday State

- Generated at: `2026-07-29T00:32:00+08:00`
- Market time ET: `2026-07-28T12:32:01-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 16, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.57 |  | 673.4644 | 0.4611 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.02 |  | 489.5607 | 0.2981 | 497.64 | 485.42 | 0.0774 | watch_only | none |
| SMH | semiconductor_index | 529.22 |  | 526.8845 | 0.4433 | 533.01 | 523.325 | 0.0397 | watch_only | none |
| SPY | market_regime | 741.03 |  | 738.9676 | 0.2791 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.695 |  | 195.6426 | 0.5379 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.155 |  | 377.9768 | 0.5763 | 378.64 | 371.57 | 0.292 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.03 |  | 738.9676 | 0.2791 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.41 |  | 163.674 | 1.6716 | 165.975 | 160.51 | 0.1082 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.495 |  | 329.2049 | 1.3032 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.03 |  | 738.9676 | 0.2791 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 196.695 |  | 195.6426 | 0.5379 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 491.02 |  | 489.5607 | 0.2981 | 497.64 | 485.42 | 0.0774 | watch_only | none |
| 4 | IWM | market_regime | 292.81 |  | 292.0727 | 0.2524 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 5 | AVGO | custom_silicon_networking | 380.155 |  | 377.9768 | 0.5763 | 378.64 | 371.57 | 0.292 | buy_precheck_manual_confirm | none |
| 6 | APLD | high_beta_ai_infrastructure | 26.62 |  | 26.5316 | 0.3331 | 27 | 25.42 | 0.0751 | watch_only | none |
| 7 | SMH | semiconductor_index | 529.22 |  | 526.8845 | 0.4433 | 533.01 | 523.325 | 0.0397 | watch_only | none |
| 8 | QQQ | market_regime | 676.57 |  | 673.4644 | 0.4611 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 9 | META | cloud_ai_capex | 596.54 |  | 593.6854 | 0.4808 | 600.765 | 594.21 | 0.0838 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 398.34 |  | 395.9327 | 0.608 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 11 | AMZN | cloud_ai_capex | 231.44 |  | 230.1234 | 0.5721 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 12 | HPE | ai_server_oem | 44.74 |  | 44.418 | 0.7249 | 46.19 | 44.33 | 0.0894 | watch_only | none |
| 13 | IREN | high_beta_ai_infrastructure | 33.91 |  | 33.6641 | 0.7303 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| 14 | AAPL | mega_cap_platform | 340.08 |  | 338.7567 | 0.3906 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 15 | TT | data_center_power_cooling | 467.61 |  | 464.6489 | 0.6373 | 477.73 | 460.77 | 0.201 | watch_only | none |
| 16 | GOOGL | cloud_ai_capex | 333.495 |  | 329.2049 | 1.3032 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 17 | ANET | ai_networking_optical | 166.41 |  | 163.674 | 1.6716 | 165.975 | 160.51 | 0.1082 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 28.245 |  | 27.8874 | 1.2824 | 28.86 | 27.59 | 0.0708 | watch_only | none |
| 19 | LIN | industrial_gases | 518.93 |  | 518.5246 | 0.0782 | 518.6 | 511.495 | 4.2761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CORZ | high_beta_ai_infrastructure | 20.24 |  | 19.9941 | 1.2298 | 20.97 | 19.755 | 0.0988 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.695 |  | 195.6426 | 0.5379 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.155 |  | 377.9768 | 0.5763 | 378.64 | 371.57 | 0.292 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.03 |  | 738.9676 | 0.2791 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.41 |  | 163.674 | 1.6716 | 165.975 | 160.51 | 0.1082 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.495 |  | 329.2049 | 1.3032 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 6 | ETN | data_center_power_cooling | 385.83 |  | 379.9276 | 1.5535 | 384.565 | 377.43 | 3.9318 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 518.93 |  | 518.5246 | 0.0782 | 518.6 | 511.495 | 4.2761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ORCL | cloud_ai_capex | 120.39 |  | 117.6308 | 2.3457 | 117.17 | 115.25 | 4.502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 529.22 |  | 526.8845 | 0.4433 | 533.01 | 523.325 | 0.0397 | watch_only | none |
| 10 | SOXX | semiconductor_index | 491.02 |  | 489.5607 | 0.2981 | 497.64 | 485.42 | 0.0774 | watch_only | none |
| 11 | QQQ | market_regime | 676.57 |  | 673.4644 | 0.4611 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 12 | TT | data_center_power_cooling | 467.61 |  | 464.6489 | 0.6373 | 477.73 | 460.77 | 0.201 | watch_only | none |
| 13 | STX | memory_hbm_storage | 740.78 |  | 724.8574 | 2.1966 | 774.805 | 719.02 | 0.3132 | watch_only | none |
| 14 | IWM | market_regime | 292.81 |  | 292.0727 | 0.2524 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 15 | META | cloud_ai_capex | 596.54 |  | 593.6854 | 0.4808 | 600.765 | 594.21 | 0.0838 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 398.34 |  | 395.9327 | 0.608 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.44 |  | 230.1234 | 0.5721 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 18 | HPE | ai_server_oem | 44.74 |  | 44.418 | 0.7249 | 46.19 | 44.33 | 0.0894 | watch_only | none |
| 19 | SMCI | ai_server_oem | 28.245 |  | 27.8874 | 1.2824 | 28.86 | 27.59 | 0.0708 | watch_only | none |
| 20 | IREN | high_beta_ai_infrastructure | 33.91 |  | 33.6641 | 0.7303 | 35.08 | 33.52 | 0.0295 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.57 |  | 673.4644 | 0.4611 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.84 |  | 60.8716 | 1.591 | 62.01 | 60.23 | 0.0323 | watch_only | none |
| NVDA | ai_accelerator | 196.695 |  | 195.6426 | 0.5379 | 195.4 | 193.65 | 0.0153 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.34 |  | 395.9327 | 0.608 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| AAPL | mega_cap_platform | 340.08 |  | 338.7567 | 0.3906 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.495 |  | 329.2049 | 1.3032 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.12 |  | 454.7815 | 0.7341 | 472.485 | 453.76 | 3.0254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 389.91 |  | 386.8889 | 0.7809 | 390.46 | 382.495 | 1.349 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.02 |  | 489.5607 | 0.2981 | 497.64 | 485.42 | 0.0774 | watch_only | none |
| SMH | semiconductor_index | 529.22 |  | 526.8845 | 0.4433 | 533.01 | 523.325 | 0.0397 | watch_only | none |
| AVGO | custom_silicon_networking | 380.155 |  | 377.9768 | 0.5763 | 378.64 | 371.57 | 0.292 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 818.62 |  | 813.9962 | 0.568 | 846.4 | 813.91 | 0.9125 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.21 |  | 173.715 | 1.4363 | 181.24 | 172.395 | 1.4755 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 382.54 |  | 373.9587 | 2.2947 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.74 |  | 44.418 | 0.7249 | 46.19 | 44.33 | 0.0894 | watch_only | none |
| SMCI | ai_server_oem | 28.245 |  | 27.8874 | 1.2824 | 28.86 | 27.59 | 0.0708 | watch_only | none |
| SPY | market_regime | 741.03 |  | 738.9676 | 0.2791 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.81 |  | 292.0727 | 0.2524 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.39 |  | 117.6308 | 2.3457 | 117.17 | 115.25 | 4.502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.59 |  | 66.0701 | 0.7869 | 68.995 | 65.635 | 2.2526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.61 |  | 266.1298 | 0.1804 | 273.86 | 266.04 | 0.6714 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.83 |  | 379.9276 | 1.5535 | 384.565 | 377.43 | 3.9318 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 586.44 |  | 581.159 | 0.9087 | 603.25 | 584.69 | 1.9559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 943.81 |  | 936.5898 | 0.7709 | 955.825 | 935.665 | 2.8438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 467.61 |  | 464.6489 | 0.6373 | 477.73 | 460.77 | 0.201 | watch_only | none |
| JCI | data_center_power_cooling | 139.195 |  | 138.1566 | 0.7516 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.41 |  | 163.674 | 1.6716 | 165.975 | 160.51 | 0.1082 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 238.785 |  | 236.1586 | 1.1121 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 643.76 |  | 628.2661 | 2.4661 | 673.65 | 624.91 | 1.9728 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.33 |  | 336.5917 | 1.1106 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.225 |  | 85.4184 | 2.115 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 264.905 |  | 258.3689 | 2.5298 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1573.01 |  | 1576.1307 | -0.198 | 1586.01 | 1565.95 | 0.0598 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 473.97 |  | 477.17 | -0.6706 | 494.87 | 477.03 | 0.4789 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 266.825 |  | 265.9091 | 0.3444 | 276.85 | 267.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 190.26 |  | 190.5228 | -0.1379 | 194.96 | 189.48 | 0.042 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 308.94 |  | 307.5113 | 0.4646 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 235.9 |  | 236.4443 | -0.2302 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.59 |  | 46.8633 | -2.717 | 51.64 | 47.435 | 1.1187 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.14 |  | 42.5326 | -0.9231 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.57 |  | 119.4482 | -0.7352 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 283.55 |  | 281.9763 | 0.5581 | 296.8 | 283.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 518.93 |  | 518.5246 | 0.0782 | 518.6 | 511.495 | 4.2761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.86 |  | 295.9067 | -0.0158 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.62 |  | 26.5316 | 0.3331 | 27 | 25.42 | 0.0751 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.91 |  | 33.6641 | 0.7303 | 35.08 | 33.52 | 0.0295 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.24 |  | 19.9941 | 1.2298 | 20.97 | 19.755 | 0.0988 | watch_only | none |
| SNDK | memory_hbm_storage | 1093.58 |  | 1102.7676 | -0.8331 | 1185.19 | 1114.57 | 1.2637 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 452.825 |  | 436.3542 | 3.7746 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 740.78 |  | 724.8574 | 2.1966 | 774.805 | 719.02 | 0.3132 | watch_only | none |
| AMZN | cloud_ai_capex | 231.44 |  | 230.1234 | 0.5721 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 596.54 |  | 593.6854 | 0.4808 | 600.765 | 594.21 | 0.0838 | watch_only | none |
| ARM | ai_accelerator | 245 |  | 245.1273 | -0.052 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131.505 |  | 131.5655 | -0.046 | 136.45 | 131.735 | 1.5361 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
