# Intraday State

- Generated at: `2026-07-16T03:16:34+08:00`
- Market time ET: `2026-07-15T15:16:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'watch_only': 6, 'below_vwap': 4, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.25 |  | 716.3535 | -0.0144 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 552.345 |  | 551.4889 | 0.1552 | 575.7 | 565.33 | 0.0887 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.24 |  | 587.3133 | 0.1578 | 606.85 | 597.81 | 0.0697 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.73 |  | 753.3116 | 0.0555 | 755.54 | 754.215 | 0.0305 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.32 |  | 368.9915 | 0.36 | 364.41 | 357.885 | 0.081 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 327.69 |  | 325.808 | 0.5776 | 321.14 | 317.4 | 0.0183 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.595 |  | 21.9577 | 2.9026 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 295.65 |  | 295.6389 | 0.0038 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 2 | ORCL | cloud_ai_capex | 132.12 |  | 131.9278 | 0.1457 | 132.925 | 129.92 | 0.0303 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 393.65 |  | 392.164 | 0.3789 | 397.94 | 392.62 | 0.0965 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 370.32 |  | 368.9915 | 0.36 | 364.41 | 357.885 | 0.081 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.69 |  | 325.808 | 0.5776 | 321.14 | 317.4 | 0.0183 | buy_precheck_manual_confirm | none |
| 6 | NVDA | ai_accelerator | 211.6 |  | 209.4047 | 1.0483 | 213.775 | 211.225 | 0.2977 | watch_only | none |
| 7 | ASML | semiconductor_equipment | 1796.77 |  | 1773.0205 | 1.3395 | 1829.9 | 1759.045 | 0.1787 | watch_only | none |
| 8 | APLD | high_beta_ai_infrastructure | 28.63 |  | 28.3239 | 1.0806 | 29.055 | 28.28 | 0.1397 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.595 |  | 21.9577 | 2.9026 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 552.345 |  | 551.4889 | 0.1552 | 575.7 | 565.33 | 0.0887 | below_opening_15m_low | below_opening_15m_low |
| 11 | SPY | market_regime | 753.73 |  | 753.3116 | 0.0555 | 755.54 | 754.215 | 0.0305 | below_opening_15m_low | below_opening_15m_low |
| 12 | AMD | ai_accelerator | 527.59 |  | 527.447 | 0.0271 | 558.62 | 548.745 | 0.1175 | below_opening_15m_low | below_opening_15m_low |
| 13 | SMH | semiconductor_index | 588.24 |  | 587.3133 | 0.1578 | 606.85 | 597.81 | 0.0697 | below_opening_15m_low | below_opening_15m_low |
| 14 | META | cloud_ai_capex | 677.255 |  | 675.6233 | 0.2415 | 664.875 | 657.17 | 0.4636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 478.71 |  | 478.6727 | 0.0078 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 142.28 |  | 141.8142 | 0.3285 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | LRCX | semiconductor_equipment | 331.65 |  | 331.3998 | 0.0755 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | LIN | industrial_gases | 516.45 |  | 516.0991 | 0.068 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 411.88 |  | 408.6514 | 0.7901 | 417.84 | 413.82 | 0.0995 | below_opening_15m_low | below_opening_15m_low |
| 20 | COHU | semiconductor_test_packaging | 54.46 |  | 54.3621 | 0.1802 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.32 |  | 368.9915 | 0.36 | 364.41 | 357.885 | 0.081 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 327.69 |  | 325.808 | 0.5776 | 321.14 | 317.4 | 0.0183 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.595 |  | 21.9577 | 2.9026 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 395.145 |  | 395.3781 | -0.059 | 391.33 | 387.05 | 0.2505 | below_vwap | below_vwap |
| 5 | AMZN | cloud_ai_capex | 254.165 |  | 254.4946 | -0.1295 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| 6 | NVDA | ai_accelerator | 211.6 |  | 209.4047 | 1.0483 | 213.775 | 211.225 | 0.2977 | watch_only | none |
| 7 | AVGO | custom_silicon_networking | 393.65 |  | 392.164 | 0.3789 | 397.94 | 392.62 | 0.0965 | watch_only | none |
| 8 | META | cloud_ai_capex | 677.255 |  | 675.6233 | 0.2415 | 664.875 | 657.17 | 0.4636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1796.77 |  | 1773.0205 | 1.3395 | 1829.9 | 1759.045 | 0.1787 | watch_only | none |
| 10 | IWM | market_regime | 295.65 |  | 295.6389 | 0.0038 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 11 | ORCL | cloud_ai_capex | 132.12 |  | 131.9278 | 0.1457 | 132.925 | 129.92 | 0.0303 | watch_only | none |
| 12 | APLD | high_beta_ai_infrastructure | 28.63 |  | 28.3239 | 1.0806 | 29.055 | 28.28 | 0.1397 | watch_only | none |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IREN | high_beta_ai_infrastructure | 38.92 |  | 39.2609 | -0.8683 | 40.01 | 38.815 | 0.0514 | below_vwap | below_vwap |
| 15 | CIEN | ai_networking_optical | 421.27 |  | 419.7363 | 0.3654 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | SOXX | semiconductor_index | 552.345 |  | 551.4889 | 0.1552 | 575.7 | 565.33 | 0.0887 | below_opening_15m_low | below_opening_15m_low |
| 17 | SPY | market_regime | 753.73 |  | 753.3116 | 0.0555 | 755.54 | 754.215 | 0.0305 | below_opening_15m_low | below_opening_15m_low |
| 18 | AMD | ai_accelerator | 527.59 |  | 527.447 | 0.0271 | 558.62 | 548.745 | 0.1175 | below_opening_15m_low | below_opening_15m_low |
| 19 | TT | data_center_power_cooling | 478.71 |  | 478.6727 | 0.0078 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | VRT | data_center_power_cooling | 302.73 |  | 299.4519 | 1.0947 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.25 |  | 716.3535 | -0.0144 | 724.31 | 721.08 | 0.0307 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.96 |  | 74.1948 | -0.3165 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.6 |  | 209.4047 | 1.0483 | 213.775 | 211.225 | 0.2977 | watch_only | none |
| MSFT | cloud_ai_capex | 395.145 |  | 395.3781 | -0.059 | 391.33 | 387.05 | 0.2505 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 327.69 |  | 325.808 | 0.5776 | 321.14 | 317.4 | 0.0183 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.32 |  | 368.9915 | 0.36 | 364.41 | 357.885 | 0.081 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 527.59 |  | 527.447 | 0.0271 | 558.62 | 548.745 | 0.1175 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 419.52 |  | 418.9948 | 0.1253 | 428.59 | 422.945 | 0.3599 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 552.345 |  | 551.4889 | 0.1552 | 575.7 | 565.33 | 0.0887 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.24 |  | 587.3133 | 0.1578 | 606.85 | 597.81 | 0.0697 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 393.65 |  | 392.164 | 0.3789 | 397.94 | 392.62 | 0.0965 | watch_only | none |
| MU | memory_hbm_storage | 900.51 |  | 909.8482 | -1.0264 | 977.7 | 953.67 | 0.0311 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 205.58 |  | 208.2243 | -1.2699 | 223.02 | 214.85 | 0.0778 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 406.5 |  | 406.9739 | -0.1164 | 457.935 | 442.67 | 1.0012 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.49 |  | 46.9473 | 1.1559 | 50.2 | 48.995 | 0.0211 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.05 |  | 26.8904 | 0.5934 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.73 |  | 753.3116 | 0.0555 | 755.54 | 754.215 | 0.0305 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.65 |  | 295.6389 | 0.0038 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 132.12 |  | 131.9278 | 0.1457 | 132.925 | 129.92 | 0.0303 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.17 |  | 77.4978 | -0.423 | 80.585 | 78.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 302.73 |  | 299.4519 | 1.0947 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.88 |  | 408.6514 | 0.7901 | 417.84 | 413.82 | 0.0995 | below_opening_15m_low | below_opening_15m_low |
| PWR | data_center_power_cooling | 651.84 |  | 646.0952 | 0.8892 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1053.94 |  | 1036.445 | 1.688 | 1073.34 | 1059.27 | 0.1139 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 478.71 |  | 478.6727 | 0.0078 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 142.28 |  | 141.8142 | 0.3285 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.42 |  | 171.8057 | -0.2245 | 186.095 | 178.355 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 295.65 |  | 294.0641 | 0.5393 | 315.74 | 303.34 | 0.8896 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LITE | ai_networking_optical | 748.13 |  | 749.1395 | -0.1347 | 820.15 | 780.365 | 3.7306 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 421.27 |  | 419.7363 | 0.3654 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 108.77 |  | 112.0013 | -2.885 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 347.62 |  | 344.8632 | 0.7994 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1796.77 |  | 1773.0205 | 1.3395 | 1829.9 | 1759.045 | 0.1787 | watch_only | none |
| AMAT | semiconductor_equipment | 576.27 |  | 577.5935 | -0.2291 | 610.62 | 586.86 | 0.1874 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 331.65 |  | 331.3998 | 0.0755 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 222.75 |  | 222.675 | 0.0337 | 236.49 | 225.11 | 0.3636 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 339.775 |  | 336.2637 | 1.0442 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 304.41 |  | 307.1694 | -0.8983 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.38 |  | 67.025 | 0.5296 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.46 |  | 54.3621 | 0.1802 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 137.31 |  | 137.6497 | -0.2468 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 350.42 |  | 348.8425 | 0.4522 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.45 |  | 516.0991 | 0.068 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 294.36 |  | 294.4161 | -0.0191 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.63 |  | 28.3239 | 1.0806 | 29.055 | 28.28 | 0.1397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.92 |  | 39.2609 | -0.8683 | 40.01 | 38.815 | 0.0514 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.595 |  | 21.9577 | 2.9026 | 22.36 | 21.94 | 0.0443 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1621.885 |  | 1582.2792 | 2.5031 | 1726.34 | 1665.91 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 510.66 |  | 516.3072 | -1.0938 | 568.16 | 542.4 | 1.7624 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 816.89 |  | 817.5606 | -0.082 | 889.1 | 850.01 | 2.4887 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 254.165 |  | 254.4946 | -0.1295 | 252.89 | 249.98 | 0.0118 | below_vwap | below_vwap |
| META | cloud_ai_capex | 677.255 |  | 675.6233 | 0.2415 | 664.875 | 657.17 | 0.4636 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 273.75 |  | 275.5763 | -0.6627 | 286.73 | 280.14 | 4.7489 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 174.165 |  | 175.9188 | -0.997 | 183.63 | 176.08 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
