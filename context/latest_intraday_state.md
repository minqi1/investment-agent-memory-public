# Intraday State

- Generated at: `2026-07-28T23:45:39+08:00`
- Market time ET: `2026-07-28T11:45:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'spread_too_wide_or_missing': 29, 'watch_only': 8, 'price_stale_or_missing': 1, 'below_vwap': 4, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.23 |  | 672.6034 | 0.8365 | 677.3 | 670.84 | 0.0354 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 495.96 |  | 489.0399 | 1.415 | 497.64 | 485.42 | 0.0625 | watch_only | none |
| SMH | semiconductor_index | 533.72 |  | 526.3005 | 1.4097 | 533.01 | 523.325 | 0.0656 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.07 |  | 738.4511 | 0.4901 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 533.72 |  | 526.3005 | 1.4097 | 533.01 | 523.325 | 0.0656 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 383.93 |  | 377.0602 | 1.8219 | 378.64 | 371.57 | 0.1459 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.07 |  | 738.4511 | 0.4901 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.23 |  | 672.6034 | 0.8365 | 677.3 | 670.84 | 0.0354 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.33 |  | 328.5571 | 1.4527 | 330.21 | 324.97 | 0.006 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.35 |  | 291.9488 | 0.4799 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.23 |  | 116.9392 | 2.8141 | 117.17 | 115.25 | 0.2911 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.29 |  | 60.6605 | 2.6863 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 293.35 |  | 291.9488 | 0.4799 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 742.07 |  | 738.4511 | 0.4901 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 230.37 |  | 229.9251 | 0.1935 | 233.05 | 229.7 | 0.0174 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.63 |  | 338.5988 | 0.3046 | 342.87 | 337.78 | 0.0177 | watch_only | none |
| 5 | SMH | semiconductor_index | 533.72 |  | 526.3005 | 1.4097 | 533.01 | 523.325 | 0.0656 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 678.23 |  | 672.6034 | 0.8365 | 677.3 | 670.84 | 0.0354 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.33 |  | 328.5571 | 1.4527 | 330.21 | 324.97 | 0.006 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 495.96 |  | 489.0399 | 1.415 | 497.64 | 485.42 | 0.0625 | watch_only | none |
| 9 | TT | data_center_power_cooling | 468.33 |  | 464.3903 | 0.8484 | 477.73 | 460.77 | 0.1922 | watch_only | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.17 |  | 19.9483 | 1.1115 | 20.97 | 19.755 | 0.0496 | watch_only | none |
| 11 | AVGO | custom_silicon_networking | 383.93 |  | 377.0602 | 1.8219 | 378.64 | 371.57 | 0.1459 | buy_precheck_manual_confirm | none |
| 12 | ARM | ai_accelerator | 246.69 |  | 244.8613 | 0.7468 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ONTO | semiconductor_test_packaging | 236.9 |  | 236.3726 | 0.2231 | 248.8 | 236.42 | 4.6729 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | HPE | ai_server_oem | 45.07 |  | 44.2964 | 1.7464 | 46.19 | 44.33 | 0.1331 | watch_only | none |
| 15 | AMAT | semiconductor_equipment | 480.11 |  | 476.7453 | 0.7058 | 494.87 | 477.03 | 1.5788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SMCI | ai_server_oem | 28.51 |  | 27.8034 | 2.5412 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 34.545 |  | 33.4987 | 3.1234 | 35.08 | 33.52 | 0.0579 | watch_only | none |
| 18 | MSFT | cloud_ai_capex | 398.8 |  | 395.6667 | 0.7919 | 400.09 | 392.355 | 0.657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ENTG | semiconductor_materials | 119.96 |  | 119.3914 | 0.4763 | 121 | 117.72 | 0.5335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ORCL | cloud_ai_capex | 120.23 |  | 116.9392 | 2.8141 | 117.17 | 115.25 | 0.2911 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 533.72 |  | 526.3005 | 1.4097 | 533.01 | 523.325 | 0.0656 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 383.93 |  | 377.0602 | 1.8219 | 378.64 | 371.57 | 0.1459 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 742.07 |  | 738.4511 | 0.4901 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 678.23 |  | 672.6034 | 0.8365 | 677.3 | 670.84 | 0.0354 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 333.33 |  | 328.5571 | 1.4527 | 330.21 | 324.97 | 0.006 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 293.35 |  | 291.9488 | 0.4799 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 120.23 |  | 116.9392 | 2.8141 | 117.17 | 115.25 | 0.2911 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 62.29 |  | 60.6605 | 2.6863 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 197.77 |  | 195.1691 | 1.3327 | 195.4 | 193.65 | 0.4753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | TSM | foundry | 392.23 |  | 385.7674 | 1.6753 | 390.46 | 382.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ASML | semiconductor_equipment | 1586.35 |  | 1572.9827 | 0.8498 | 1586.01 | 1565.95 | 0.5718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ANET | ai_networking_optical | 166.145 |  | 163.176 | 1.8195 | 165.975 | 160.51 | 1.282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ETN | data_center_power_cooling | 384.99 |  | 379.2291 | 1.5191 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SOXX | semiconductor_index | 495.96 |  | 489.0399 | 1.415 | 497.64 | 485.42 | 0.0625 | watch_only | none |
| 15 | TT | data_center_power_cooling | 468.33 |  | 464.3903 | 0.8484 | 477.73 | 460.77 | 0.1922 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 230.37 |  | 229.9251 | 0.1935 | 233.05 | 229.7 | 0.0174 | watch_only | none |
| 17 | HPE | ai_server_oem | 45.07 |  | 44.2964 | 1.7464 | 46.19 | 44.33 | 0.1331 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.51 |  | 27.8034 | 2.5412 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34.545 |  | 33.4987 | 3.1234 | 35.08 | 33.52 | 0.0579 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.63 |  | 338.5988 | 0.3046 | 342.87 | 337.78 | 0.0177 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.23 |  | 672.6034 | 0.8365 | 677.3 | 670.84 | 0.0354 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.29 |  | 60.6605 | 2.6863 | 62.01 | 60.23 | 0.0161 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 197.77 |  | 195.1691 | 1.3327 | 195.4 | 193.65 | 0.4753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 398.8 |  | 395.6667 | 0.7919 | 400.09 | 392.355 | 0.657 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 339.63 |  | 338.5988 | 0.3046 | 342.87 | 337.78 | 0.0177 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.33 |  | 328.5571 | 1.4527 | 330.21 | 324.97 | 0.006 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 461.72 |  | 453.3505 | 1.8461 | 472.485 | 453.76 | 2.8805 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.23 |  | 385.7674 | 1.6753 | 390.46 | 382.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 495.96 |  | 489.0399 | 1.415 | 497.64 | 485.42 | 0.0625 | watch_only | none |
| SMH | semiconductor_index | 533.72 |  | 526.3005 | 1.4097 | 533.01 | 523.325 | 0.0656 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 383.93 |  | 377.0602 | 1.8219 | 378.64 | 371.57 | 0.1459 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 824.4 |  | 812.61 | 1.4509 | 846.4 | 813.91 | 0.4367 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 178.26 |  | 173.1204 | 2.9688 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 382.71 |  | 372.6697 | 2.6942 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.07 |  | 44.2964 | 1.7464 | 46.19 | 44.33 | 0.1331 | watch_only | none |
| SMCI | ai_server_oem | 28.51 |  | 27.8034 | 2.5412 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 742.07 |  | 738.4511 | 0.4901 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.35 |  | 291.9488 | 0.4799 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.23 |  | 116.9392 | 2.8141 | 117.17 | 115.25 | 0.2911 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.66 |  | 65.9414 | 1.0898 | 68.995 | 65.635 | 3.8554 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 268.55 |  | 265.7372 | 1.0585 | 273.86 | 266.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 384.99 |  | 379.2291 | 1.5191 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 584.63 |  | 579.4819 | 0.8884 | 603.25 | 584.69 | 3.5971 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 949.18 |  | 933.9269 | 1.6332 | 955.825 | 935.665 | 1.0883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.33 |  | 464.3903 | 0.8484 | 477.73 | 460.77 | 0.1922 | watch_only | none |
| JCI | data_center_power_cooling | 139.23 |  | 137.9829 | 0.9038 | 139.755 | 137.31 | 3.8067 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 166.145 |  | 163.176 | 1.8195 | 165.975 | 160.51 | 1.282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 238.76 |  | 235.8729 | 1.224 | 256.145 | 236.73 | 0.5152 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 639.665 |  | 625.3666 | 2.2864 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 336.75 |  | 335.9919 | 0.2256 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 87.29 |  | 85.1177 | 2.5521 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 263.65 |  | 256.5377 | 2.7724 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1586.35 |  | 1572.9827 | 0.8498 | 1586.01 | 1565.95 | 0.5718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 480.11 |  | 476.7453 | 0.7058 | 494.87 | 477.03 | 1.5788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 267.81 |  | 265.5868 | 0.8371 | 276.85 | 267.14 | 0.5601 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 192.53 |  | 190.1002 | 1.2782 | 194.96 | 189.48 | 3.9838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 313.08 |  | 306.0815 | 2.2865 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 236.9 |  | 236.3726 | 0.2231 | 248.8 | 236.42 | 4.6729 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.56 |  | 47.066 | -1.075 | 51.64 | 47.435 | 4.9828 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.53 |  | 42.5459 | -0.0374 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.96 |  | 119.3914 | 0.4763 | 121 | 117.72 | 0.5335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 282.82 |  | 281.5381 | 0.4553 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 517.695 |  | 518.6017 | -0.1748 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.44 |  | 296.1565 | -0.5796 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.72 |  | 26.4425 | 1.0493 | 27 | 25.42 | 0.7485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.545 |  | 33.4987 | 3.1234 | 35.08 | 33.52 | 0.0579 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.17 |  | 19.9483 | 1.1115 | 20.97 | 19.755 | 0.0496 | watch_only | none |
| SNDK | memory_hbm_storage | 1104.68 |  | 1101.8366 | 0.2581 | 1185.19 | 1114.57 | 3.42 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 448.01 |  | 434.5574 | 3.0957 | 465.04 | 435.22 | 2.6785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 736.82 |  | 723.1987 | 1.8835 | 774.805 | 719.02 | 1.5838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.37 |  | 229.9251 | 0.1935 | 233.05 | 229.7 | 0.0174 | watch_only | none |
| META | cloud_ai_capex | 594.09 |  | 593.2009 | 0.1499 | 600.765 | 594.21 | 0.7743 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 246.69 |  | 244.8613 | 0.7468 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.07 |  | 131.3534 | 1.3068 | 136.45 | 131.735 | 1.781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
