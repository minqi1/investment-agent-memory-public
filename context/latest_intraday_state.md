# Intraday State

- Generated at: `2026-07-16T03:00:38+08:00`
- Market time ET: `2026-07-15T15:00:39-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'spread_too_wide_or_missing': 2, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 2, 'below_vwap': 3, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.44 |  | 716.3599 | -0.1284 | 724.31 | 721.08 | 0.0224 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.05 |  | 551.4244 | -0.2492 | 575.7 | 565.33 | 0.0582 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.37 |  | 587.3067 | -0.3298 | 606.85 | 597.81 | 0.0786 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.16 |  | 753.3032 | -0.019 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.27 |  | 368.9463 | 0.3588 | 364.41 | 357.885 | 0.3079 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 327.51 |  | 325.723 | 0.5486 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.9293 | 2.7394 | 22.36 | 21.94 | 0.0888 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ORCL | cloud_ai_capex | 132.1 |  | 131.903 | 0.1493 | 132.925 | 129.92 | 0.0606 | watch_only | none |
| 2 | ASML | semiconductor_equipment | 1778.95 |  | 1772.6713 | 0.3542 | 1829.9 | 1759.045 | 0.0922 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 327.51 |  | 325.723 | 0.5486 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | APLD | high_beta_ai_infrastructure | 28.46 |  | 28.314 | 0.5156 | 29.055 | 28.28 | 0.0703 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 370.27 |  | 368.9463 | 0.3588 | 364.41 | 357.885 | 0.3079 | buy_precheck_manual_confirm | none |
| 6 | CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.9293 | 2.7394 | 22.36 | 21.94 | 0.0888 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 395.67 |  | 395.3713 | 0.0756 | 391.33 | 387.05 | 0.4878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | SMCI | ai_server_oem | 26.91 |  | 26.8859 | 0.0898 | 28.295 | 27.55 | 0.0743 | below_opening_15m_low | below_opening_15m_low |
| 9 | META | cloud_ai_capex | 676.25 |  | 675.5487 | 0.1038 | 664.875 | 657.17 | 0.6063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | HPE | ai_server_oem | 47.02 |  | 46.9254 | 0.2017 | 50.2 | 48.995 | 0.0425 | below_opening_15m_low | below_opening_15m_low |
| 11 | CIEN | ai_networking_optical | 421.035 |  | 419.6775 | 0.3235 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 142.14 |  | 141.7991 | 0.2404 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 13 | NVDA | ai_accelerator | 210.27 |  | 209.2907 | 0.4679 | 213.775 | 211.225 | 0.019 | below_opening_15m_low | below_opening_15m_low |
| 14 | LIN | industrial_gases | 516.65 |  | 516.1 | 0.1066 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | ETN | data_center_power_cooling | 410.86 |  | 408.6119 | 0.5502 | 417.84 | 413.82 | 0.0852 | below_opening_15m_low | below_opening_15m_low |
| 16 | AMKR | semiconductor_test_packaging | 67.04 |  | 67.0109 | 0.0435 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | IWM | market_regime | 295.27 |  | 295.6436 | -0.1264 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 18 | AMZN | cloud_ai_capex | 254.31 |  | 254.4979 | -0.0738 | 252.89 | 249.98 | 0.0275 | below_vwap | below_vwap |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | VRT | data_center_power_cooling | 300.905 |  | 299.3711 | 0.5124 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 370.27 |  | 368.9463 | 0.3588 | 364.41 | 357.885 | 0.3079 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 327.51 |  | 325.723 | 0.5486 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.9293 | 2.7394 | 22.36 | 21.94 | 0.0888 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 254.31 |  | 254.4979 | -0.0738 | 252.89 | 249.98 | 0.0275 | below_vwap | below_vwap |
| 5 | MSFT | cloud_ai_capex | 395.67 |  | 395.3713 | 0.0756 | 391.33 | 387.05 | 0.4878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | META | cloud_ai_capex | 676.25 |  | 675.5487 | 0.1038 | 664.875 | 657.17 | 0.6063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1778.95 |  | 1772.6713 | 0.3542 | 1829.9 | 1759.045 | 0.0922 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.1 |  | 131.903 | 0.1493 | 132.925 | 129.92 | 0.0606 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.46 |  | 28.314 | 0.5156 | 29.055 | 28.28 | 0.0703 | watch_only | none |
| 10 | IWM | market_regime | 295.27 |  | 295.6436 | -0.1264 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | NVDA | ai_accelerator | 210.27 |  | 209.2907 | 0.4679 | 213.775 | 211.225 | 0.019 | below_opening_15m_low | below_opening_15m_low |
| 13 | CIEN | ai_networking_optical | 421.035 |  | 419.6775 | 0.3235 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 14 | VRT | data_center_power_cooling | 300.905 |  | 299.3711 | 0.5124 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | SNDK | memory_hbm_storage | 1601.16 |  | 1580.6291 | 1.2989 | 1726.34 | 1665.91 | 4.5461 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | JCI | data_center_power_cooling | 142.14 |  | 141.7991 | 0.2404 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | PWR | data_center_power_cooling | 652.745 |  | 645.9593 | 1.0505 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | GEV | data_center_power_cooling | 1051.69 |  | 1035.5929 | 1.5544 | 1073.34 | 1059.27 | 2.5236 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | ALAB | ai_networking_optical | 346.74 |  | 344.7769 | 0.5694 | 369.23 | 356.615 | 3.1926 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | ETN | data_center_power_cooling | 410.86 |  | 408.6119 | 0.5502 | 417.84 | 413.82 | 0.0852 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.44 |  | 716.3599 | -0.1284 | 724.31 | 721.08 | 0.0224 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.67 |  | 74.2004 | -0.7148 | 76.46 | 75.39 | 0.0136 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 210.27 |  | 209.2907 | 0.4679 | 213.775 | 211.225 | 0.019 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 395.67 |  | 395.3713 | 0.0756 | 391.33 | 387.05 | 0.4878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 327.51 |  | 325.723 | 0.5486 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.27 |  | 368.9463 | 0.3588 | 364.41 | 357.885 | 0.3079 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 525.88 |  | 527.4526 | -0.2981 | 558.62 | 548.745 | 0.7245 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.79 |  | 418.9908 | -0.2866 | 428.59 | 422.945 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.05 |  | 551.4244 | -0.2492 | 575.7 | 565.33 | 0.0582 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.37 |  | 587.3067 | -0.3298 | 606.85 | 597.81 | 0.0786 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 391.93 |  | 392.0759 | -0.0372 | 397.94 | 392.62 | 0.8701 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 900.87 |  | 910.0557 | -1.0094 | 977.7 | 953.67 | 0.3075 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 205.87 |  | 208.3341 | -1.1827 | 223.02 | 214.85 | 0.1214 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 403.9 |  | 407.0118 | -0.7646 | 457.935 | 442.67 | 2.4362 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.02 |  | 46.9254 | 0.2017 | 50.2 | 48.995 | 0.0425 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 26.91 |  | 26.8859 | 0.0898 | 28.295 | 27.55 | 0.0743 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.16 |  | 753.3032 | -0.019 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.27 |  | 295.6436 | -0.1264 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.1 |  | 131.903 | 0.1493 | 132.925 | 129.92 | 0.0606 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 76.96 |  | 77.5057 | -0.7041 | 80.585 | 78.73 | 2.5338 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 300.905 |  | 299.3711 | 0.5124 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 410.86 |  | 408.6119 | 0.5502 | 417.84 | 413.82 | 0.0852 | below_opening_15m_low | below_opening_15m_low |
| PWR | data_center_power_cooling | 652.745 |  | 645.9593 | 1.0505 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1051.69 |  | 1035.5929 | 1.5544 | 1073.34 | 1059.27 | 2.5236 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 478.05 |  | 478.6919 | -0.1341 | 485.9 | 482.93 | 0.228 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 142.14 |  | 141.7991 | 0.2404 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 170.43 |  | 171.8318 | -0.8158 | 186.095 | 178.355 | 2.1182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 292.97 |  | 294.0617 | -0.3712 | 315.74 | 303.34 | 3.1539 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 747.285 |  | 749.2182 | -0.258 | 820.15 | 780.365 | 3.8553 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 421.035 |  | 419.6775 | 0.3235 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 109.26 |  | 112.1493 | -2.5763 | 123.995 | 117.25 | 0.2654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ALAB | ai_networking_optical | 346.74 |  | 344.7769 | 0.5694 | 369.23 | 356.615 | 3.1926 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1778.95 |  | 1772.6713 | 0.3542 | 1829.9 | 1759.045 | 0.0922 | watch_only | none |
| AMAT | semiconductor_equipment | 573.6 |  | 577.643 | -0.6999 | 610.62 | 586.86 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 329.15 |  | 331.4167 | -0.6839 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.09 |  | 222.6706 | -0.2607 | 236.49 | 225.11 | 0.1891 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 338.09 |  | 336.1623 | 0.5734 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 302.84 |  | 307.2865 | -1.447 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.04 |  | 67.0109 | 0.0435 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.54 |  | 54.3612 | 0.329 | 57.92 | 55.2 | 3.4103 | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_too_wide,stale_or_missing |
| ENTG | semiconductor_materials | 136.525 |  | 137.663 | -0.8267 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 348.54 |  | 348.7907 | -0.0719 | 368.67 | 358.39 | 0.3558 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.65 |  | 516.1 | 0.1066 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 294.12 |  | 294.4569 | -0.1144 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.46 |  | 28.314 | 0.5156 | 29.055 | 28.28 | 0.0703 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.74 |  | 39.2819 | -1.3794 | 40.01 | 38.815 | 0.0516 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.53 |  | 21.9293 | 2.7394 | 22.36 | 21.94 | 0.0888 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1601.16 |  | 1580.6291 | 1.2989 | 1726.34 | 1665.91 | 4.5461 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 510.55 |  | 516.4284 | -1.1383 | 568.16 | 542.4 | 4.1132 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 814.98 |  | 817.6257 | -0.3236 | 889.1 | 850.01 | 2.4798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 254.31 |  | 254.4979 | -0.0738 | 252.89 | 249.98 | 0.0275 | below_vwap | below_vwap |
| META | cloud_ai_capex | 676.25 |  | 675.5487 | 0.1038 | 664.875 | 657.17 | 0.6063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 272.52 |  | 275.6643 | -1.1406 | 286.73 | 280.14 | 4.7703 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 175.49 |  | 175.9246 | -0.2471 | 183.63 | 176.08 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
