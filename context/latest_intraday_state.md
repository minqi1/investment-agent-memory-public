# Intraday State

- Generated at: `2026-07-17T00:40:12+08:00`
- Market time ET: `2026-07-16T12:40:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 35, 'manual_confirm_candidate': 2, 'below_vwap': 15, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.815 |  | 710.1252 | -0.3253 | 713.55 | 708.25 | 0.0367 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 530.7 |  | 536.3962 | -1.0619 | 543.4 | 535.47 | 0.0565 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.38 |  | 574.5186 | -0.8944 | 580.31 | 572.21 | 0.079 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.925 |  | 752.7834 | -0.114 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.215 |  | 396.8796 | 1.0924 | 398.69 | 392.2 | 0.0698 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.25 |  | 329.9157 | 0.1013 | 328.98 | 326.885 | 0.0908 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.25 |  | 329.9157 | 0.1013 | 328.98 | 326.885 | 0.0908 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.46 |  | 255.3987 | 0.024 | 258.07 | 252.62 | 0.0431 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 401.215 |  | 396.8796 | 1.0924 | 398.69 | 392.2 | 0.0698 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 516 |  | 514.7922 | 0.2346 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 296.66 |  | 294.7465 | 0.6492 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | TT | data_center_power_cooling | 472.41 |  | 474.0713 | -0.3504 | 474.085 | 467.64 | 0.0974 | below_vwap | below_vwap |
| 7 | ASML | semiconductor_equipment | 1809.58 |  | 1823.4046 | -0.7582 | 1823.13 | 1796.26 | 0.1006 | below_vwap | below_vwap |
| 8 | AMAT | semiconductor_equipment | 565.95 |  | 573.6476 | -1.3419 | 572.69 | 562.32 | 0.1467 | below_vwap | below_vwap |
| 9 | KLAC | semiconductor_equipment | 218.76 |  | 221.8989 | -1.4146 | 222.19 | 218.09 | 0.1417 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 751.925 |  | 752.7834 | -0.114 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 296.08 |  | 296.4596 | -0.128 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | GOOGL | cloud_ai_capex | 371.46 |  | 371.8894 | -0.1155 | 375.18 | 369.2 | 0.1346 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | TSM | foundry | 406.77 |  | 410.6184 | -0.9372 | 414.385 | 406.61 | 0.2827 | below_vwap | below_vwap |
| 15 | ANET | ai_networking_optical | 166.05 |  | 166.3218 | -0.1634 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 139.925 |  | 140.5502 | -0.4448 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | META | cloud_ai_capex | 669.875 |  | 673.8624 | -0.5917 | 680.09 | 667.1 | 0.2523 | below_vwap | below_vwap |
| 18 | ENTG | semiconductor_materials | 134.55 |  | 135.2745 | -0.5356 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 380.51 |  | 381.6556 | -0.3002 | 386.58 | 378.53 | 0.6833 | below_vwap | below_vwap,spread_too_wide |
| 20 | GEV | data_center_power_cooling | 1021.13 |  | 1030.3055 | -0.8906 | 1035.07 | 1021.09 | 4.5959 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.215 |  | 396.8796 | 1.0924 | 398.69 | 392.2 | 0.0698 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 330.25 |  | 329.9157 | 0.1013 | 328.98 | 326.885 | 0.0908 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 516 |  | 514.7922 | 0.2346 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.66 |  | 294.7465 | 0.6492 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | AMZN | cloud_ai_capex | 255.46 |  | 255.3987 | 0.024 | 258.07 | 252.62 | 0.0431 | watch_only | none |
| 6 | ANET | ai_networking_optical | 166.05 |  | 166.3218 | -0.1634 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| 7 | TSM | foundry | 406.77 |  | 410.6184 | -0.9372 | 414.385 | 406.61 | 0.2827 | below_vwap | below_vwap |
| 8 | AVGO | custom_silicon_networking | 380.51 |  | 381.6556 | -0.3002 | 386.58 | 378.53 | 0.6833 | below_vwap | below_vwap,spread_too_wide |
| 9 | TT | data_center_power_cooling | 472.41 |  | 474.0713 | -0.3504 | 474.085 | 467.64 | 0.0974 | below_vwap | below_vwap |
| 10 | JCI | data_center_power_cooling | 139.925 |  | 140.5502 | -0.4448 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GEV | data_center_power_cooling | 1021.13 |  | 1030.3055 | -0.8906 | 1035.07 | 1021.09 | 4.5959 | below_vwap | below_vwap,spread_too_wide |
| 12 | ASML | semiconductor_equipment | 1809.58 |  | 1823.4046 | -0.7582 | 1823.13 | 1796.26 | 0.1006 | below_vwap | below_vwap |
| 13 | AMAT | semiconductor_equipment | 565.95 |  | 573.6476 | -1.3419 | 572.69 | 562.32 | 0.1467 | below_vwap | below_vwap |
| 14 | KLAC | semiconductor_equipment | 218.76 |  | 221.8989 | -1.4146 | 222.19 | 218.09 | 0.1417 | below_vwap | below_vwap |
| 15 | SPY | market_regime | 751.925 |  | 752.7834 | -0.114 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 16 | IWM | market_regime | 296.08 |  | 296.4596 | -0.128 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ENTG | semiconductor_materials | 134.55 |  | 135.2745 | -0.5356 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 371.46 |  | 371.8894 | -0.1155 | 375.18 | 369.2 | 0.1346 | below_vwap | below_vwap |
| 20 | META | cloud_ai_capex | 669.875 |  | 673.8624 | -0.5917 | 680.09 | 667.1 | 0.2523 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.815 |  | 710.1252 | -0.3253 | 713.55 | 708.25 | 0.0367 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.3 |  | 72.0781 | -1.0795 | 73.09 | 71.45 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.19 |  | 207.5521 | -0.1745 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.215 |  | 396.8796 | 1.0924 | 398.69 | 392.2 | 0.0698 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.25 |  | 329.9157 | 0.1013 | 328.98 | 326.885 | 0.0908 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.46 |  | 371.8894 | -0.1155 | 375.18 | 369.2 | 0.1346 | below_vwap | below_vwap |
| AMD | ai_accelerator | 500.705 |  | 508.01 | -1.438 | 518.33 | 507.62 | 0.0919 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 406.77 |  | 410.6184 | -0.9372 | 414.385 | 406.61 | 0.2827 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.7 |  | 536.3962 | -1.0619 | 543.4 | 535.47 | 0.0565 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.38 |  | 574.5186 | -0.8944 | 580.31 | 572.21 | 0.079 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.51 |  | 381.6556 | -0.3002 | 386.58 | 378.53 | 0.6833 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 852.29 |  | 861.6264 | -1.0836 | 887.1 | 866.765 | 0.2616 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.55 |  | 192.5263 | -2.0653 | 201.61 | 194.19 | 0.122 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 399.26 |  | 403.6852 | -1.0962 | 411.65 | 400.635 | 1.1672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.225 |  | 46.0868 | -1.8699 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.05 |  | 25.5387 | -1.9137 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 751.925 |  | 752.7834 | -0.114 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 296.08 |  | 296.4596 | -0.128 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.605 |  | 126.776 | -0.1349 | 131.36 | 126.665 | 2.7645 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.74 |  | 73.5359 | -1.0824 | 75.54 | 73.985 | 1.9797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.865 |  | 295.1456 | -1.7892 | 300.385 | 293.64 | 1.7801 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 391.37 |  | 400.3814 | -2.2507 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.35 |  | 632.543 | -0.821 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1021.13 |  | 1030.3055 | -0.8906 | 1035.07 | 1021.09 | 4.5959 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 472.41 |  | 474.0713 | -0.3504 | 474.085 | 467.64 | 0.0974 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 139.925 |  | 140.5502 | -0.4448 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.05 |  | 166.3218 | -0.1634 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 277.48 |  | 282.4776 | -1.7692 | 288.48 | 280.67 | 0.4325 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.83 |  | 712.4932 | -1.6369 | 737.175 | 720.21 | 2.5341 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 391.6 |  | 396.8044 | -1.3116 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.36 |  | 102.3969 | -2.9659 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.07 |  | 325.1314 | -2.1718 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1809.58 |  | 1823.4046 | -0.7582 | 1823.13 | 1796.26 | 0.1006 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.95 |  | 573.6476 | -1.3419 | 572.69 | 562.32 | 0.1467 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 320.58 |  | 325.5056 | -1.5132 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.76 |  | 221.8989 | -1.4146 | 222.19 | 218.09 | 0.1417 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.335 |  | 327.8886 | -1.6938 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.82 |  | 289.7452 | -1.6998 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.98 |  | 64.4277 | -2.247 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.685 |  | 52.3066 | -1.1884 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.55 |  | 135.2745 | -0.5356 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.07 |  | 339.0714 | -1.1801 | 346.26 | 338 | 3.9246 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516 |  | 514.7922 | 0.2346 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.66 |  | 294.7465 | 0.6492 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.275 |  | 27.1185 | -3.1106 | 28.05 | 27.6 | 0.0761 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.86 |  | 35.7736 | -2.5537 | 37.365 | 36.4 | 0.0574 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.855 |  | 21.4259 | -2.6646 | 22.18 | 21.78 | 0.048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1433.47 |  | 1478.1448 | -3.0224 | 1549.47 | 1482.06 | 3.488 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 458.69 |  | 478.6423 | -4.1685 | 498.04 | 480.14 | 0.2834 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 753.01 |  | 769.593 | -2.1548 | 797.155 | 768.7 | 3.9256 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.46 |  | 255.3987 | 0.024 | 258.07 | 252.62 | 0.0431 | watch_only | none |
| META | cloud_ai_capex | 669.875 |  | 673.8624 | -0.5917 | 680.09 | 667.1 | 0.2523 | below_vwap | below_vwap |
| ARM | ai_accelerator | 254.005 |  | 257.9019 | -1.511 | 265.96 | 258.1 | 3.9369 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 160.42 |  | 163.4196 | -1.8355 | 168.11 | 162.41 | 2.7989 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
