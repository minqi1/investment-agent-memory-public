# Intraday State

- Generated at: `2026-07-29T02:46:13+08:00`
- Market time ET: `2026-07-28T14:46:14-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 16, 'manual_confirm_candidate': 4, 'below_vwap': 10, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 1, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.235 |  | 674.1294 | 0.3123 | 677.3 | 670.84 | 0.0384 | watch_only | none |
| SOXX | semiconductor_index | 491.11 |  | 489.9717 | 0.2323 | 497.64 | 485.42 | 0.0672 | watch_only | none |
| SMH | semiconductor_index | 529.11 |  | 527.3569 | 0.3324 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| SPY | market_regime | 741.02 |  | 739.5423 | 0.1998 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.06 |  | 196.0721 | 0.5038 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.02 |  | 739.5423 | 0.1998 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| 3 | ANET | ai_networking_optical | 168.88 |  | 164.9358 | 2.3913 | 165.975 | 160.51 | 0.2961 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.66 |  | 330.8396 | 1.457 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.02 |  | 739.5423 | 0.1998 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 529.11 |  | 527.3569 | 0.3324 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| 3 | SOXX | semiconductor_index | 491.11 |  | 489.9717 | 0.2323 | 497.64 | 485.42 | 0.0672 | watch_only | none |
| 4 | QQQ | market_regime | 676.235 |  | 674.1294 | 0.3123 | 677.3 | 670.84 | 0.0384 | watch_only | none |
| 5 | TT | data_center_power_cooling | 466.52 |  | 465.2149 | 0.2805 | 477.73 | 460.77 | 0.1093 | watch_only | none |
| 6 | IWM | market_regime | 292.925 |  | 292.3775 | 0.1873 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 7 | NVDA | ai_accelerator | 197.06 |  | 196.0721 | 0.5038 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 231.19 |  | 230.4887 | 0.3043 | 233.05 | 229.7 | 0.0562 | watch_only | none |
| 9 | HPE | ai_server_oem | 44.53 |  | 44.4401 | 0.2022 | 46.19 | 44.33 | 0.0674 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 191.13 |  | 190.7686 | 0.1895 | 194.96 | 189.48 | 0.1517 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 397.58 |  | 396.3741 | 0.3042 | 400.09 | 392.355 | 0.2213 | watch_only | none |
| 12 | MU | memory_hbm_storage | 820.01 |  | 815.4481 | 0.5594 | 846.4 | 813.91 | 0.0951 | watch_only | none |
| 13 | MRVL | custom_silicon_networking | 175.06 |  | 174.1992 | 0.4941 | 181.24 | 172.395 | 0.2856 | watch_only | none |
| 14 | GOOGL | cloud_ai_capex | 335.66 |  | 330.8396 | 1.457 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 28.24 |  | 28.0016 | 0.8514 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 16 | JCI | data_center_power_cooling | 139.725 |  | 138.5686 | 0.8345 | 139.755 | 137.31 | 0.2648 | watch_only | none |
| 17 | ASML | semiconductor_equipment | 1581.41 |  | 1577.3046 | 0.2603 | 1586.01 | 1565.95 | 1.357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | GEV | data_center_power_cooling | 939.35 |  | 937.563 | 0.1906 | 955.825 | 935.665 | 0.5387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 456.425 |  | 455.5368 | 0.195 | 472.485 | 453.76 | 4.6798 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ALAB | ai_networking_optical | 260.33 |  | 259.0846 | 0.4807 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.06 |  | 196.0721 | 0.5038 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.02 |  | 739.5423 | 0.1998 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| 3 | ANET | ai_networking_optical | 168.88 |  | 164.9358 | 2.3913 | 165.975 | 160.51 | 0.2961 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.66 |  | 330.8396 | 1.457 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 391.48 |  | 387.7544 | 0.9608 | 390.46 | 382.495 | 1.1852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AVGO | custom_silicon_networking | 380.62 |  | 378.609 | 0.5311 | 378.64 | 371.57 | 2.4408 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ETN | data_center_power_cooling | 384.92 |  | 381.2442 | 0.9642 | 384.565 | 377.43 | 2.6369 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ORCL | cloud_ai_capex | 121.135 |  | 118.4986 | 2.2249 | 117.17 | 115.25 | 0.7017 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MU | memory_hbm_storage | 820.01 |  | 815.4481 | 0.5594 | 846.4 | 813.91 | 0.0951 | watch_only | none |
| 10 | SMH | semiconductor_index | 529.11 |  | 527.3569 | 0.3324 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| 11 | SOXX | semiconductor_index | 491.11 |  | 489.9717 | 0.2323 | 497.64 | 485.42 | 0.0672 | watch_only | none |
| 12 | QQQ | market_regime | 676.235 |  | 674.1294 | 0.3123 | 677.3 | 670.84 | 0.0384 | watch_only | none |
| 13 | TT | data_center_power_cooling | 466.52 |  | 465.2149 | 0.2805 | 477.73 | 460.77 | 0.1093 | watch_only | none |
| 14 | JCI | data_center_power_cooling | 139.725 |  | 138.5686 | 0.8345 | 139.755 | 137.31 | 0.2648 | watch_only | none |
| 15 | IWM | market_regime | 292.925 |  | 292.3775 | 0.1873 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 16 | KLAC | semiconductor_equipment | 191.13 |  | 190.7686 | 0.1895 | 194.96 | 189.48 | 0.1517 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 397.58 |  | 396.3741 | 0.3042 | 400.09 | 392.355 | 0.2213 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.19 |  | 230.4887 | 0.3043 | 233.05 | 229.7 | 0.0562 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.53 |  | 44.4401 | 0.2022 | 46.19 | 44.33 | 0.0674 | watch_only | none |
| 20 | MRVL | custom_silicon_networking | 175.06 |  | 174.1992 | 0.4941 | 181.24 | 172.395 | 0.2856 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.235 |  | 674.1294 | 0.3123 | 677.3 | 670.84 | 0.0384 | watch_only | none |
| TQQQ | leveraged_tool | 61.71 |  | 61.109 | 0.9836 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.06 |  | 196.0721 | 0.5038 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.58 |  | 396.3741 | 0.3042 | 400.09 | 392.355 | 0.2213 | watch_only | none |
| AAPL | mega_cap_platform | 338.64 |  | 338.9625 | -0.0952 | 342.87 | 337.78 | 0.0089 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 335.66 |  | 330.8396 | 1.457 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 456.425 |  | 455.5368 | 0.195 | 472.485 | 453.76 | 4.6798 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.48 |  | 387.7544 | 0.9608 | 390.46 | 382.495 | 1.1852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.11 |  | 489.9717 | 0.2323 | 497.64 | 485.42 | 0.0672 | watch_only | none |
| SMH | semiconductor_index | 529.11 |  | 527.3569 | 0.3324 | 533.01 | 523.325 | 0.0567 | watch_only | none |
| AVGO | custom_silicon_networking | 380.62 |  | 378.609 | 0.5311 | 378.64 | 371.57 | 2.4408 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 820.01 |  | 815.4481 | 0.5594 | 846.4 | 813.91 | 0.0951 | watch_only | none |
| MRVL | custom_silicon_networking | 175.06 |  | 174.1992 | 0.4941 | 181.24 | 172.395 | 0.2856 | watch_only | none |
| DELL | ai_server_oem | 387.24 |  | 375.1765 | 3.2154 | 402 | 374.02 | 3.3648 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.53 |  | 44.4401 | 0.2022 | 46.19 | 44.33 | 0.0674 | watch_only | none |
| SMCI | ai_server_oem | 28.24 |  | 28.0016 | 0.8514 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 741.02 |  | 739.5423 | 0.1998 | 739.42 | 736.57 | 0.0216 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.925 |  | 292.3775 | 0.1873 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 121.135 |  | 118.4986 | 2.2249 | 117.17 | 115.25 | 0.7017 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.59 |  | 66.2558 | 0.5044 | 68.995 | 65.635 | 2.5079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.08 |  | 266.1252 | -0.017 | 273.86 | 266.04 | 0.2029 | below_vwap | below_vwap |
| ETN | data_center_power_cooling | 384.92 |  | 381.2442 | 0.9642 | 384.565 | 377.43 | 2.6369 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 586.01 |  | 582.368 | 0.6254 | 603.25 | 584.69 | 2.5597 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 939.35 |  | 937.563 | 0.1906 | 955.825 | 935.665 | 0.5387 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 466.52 |  | 465.2149 | 0.2805 | 477.73 | 460.77 | 0.1093 | watch_only | none |
| JCI | data_center_power_cooling | 139.725 |  | 138.5686 | 0.8345 | 139.755 | 137.31 | 0.2648 | watch_only | none |
| ANET | ai_networking_optical | 168.88 |  | 164.9358 | 2.3913 | 165.975 | 160.51 | 0.2961 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 241.97 |  | 237.4171 | 1.9177 | 256.145 | 236.73 | 0.1446 | watch_only | none |
| LITE | ai_networking_optical | 644.08 |  | 632.1473 | 1.8877 | 673.65 | 624.91 | 4.7634 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 341.51 |  | 337.4327 | 1.2083 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.46 |  | 85.8152 | 1.9167 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.33 |  | 259.0846 | 0.4807 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1581.41 |  | 1577.3046 | 0.2603 | 1586.01 | 1565.95 | 1.357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 474.97 |  | 476.3516 | -0.29 | 494.87 | 477.03 | 2.0296 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 270.34 |  | 266.651 | 1.3835 | 276.85 | 267.14 | 0.9063 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.13 |  | 190.7686 | 0.1895 | 194.96 | 189.48 | 0.1517 | watch_only | none |
| TER | semiconductor_test_packaging | 311.6 |  | 308.6158 | 0.967 | 315.21 | 304.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 238.47 |  | 236.7558 | 0.724 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.31 |  | 46.7028 | -2.9824 | 51.64 | 47.435 | 1.6111 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.985 |  | 42.4423 | -1.0775 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.67 |  | 119.1706 | -0.4201 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 282.03 |  | 282.3586 | -0.1164 | 296.8 | 283.22 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 516.14 |  | 518.1157 | -0.3813 | 518.6 | 511.495 | 4.8068 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.33 |  | 295.7539 | -0.1433 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.46 |  | 26.5157 | -0.2102 | 27 | 25.42 | 0.1134 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.64 |  | 33.7091 | -0.205 | 35.08 | 33.52 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.75 |  | 20.0851 | 3.3106 | 20.97 | 19.755 | 0.0964 | watch_only | none |
| SNDK | memory_hbm_storage | 1084.98 |  | 1099.6359 | -1.3328 | 1185.19 | 1114.57 | 3.0231 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 456.59 |  | 439.9292 | 3.7872 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 749.78 |  | 731.709 | 2.4697 | 774.805 | 719.02 | 4.9068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.19 |  | 230.4887 | 0.3043 | 233.05 | 229.7 | 0.0562 | watch_only | none |
| META | cloud_ai_capex | 593.86 |  | 593.8185 | 0.007 | 600.765 | 594.21 | 0.2307 | below_opening_15m_low | below_opening_15m_low |
| ARM | ai_accelerator | 244.45 |  | 245.2253 | -0.3162 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.15 |  | 131.5412 | -1.0576 | 136.45 | 131.735 | 0.1921 | below_opening_15m_low | below_opening_15m_low,below_vwap |
