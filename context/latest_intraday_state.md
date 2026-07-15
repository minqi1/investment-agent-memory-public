# Intraday State

- Generated at: `2026-07-16T02:08:51+08:00`
- Market time ET: `2026-07-15T14:08:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 39, 'spread_too_wide_or_missing': 3, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'below_vwap': 2, 'watch_only': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.06 |  | 716.2631 | 0.2509 | 724.31 | 721.08 | 0.0167 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.825 |  | 551.3124 | 0.6371 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.135 |  | 587.2498 | 0.321 | 606.85 | 597.81 | 0.0679 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.55 |  | 753.1827 | 0.1815 | 755.54 | 754.215 | 0.0278 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 371.69 |  | 368.7083 | 0.8087 | 364.41 | 357.885 | 0.0215 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.71 |  | 254.4585 | 0.0988 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.37 |  | 325.5426 | 0.5613 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.7901 | 3.4874 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.07 |  | 28.2199 | 3.0123 | 29.055 | 28.28 | 0.1032 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.71 |  | 254.4585 | 0.0988 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.55 |  | 753.1827 | 0.1815 | 755.54 | 754.215 | 0.0278 | watch_only | none |
| 3 | IWM | market_regime | 296.02 |  | 295.6358 | 0.13 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 327.37 |  | 325.5426 | 0.5613 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 395.155 |  | 391.8247 | 0.8499 | 397.94 | 392.62 | 0.0506 | watch_only | none |
| 6 | ASML | semiconductor_equipment | 1793.46 |  | 1771.4909 | 1.2401 | 1829.9 | 1759.045 | 0.0524 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 371.69 |  | 368.7083 | 0.8087 | 364.41 | 357.885 | 0.0215 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 29.07 |  | 28.2199 | 3.0123 | 29.055 | 28.28 | 0.1032 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.7901 | 3.4874 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 10 | MSFT | cloud_ai_capex | 396.01 |  | 395.1517 | 0.2172 | 391.33 | 387.05 | 0.4646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | SMH | semiconductor_index | 589.135 |  | 587.2498 | 0.321 | 606.85 | 597.81 | 0.0679 | below_opening_15m_low | below_opening_15m_low |
| 12 | QQQ | market_regime | 718.06 |  | 716.2631 | 0.2509 | 724.31 | 721.08 | 0.0167 | below_opening_15m_low | below_opening_15m_low |
| 13 | IREN | high_beta_ai_infrastructure | 39.955 |  | 39.1435 | 2.0731 | 40.01 | 38.815 | 0.0751 | watch_only | none |
| 14 | AMAT | semiconductor_equipment | 577.99 |  | 577.7428 | 0.0428 | 610.62 | 586.86 | 0.1592 | below_opening_15m_low | below_opening_15m_low |
| 15 | TT | data_center_power_cooling | 478.86 |  | 478.7437 | 0.0243 | 485.9 | 482.93 | 0.2088 | below_opening_15m_low | below_opening_15m_low |
| 16 | JCI | data_center_power_cooling | 142.005 |  | 141.7013 | 0.2143 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | NVDA | ai_accelerator | 210.26 |  | 209.1884 | 0.5122 | 213.775 | 211.225 | 0.038 | below_opening_15m_low | below_opening_15m_low |
| 18 | SOXX | semiconductor_index | 554.825 |  | 551.3124 | 0.6371 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| 19 | ENTG | semiconductor_materials | 137.86 |  | 137.6799 | 0.1308 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | HPE | ai_server_oem | 47.11 |  | 46.9187 | 0.4078 | 50.2 | 48.995 | 0.0425 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 371.69 |  | 368.7083 | 0.8087 | 364.41 | 357.885 | 0.0215 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.71 |  | 254.4585 | 0.0988 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.37 |  | 325.5426 | 0.5613 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.7901 | 3.4874 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| 5 | APLD | high_beta_ai_infrastructure | 29.07 |  | 28.2199 | 3.0123 | 29.055 | 28.28 | 0.1032 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 675.17 |  | 675.4718 | -0.0447 | 664.875 | 657.17 | 1.3952 | below_vwap | below_vwap,spread_too_wide |
| 7 | MSFT | cloud_ai_capex | 396.01 |  | 395.1517 | 0.2172 | 391.33 | 387.05 | 0.4646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AVGO | custom_silicon_networking | 395.155 |  | 391.8247 | 0.8499 | 397.94 | 392.62 | 0.0506 | watch_only | none |
| 9 | ASML | semiconductor_equipment | 1793.46 |  | 1771.4909 | 1.2401 | 1829.9 | 1759.045 | 0.0524 | watch_only | none |
| 10 | SPY | market_regime | 754.55 |  | 753.1827 | 0.1815 | 755.54 | 754.215 | 0.0278 | watch_only | none |
| 11 | ORCL | cloud_ai_capex | 132.98 |  | 131.7024 | 0.97 | 132.925 | 129.92 | 0.6618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | IWM | market_regime | 296.02 |  | 295.6358 | 0.13 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 13 | IREN | high_beta_ai_infrastructure | 39.955 |  | 39.1435 | 2.0731 | 40.01 | 38.815 | 0.0751 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 178.925 |  | 175.6259 | 1.8785 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | NVDA | ai_accelerator | 210.26 |  | 209.1884 | 0.5122 | 213.775 | 211.225 | 0.038 | below_opening_15m_low | below_opening_15m_low |
| 17 | MU | memory_hbm_storage | 914.005 |  | 910.1855 | 0.4196 | 977.7 | 953.67 | 0.9726 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 424.095 |  | 419.0736 | 1.1982 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SOXX | semiconductor_index | 554.825 |  | 551.3124 | 0.6371 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| 20 | STX | memory_hbm_storage | 822.34 |  | 817.3043 | 0.6161 | 889.1 | 850.01 | 1.6842 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.06 |  | 716.2631 | 0.2509 | 724.31 | 721.08 | 0.0167 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.45 |  | 74.1952 | 0.3435 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.26 |  | 209.1884 | 0.5122 | 213.775 | 211.225 | 0.038 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.01 |  | 395.1517 | 0.2172 | 391.33 | 387.05 | 0.4646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 327.37 |  | 325.5426 | 0.5613 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.69 |  | 368.7083 | 0.8087 | 364.41 | 357.885 | 0.0215 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 531.07 |  | 527.212 | 0.7318 | 558.62 | 548.745 | 0.3709 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 421.33 |  | 418.9043 | 0.5791 | 428.59 | 422.945 | 0.9185 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.825 |  | 551.3124 | 0.6371 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.135 |  | 587.2498 | 0.321 | 606.85 | 597.81 | 0.0679 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 395.155 |  | 391.8247 | 0.8499 | 397.94 | 392.62 | 0.0506 | watch_only | none |
| MU | memory_hbm_storage | 914.005 |  | 910.1855 | 0.4196 | 977.7 | 953.67 | 0.9726 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 208.25 |  | 208.4916 | -0.1159 | 223.02 | 214.85 | 0.1681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 406.935 |  | 407.2375 | -0.0743 | 457.935 | 442.67 | 0.0885 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 47.11 |  | 46.9187 | 0.4078 | 50.2 | 48.995 | 0.0425 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.09 |  | 26.8736 | 0.8051 | 28.295 | 27.55 | 0.0738 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.55 |  | 753.1827 | 0.1815 | 755.54 | 754.215 | 0.0278 | watch_only | none |
| IWM | market_regime | 296.02 |  | 295.6358 | 0.13 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 132.98 |  | 131.7024 | 0.97 | 132.925 | 129.92 | 0.6618 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 78.51 |  | 77.4348 | 1.3885 | 80.585 | 78.73 | 3.5027 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 301.74 |  | 299.1326 | 0.8716 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 411.37 |  | 408.4899 | 0.7051 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.755 |  | 644.7998 | 1.0787 | 663.475 | 653.94 | 5.0909 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 1049.99 |  | 1032.7076 | 1.6735 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.86 |  | 478.7437 | 0.0243 | 485.9 | 482.93 | 0.2088 | below_opening_15m_low | below_opening_15m_low |
| JCI | data_center_power_cooling | 142.005 |  | 141.7013 | 0.2143 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ANET | ai_networking_optical | 171.72 |  | 171.8746 | -0.09 | 186.095 | 178.355 | 4.6587 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 296.5 |  | 293.9525 | 0.8666 | 315.74 | 303.34 | 0.344 | below_opening_15m_low | below_opening_15m_low |
| LITE | ai_networking_optical | 757.155 |  | 748.5451 | 1.1502 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 424.095 |  | 419.0736 | 1.1982 | 438.14 | 427.54 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 111.95 |  | 112.3134 | -0.3236 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 349.86 |  | 344.6617 | 1.5082 | 369.23 | 356.615 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ASML | semiconductor_equipment | 1793.46 |  | 1771.4909 | 1.2401 | 1829.9 | 1759.045 | 0.0524 | watch_only | none |
| AMAT | semiconductor_equipment | 577.99 |  | 577.7428 | 0.0428 | 610.62 | 586.86 | 0.1592 | below_opening_15m_low | below_opening_15m_low |
| LRCX | semiconductor_equipment | 332.06 |  | 331.4161 | 0.1943 | 355.245 | 340.745 | 0.9848 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 223.3 |  | 222.6382 | 0.2973 | 236.49 | 225.11 | 1.5584 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TER | semiconductor_test_packaging | 340.23 |  | 335.522 | 1.4032 | 356.29 | 343.785 | 0.8671 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 306.94 |  | 307.4856 | -0.1774 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.765 |  | 66.8816 | 1.3208 | 70.42 | 68.43 | 3.6154 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.675 |  | 54.3438 | 0.6094 | 57.92 | 55.2 | 0.6584 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ENTG | semiconductor_materials | 137.86 |  | 137.6799 | 0.1308 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| MKSI | semiconductor_materials | 352.79 |  | 348.5999 | 1.202 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.555 |  | 516.1031 | -0.1062 | 521.075 | 518.3 | 4.7075 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.095 |  | 294.8317 | -0.5891 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.07 |  | 28.2199 | 3.0123 | 29.055 | 28.28 | 0.1032 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 39.955 |  | 39.1435 | 2.0731 | 40.01 | 38.815 | 0.0751 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.55 |  | 21.7901 | 3.4874 | 22.36 | 21.94 | 0.0887 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1628.025 |  | 1572.984 | 3.4991 | 1726.34 | 1665.91 | 0.5061 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 515.18 |  | 516.606 | -0.276 | 568.16 | 542.4 | 0.4542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 822.34 |  | 817.3043 | 0.6161 | 889.1 | 850.01 | 1.6842 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMZN | cloud_ai_capex | 254.71 |  | 254.4585 | 0.0988 | 252.89 | 249.98 | 0.0275 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.17 |  | 675.4718 | -0.0447 | 664.875 | 657.17 | 1.3952 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 274.46 |  | 275.9129 | -0.5266 | 286.73 | 280.14 | 1.8582 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 178.925 |  | 175.6259 | 1.8785 | 183.63 | 176.08 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
