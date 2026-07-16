# Intraday State

- Generated at: `2026-07-17T01:15:54+08:00`
- Market time ET: `2026-07-16T13:15:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 36, 'manual_confirm_candidate': 2, 'below_vwap': 11, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.675 |  | 709.8969 | -0.313 | 713.55 | 708.25 | 0.0268 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.79 |  | 535.9881 | -1.1564 | 543.4 | 535.47 | 0.068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.41 |  | 573.5102 | -0.8893 | 580.31 | 572.21 | 0.0669 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.17 |  | 752.7366 | -0.0753 | 753.51 | 751.13 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.46 |  | 397.812 | 0.917 | 398.69 | 392.2 | 0.2939 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.775 |  | 330.0875 | 0.5112 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 256.17 |  | 255.4735 | 0.2726 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 331.775 |  | 330.0875 | 0.5112 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.9 |  | 140.5349 | 0.2598 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 515.94 |  | 514.9185 | 0.1984 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 401.46 |  | 397.812 | 0.917 | 398.69 | 392.2 | 0.2939 | buy_precheck_manual_confirm | none |
| 6 | APD | industrial_gases | 295.79 |  | 294.8505 | 0.3186 | 293.89 | 291.35 | 4.1922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 167.595 |  | 166.4256 | 0.7027 | 169.91 | 165.6 | 4.3199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | TT | data_center_power_cooling | 476.205 |  | 474.1917 | 0.4246 | 474.085 | 467.64 | 4.5443 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1801.64 |  | 1822.0677 | -1.1211 | 1823.13 | 1796.26 | 0.0466 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 752.17 |  | 752.7366 | -0.0753 | 753.51 | 751.13 | 0.0027 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.76 |  | 296.3908 | -0.2128 | 296.28 | 294.65 | 0.0101 | below_vwap | below_vwap |
| 12 | GOOGL | cloud_ai_capex | 371.045 |  | 371.8658 | -0.2207 | 375.18 | 369.2 | 0.0162 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | AMAT | semiconductor_equipment | 565.76 |  | 572.7528 | -1.2209 | 572.69 | 562.32 | 0.1538 | below_vwap | below_vwap |
| 15 | KLAC | semiconductor_equipment | 219.27 |  | 221.5519 | -1.03 | 222.19 | 218.09 | 0.187 | below_vwap | below_vwap |
| 16 | META | cloud_ai_capex | 668.735 |  | 673.0774 | -0.6452 | 680.09 | 667.1 | 0.2587 | below_vwap | below_vwap |
| 17 | ENTG | semiconductor_materials | 134.3 |  | 135.1418 | -0.6229 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | GEV | data_center_power_cooling | 1026.075 |  | 1029.1587 | -0.2996 | 1035.07 | 1021.09 | 4.1206 | below_vwap | below_vwap,spread_too_wide |
| 19 | DELL | ai_server_oem | 400.805 |  | 403.3018 | -0.6191 | 411.65 | 400.635 | 4.1841 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 529.79 |  | 535.9881 | -1.1564 | 543.4 | 535.47 | 0.068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.46 |  | 397.812 | 0.917 | 398.69 | 392.2 | 0.2939 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.775 |  | 330.0875 | 0.5112 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 476.205 |  | 474.1917 | 0.4246 | 474.085 | 467.64 | 4.5443 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | JCI | data_center_power_cooling | 140.9 |  | 140.5349 | 0.2598 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 515.94 |  | 514.9185 | 0.1984 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 295.79 |  | 294.8505 | 0.3186 | 293.89 | 291.35 | 4.1922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AMZN | cloud_ai_capex | 256.17 |  | 255.4735 | 0.2726 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| 8 | GEV | data_center_power_cooling | 1026.075 |  | 1029.1587 | -0.2996 | 1035.07 | 1021.09 | 4.1206 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1801.64 |  | 1822.0677 | -1.1211 | 1823.13 | 1796.26 | 0.0466 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 565.76 |  | 572.7528 | -1.2209 | 572.69 | 562.32 | 0.1538 | below_vwap | below_vwap |
| 11 | KLAC | semiconductor_equipment | 219.27 |  | 221.5519 | -1.03 | 222.19 | 218.09 | 0.187 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 752.17 |  | 752.7366 | -0.0753 | 753.51 | 751.13 | 0.0027 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 295.76 |  | 296.3908 | -0.2128 | 296.28 | 294.65 | 0.0101 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | DELL | ai_server_oem | 400.805 |  | 403.3018 | -0.6191 | 411.65 | 400.635 | 4.1841 | below_vwap | below_vwap,spread_too_wide |
| 16 | ENTG | semiconductor_materials | 134.3 |  | 135.1418 | -0.6229 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 371.045 |  | 371.8658 | -0.2207 | 375.18 | 369.2 | 0.0162 | below_vwap | below_vwap |
| 18 | META | cloud_ai_capex | 668.735 |  | 673.0774 | -0.6452 | 680.09 | 667.1 | 0.2587 | below_vwap | below_vwap |
| 19 | ANET | ai_networking_optical | 167.595 |  | 166.4256 | 0.7027 | 169.91 | 165.6 | 4.3199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SOXX | semiconductor_index | 529.79 |  | 535.9881 | -1.1564 | 543.4 | 535.47 | 0.068 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.675 |  | 709.8969 | -0.313 | 713.55 | 708.25 | 0.0268 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.25 |  | 72.0221 | -1.072 | 73.09 | 71.45 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.085 |  | 207.5054 | -0.2026 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.46 |  | 397.812 | 0.917 | 398.69 | 392.2 | 0.2939 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.775 |  | 330.0875 | 0.5112 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.045 |  | 371.8658 | -0.2207 | 375.18 | 369.2 | 0.0162 | below_vwap | below_vwap |
| AMD | ai_accelerator | 498.48 |  | 506.9433 | -1.6695 | 518.33 | 507.62 | 0.6339 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.9 |  | 410.1534 | -1.037 | 414.385 | 406.61 | 0.2538 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.79 |  | 535.9881 | -1.1564 | 543.4 | 535.47 | 0.068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.41 |  | 573.5102 | -0.8893 | 580.31 | 572.21 | 0.0669 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.61 |  | 381.0934 | -0.9141 | 386.58 | 378.53 | 1.5889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.43 |  | 859.8772 | -1.3313 | 887.1 | 866.765 | 0.343 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.035 |  | 192.208 | -2.1711 | 201.61 | 194.19 | 0.6541 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.805 |  | 403.3018 | -0.6191 | 411.65 | 400.635 | 4.1841 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.32 |  | 46.0007 | -1.4797 | 47.65 | 46.165 | 0.0441 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.005 |  | 25.477 | -1.8528 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.17 |  | 752.7366 | -0.0753 | 753.51 | 751.13 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 295.76 |  | 296.3908 | -0.2128 | 296.28 | 294.65 | 0.0101 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.47 |  | 126.7549 | -0.2248 | 131.36 | 126.665 | 0.4349 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.875 |  | 73.5075 | -0.8605 | 75.54 | 73.985 | 0.6998 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 292.5 |  | 294.7378 | -0.7593 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 397.05 |  | 399.9704 | -0.7302 | 406.24 | 399.495 | 5.0069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 629.53 |  | 632.0739 | -0.4025 | 640.25 | 631.005 | 0.3622 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1026.075 |  | 1029.1587 | -0.2996 | 1035.07 | 1021.09 | 4.1206 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 476.205 |  | 474.1917 | 0.4246 | 474.085 | 467.64 | 4.5443 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.9 |  | 140.5349 | 0.2598 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.595 |  | 166.4256 | 0.7027 | 169.91 | 165.6 | 4.3199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.61 |  | 281.9019 | -1.5225 | 288.48 | 280.67 | 4.8773 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.545 |  | 710.9065 | -1.7388 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 392.38 |  | 396.2442 | -0.9752 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.14 |  | 102.0564 | -2.8577 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.73 |  | 324.3825 | -2.3591 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1801.64 |  | 1822.0677 | -1.1211 | 1823.13 | 1796.26 | 0.0466 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.76 |  | 572.7528 | -1.2209 | 572.69 | 562.32 | 0.1538 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.97 |  | 324.905 | -1.5189 | 328.96 | 324.11 | 4.1723 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 219.27 |  | 221.5519 | -1.03 | 222.19 | 218.09 | 0.187 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 324.91 |  | 327.5027 | -0.7917 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.82 |  | 289.1959 | -1.5131 | 295.83 | 285.02 | 0.474 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 63.02 |  | 64.3259 | -2.0301 | 66.19 | 63.93 | 4.7604 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.415 |  | 52.2393 | -1.578 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.3 |  | 135.1418 | -0.6229 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 334.66 |  | 338.6205 | -1.1696 | 346.26 | 338 | 3.765 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.94 |  | 514.9185 | 0.1984 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.79 |  | 294.8505 | 0.3186 | 293.89 | 291.35 | 4.1922 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.19 |  | 27.0132 | -3.0473 | 28.05 | 27.6 | 0.0764 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.81 |  | 35.7003 | -2.4939 | 37.365 | 36.4 | 0.0575 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.89 |  | 21.3323 | -2.0733 | 22.18 | 21.78 | 0.0957 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1436.85 |  | 1474.3266 | -2.5419 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 459.55 |  | 477.0604 | -3.6705 | 498.04 | 480.14 | 2.5286 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 751.59 |  | 768.9281 | -2.2548 | 797.155 | 768.7 | 0.5375 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.17 |  | 255.4735 | 0.2726 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| META | cloud_ai_capex | 668.735 |  | 673.0774 | -0.6452 | 680.09 | 667.1 | 0.2587 | below_vwap | below_vwap |
| ARM | ai_accelerator | 256.03 |  | 257.4579 | -0.5546 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 158.02 |  | 163.1173 | -3.1249 | 168.11 | 162.41 | 1.8985 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
