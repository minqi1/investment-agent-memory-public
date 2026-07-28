# Intraday State

- Generated at: `2026-07-29T02:38:34+08:00`
- Market time ET: `2026-07-28T14:38:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 13, 'manual_confirm_candidate': 3, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.07 |  | 674.1167 | 0.2898 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| SOXX | semiconductor_index | 491.26 |  | 489.9687 | 0.2636 | 497.64 | 485.42 | 0.0387 | watch_only | none |
| SMH | semiconductor_index | 529.38 |  | 527.3472 | 0.3855 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| SPY | market_regime | 740.93 |  | 739.5254 | 0.1899 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.235 |  | 196.0555 | 0.6016 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.93 |  | 739.5254 | 0.1899 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.97 |  | 330.7361 | 1.2802 | 330.21 | 324.97 | 0.0358 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.93 |  | 739.5254 | 0.1899 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 491.26 |  | 489.9687 | 0.2636 | 497.64 | 485.42 | 0.0387 | watch_only | none |
| 3 | QQQ | market_regime | 676.07 |  | 674.1167 | 0.2898 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| 4 | IWM | market_regime | 292.93 |  | 292.3671 | 0.1925 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 5 | KLAC | semiconductor_equipment | 191.255 |  | 190.7639 | 0.2574 | 194.96 | 189.48 | 0.1098 | watch_only | none |
| 6 | NVDA | ai_accelerator | 197.235 |  | 196.0555 | 0.6016 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 231.18 |  | 230.4795 | 0.3039 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 8 | HPE | ai_server_oem | 44.49 |  | 44.4399 | 0.1128 | 46.19 | 44.33 | 0.0899 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 339.23 |  | 338.9666 | 0.0777 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 397.24 |  | 396.3608 | 0.2218 | 400.09 | 392.355 | 0.2819 | watch_only | none |
| 11 | SMH | semiconductor_index | 529.38 |  | 527.3472 | 0.3855 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 139.635 |  | 138.54 | 0.7904 | 139.755 | 137.31 | 0.2721 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 334.97 |  | 330.7361 | 1.2802 | 330.21 | 324.97 | 0.0358 | buy_precheck_manual_confirm | none |
| 14 | TT | data_center_power_cooling | 466.79 |  | 465.2022 | 0.3413 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SMCI | ai_server_oem | 28.26 |  | 27.9983 | 0.9345 | 28.86 | 27.59 | 0.0708 | watch_only | none |
| 16 | ASML | semiconductor_equipment | 1583.23 |  | 1577.2725 | 0.3777 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | GEV | data_center_power_cooling | 938.44 |  | 937.549 | 0.095 | 955.825 | 935.665 | 2.3624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 456.35 |  | 455.5317 | 0.1796 | 472.485 | 453.76 | 0.4426 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 175.02 |  | 174.19 | 0.4765 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 238.38 |  | 236.7502 | 0.6884 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.235 |  | 196.0555 | 0.6016 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.93 |  | 739.5254 | 0.1899 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.97 |  | 330.7361 | 1.2802 | 330.21 | 324.97 | 0.0358 | buy_precheck_manual_confirm | none |
| 4 | TSM | foundry | 392.09 |  | 387.7046 | 1.1311 | 390.46 | 382.495 | 0.8952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AVGO | custom_silicon_networking | 380.17 |  | 378.5909 | 0.4171 | 378.64 | 371.57 | 2.32 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 168.615 |  | 164.8782 | 2.2664 | 165.975 | 160.51 | 3.8253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ETN | data_center_power_cooling | 384.6 |  | 381.2047 | 0.8907 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ORCL | cloud_ai_capex | 120.56 |  | 118.474 | 1.7608 | 117.17 | 115.25 | 1.2774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 529.38 |  | 527.3472 | 0.3855 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| 10 | SOXX | semiconductor_index | 491.26 |  | 489.9687 | 0.2636 | 497.64 | 485.42 | 0.0387 | watch_only | none |
| 11 | QQQ | market_regime | 676.07 |  | 674.1167 | 0.2898 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 139.635 |  | 138.54 | 0.7904 | 139.755 | 137.31 | 0.2721 | watch_only | none |
| 13 | IWM | market_regime | 292.93 |  | 292.3671 | 0.1925 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 14 | KLAC | semiconductor_equipment | 191.255 |  | 190.7639 | 0.2574 | 194.96 | 189.48 | 0.1098 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 397.24 |  | 396.3608 | 0.2218 | 400.09 | 392.355 | 0.2819 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 231.18 |  | 230.4795 | 0.3039 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 17 | HPE | ai_server_oem | 44.49 |  | 44.4399 | 0.1128 | 46.19 | 44.33 | 0.0899 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.26 |  | 27.9983 | 0.9345 | 28.86 | 27.59 | 0.0708 | watch_only | none |
| 19 | AAPL | mega_cap_platform | 339.23 |  | 338.9666 | 0.0777 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 20 | CORZ | high_beta_ai_infrastructure | 20.72 |  | 20.0707 | 3.2351 | 20.97 | 19.755 | 0.0483 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.07 |  | 674.1167 | 0.2898 | 677.3 | 670.84 | 0.0074 | watch_only | none |
| TQQQ | leveraged_tool | 61.67 |  | 61.1056 | 0.9237 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.235 |  | 196.0555 | 0.6016 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.24 |  | 396.3608 | 0.2218 | 400.09 | 392.355 | 0.2819 | watch_only | none |
| AAPL | mega_cap_platform | 339.23 |  | 338.9666 | 0.0777 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.97 |  | 330.7361 | 1.2802 | 330.21 | 324.97 | 0.0358 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.35 |  | 455.5317 | 0.1796 | 472.485 | 453.76 | 0.4426 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 392.09 |  | 387.7046 | 1.1311 | 390.46 | 382.495 | 0.8952 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.26 |  | 489.9687 | 0.2636 | 497.64 | 485.42 | 0.0387 | watch_only | none |
| SMH | semiconductor_index | 529.38 |  | 527.3472 | 0.3855 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| AVGO | custom_silicon_networking | 380.17 |  | 378.5909 | 0.4171 | 378.64 | 371.57 | 2.32 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 819.01 |  | 815.3555 | 0.4482 | 846.4 | 813.91 | 0.7936 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 175.02 |  | 174.19 | 0.4765 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 385.56 |  | 375.0924 | 2.7907 | 402 | 374.02 | 3.8049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.49 |  | 44.4399 | 0.1128 | 46.19 | 44.33 | 0.0899 | watch_only | none |
| SMCI | ai_server_oem | 28.26 |  | 27.9983 | 0.9345 | 28.86 | 27.59 | 0.0708 | watch_only | none |
| SPY | market_regime | 740.93 |  | 739.5254 | 0.1899 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.93 |  | 292.3671 | 0.1925 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.56 |  | 118.474 | 1.7608 | 117.17 | 115.25 | 1.2774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.325 |  | 66.2554 | 0.105 | 68.995 | 65.635 | 2.2013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.12 |  | 266.1348 | -0.3813 | 273.86 | 266.04 | 0.2376 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 384.6 |  | 381.2047 | 0.8907 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.21 |  | 582.2868 | 0.502 | 603.25 | 584.69 | 1.8182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 938.44 |  | 937.549 | 0.095 | 955.825 | 935.665 | 2.3624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.79 |  | 465.2022 | 0.3413 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.635 |  | 138.54 | 0.7904 | 139.755 | 137.31 | 0.2721 | watch_only | none |
| ANET | ai_networking_optical | 168.615 |  | 164.8782 | 2.2664 | 165.975 | 160.51 | 3.8253 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 240.68 |  | 237.3629 | 1.3975 | 256.145 | 236.73 | 4.4873 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 645.11 |  | 632.0301 | 2.0695 | 673.65 | 624.91 | 4.5806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 340.44 |  | 337.4112 | 0.8977 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.2 |  | 85.7994 | 1.6324 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.37 |  | 259.0749 | 0.4999 | 268.265 | 253.05 | 3.8522 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1583.23 |  | 1577.2725 | 0.3777 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 475.22 |  | 476.371 | -0.2416 | 494.87 | 477.03 | 4.5263 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.84 |  | 266.6281 | 1.5797 | 276.85 | 267.14 | 4.4307 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.255 |  | 190.7639 | 0.2574 | 194.96 | 189.48 | 0.1098 | watch_only | none |
| TER | semiconductor_test_packaging | 310.59 |  | 308.5382 | 0.665 | 315.21 | 304.11 | 0.4089 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 238.38 |  | 236.7502 | 0.6884 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.41 |  | 46.7187 | -2.8013 | 51.64 | 47.435 | 0.1982 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.09 |  | 42.4456 | -0.8378 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.03 |  | 119.1805 | -0.1263 | 121 | 117.72 | 5.1164 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 282.15 |  | 282.3699 | -0.0779 | 296.8 | 283.22 | 4.6394 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.885 |  | 518.1605 | -0.6321 | 518.6 | 511.495 | 5.0322 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.89 |  | 295.7701 | -0.2976 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.4 |  | 26.517 | -0.4412 | 27 | 25.42 | 2.4242 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.51 |  | 33.7113 | -0.5972 | 35.08 | 33.52 | 0.0597 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.72 |  | 20.0707 | 3.2351 | 20.97 | 19.755 | 0.0483 | watch_only | none |
| SNDK | memory_hbm_storage | 1078.13 |  | 1100.0476 | -1.9924 | 1185.19 | 1114.57 | 1.8328 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.78 |  | 439.7581 | 3.8707 | 465.04 | 435.22 | 3.7611 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 750.54 |  | 731.4492 | 2.61 | 774.805 | 719.02 | 4.4768 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.18 |  | 230.4795 | 0.3039 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 592.77 |  | 593.8344 | -0.1792 | 600.765 | 594.21 | 1.2096 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.7 |  | 245.2379 | -0.2193 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.03 |  | 131.5605 | -1.1633 | 136.45 | 131.735 | 0.6383 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
