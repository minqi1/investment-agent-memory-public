# Intraday State

- Generated at: `2026-07-28T22:03:04+08:00`
- Market time ET: `2026-07-28T10:03:05-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 31, 'watch_only': 3, 'below_vwap': 14, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.23 |  | 672.0512 | -0.271 | 677.3 | 670.84 | 0.0612 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 487.38 |  | 489.3413 | -0.4008 | 497.64 | 485.42 | 0.1128 | below_vwap | below_vwap |
| SMH | semiconductor_index | 524.25 |  | 526.0671 | -0.3454 | 533.01 | 523.325 | 0.0706 | below_vwap | below_vwap |
| SPY | market_regime | 737.175 |  | 737.63 | -0.0617 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 520.215 |  | 517.8408 | 0.4585 | 518.6 | 511.495 | 0.1249 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 520.215 |  | 517.8408 | 0.4585 | 518.6 | 511.495 | 0.1249 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 194.3 |  | 194.1253 | 0.09 | 195.4 | 193.65 | 0.0206 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 377.57 |  | 374.8632 | 0.7221 | 378.64 | 371.57 | 0.1139 | watch_only | none |
| 4 | APLD | high_beta_ai_infrastructure | 26.49 |  | 26.3125 | 0.6744 | 27 | 25.42 | 0.2643 | watch_only | none |
| 5 | JCI | data_center_power_cooling | 138.43 |  | 138.1268 | 0.2195 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ALAB | ai_networking_optical | 255.67 |  | 255.2555 | 0.1624 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TER | semiconductor_test_packaging | 305.55 |  | 305.4068 | 0.0469 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ENTG | semiconductor_materials | 119.48 |  | 119.3973 | 0.0692 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ANET | ai_networking_optical | 162.2 |  | 161.6146 | 0.3622 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | APD | industrial_gases | 296.48 |  | 295.4704 | 0.3417 | 297.25 | 293.555 | 1.5785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SMH | semiconductor_index | 524.25 |  | 526.0671 | -0.3454 | 533.01 | 523.325 | 0.0706 | below_vwap | below_vwap |
| 12 | SOXX | semiconductor_index | 487.38 |  | 489.3413 | -0.4008 | 497.64 | 485.42 | 0.1128 | below_vwap | below_vwap |
| 13 | SPY | market_regime | 737.175 |  | 737.63 | -0.0617 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| 14 | GOOGL | cloud_ai_capex | 326.08 |  | 326.9779 | -0.2746 | 330.21 | 324.97 | 0.0429 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | CRWV | gpu_cloud_ai_factory | 65.82 |  | 66.2319 | -0.6219 | 68.995 | 65.635 | 0.0912 | below_vwap | below_vwap |
| 17 | CORZ | high_beta_ai_infrastructure | 19.905 |  | 20.0474 | -0.7104 | 20.97 | 19.755 | 0.1005 | below_vwap | below_vwap |
| 18 | KLAC | semiconductor_equipment | 189.94 |  | 191.3139 | -0.7181 | 194.96 | 189.48 | 0.2001 | below_vwap | below_vwap |
| 19 | TT | data_center_power_cooling | 464.27 |  | 464.6722 | -0.0866 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | COHU | semiconductor_test_packaging | 42.57 |  | 43.3131 | -1.7157 | 44.155 | 42.57 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 520.215 |  | 517.8408 | 0.4585 | 518.6 | 511.495 | 0.1249 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 194.3 |  | 194.1253 | 0.09 | 195.4 | 193.65 | 0.0206 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 377.57 |  | 374.8632 | 0.7221 | 378.64 | 371.57 | 0.1139 | watch_only | none |
| 4 | APLD | high_beta_ai_infrastructure | 26.49 |  | 26.3125 | 0.6744 | 27 | 25.42 | 0.2643 | watch_only | none |
| 5 | TSM | foundry | 384.54 |  | 385.7201 | -0.3059 | 390.46 | 382.495 | 1.074 | below_vwap | below_vwap,spread_too_wide |
| 6 | SMH | semiconductor_index | 524.25 |  | 526.0671 | -0.3454 | 533.01 | 523.325 | 0.0706 | below_vwap | below_vwap |
| 7 | SOXX | semiconductor_index | 487.38 |  | 489.3413 | -0.4008 | 497.64 | 485.42 | 0.1128 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 737.175 |  | 737.63 | -0.0617 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| 9 | TT | data_center_power_cooling | 464.27 |  | 464.6722 | -0.0866 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | GOOGL | cloud_ai_capex | 326.08 |  | 326.9779 | -0.2746 | 330.21 | 324.97 | 0.0429 | below_vwap | below_vwap |
| 11 | AMAT | semiconductor_equipment | 477.06 |  | 481.0764 | -0.8349 | 494.87 | 477.03 | 0.8091 | below_vwap | below_vwap,spread_too_wide |
| 12 | AMD | ai_accelerator | 453.76 |  | 458.1029 | -0.948 | 472.485 | 453.76 | 2.9311 | below_vwap | below_vwap,spread_too_wide |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 189.94 |  | 191.3139 | -0.7181 | 194.96 | 189.48 | 0.2001 | below_vwap | below_vwap |
| 15 | ORCL | cloud_ai_capex | 115.87 |  | 115.8774 | -0.0064 | 117.17 | 115.25 | 1.0098 | below_vwap | below_vwap,spread_too_wide |
| 16 | COHU | semiconductor_test_packaging | 42.57 |  | 43.3131 | -1.7157 | 44.155 | 42.57 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CRWV | gpu_cloud_ai_factory | 65.82 |  | 66.2319 | -0.6219 | 68.995 | 65.635 | 0.0912 | below_vwap | below_vwap |
| 18 | CORZ | high_beta_ai_infrastructure | 19.905 |  | 20.0474 | -0.7104 | 20.97 | 19.755 | 0.1005 | below_vwap | below_vwap |
| 19 | ANET | ai_networking_optical | 162.2 |  | 161.6146 | 0.3622 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | JCI | data_center_power_cooling | 138.43 |  | 138.1268 | 0.2195 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 670.23 |  | 672.0512 | -0.271 | 677.3 | 670.84 | 0.0612 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 60.13 |  | 60.5915 | -0.7616 | 62.01 | 60.23 | 0.0333 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 194.3 |  | 194.1253 | 0.09 | 195.4 | 193.65 | 0.0206 | watch_only | none |
| MSFT | cloud_ai_capex | 392.31 |  | 394.524 | -0.5612 | 400.09 | 392.355 | 0.9227 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 337.64 |  | 339.2528 | -0.4754 | 342.87 | 337.78 | 0.0296 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 326.08 |  | 326.9779 | -0.2746 | 330.21 | 324.97 | 0.0429 | below_vwap | below_vwap |
| AMD | ai_accelerator | 453.76 |  | 458.1029 | -0.948 | 472.485 | 453.76 | 2.9311 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 384.54 |  | 385.7201 | -0.3059 | 390.46 | 382.495 | 1.074 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1555000 |  | 1782642.2481 | -12.7699 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 487.38 |  | 489.3413 | -0.4008 | 497.64 | 485.42 | 0.1128 | below_vwap | below_vwap |
| SMH | semiconductor_index | 524.25 |  | 526.0671 | -0.3454 | 533.01 | 523.325 | 0.0706 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 377.57 |  | 374.8632 | 0.7221 | 378.64 | 371.57 | 0.1139 | watch_only | none |
| MU | memory_hbm_storage | 811.38 |  | 822.5121 | -1.3534 | 846.4 | 813.91 | 1.161 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 171.64 |  | 173.9454 | -1.3253 | 181.24 | 172.395 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| DELL | ai_server_oem | 364.57 |  | 372.6826 | -2.1768 | 402 | 374.02 | 0.2688 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 44.045 |  | 44.3611 | -0.7126 | 46.19 | 44.33 | 0.2043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 27.315 |  | 27.764 | -1.6171 | 28.86 | 27.59 | 0.1098 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 737.175 |  | 737.63 | -0.0617 | 739.42 | 736.57 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 291.18 |  | 291.9703 | -0.2707 | 293.26 | 291.55 | 0.0103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 115.87 |  | 115.8774 | -0.0064 | 117.17 | 115.25 | 1.0098 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 65.82 |  | 66.2319 | -0.6219 | 68.995 | 65.635 | 0.0912 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 264.23 |  | 268.643 | -1.6427 | 273.86 | 266.04 | 0.5336 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 377.42 |  | 379.0978 | -0.4426 | 384.565 | 377.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 580.88 |  | 585.4899 | -0.7874 | 603.25 | 584.69 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 927.045 |  | 941.6807 | -1.5542 | 955.825 | 935.665 | 4.1648 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 464.27 |  | 464.6722 | -0.0866 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 138.43 |  | 138.1268 | 0.2195 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 162.2 |  | 161.6146 | 0.3622 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 235.615 |  | 239.5132 | -1.6276 | 256.145 | 236.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 621.225 |  | 631.8089 | -1.6752 | 673.65 | 624.91 | 4.3302 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 335.16 |  | 340.8194 | -1.6605 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 83.32 |  | 85.6015 | -2.6652 | 92.95 | 84.63 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 255.67 |  | 255.2555 | 0.1624 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1565.69 |  | 1574.1189 | -0.5355 | 1586.01 | 1565.95 | 0.6246 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 477.06 |  | 481.0764 | -0.8349 | 494.87 | 477.03 | 0.8091 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 265 |  | 268.4516 | -1.2857 | 276.85 | 267.14 | 4.5019 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 189.94 |  | 191.3139 | -0.7181 | 194.96 | 189.48 | 0.2001 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 305.55 |  | 305.4068 | 0.0469 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 235.03 |  | 239.1992 | -1.743 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.255 |  | 48.0299 | -3.6955 | 51.64 | 47.435 | 0.3027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.57 |  | 43.3131 | -1.7157 | 44.155 | 42.57 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.48 |  | 119.3973 | 0.0692 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 283.15 |  | 285.3389 | -0.7671 | 296.8 | 283.22 | 2.4192 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 520.215 |  | 517.8408 | 0.4585 | 518.6 | 511.495 | 0.1249 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.48 |  | 295.4704 | 0.3417 | 297.25 | 293.555 | 1.5785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.49 |  | 26.3125 | 0.6744 | 27 | 25.42 | 0.2643 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.14 |  | 33.4207 | -0.8399 | 35.08 | 33.52 | 0.0604 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 19.905 |  | 20.0474 | -0.7104 | 20.97 | 19.755 | 0.1005 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1096.57 |  | 1123.1545 | -2.367 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 431.11 |  | 438.4353 | -1.6708 | 465.04 | 435.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 714.28 |  | 725.3878 | -1.5313 | 774.805 | 719.02 | 0.301 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 229.66 |  | 230.5177 | -0.3721 | 233.05 | 229.7 | 0.0218 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 593.98 |  | 596.1451 | -0.3632 | 600.765 | 594.21 | 0.2071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 242.61 |  | 245.6972 | -1.2565 | 253.38 | 243.72 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 129.76 |  | 131.9335 | -1.6474 | 136.45 | 131.735 | 0.447 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
