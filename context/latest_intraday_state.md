# Intraday State

- Generated at: `2026-07-17T01:59:44+08:00`
- Market time ET: `2026-07-16T13:59:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'below_vwap': 9, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.5 |  | 709.7045 | -0.4515 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 525.8 |  | 534.5438 | -1.6358 | 543.4 | 535.47 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.895 |  | 572.4671 | -1.3227 | 580.31 | 572.21 | 0.0708 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.28 |  | 752.661 | -0.1835 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.61 |  | 398.5011 | 1.0311 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.78 |  | 330.5541 | 0.3709 | 328.98 | 326.885 | 0.1055 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.78 |  | 330.5541 | 0.3709 | 328.98 | 326.885 | 0.1055 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 402.61 |  | 398.5011 | 1.0311 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 516.93 |  | 514.9937 | 0.376 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ANET | ai_networking_optical | 166.775 |  | 166.4889 | 0.1719 | 169.91 | 165.6 | 3.2079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | APD | industrial_gases | 295.34 |  | 294.8827 | 0.1551 | 293.89 | 291.35 | 4.2189 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SPY | market_regime | 751.28 |  | 752.661 | -0.1835 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 7 | IWM | market_regime | 294.955 |  | 296.266 | -0.4425 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 140.12 |  | 140.5369 | -0.2966 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | GOOGL | cloud_ai_capex | 371.55 |  | 371.8416 | -0.0784 | 375.18 | 369.2 | 0.218 | below_vwap | below_vwap |
| 11 | KLAC | semiconductor_equipment | 218.185 |  | 221.0903 | -1.3141 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AMZN | cloud_ai_capex | 255.05 |  | 255.5512 | -0.1961 | 258.07 | 252.62 | 0.2078 | below_vwap | below_vwap |
| 13 | TT | data_center_power_cooling | 474.36 |  | 474.4235 | -0.0134 | 474.085 | 467.64 | 4.9751 | below_vwap | below_vwap,spread_too_wide |
| 14 | META | cloud_ai_capex | 668.91 |  | 672.2839 | -0.5019 | 680.09 | 667.1 | 0.4425 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 525.8 |  | 534.5438 | -1.6358 | 543.4 | 535.47 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 706.5 |  | 709.7045 | -0.4515 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.61 |  | 207.4129 | -0.3871 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ASML | semiconductor_equipment | 1791.935 |  | 1820.023 | -1.5433 | 1823.13 | 1796.26 | 0.1144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 564.895 |  | 572.4671 | -1.3227 | 580.31 | 572.21 | 0.0708 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | HPE | ai_server_oem | 44.93 |  | 45.8987 | -2.1105 | 47.65 | 46.165 | 0.0445 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.61 |  | 398.5011 | 1.0311 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.78 |  | 330.5541 | 0.3709 | 328.98 | 326.885 | 0.1055 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.36 |  | 474.4235 | -0.0134 | 474.085 | 467.64 | 4.9751 | below_vwap | below_vwap,spread_too_wide |
| 4 | LIN | industrial_gases | 516.93 |  | 514.9937 | 0.376 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.34 |  | 294.8827 | 0.1551 | 293.89 | 291.35 | 4.2189 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | JCI | data_center_power_cooling | 140.12 |  | 140.5369 | -0.2966 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | KLAC | semiconductor_equipment | 218.185 |  | 221.0903 | -1.3141 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | SPY | market_regime | 751.28 |  | 752.661 | -0.1835 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 294.955 |  | 296.266 | -0.4425 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GOOGL | cloud_ai_capex | 371.55 |  | 371.8416 | -0.0784 | 375.18 | 369.2 | 0.218 | below_vwap | below_vwap |
| 12 | AMZN | cloud_ai_capex | 255.05 |  | 255.5512 | -0.1961 | 258.07 | 252.62 | 0.2078 | below_vwap | below_vwap |
| 13 | META | cloud_ai_capex | 668.91 |  | 672.2839 | -0.5019 | 680.09 | 667.1 | 0.4425 | below_vwap | below_vwap,spread_too_wide |
| 14 | ANET | ai_networking_optical | 166.775 |  | 166.4889 | 0.1719 | 169.91 | 165.6 | 3.2079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | SOXX | semiconductor_index | 525.8 |  | 534.5438 | -1.6358 | 543.4 | 535.47 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 403.9 |  | 409.339 | -1.3287 | 414.385 | 406.61 | 0.1956 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | CIEN | ai_networking_optical | 388.11 |  | 395.5262 | -1.875 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 706.5 |  | 709.7045 | -0.4515 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 376.38 |  | 380.4899 | -1.0802 | 386.58 | 378.53 | 1.5941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 844.79 |  | 858.0442 | -1.5447 | 887.1 | 866.765 | 0.6262 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.5 |  | 709.7045 | -0.4515 | 713.55 | 708.25 | 0.0212 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.86 |  | 71.9264 | -1.4827 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.61 |  | 207.4129 | -0.3871 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.61 |  | 398.5011 | 1.0311 | 398.69 | 392.2 | 0.1416 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.78 |  | 330.5541 | 0.3709 | 328.98 | 326.885 | 0.1055 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.55 |  | 371.8416 | -0.0784 | 375.18 | 369.2 | 0.218 | below_vwap | below_vwap |
| AMD | ai_accelerator | 492.99 |  | 505.312 | -2.4385 | 518.33 | 507.62 | 0.4483 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 403.9 |  | 409.339 | -1.3287 | 414.385 | 406.61 | 0.1956 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 525.8 |  | 534.5438 | -1.6358 | 543.4 | 535.47 | 0.0609 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 564.895 |  | 572.4671 | -1.3227 | 580.31 | 572.21 | 0.0708 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.38 |  | 380.4899 | -1.0802 | 386.58 | 378.53 | 1.5941 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 844.79 |  | 858.0442 | -1.5447 | 887.1 | 866.765 | 0.6262 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 186.56 |  | 191.4727 | -2.5658 | 201.61 | 194.19 | 0.1447 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 395.42 |  | 402.7674 | -1.8242 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.93 |  | 45.8987 | -2.1105 | 47.65 | 46.165 | 0.0445 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.93 |  | 25.3983 | -1.8437 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.28 |  | 752.661 | -0.1835 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.955 |  | 296.266 | -0.4425 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.88 |  | 126.6993 | -0.6467 | 131.36 | 126.665 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.12 |  | 73.3965 | -1.7392 | 75.54 | 73.985 | 0.1109 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 287.69 |  | 294.01 | -2.1496 | 300.385 | 293.64 | 1.0567 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.265 |  | 399.5658 | -1.3266 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.22 |  | 631.7085 | -0.8688 | 640.25 | 631.005 | 0.2363 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1018.58 |  | 1028.2288 | -0.9384 | 1035.07 | 1021.09 | 0.1698 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 474.36 |  | 474.4235 | -0.0134 | 474.085 | 467.64 | 4.9751 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.12 |  | 140.5369 | -0.2966 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.775 |  | 166.4889 | 0.1719 | 169.91 | 165.6 | 3.2079 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 274.99 |  | 281.304 | -2.2446 | 288.48 | 280.67 | 2.1819 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 694.24 |  | 709.5364 | -2.1558 | 737.175 | 720.21 | 2.1318 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.11 |  | 395.5262 | -1.875 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.24 |  | 101.6208 | -3.3269 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 315.54 |  | 323.9022 | -2.5817 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1791.935 |  | 1820.023 | -1.5433 | 1823.13 | 1796.26 | 0.1144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 559.25 |  | 570.8911 | -2.0391 | 572.69 | 562.32 | 1.3411 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 315.85 |  | 323.3888 | -2.3312 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.185 |  | 221.0903 | -1.3141 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 319.54 |  | 326.9966 | -2.2803 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.1 |  | 287.9699 | -2.7329 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.365 |  | 64.1022 | -2.71 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.525 |  | 52.1223 | -3.0644 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.59 |  | 135.0225 | -1.0609 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.925 |  | 337.5093 | -2.2471 | 346.26 | 338 | 4.6162 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.93 |  | 514.9937 | 0.376 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.34 |  | 294.8827 | 0.1551 | 293.89 | 291.35 | 4.2189 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 25.83 |  | 26.8888 | -3.9378 | 28.05 | 27.6 | 0.0387 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.525 |  | 35.5623 | -2.9169 | 37.365 | 36.4 | 0.029 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.775 |  | 21.2514 | -2.2418 | 22.18 | 21.78 | 0.0481 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1412.955 |  | 1468.2702 | -3.7674 | 1549.47 | 1482.06 | 3.5387 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.68 |  | 475.5628 | -4.3912 | 498.04 | 480.14 | 2.4193 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 742.97 |  | 767.0376 | -3.1377 | 797.155 | 768.7 | 4.5358 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.05 |  | 255.5512 | -0.1961 | 258.07 | 252.62 | 0.2078 | below_vwap | below_vwap |
| META | cloud_ai_capex | 668.91 |  | 672.2839 | -0.5019 | 680.09 | 667.1 | 0.4425 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.28 |  | 257.3153 | -0.791 | 265.96 | 258.1 | 2.1232 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.295 |  | 162.1706 | -3.6231 | 168.11 | 162.41 | 1.7531 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
