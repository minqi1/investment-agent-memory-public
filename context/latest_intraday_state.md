# Intraday State

- Generated at: `2026-07-29T01:56:22+08:00`
- Market time ET: `2026-07-28T13:56:23-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 6, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 1, 'below_vwap': 9, 'below_opening_15m_low': 12}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.23 |  | 673.9758 | 0.3345 | 677.3 | 670.84 | 0.0133 | watch_only | none |
| SOXX | semiconductor_index | 490.15 |  | 489.9063 | 0.0497 | 497.64 | 485.42 | 0.049 | watch_only | none |
| SMH | semiconductor_index | 528.01 |  | 527.2918 | 0.1362 | 533.01 | 523.325 | 0.0625 | watch_only | none |
| SPY | market_regime | 740.605 |  | 739.4265 | 0.1594 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.75 |  | 195.979 | 0.3934 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 378.99 |  | 378.5329 | 0.1208 | 378.64 | 371.57 | 0.0712 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.605 |  | 739.4265 | 0.1594 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.72 |  | 164.2541 | 1.5012 | 165.975 | 160.51 | 0.126 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.345 |  | 330.3135 | 1.5232 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.29 |  | 118.1726 | 1.7918 | 117.17 | 115.25 | 0.1164 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 378.99 |  | 378.5329 | 0.1208 | 378.64 | 371.57 | 0.0712 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.605 |  | 739.4265 | 0.1594 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 3 | NVDA | ai_accelerator | 196.75 |  | 195.979 | 0.3934 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 528.01 |  | 527.2918 | 0.1362 | 533.01 | 523.325 | 0.0625 | watch_only | none |
| 5 | SOXX | semiconductor_index | 490.15 |  | 489.9063 | 0.0497 | 497.64 | 485.42 | 0.049 | watch_only | none |
| 6 | QQQ | market_regime | 676.23 |  | 673.9758 | 0.3345 | 677.3 | 670.84 | 0.0133 | watch_only | none |
| 7 | TT | data_center_power_cooling | 465.52 |  | 464.9957 | 0.1128 | 477.73 | 460.77 | 0.1074 | watch_only | none |
| 8 | IWM | market_regime | 292.73 |  | 292.3059 | 0.1451 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 9 | KLAC | semiconductor_equipment | 191.15 |  | 190.7406 | 0.2146 | 194.96 | 189.48 | 0.0366 | watch_only | none |
| 10 | TER | semiconductor_test_packaging | 309.31 |  | 308.373 | 0.3039 | 315.21 | 304.11 | 0.1164 | watch_only | none |
| 11 | AMZN | cloud_ai_capex | 231.21 |  | 230.4387 | 0.3347 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 12 | AAPL | mega_cap_platform | 339.71 |  | 338.9087 | 0.2364 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 13 | TSM | foundry | 389.28 |  | 387.4993 | 0.4595 | 390.46 | 382.495 | 0.036 | watch_only | none |
| 14 | MSFT | cloud_ai_capex | 398.96 |  | 396.2714 | 0.6785 | 400.09 | 392.355 | 0.0351 | watch_only | none |
| 15 | ANET | ai_networking_optical | 166.72 |  | 164.2541 | 1.5012 | 165.975 | 160.51 | 0.126 | buy_precheck_manual_confirm | none |
| 16 | SMCI | ai_server_oem | 28.21 |  | 27.9797 | 0.8233 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 17 | JCI | data_center_power_cooling | 138.85 |  | 138.3769 | 0.3419 | 139.755 | 137.31 | 4.1051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 456.47 |  | 455.48 | 0.2174 | 472.485 | 453.76 | 2.6858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 174.695 |  | 174.1239 | 0.328 | 181.24 | 172.395 | 3.3888 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | GOOGL | cloud_ai_capex | 335.345 |  | 330.3135 | 1.5232 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.75 |  | 195.979 | 0.3934 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 378.99 |  | 378.5329 | 0.1208 | 378.64 | 371.57 | 0.0712 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.605 |  | 739.4265 | 0.1594 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.72 |  | 164.2541 | 1.5012 | 165.975 | 160.51 | 0.126 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 335.345 |  | 330.3135 | 1.5232 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.29 |  | 118.1726 | 1.7918 | 117.17 | 115.25 | 0.1164 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 389.28 |  | 387.4993 | 0.4595 | 390.46 | 382.495 | 0.036 | watch_only | none |
| 8 | SMH | semiconductor_index | 528.01 |  | 527.2918 | 0.1362 | 533.01 | 523.325 | 0.0625 | watch_only | none |
| 9 | SOXX | semiconductor_index | 490.15 |  | 489.9063 | 0.0497 | 497.64 | 485.42 | 0.049 | watch_only | none |
| 10 | QQQ | market_regime | 676.23 |  | 673.9758 | 0.3345 | 677.3 | 670.84 | 0.0133 | watch_only | none |
| 11 | TT | data_center_power_cooling | 465.52 |  | 464.9957 | 0.1128 | 477.73 | 460.77 | 0.1074 | watch_only | none |
| 12 | IWM | market_regime | 292.73 |  | 292.3059 | 0.1451 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 13 | KLAC | semiconductor_equipment | 191.15 |  | 190.7406 | 0.2146 | 194.96 | 189.48 | 0.0366 | watch_only | none |
| 14 | TER | semiconductor_test_packaging | 309.31 |  | 308.373 | 0.3039 | 315.21 | 304.11 | 0.1164 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 398.96 |  | 396.2714 | 0.6785 | 400.09 | 392.355 | 0.0351 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 231.21 |  | 230.4387 | 0.3347 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 17 | SMCI | ai_server_oem | 28.21 |  | 27.9797 | 0.8233 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 18 | AAPL | mega_cap_platform | 339.71 |  | 338.9087 | 0.2364 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| 19 | CORZ | high_beta_ai_infrastructure | 20.41 |  | 20.0362 | 1.8654 | 20.97 | 19.755 | 0.098 | watch_only | none |
| 20 | TQQQ | leveraged_tool | 61.59 |  | 61.0734 | 0.8458 | 62.01 | 60.23 | 0.0162 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.23 |  | 673.9758 | 0.3345 | 677.3 | 670.84 | 0.0133 | watch_only | none |
| TQQQ | leveraged_tool | 61.59 |  | 61.0734 | 0.8458 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 196.75 |  | 195.979 | 0.3934 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.96 |  | 396.2714 | 0.6785 | 400.09 | 392.355 | 0.0351 | watch_only | none |
| AAPL | mega_cap_platform | 339.71 |  | 338.9087 | 0.2364 | 342.87 | 337.78 | 0.0147 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.345 |  | 330.3135 | 1.5232 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.47 |  | 455.48 | 0.2174 | 472.485 | 453.76 | 2.6858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 389.28 |  | 387.4993 | 0.4595 | 390.46 | 382.495 | 0.036 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.15 |  | 489.9063 | 0.0497 | 497.64 | 485.42 | 0.049 | watch_only | none |
| SMH | semiconductor_index | 528.01 |  | 527.2918 | 0.1362 | 533.01 | 523.325 | 0.0625 | watch_only | none |
| AVGO | custom_silicon_networking | 378.99 |  | 378.5329 | 0.1208 | 378.64 | 371.57 | 0.0712 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 813.07 |  | 815.2413 | -0.2663 | 846.4 | 813.91 | 0.0615 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 174.695 |  | 174.1239 | 0.328 | 181.24 | 172.395 | 3.3888 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 381.83 |  | 374.7277 | 1.8953 | 402 | 374.02 | 4.7037 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.21 |  | 44.4457 | -0.5302 | 46.19 | 44.33 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 28.21 |  | 27.9797 | 0.8233 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 740.605 |  | 739.4265 | 0.1594 | 739.42 | 736.57 | 0.0041 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.73 |  | 292.3059 | 0.1451 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.29 |  | 118.1726 | 1.7918 | 117.17 | 115.25 | 0.1164 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.155 |  | 66.2534 | -0.1485 | 68.995 | 65.635 | 2.3581 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 264.18 |  | 266.2755 | -0.787 | 273.86 | 266.04 | 1.6807 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 383.98 |  | 380.9057 | 0.8071 | 384.565 | 377.43 | 2.4376 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 583.67 |  | 582.0379 | 0.2804 | 603.25 | 584.69 | 1.5608 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 935.52 |  | 937.5581 | -0.2174 | 955.825 | 935.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 465.52 |  | 464.9957 | 0.1128 | 477.73 | 460.77 | 0.1074 | watch_only | none |
| JCI | data_center_power_cooling | 138.85 |  | 138.3769 | 0.3419 | 139.755 | 137.31 | 4.1051 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 166.72 |  | 164.2541 | 1.5012 | 165.975 | 160.51 | 0.126 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 241.39 |  | 237.0691 | 1.8226 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 639.68 |  | 631.4272 | 1.307 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 340.33 |  | 337.2483 | 0.9138 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.16 |  | 85.7432 | 1.6524 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.21 |  | 258.9147 | 0.5003 | 268.265 | 253.05 | 3.8392 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1575 |  | 1577.1437 | -0.1359 | 1586.01 | 1565.95 | 0.1644 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 472 |  | 476.6409 | -0.9737 | 494.87 | 477.03 | 0.1462 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 268.7 |  | 266.3935 | 0.8658 | 276.85 | 267.14 | 4.4659 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.15 |  | 190.7406 | 0.2146 | 194.96 | 189.48 | 0.0366 | watch_only | none |
| TER | semiconductor_test_packaging | 309.31 |  | 308.373 | 0.3039 | 315.21 | 304.11 | 0.1164 | watch_only | none |
| ONTO | semiconductor_test_packaging | 237.5 |  | 236.5863 | 0.3862 | 248.8 | 236.42 | 0.4758 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.95 |  | 46.7719 | -1.7572 | 51.64 | 47.435 | 0.0218 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 41.935 |  | 42.4893 | -1.3047 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.03 |  | 119.3931 | -1.1417 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.41 |  | 282.4337 | -0.3625 | 296.8 | 283.22 | 4.2998 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.48 |  | 518.4906 | -0.5806 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.97 |  | 295.8436 | -0.2953 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.06 |  | 26.528 | -1.7642 | 27 | 25.42 | 0.1535 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.625 |  | 33.7189 | -0.2785 | 35.08 | 33.52 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.41 |  | 20.0362 | 1.8654 | 20.97 | 19.755 | 0.098 | watch_only | none |
| SNDK | memory_hbm_storage | 1071.865 |  | 1101.2388 | -2.6673 | 1185.19 | 1114.57 | 1.3267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 450.73 |  | 438.6695 | 2.7493 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 743.08 |  | 728.99 | 1.9328 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.21 |  | 230.4387 | 0.3347 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 593.13 |  | 593.8334 | -0.1185 | 600.765 | 594.21 | 0.0995 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 243.445 |  | 245.3429 | -0.7736 | 253.38 | 243.72 | 3.9064 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 130.85 |  | 131.6411 | -0.6009 | 136.45 | 131.735 | 2.5984 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
