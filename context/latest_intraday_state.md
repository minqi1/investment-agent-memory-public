# Intraday State

- Generated at: `2026-07-17T02:19:45+08:00`
- Market time ET: `2026-07-16T14:19:46-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 1, 'below_vwap': 11, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.145 |  | 709.5814 | -0.3434 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.12 |  | 534.0544 | -0.9239 | 543.4 | 535.47 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.56 |  | 572.1603 | -0.804 | 580.31 | 572.21 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.18 |  | 752.4917 | -0.1743 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.555 |  | 398.8453 | 1.4315 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.555 |  | 398.8453 | 1.4315 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.66 |  | 294.9 | 0.2577 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | LIN | industrial_gases | 516.99 |  | 515.0437 | 0.3779 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ASML | semiconductor_equipment | 1796.37 |  | 1819.2063 | -1.2553 | 1823.13 | 1796.26 | 0.0891 | below_vwap | below_vwap |
| 5 | SPY | market_regime | 751.18 |  | 752.4917 | -0.1743 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 6 | IWM | market_regime | 295.375 |  | 296.1795 | -0.2716 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 7 | ANET | ai_networking_optical | 168.1 |  | 166.5303 | 0.9426 | 169.91 | 165.6 | 4.0214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AMZN | cloud_ai_capex | 253.61 |  | 255.4903 | -0.736 | 258.07 | 252.62 | 0.0197 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ARM | ai_accelerator | 258 |  | 257.2805 | 0.2797 | 265.96 | 258.1 | 3.876 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 11 | TT | data_center_power_cooling | 473.03 |  | 474.2258 | -0.2522 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 140.46 |  | 140.5101 | -0.0356 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1024.16 |  | 1027.7232 | -0.3467 | 1035.07 | 1021.09 | 2.2067 | below_vwap | below_vwap,spread_too_wide |
| 14 | KLAC | semiconductor_equipment | 219.82 |  | 221.0265 | -0.5459 | 222.19 | 218.09 | 4.49 | below_vwap | below_vwap,spread_too_wide |
| 15 | META | cloud_ai_capex | 669.85 |  | 671.9475 | -0.3121 | 680.09 | 667.1 | 1.9781 | below_vwap | below_vwap,spread_too_wide |
| 16 | AAPL | mega_cap_platform | 330.17 |  | 330.592 | -0.1276 | 328.98 | 326.885 | 0.5331 | below_vwap | below_vwap,spread_too_wide |
| 17 | SOXX | semiconductor_index | 529.12 |  | 534.0544 | -0.9239 | 543.4 | 535.47 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | QQQ | market_regime | 707.145 |  | 709.5814 | -0.3434 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | MU | memory_hbm_storage | 851 |  | 857.5623 | -0.7652 | 887.1 | 866.765 | 0.1199 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | NVDA | ai_accelerator | 206.92 |  | 207.378 | -0.2209 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.555 |  | 398.8453 | 1.4315 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.17 |  | 330.592 | -0.1276 | 328.98 | 326.885 | 0.5331 | below_vwap | below_vwap,spread_too_wide |
| 3 | LIN | industrial_gases | 516.99 |  | 515.0437 | 0.3779 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 295.66 |  | 294.9 | 0.2577 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 473.03 |  | 474.2258 | -0.2522 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.46 |  | 140.5101 | -0.0356 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | GEV | data_center_power_cooling | 1024.16 |  | 1027.7232 | -0.3467 | 1035.07 | 1021.09 | 2.2067 | below_vwap | below_vwap,spread_too_wide |
| 8 | ASML | semiconductor_equipment | 1796.37 |  | 1819.2063 | -1.2553 | 1823.13 | 1796.26 | 0.0891 | below_vwap | below_vwap |
| 9 | KLAC | semiconductor_equipment | 219.82 |  | 221.0265 | -0.5459 | 222.19 | 218.09 | 4.49 | below_vwap | below_vwap,spread_too_wide |
| 10 | SPY | market_regime | 751.18 |  | 752.4917 | -0.1743 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.375 |  | 296.1795 | -0.2716 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AMZN | cloud_ai_capex | 253.61 |  | 255.4903 | -0.736 | 258.07 | 252.62 | 0.0197 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 669.85 |  | 671.9475 | -0.3121 | 680.09 | 667.1 | 1.9781 | below_vwap | below_vwap,spread_too_wide |
| 15 | ANET | ai_networking_optical | 168.1 |  | 166.5303 | 0.9426 | 169.91 | 165.6 | 4.0214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ARM | ai_accelerator | 258 |  | 257.2805 | 0.2797 | 265.96 | 258.1 | 3.876 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 17 | SOXX | semiconductor_index | 529.12 |  | 534.0544 | -0.9239 | 543.4 | 535.47 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | TSM | foundry | 405.275 |  | 409.1362 | -0.9437 | 414.385 | 406.61 | 0.6267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | CIEN | ai_networking_optical | 391.03 |  | 395.0454 | -1.0164 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 20 | QQQ | market_regime | 707.145 |  | 709.5814 | -0.3434 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.145 |  | 709.5814 | -0.3434 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.1 |  | 71.8808 | -1.0862 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.92 |  | 207.378 | -0.2209 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.555 |  | 398.8453 | 1.4315 | 398.69 | 392.2 | 0.1211 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.17 |  | 330.592 | -0.1276 | 328.98 | 326.885 | 0.5331 | below_vwap | below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 364.55 |  | 370.4449 | -1.5913 | 375.18 | 369.2 | 0.181 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 496.9 |  | 504.5782 | -1.5217 | 518.33 | 507.62 | 1.8877 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.275 |  | 409.1362 | -0.9437 | 414.385 | 406.61 | 0.6267 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.12 |  | 534.0544 | -0.9239 | 543.4 | 535.47 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.56 |  | 572.1603 | -0.804 | 580.31 | 572.21 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.66 |  | 380.1914 | -0.9288 | 386.58 | 378.53 | 0.6159 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 851 |  | 857.5623 | -0.7652 | 887.1 | 866.765 | 0.1199 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.79 |  | 191.2108 | -1.789 | 201.61 | 194.19 | 0.5804 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 398.86 |  | 402.4213 | -0.885 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.265 |  | 45.8595 | -1.2963 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.92 |  | 25.3664 | -1.76 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.18 |  | 752.4917 | -0.1743 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.375 |  | 296.1795 | -0.2716 | 296.28 | 294.65 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.15 |  | 126.6691 | -0.4098 | 131.36 | 126.665 | 3.9635 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.59 |  | 73.3372 | -1.0188 | 75.54 | 73.985 | 1.6393 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.14 |  | 293.7062 | -1.5547 | 300.385 | 293.64 | 1.6808 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 395.62 |  | 399.4231 | -0.9522 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.9 |  | 631.5318 | -0.7334 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1024.16 |  | 1027.7232 | -0.3467 | 1035.07 | 1021.09 | 2.2067 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.03 |  | 474.2258 | -0.2522 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.46 |  | 140.5101 | -0.0356 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.1 |  | 166.5303 | 0.9426 | 169.91 | 165.6 | 4.0214 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.98 |  | 280.9324 | -1.4069 | 288.48 | 280.67 | 0.4369 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 704.155 |  | 708.5712 | -0.6233 | 737.175 | 720.21 | 0.2542 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 391.03 |  | 395.0454 | -1.0164 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.39 |  | 101.4857 | -3.0504 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.21 |  | 323.7098 | -1.699 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.37 |  | 1819.2063 | -1.2553 | 1823.13 | 1796.26 | 0.0891 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 561.32 |  | 570.3908 | -1.5903 | 572.69 | 562.32 | 3.816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.28 |  | 323.0909 | -1.489 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.82 |  | 221.0265 | -0.5459 | 222.19 | 218.09 | 4.49 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 323.48 |  | 326.8207 | -1.0222 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.85 |  | 287.2421 | -2.2253 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.79 |  | 63.9983 | -1.8879 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.71 |  | 51.9189 | -2.3285 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.7 |  | 134.9931 | -0.9579 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.23 |  | 336.0268 | -1.7251 | 346.26 | 338 | 0.4875 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.99 |  | 515.0437 | 0.3779 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.66 |  | 294.9 | 0.2577 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.145 |  | 26.8304 | -2.5544 | 28.05 | 27.6 | 0.0382 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.08 |  | 35.5229 | -1.2469 | 37.365 | 36.4 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.93 |  | 21.2339 | -1.4314 | 22.18 | 21.78 | 0.0956 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1427.46 |  | 1466.06 | -2.6329 | 1549.47 | 1482.06 | 1.6729 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 458.19 |  | 474.897 | -3.518 | 498.04 | 480.14 | 3.1603 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 748.78 |  | 766.2404 | -2.2787 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 253.61 |  | 255.4903 | -0.736 | 258.07 | 252.62 | 0.0197 | below_vwap | below_vwap |
| META | cloud_ai_capex | 669.85 |  | 671.9475 | -0.3121 | 680.09 | 667.1 | 1.9781 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258 |  | 257.2805 | 0.2797 | 265.96 | 258.1 | 3.876 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| SKHY | memory_hbm_storage | 156.44 |  | 161.9535 | -3.4044 | 168.11 | 162.41 | 1.2848 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
