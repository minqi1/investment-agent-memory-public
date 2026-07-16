# Intraday State

- Generated at: `2026-07-17T03:15:25+08:00`
- Market time ET: `2026-07-16T15:15:26-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 43, 'manual_confirm_candidate': 2, 'below_vwap': 4, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.05 |  | 709.126 | -0.5748 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.15 |  | 533.5929 | -1.0201 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.75 |  | 571.5403 | -0.8381 | 580.31 | 572.21 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.73 |  | 752.1476 | -0.3214 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.55 |  | 399.9666 | 0.6459 | 398.69 | 392.2 | 0.0298 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.2 |  | 331.0959 | 0.9375 | 328.98 | 326.885 | 0.0329 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 140.765 |  | 140.5557 | 0.1489 | 140.83 | 139.43 | 0.1066 | watch_only | none |
| 2 | MSFT | cloud_ai_capex | 402.55 |  | 399.9666 | 0.6459 | 398.69 | 392.2 | 0.0298 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.08 |  | 474.1437 | 0.1975 | 474.085 | 467.64 | 4.9718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | AAPL | mega_cap_platform | 334.2 |  | 331.0959 | 0.9375 | 328.98 | 326.885 | 0.0329 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 167.17 |  | 166.5907 | 0.3477 | 169.91 | 165.6 | 4.5523 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GEV | data_center_power_cooling | 1027.73 |  | 1027.1049 | 0.0609 | 1035.07 | 1021.09 | 3.9106 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 518.73 |  | 515.3542 | 0.6551 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 296.225 |  | 295.0203 | 0.4084 | 293.89 | 291.35 | 3.7978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | KLAC | semiconductor_equipment | 219.51 |  | 220.8921 | -0.6257 | 222.19 | 218.09 | 0.0774 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 294.86 |  | 296.0387 | -0.3982 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | TSM | foundry | 407.28 |  | 408.6867 | -0.3442 | 414.385 | 406.61 | 0.7071 | below_vwap | below_vwap,spread_too_wide |
| 13 | SOXX | semiconductor_index | 528.15 |  | 533.5929 | -1.0201 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | QQQ | market_regime | 705.05 |  | 709.126 | -0.5748 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | MU | memory_hbm_storage | 846.54 |  | 856.3304 | -1.1433 | 887.1 | 866.765 | 0.0508 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | NVDA | ai_accelerator | 206.81 |  | 207.3439 | -0.2575 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | ASML | semiconductor_equipment | 1791.81 |  | 1816.5242 | -1.3605 | 1823.13 | 1796.26 | 0.0742 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | SMH | semiconductor_index | 566.75 |  | 571.5403 | -0.8381 | 580.31 | 572.21 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SPY | market_regime | 749.73 |  | 752.1476 | -0.3214 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | HPE | ai_server_oem | 45.31 |  | 45.7515 | -0.9649 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 402.55 |  | 399.9666 | 0.6459 | 398.69 | 392.2 | 0.0298 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 334.2 |  | 331.0959 | 0.9375 | 328.98 | 326.885 | 0.0329 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.08 |  | 474.1437 | 0.1975 | 474.085 | 467.64 | 4.9718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 518.73 |  | 515.3542 | 0.6551 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 296.225 |  | 295.0203 | 0.4084 | 293.89 | 291.35 | 3.7978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | JCI | data_center_power_cooling | 140.765 |  | 140.5557 | 0.1489 | 140.83 | 139.43 | 0.1066 | watch_only | none |
| 7 | TSM | foundry | 407.28 |  | 408.6867 | -0.3442 | 414.385 | 406.61 | 0.7071 | below_vwap | below_vwap,spread_too_wide |
| 8 | KLAC | semiconductor_equipment | 219.51 |  | 220.8921 | -0.6257 | 222.19 | 218.09 | 0.0774 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 294.86 |  | 296.0387 | -0.3982 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ANET | ai_networking_optical | 167.17 |  | 166.5907 | 0.3477 | 169.91 | 165.6 | 4.5523 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | GEV | data_center_power_cooling | 1027.73 |  | 1027.1049 | 0.0609 | 1035.07 | 1021.09 | 3.9106 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | SOXX | semiconductor_index | 528.15 |  | 533.5929 | -1.0201 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | CIEN | ai_networking_optical | 388.82 |  | 393.8809 | -1.2849 | 410 | 397.68 | 0.2623 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 705.05 |  | 709.126 | -0.5748 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | AVGO | custom_silicon_networking | 375.89 |  | 379.5812 | -0.9724 | 386.58 | 378.53 | 0.2208 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | MU | memory_hbm_storage | 846.54 |  | 856.3304 | -1.1433 | 887.1 | 866.765 | 0.0508 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | VRT | data_center_power_cooling | 289.99 |  | 293.1659 | -1.0833 | 300.385 | 293.64 | 1.838 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 19 | NVDA | ai_accelerator | 206.81 |  | 207.3439 | -0.2575 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AMD | ai_accelerator | 496.46 |  | 503.3534 | -1.3695 | 518.33 | 507.62 | 1.0454 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.05 |  | 709.126 | -0.5748 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.465 |  | 71.7484 | -1.7888 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.81 |  | 207.3439 | -0.2575 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.55 |  | 399.9666 | 0.6459 | 398.69 | 392.2 | 0.0298 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 334.2 |  | 331.0959 | 0.9375 | 328.98 | 326.885 | 0.0329 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 354.16 |  | 366.892 | -3.4702 | 375.18 | 369.2 | 0.0367 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 496.46 |  | 503.3534 | -1.3695 | 518.33 | 507.62 | 1.0454 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 407.28 |  | 408.6867 | -0.3442 | 414.385 | 406.61 | 0.7071 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.15 |  | 533.5929 | -1.0201 | 543.4 | 535.47 | 0.0587 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 566.75 |  | 571.5403 | -0.8381 | 580.31 | 572.21 | 0.06 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.89 |  | 379.5812 | -0.9724 | 386.58 | 378.53 | 0.2208 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 846.54 |  | 856.3304 | -1.1433 | 887.1 | 866.765 | 0.0508 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.3 |  | 190.7515 | -1.8094 | 201.61 | 194.19 | 0.1548 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 395.05 |  | 401.7695 | -1.6725 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.31 |  | 45.7515 | -0.9649 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25 |  | 25.3011 | -1.1901 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.73 |  | 752.1476 | -0.3214 | 753.51 | 751.13 | 0.0027 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.86 |  | 296.0387 | -0.3982 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.09 |  | 126.5397 | -1.1457 | 131.36 | 126.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 73.285 |  | 73.2954 | -0.0142 | 75.54 | 73.985 | 4.3802 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.99 |  | 293.1659 | -1.0833 | 300.385 | 293.64 | 1.838 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.795 |  | 399.2039 | -0.6034 | 406.24 | 399.495 | 5.0631 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 628.69 |  | 631.1523 | -0.3901 | 640.25 | 631.005 | 4.8355 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1027.73 |  | 1027.1049 | 0.0609 | 1035.07 | 1021.09 | 3.9106 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.08 |  | 474.1437 | 0.1975 | 474.085 | 467.64 | 4.9718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.765 |  | 140.5557 | 0.1489 | 140.83 | 139.43 | 0.1066 | watch_only | none |
| ANET | ai_networking_optical | 167.17 |  | 166.5907 | 0.3477 | 169.91 | 165.6 | 4.5523 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 275.49 |  | 280.5714 | -1.8111 | 288.48 | 280.67 | 1.1906 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.32 |  | 707.5549 | -1.3052 | 737.175 | 720.21 | 3.1003 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 388.82 |  | 393.8809 | -1.2849 | 410 | 397.68 | 0.2623 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.3 |  | 101.1778 | -1.8559 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.775 |  | 323.1268 | -1.6563 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1791.81 |  | 1816.5242 | -1.3605 | 1823.13 | 1796.26 | 0.0742 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 560.86 |  | 569.5185 | -1.5203 | 572.69 | 562.32 | 0.7881 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.73 |  | 322.6839 | -1.5352 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.51 |  | 220.8921 | -0.6257 | 222.19 | 218.09 | 0.0774 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.82 |  | 326.4845 | -1.4287 | 332.49 | 326.685 | 3.011 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.07 |  | 286.1919 | -2.1391 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.87 |  | 63.8495 | -1.534 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.05 |  | 51.7568 | -1.3656 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.68 |  | 134.756 | -0.7985 | 138.07 | 133.73 | 4.7277 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 328.41 |  | 334.0074 | -1.6758 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.73 |  | 515.3542 | 0.6551 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.225 |  | 295.0203 | 0.4084 | 293.89 | 291.35 | 3.7978 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.355 |  | 26.7689 | -1.546 | 28.05 | 27.6 | 0.0759 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.48 |  | 35.5019 | -0.0618 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.065 |  | 21.2 | -0.6369 | 22.18 | 21.78 | 0.0949 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1399.86 |  | 1457.4963 | -3.9545 | 1549.47 | 1482.06 | 4.6433 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 461.46 |  | 472.678 | -2.3733 | 498.04 | 480.14 | 0.0975 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 743.76 |  | 762.9769 | -2.5187 | 797.155 | 768.7 | 0.2393 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 252.17 |  | 254.9527 | -1.0915 | 258.07 | 252.62 | 0.0159 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 664.71 |  | 671.0135 | -0.9394 | 680.09 | 667.1 | 0.8003 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 256.32 |  | 257.268 | -0.3685 | 265.96 | 258.1 | 2.532 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.545 |  | 161.4159 | -3.6371 | 168.11 | 162.41 | 0.1157 | below_opening_15m_low | below_opening_15m_low,below_vwap |
