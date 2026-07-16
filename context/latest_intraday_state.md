# Intraday State

- Generated at: `2026-07-17T01:35:50+08:00`
- Market time ET: `2026-07-16T13:35:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 2, 'below_vwap': 10, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.72 |  | 709.8387 | -0.2985 | 713.55 | 708.25 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.12 |  | 534.9772 | -1.2818 | 543.4 | 535.47 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.3 |  | 573.05 | -1.0034 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.105 |  | 752.7197 | -0.0817 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.805 |  | 398.1301 | 1.1742 | 398.69 | 392.2 | 0.3327 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.22 |  | 330.3061 | 0.8822 | 328.98 | 326.885 | 0.021 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 255.87 |  | 255.553 | 0.124 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 2 | TT | data_center_power_cooling | 475.66 |  | 474.33 | 0.2804 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | LIN | industrial_gases | 516.225 |  | 514.9544 | 0.2467 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | AAPL | mega_cap_platform | 333.22 |  | 330.3061 | 0.8822 | 328.98 | 326.885 | 0.021 | buy_precheck_manual_confirm | none |
| 5 | APD | industrial_gases | 295.07 |  | 294.873 | 0.0668 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | MSFT | cloud_ai_capex | 402.805 |  | 398.1301 | 1.1742 | 398.69 | 392.2 | 0.3327 | buy_precheck_manual_confirm | none |
| 7 | ANET | ai_networking_optical | 167.49 |  | 166.4706 | 0.6124 | 169.91 | 165.6 | 4.0779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1796.95 |  | 1821.2845 | -1.3361 | 1823.13 | 1796.26 | 0.0668 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 752.105 |  | 752.7197 | -0.0817 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.51 |  | 296.3596 | -0.2867 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 218.92 |  | 221.2889 | -1.0705 | 222.19 | 218.09 | 0.1644 | below_vwap | below_vwap |
| 13 | GOOGL | cloud_ai_capex | 371.665 |  | 371.8545 | -0.051 | 375.18 | 369.2 | 0.3175 | below_vwap | below_vwap |
| 14 | ENTG | semiconductor_materials | 134.1 |  | 135.1147 | -0.751 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 140.5 |  | 140.5462 | -0.0329 | 140.83 | 139.43 | 0.4769 | below_vwap | below_vwap,spread_too_wide |
| 16 | GEV | data_center_power_cooling | 1022.13 |  | 1028.7035 | -0.639 | 1035.07 | 1021.09 | 2.1876 | below_vwap | below_vwap,spread_too_wide |
| 17 | META | cloud_ai_capex | 669.12 |  | 672.7282 | -0.5364 | 680.09 | 667.1 | 2.1252 | below_vwap | below_vwap,spread_too_wide |
| 18 | SOXX | semiconductor_index | 528.12 |  | 534.9772 | -1.2818 | 543.4 | 535.47 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | QQQ | market_regime | 707.72 |  | 709.8387 | -0.2985 | 713.55 | 708.25 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | NVDA | ai_accelerator | 206.975 |  | 207.4775 | -0.2422 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.805 |  | 398.1301 | 1.1742 | 398.69 | 392.2 | 0.3327 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.22 |  | 330.3061 | 0.8822 | 328.98 | 326.885 | 0.021 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.66 |  | 474.33 | 0.2804 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 516.225 |  | 514.9544 | 0.2467 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 295.07 |  | 294.873 | 0.0668 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | AMZN | cloud_ai_capex | 255.87 |  | 255.553 | 0.124 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 7 | JCI | data_center_power_cooling | 140.5 |  | 140.5462 | -0.0329 | 140.83 | 139.43 | 0.4769 | below_vwap | below_vwap,spread_too_wide |
| 8 | GEV | data_center_power_cooling | 1022.13 |  | 1028.7035 | -0.639 | 1035.07 | 1021.09 | 2.1876 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1796.95 |  | 1821.2845 | -1.3361 | 1823.13 | 1796.26 | 0.0668 | below_vwap | below_vwap |
| 10 | KLAC | semiconductor_equipment | 218.92 |  | 221.2889 | -1.0705 | 222.19 | 218.09 | 0.1644 | below_vwap | below_vwap |
| 11 | SPY | market_regime | 752.105 |  | 752.7197 | -0.0817 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 12 | IWM | market_regime | 295.51 |  | 296.3596 | -0.2867 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 134.1 |  | 135.1147 | -0.751 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | GOOGL | cloud_ai_capex | 371.665 |  | 371.8545 | -0.051 | 375.18 | 369.2 | 0.3175 | below_vwap | below_vwap |
| 16 | META | cloud_ai_capex | 669.12 |  | 672.7282 | -0.5364 | 680.09 | 667.1 | 2.1252 | below_vwap | below_vwap,spread_too_wide |
| 17 | ANET | ai_networking_optical | 167.49 |  | 166.4706 | 0.6124 | 169.91 | 165.6 | 4.0779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | SOXX | semiconductor_index | 528.12 |  | 534.9772 | -1.2818 | 543.4 | 535.47 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | TSM | foundry | 405.49 |  | 409.9101 | -1.0783 | 414.385 | 406.61 | 0.4069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | CIEN | ai_networking_optical | 391.16 |  | 396.0394 | -1.2321 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.72 |  | 709.8387 | -0.2985 | 713.55 | 708.25 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.255 |  | 71.9832 | -1.0117 | 73.09 | 71.45 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.975 |  | 207.4775 | -0.2422 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.805 |  | 398.1301 | 1.1742 | 398.69 | 392.2 | 0.3327 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.22 |  | 330.3061 | 0.8822 | 328.98 | 326.885 | 0.021 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.665 |  | 371.8545 | -0.051 | 375.18 | 369.2 | 0.3175 | below_vwap | below_vwap |
| AMD | ai_accelerator | 496.5 |  | 506.3318 | -1.9418 | 518.33 | 507.62 | 0.3887 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.49 |  | 409.9101 | -1.0783 | 414.385 | 406.61 | 0.4069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.12 |  | 534.9772 | -1.2818 | 543.4 | 535.47 | 0.0757 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.3 |  | 573.05 | -1.0034 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.83 |  | 380.7923 | -0.7779 | 386.58 | 378.53 | 0.6537 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 847.86 |  | 859.0846 | -1.3066 | 887.1 | 866.765 | 1.5203 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.49 |  | 191.9125 | -2.3044 | 201.61 | 194.19 | 0.224 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 400.05 |  | 403.188 | -0.7783 | 411.65 | 400.635 | 4.5544 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.43 |  | 45.9779 | -1.1916 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.09 |  | 25.4444 | -1.3928 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.105 |  | 752.7197 | -0.0817 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.51 |  | 296.3596 | -0.2867 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.64 |  | 126.7422 | -0.0806 | 131.36 | 126.665 | 0.0711 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.885 |  | 73.4867 | -0.8188 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 290.22 |  | 294.5058 | -1.4552 | 300.385 | 293.64 | 1.6987 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.755 |  | 399.6796 | -1.2321 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 628.18 |  | 631.9483 | -0.5963 | 640.25 | 631.005 | 4.7359 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1022.13 |  | 1028.7035 | -0.639 | 1035.07 | 1021.09 | 2.1876 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.66 |  | 474.33 | 0.2804 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.5 |  | 140.5462 | -0.0329 | 140.83 | 139.43 | 0.4769 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 167.49 |  | 166.4706 | 0.6124 | 169.91 | 165.6 | 4.0779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.66 |  | 281.7274 | -1.7987 | 288.48 | 280.67 | 1.5434 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.24 |  | 710.3512 | -1.8457 | 737.175 | 720.21 | 3.2414 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 391.16 |  | 396.0394 | -1.2321 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.04 |  | 101.9256 | -2.831 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.17 |  | 324.0791 | -2.4405 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.95 |  | 1821.2845 | -1.3361 | 1823.13 | 1796.26 | 0.0668 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 561.67 |  | 572.1406 | -1.8301 | 572.69 | 562.32 | 0.1389 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 318.27 |  | 324.6925 | -1.978 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.92 |  | 221.2889 | -1.0705 | 222.19 | 218.09 | 0.1644 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.34 |  | 327.3122 | -1.5191 | 332.49 | 326.685 | 0.2513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ONTO | semiconductor_test_packaging | 281.78 |  | 288.5425 | -2.3437 | 295.83 | 285.02 | 0.4046 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.69 |  | 64.2372 | -2.4085 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.16 |  | 52.2255 | -2.0401 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.1 |  | 135.1147 | -0.751 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 330.73 |  | 338.1342 | -2.1897 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 516.225 |  | 514.9544 | 0.2467 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.07 |  | 294.873 | 0.0668 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.175 |  | 26.975 | -2.9659 | 28.05 | 27.6 | 0.1528 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.69 |  | 35.6356 | -2.6534 | 37.365 | 36.4 | 0.0577 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.845 |  | 21.2825 | -2.0556 | 22.18 | 21.78 | 0.0959 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1432.385 |  | 1472.2802 | -2.7098 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 457.35 |  | 476.4229 | -4.0033 | 498.04 | 480.14 | 0.387 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 747.32 |  | 767.892 | -2.679 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.87 |  | 255.553 | 0.124 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 669.12 |  | 672.7282 | -0.5364 | 680.09 | 667.1 | 2.1252 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.81 |  | 257.3878 | -0.613 | 265.96 | 258.1 | 3.9092 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.56 |  | 162.5476 | -3.6836 | 168.11 | 162.41 | 1.4371 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
