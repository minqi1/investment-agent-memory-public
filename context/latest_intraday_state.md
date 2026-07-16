# Intraday State

- Generated at: `2026-07-16T23:52:36+08:00`
- Market time ET: `2026-07-16T11:52:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 6, 'manual_confirm_candidate': 5, 'below_opening_15m_low': 23, 'below_vwap': 15, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.9 |  | 710.5147 | 0.0542 | 713.55 | 708.25 | 0.0225 | watch_only | none |
| SOXX | semiconductor_index | 534.88 |  | 537.3808 | -0.4654 | 543.4 | 535.47 | 0.0654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 573.38 |  | 575.1969 | -0.3159 | 580.31 | 572.21 | 0.0855 | below_vwap | below_vwap |
| SPY | market_regime | 753.97 |  | 752.8577 | 0.1477 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1826.69 |  | 1825.594 | 0.06 | 1823.13 | 1796.26 | 0.0602 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.97 |  | 752.8577 | 0.1477 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.72 |  | 296.6203 | 0.0336 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 399.61 |  | 396.0785 | 0.8916 | 398.69 | 392.2 | 0.0776 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.02 |  | 329.582 | 0.7397 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1826.69 |  | 1825.594 | 0.06 | 1823.13 | 1796.26 | 0.0602 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.97 |  | 752.8577 | 0.1477 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.72 |  | 296.6203 | 0.0336 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 710.9 |  | 710.5147 | 0.0542 | 713.55 | 708.25 | 0.0225 | watch_only | none |
| 5 | NVDA | ai_accelerator | 207.735 |  | 207.6264 | 0.0523 | 211.03 | 207.49 | 0.0144 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 372.6 |  | 371.9913 | 0.1636 | 375.18 | 369.2 | 0.059 | watch_only | none |
| 7 | AVGO | custom_silicon_networking | 382.14 |  | 381.8557 | 0.0745 | 386.58 | 378.53 | 0.2041 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 332.02 |  | 329.582 | 0.7397 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 9 | MSFT | cloud_ai_capex | 399.61 |  | 396.0785 | 0.8916 | 398.69 | 392.2 | 0.0776 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 256.255 |  | 255.2602 | 0.3897 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| 11 | ONTO | semiconductor_test_packaging | 290.7 |  | 290.6078 | 0.0317 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TT | data_center_power_cooling | 475.235 |  | 474.4152 | 0.1728 | 474.085 | 467.64 | 4.764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | LIN | industrial_gases | 517.195 |  | 514.5953 | 0.5052 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ANET | ai_networking_optical | 167.19 |  | 166.293 | 0.5394 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APD | industrial_gases | 296.12 |  | 294.5254 | 0.5414 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | META | cloud_ai_capex | 677.11 |  | 675.0482 | 0.3054 | 680.09 | 667.1 | 0.7148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TSM | foundry | 410.355 |  | 411.3417 | -0.2399 | 414.385 | 406.61 | 0.0585 | below_vwap | below_vwap |
| 18 | JCI | data_center_power_cooling | 140.4 |  | 140.7017 | -0.2144 | 140.83 | 139.43 | 0.0926 | below_vwap | below_vwap |
| 19 | KLAC | semiconductor_equipment | 221.635 |  | 222.731 | -0.4921 | 222.19 | 218.09 | 0.1354 | below_vwap | below_vwap |
| 20 | SMH | semiconductor_index | 573.38 |  | 575.1969 | -0.3159 | 580.31 | 572.21 | 0.0855 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1826.69 |  | 1825.594 | 0.06 | 1823.13 | 1796.26 | 0.0602 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.97 |  | 752.8577 | 0.1477 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.72 |  | 296.6203 | 0.0336 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 399.61 |  | 396.0785 | 0.8916 | 398.69 | 392.2 | 0.0776 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.02 |  | 329.582 | 0.7397 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 475.235 |  | 474.4152 | 0.1728 | 474.085 | 467.64 | 4.764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 517.195 |  | 514.5953 | 0.5052 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 296.12 |  | 294.5254 | 0.5414 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | QQQ | market_regime | 710.9 |  | 710.5147 | 0.0542 | 713.55 | 708.25 | 0.0225 | watch_only | none |
| 10 | AVGO | custom_silicon_networking | 382.14 |  | 381.8557 | 0.0745 | 386.58 | 378.53 | 0.2041 | watch_only | none |
| 11 | NVDA | ai_accelerator | 207.735 |  | 207.6264 | 0.0523 | 211.03 | 207.49 | 0.0144 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 372.6 |  | 371.9913 | 0.1636 | 375.18 | 369.2 | 0.059 | watch_only | none |
| 13 | AMZN | cloud_ai_capex | 256.255 |  | 255.2602 | 0.3897 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| 14 | TQQQ | leveraged_tool | 72.265 |  | 72.199 | 0.0914 | 73.09 | 71.45 | 0.0277 | watch_only | none |
| 15 | TSM | foundry | 410.355 |  | 411.3417 | -0.2399 | 414.385 | 406.61 | 0.0585 | below_vwap | below_vwap |
| 16 | JCI | data_center_power_cooling | 140.4 |  | 140.7017 | -0.2144 | 140.83 | 139.43 | 0.0926 | below_vwap | below_vwap |
| 17 | PWR | data_center_power_cooling | 632.34 |  | 633.1651 | -0.1303 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | GEV | data_center_power_cooling | 1030.795 |  | 1032.5934 | -0.1742 | 1035.07 | 1021.09 | 3.8475 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMAT | semiconductor_equipment | 572.23 |  | 574.8724 | -0.4597 | 572.69 | 562.32 | 3.565 | below_vwap | below_vwap,spread_too_wide |
| 20 | KLAC | semiconductor_equipment | 221.635 |  | 222.731 | -0.4921 | 222.19 | 218.09 | 0.1354 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.9 |  | 710.5147 | 0.0542 | 713.55 | 708.25 | 0.0225 | watch_only | none |
| TQQQ | leveraged_tool | 72.265 |  | 72.199 | 0.0914 | 73.09 | 71.45 | 0.0277 | watch_only | none |
| NVDA | ai_accelerator | 207.735 |  | 207.6264 | 0.0523 | 211.03 | 207.49 | 0.0144 | watch_only | none |
| MSFT | cloud_ai_capex | 399.61 |  | 396.0785 | 0.8916 | 398.69 | 392.2 | 0.0776 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.02 |  | 329.582 | 0.7397 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.6 |  | 371.9913 | 0.1636 | 375.18 | 369.2 | 0.059 | watch_only | none |
| AMD | ai_accelerator | 507.55 |  | 510.2643 | -0.5319 | 518.33 | 507.62 | 1.1408 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 410.355 |  | 411.3417 | -0.2399 | 414.385 | 406.61 | 0.0585 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.88 |  | 537.3808 | -0.4654 | 543.4 | 535.47 | 0.0654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 573.38 |  | 575.1969 | -0.3159 | 580.31 | 572.21 | 0.0855 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.14 |  | 381.8557 | 0.0745 | 386.58 | 378.53 | 0.2041 | watch_only | none |
| MU | memory_hbm_storage | 852.635 |  | 863.8839 | -1.3021 | 887.1 | 866.765 | 1.5833 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 190.88 |  | 193.7012 | -1.4565 | 201.61 | 194.19 | 0.943 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.18 |  | 404.7021 | -0.8703 | 411.65 | 400.635 | 4.7634 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.53 |  | 46.2337 | -1.5221 | 47.65 | 46.165 | 0.0439 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.215 |  | 25.6836 | -1.8244 | 26.71 | 25.74 | 0.0397 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.97 |  | 752.8577 | 0.1477 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.72 |  | 296.6203 | 0.0336 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.09 |  | 127.0559 | -0.7602 | 131.36 | 126.665 | 3.2913 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.94 |  | 73.8402 | -1.2191 | 75.54 | 73.985 | 0.1234 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 293.22 |  | 296.2646 | -1.0277 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.83 |  | 401.4137 | -1.391 | 406.24 | 399.495 | 4.3352 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 632.34 |  | 633.1651 | -0.1303 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.795 |  | 1032.5934 | -0.1742 | 1035.07 | 1021.09 | 3.8475 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.235 |  | 474.4152 | 0.1728 | 474.085 | 467.64 | 4.764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.4 |  | 140.7017 | -0.2144 | 140.83 | 139.43 | 0.0926 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 167.19 |  | 166.293 | 0.5394 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.8 |  | 283.7265 | -1.7364 | 288.48 | 280.67 | 2.2812 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.82 |  | 715.6135 | -1.9275 | 737.175 | 720.21 | 2.4194 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 393.69 |  | 398.0593 | -1.0976 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.01 |  | 103.0852 | -2.0131 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.855 |  | 327.3994 | -2.3043 | 337.59 | 326.16 | 0.3783 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1826.69 |  | 1825.594 | 0.06 | 1823.13 | 1796.26 | 0.0602 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 572.23 |  | 574.8724 | -0.4597 | 572.69 | 562.32 | 3.565 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 324.95 |  | 327.1026 | -0.6581 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 221.635 |  | 222.731 | -0.4921 | 222.19 | 218.09 | 0.1354 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 327.44 |  | 328.9469 | -0.4581 | 332.49 | 326.685 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.7 |  | 290.6078 | 0.0317 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.4 |  | 64.5903 | -0.2946 | 66.19 | 63.93 | 4.5963 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 52.25 |  | 52.6601 | -0.7788 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.48 |  | 135.9704 | -0.3607 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.84 |  | 341.1381 | -0.3805 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.195 |  | 514.5953 | 0.5052 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.12 |  | 294.5254 | 0.5414 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.67 |  | 27.3154 | -2.3629 | 28.05 | 27.6 | 0.1125 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.215 |  | 35.9899 | -2.1531 | 37.365 | 36.4 | 0.0568 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.09 |  | 21.5341 | -2.0623 | 22.18 | 21.78 | 0.0474 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1444.16 |  | 1486.6209 | -2.8562 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 467.28 |  | 481.9672 | -3.0474 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 760.34 |  | 776.0713 | -2.027 | 797.155 | 768.7 | 4.69 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.255 |  | 255.2602 | 0.3897 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| META | cloud_ai_capex | 677.11 |  | 675.0482 | 0.3054 | 680.09 | 667.1 | 0.7148 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 257.22 |  | 258.5002 | -0.4952 | 265.96 | 258.1 | 3.8877 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 161.36 |  | 163.6545 | -1.4021 | 168.11 | 162.41 | 1.1775 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
