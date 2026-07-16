# Intraday State

- Generated at: `2026-07-16T23:40:40+08:00`
- Market time ET: `2026-07-16T11:40:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 6, 'manual_confirm_candidate': 4, 'below_vwap': 14, 'spread_too_wide_or_missing': 15, 'price_stale_or_missing': 1, 'below_opening_15m_low': 16}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.775 |  | 710.5277 | 0.1755 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| SOXX | semiconductor_index | 536.92 |  | 537.6584 | -0.1373 | 543.4 | 535.47 | 0.0782 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.15 |  | 575.6375 | -0.0847 | 580.31 | 572.21 | 0.0452 | below_vwap | below_vwap |
| SPY | market_regime | 754.32 |  | 752.8161 | 0.1998 | 753.51 | 751.13 | 0.0305 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.32 |  | 752.8161 | 0.1998 | 753.51 | 751.13 | 0.0305 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.165 |  | 296.6206 | 0.1835 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 399.15 |  | 395.8984 | 0.8213 | 398.69 | 392.2 | 0.1077 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.38 |  | 329.4871 | 0.5745 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.32 |  | 752.8161 | 0.1998 | 753.51 | 751.13 | 0.0305 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.165 |  | 296.6206 | 0.1835 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 711.775 |  | 710.5277 | 0.1755 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 331.38 |  | 329.4871 | 0.5745 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 255.79 |  | 255.2313 | 0.2189 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 382.445 |  | 381.8662 | 0.1516 | 386.58 | 378.53 | 0.2876 | watch_only | none |
| 7 | NVDA | ai_accelerator | 207.68 |  | 207.6394 | 0.0195 | 211.03 | 207.49 | 0.1541 | watch_only | none |
| 8 | META | cloud_ai_capex | 676.075 |  | 674.9665 | 0.1642 | 680.09 | 667.1 | 0.2736 | watch_only | none |
| 9 | MSFT | cloud_ai_capex | 399.15 |  | 395.8984 | 0.8213 | 398.69 | 392.2 | 0.1077 | buy_precheck_manual_confirm | none |
| 10 | JCI | data_center_power_cooling | 140.86 |  | 140.7096 | 0.1069 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 633.9 |  | 633.236 | 0.1049 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | MKSI | semiconductor_materials | 341.56 |  | 341.2828 | 0.0812 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TER | semiconductor_test_packaging | 330.11 |  | 329.0159 | 0.3325 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AMKR | semiconductor_test_packaging | 64.71 |  | 64.6127 | 0.1505 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TT | data_center_power_cooling | 475.51 |  | 474.3874 | 0.2366 | 474.085 | 467.64 | 4.7949 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ASML | semiconductor_equipment | 1828.78 |  | 1825.7689 | 0.1649 | 1823.13 | 1796.26 | 2.1873 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | GEV | data_center_power_cooling | 1035.49 |  | 1033.007 | 0.2404 | 1035.07 | 1021.09 | 3.5732 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LIN | industrial_gases | 517.06 |  | 514.4398 | 0.5093 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TSM | foundry | 412.45 |  | 411.3868 | 0.2585 | 414.385 | 406.61 | 0.5867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 510.56 |  | 510.4358 | 0.0243 | 518.33 | 507.62 | 0.9068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.32 |  | 752.8161 | 0.1998 | 753.51 | 751.13 | 0.0305 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.165 |  | 296.6206 | 0.1835 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 399.15 |  | 395.8984 | 0.8213 | 398.69 | 392.2 | 0.1077 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.38 |  | 329.4871 | 0.5745 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 573.445 |  | 575.2906 | -0.3208 | 572.69 | 562.32 | 3.7353 | below_vwap | below_vwap,spread_too_wide |
| 6 | KLAC | semiconductor_equipment | 222.36 |  | 222.8189 | -0.2059 | 222.19 | 218.09 | 1.0973 | below_vwap | below_vwap,spread_too_wide |
| 7 | TT | data_center_power_cooling | 475.51 |  | 474.3874 | 0.2366 | 474.085 | 467.64 | 4.7949 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | JCI | data_center_power_cooling | 140.86 |  | 140.7096 | 0.1069 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | GEV | data_center_power_cooling | 1035.49 |  | 1033.007 | 0.2404 | 1035.07 | 1021.09 | 3.5732 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ASML | semiconductor_equipment | 1828.78 |  | 1825.7689 | 0.1649 | 1823.13 | 1796.26 | 2.1873 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | LIN | industrial_gases | 517.06 |  | 514.4398 | 0.5093 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | APD | industrial_gases | 296.63 |  | 294.4464 | 0.7416 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | QQQ | market_regime | 711.775 |  | 710.5277 | 0.1755 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| 14 | AVGO | custom_silicon_networking | 382.445 |  | 381.8662 | 0.1516 | 386.58 | 378.53 | 0.2876 | watch_only | none |
| 15 | NVDA | ai_accelerator | 207.68 |  | 207.6394 | 0.0195 | 211.03 | 207.49 | 0.1541 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 255.79 |  | 255.2313 | 0.2189 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 17 | META | cloud_ai_capex | 676.075 |  | 674.9665 | 0.1642 | 680.09 | 667.1 | 0.2736 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 72.555 |  | 72.2065 | 0.4827 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| 19 | SOXX | semiconductor_index | 536.92 |  | 537.6584 | -0.1373 | 543.4 | 535.47 | 0.0782 | below_vwap | below_vwap |
| 20 | VRT | data_center_power_cooling | 294.93 |  | 296.4139 | -0.5006 | 300.385 | 293.64 | 3.3906 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.775 |  | 710.5277 | 0.1755 | 713.55 | 708.25 | 0.0295 | watch_only | none |
| TQQQ | leveraged_tool | 72.555 |  | 72.2065 | 0.4827 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| NVDA | ai_accelerator | 207.68 |  | 207.6394 | 0.0195 | 211.03 | 207.49 | 0.1541 | watch_only | none |
| MSFT | cloud_ai_capex | 399.15 |  | 395.8984 | 0.8213 | 398.69 | 392.2 | 0.1077 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.38 |  | 329.4871 | 0.5745 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.19 |  | 372.0074 | -0.2197 | 375.18 | 369.2 | 0.0404 | below_vwap | below_vwap |
| AMD | ai_accelerator | 510.56 |  | 510.4358 | 0.0243 | 518.33 | 507.62 | 0.9068 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 412.45 |  | 411.3868 | 0.2585 | 414.385 | 406.61 | 0.5867 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 536.92 |  | 537.6584 | -0.1373 | 543.4 | 535.47 | 0.0782 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.15 |  | 575.6375 | -0.0847 | 580.31 | 572.21 | 0.0452 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.445 |  | 381.8662 | 0.1516 | 386.58 | 378.53 | 0.2876 | watch_only | none |
| MU | memory_hbm_storage | 863.56 |  | 864.6981 | -0.1316 | 887.1 | 866.765 | 0.1089 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 192.38 |  | 193.9119 | -0.79 | 201.61 | 194.19 | 0.2755 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 403.54 |  | 404.957 | -0.3499 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.025 |  | 46.3828 | -0.7713 | 47.65 | 46.165 | 0.0435 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.42 |  | 25.7366 | -1.2302 | 26.71 | 25.74 | 0.0393 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.32 |  | 752.8161 | 0.1998 | 753.51 | 751.13 | 0.0305 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.165 |  | 296.6206 | 0.1835 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.97 |  | 127.1226 | -0.12 | 131.36 | 126.665 | 2.4809 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.24 |  | 73.9116 | -0.9086 | 75.54 | 73.985 | 0.5598 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 294.93 |  | 296.4139 | -0.5006 | 300.385 | 293.64 | 3.3906 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.4 |  | 401.5522 | -1.2831 | 406.24 | 399.495 | 0.2952 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 633.9 |  | 633.236 | 0.1049 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1035.49 |  | 1033.007 | 0.2404 | 1035.07 | 1021.09 | 3.5732 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.51 |  | 474.3874 | 0.2366 | 474.085 | 467.64 | 4.7949 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.86 |  | 140.7096 | 0.1069 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.82 |  | 166.2791 | 0.9267 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 280.84 |  | 283.8743 | -1.0689 | 288.48 | 280.67 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 710.19 |  | 716.815 | -0.9242 | 737.175 | 720.21 | 1.8164 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.96 |  | 398.4556 | -0.6263 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.93 |  | 103.1738 | -1.2055 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 325.285 |  | 328.629 | -1.0176 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1828.78 |  | 1825.7689 | 0.1649 | 1823.13 | 1796.26 | 2.1873 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 573.445 |  | 575.2906 | -0.3208 | 572.69 | 562.32 | 3.7353 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 326.23 |  | 327.2672 | -0.3169 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.36 |  | 222.8189 | -0.2059 | 222.19 | 218.09 | 1.0973 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 330.11 |  | 329.0159 | 0.3325 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 292.19 |  | 290.5905 | 0.5504 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.71 |  | 64.6127 | 0.1505 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.64 |  | 52.6741 | -0.0647 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 136.67 |  | 135.9954 | 0.496 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 341.56 |  | 341.2828 | 0.0812 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 517.06 |  | 514.4398 | 0.5093 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.63 |  | 294.4464 | 0.7416 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.84 |  | 27.3619 | -1.9074 | 28.05 | 27.6 | 0.0745 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.68 |  | 36.0695 | -1.0799 | 37.365 | 36.4 | 0.028 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.32 |  | 21.5526 | -1.0792 | 22.18 | 21.78 | 0.1407 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1464.77 |  | 1489.8197 | -1.6814 | 1549.47 | 1482.06 | 3.7542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 474.99 |  | 482.7276 | -1.6029 | 498.04 | 480.14 | 2.3179 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 772.25 |  | 777.1468 | -0.6301 | 797.155 | 768.7 | 1.0049 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.79 |  | 255.2313 | 0.2189 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 676.075 |  | 674.9665 | 0.1642 | 680.09 | 667.1 | 0.2736 | watch_only | none |
| ARM | ai_accelerator | 257.46 |  | 258.6384 | -0.4556 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 162.83 |  | 163.7927 | -0.5878 | 168.11 | 162.41 | 3.6787 | below_vwap | below_vwap,spread_too_wide |
