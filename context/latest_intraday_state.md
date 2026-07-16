# Intraday State

- Generated at: `2026-07-17T00:59:59+08:00`
- Market time ET: `2026-07-16T13:00:00-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 15, 'below_opening_15m_low': 29, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 2, 'watch_only': 3, 'spread_too_wide_or_missing': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.8 |  | 709.9899 | -0.1676 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 531.55 |  | 536.1011 | -0.8489 | 543.4 | 535.47 | 0.0715 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 570.21 |  | 574.0088 | -0.6618 | 580.31 | 572.21 | 0.0351 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.815 |  | 752.7471 | 0.009 | 753.51 | 751.13 | 0.0013 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.83 |  | 514.8897 | 0.1826 | 515.825 | 512.23 | 0.2074 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.195 |  | 294.8023 | 0.4724 | 293.89 | 291.35 | 0.1452 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 403.15 |  | 397.5066 | 1.4197 | 398.69 | 392.2 | 0.0719 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.75 |  | 329.9989 | 0.5306 | 328.98 | 326.885 | 0.0482 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.83 |  | 514.8897 | 0.1826 | 515.825 | 512.23 | 0.2074 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.195 |  | 294.8023 | 0.4724 | 293.89 | 291.35 | 0.1452 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 752.815 |  | 752.7471 | 0.009 | 753.51 | 751.13 | 0.0013 | watch_only | none |
| 4 | ORCL | cloud_ai_capex | 126.91 |  | 126.7625 | 0.1163 | 131.36 | 126.665 | 0.0552 | watch_only | none |
| 5 | AMZN | cloud_ai_capex | 255.755 |  | 255.4415 | 0.1227 | 258.07 | 252.62 | 0.0235 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 331.75 |  | 329.9989 | 0.5306 | 328.98 | 326.885 | 0.0482 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 403.15 |  | 397.5066 | 1.4197 | 398.69 | 392.2 | 0.0719 | buy_precheck_manual_confirm | none |
| 8 | JCI | data_center_power_cooling | 140.82 |  | 140.5276 | 0.2081 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | TT | data_center_power_cooling | 475.13 |  | 474.0059 | 0.2371 | 474.085 | 467.64 | 0.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | ANET | ai_networking_optical | 167.23 |  | 166.3471 | 0.5308 | 169.91 | 165.6 | 4.437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | QQQ | market_regime | 708.8 |  | 709.9899 | -0.1676 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1810.88 |  | 1822.477 | -0.6363 | 1823.13 | 1796.26 | 0.1049 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 296.105 |  | 296.4094 | -0.1027 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 378.86 |  | 381.3805 | -0.6609 | 386.58 | 378.53 | 0.227 | below_vwap | below_vwap |
| 16 | ONTO | semiconductor_test_packaging | 285.3 |  | 289.4304 | -1.4271 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 371.665 |  | 371.8815 | -0.0582 | 375.18 | 369.2 | 0.3121 | below_vwap | below_vwap |
| 18 | TSM | foundry | 407.38 |  | 410.3529 | -0.7245 | 414.385 | 406.61 | 1.0997 | below_vwap | below_vwap,spread_too_wide |
| 19 | GEV | data_center_power_cooling | 1027 |  | 1029.3323 | -0.2266 | 1035.07 | 1021.09 | 4.0166 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 567.83 |  | 572.9467 | -0.8931 | 572.69 | 562.32 | 2.5342 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 515.83 |  | 514.8897 | 0.1826 | 515.825 | 512.23 | 0.2074 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.195 |  | 294.8023 | 0.4724 | 293.89 | 291.35 | 0.1452 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 403.15 |  | 397.5066 | 1.4197 | 398.69 | 392.2 | 0.0719 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.75 |  | 329.9989 | 0.5306 | 328.98 | 326.885 | 0.0482 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 475.13 |  | 474.0059 | 0.2371 | 474.085 | 467.64 | 0.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SPY | market_regime | 752.815 |  | 752.7471 | 0.009 | 753.51 | 751.13 | 0.0013 | watch_only | none |
| 7 | ORCL | cloud_ai_capex | 126.91 |  | 126.7625 | 0.1163 | 131.36 | 126.665 | 0.0552 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 255.755 |  | 255.4415 | 0.1227 | 258.07 | 252.62 | 0.0235 | watch_only | none |
| 9 | TSM | foundry | 407.38 |  | 410.3529 | -0.7245 | 414.385 | 406.61 | 1.0997 | below_vwap | below_vwap,spread_too_wide |
| 10 | QQQ | market_regime | 708.8 |  | 709.9899 | -0.1676 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 378.86 |  | 381.3805 | -0.6609 | 386.58 | 378.53 | 0.227 | below_vwap | below_vwap |
| 12 | GEV | data_center_power_cooling | 1027 |  | 1029.3323 | -0.2266 | 1035.07 | 1021.09 | 4.0166 | below_vwap | below_vwap,spread_too_wide |
| 13 | ASML | semiconductor_equipment | 1810.88 |  | 1822.477 | -0.6363 | 1823.13 | 1796.26 | 0.1049 | below_vwap | below_vwap |
| 14 | AMAT | semiconductor_equipment | 567.83 |  | 572.9467 | -0.8931 | 572.69 | 562.32 | 2.5342 | below_vwap | below_vwap,spread_too_wide |
| 15 | ONTO | semiconductor_test_packaging | 285.3 |  | 289.4304 | -1.4271 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | KLAC | semiconductor_equipment | 219.23 |  | 221.6891 | -1.1092 | 222.19 | 218.09 | 5.013 | below_vwap | below_vwap,spread_too_wide |
| 17 | IWM | market_regime | 296.105 |  | 296.4094 | -0.1027 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | DELL | ai_server_oem | 401.02 |  | 403.3984 | -0.5896 | 411.65 | 400.635 | 4.137 | below_vwap | below_vwap,spread_too_wide |
| 20 | ENTG | semiconductor_materials | 135.07 |  | 135.1571 | -0.0645 | 138.07 | 133.73 | 4.6124 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.8 |  | 709.9899 | -0.1676 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.69 |  | 72.0479 | -0.4968 | 73.09 | 71.45 | 0.0279 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.29 |  | 207.5274 | -0.1144 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.15 |  | 397.5066 | 1.4197 | 398.69 | 392.2 | 0.0719 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.75 |  | 329.9989 | 0.5306 | 328.98 | 326.885 | 0.0482 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.665 |  | 371.8815 | -0.0582 | 375.18 | 369.2 | 0.3121 | below_vwap | below_vwap |
| AMD | ai_accelerator | 502.42 |  | 507.3359 | -0.969 | 518.33 | 507.62 | 1.3534 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 407.38 |  | 410.3529 | -0.7245 | 414.385 | 406.61 | 1.0997 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 531.55 |  | 536.1011 | -0.8489 | 543.4 | 535.47 | 0.0715 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 570.21 |  | 574.0088 | -0.6618 | 580.31 | 572.21 | 0.0351 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 378.86 |  | 381.3805 | -0.6609 | 386.58 | 378.53 | 0.227 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 851.79 |  | 860.4112 | -1.002 | 887.1 | 866.765 | 0.5741 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 189.08 |  | 192.3393 | -1.6946 | 201.61 | 194.19 | 0.1058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 401.02 |  | 403.3984 | -0.5896 | 411.65 | 400.635 | 4.137 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.33 |  | 46.0529 | -1.5697 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.095 |  | 25.5068 | -1.6145 | 26.71 | 25.74 | 0.0398 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.815 |  | 752.7471 | 0.009 | 753.51 | 751.13 | 0.0013 | watch_only | none |
| IWM | market_regime | 296.105 |  | 296.4094 | -0.1027 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.91 |  | 126.7625 | 0.1163 | 131.36 | 126.665 | 0.0552 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 73.835 |  | 73.5202 | 0.4281 | 75.54 | 73.985 | 4.1173 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 291.28 |  | 294.8745 | -1.219 | 300.385 | 293.64 | 2.2796 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.645 |  | 400.1122 | -1.3664 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 628.96 |  | 632.2935 | -0.5272 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1027 |  | 1029.3323 | -0.2266 | 1035.07 | 1021.09 | 4.0166 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.13 |  | 474.0059 | 0.2371 | 474.085 | 467.64 | 0.743 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.82 |  | 140.5276 | 0.2081 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.23 |  | 166.3471 | 0.5308 | 169.91 | 165.6 | 4.437 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 279.355 |  | 282.0639 | -0.9604 | 288.48 | 280.67 | 4.6965 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.98 |  | 711.364 | -1.4597 | 737.175 | 720.21 | 0.3723 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 392 |  | 396.512 | -1.1379 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.52 |  | 102.174 | -2.5975 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.945 |  | 324.7494 | -1.4794 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1810.88 |  | 1822.477 | -0.6363 | 1823.13 | 1796.26 | 0.1049 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 567.83 |  | 572.9467 | -0.8931 | 572.69 | 562.32 | 2.5342 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 321.61 |  | 325.097 | -1.0726 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.23 |  | 221.6891 | -1.1092 | 222.19 | 218.09 | 5.013 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 325.62 |  | 327.5838 | -0.5995 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 285.3 |  | 289.4304 | -1.4271 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.305 |  | 64.3823 | -1.6733 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.38 |  | 52.2999 | -1.7589 | 52.72 | 51.735 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.07 |  | 135.1571 | -0.0645 | 138.07 | 133.73 | 4.6124 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 335.645 |  | 338.7585 | -0.9191 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 515.83 |  | 514.8897 | 0.1826 | 515.825 | 512.23 | 0.2074 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.195 |  | 294.8023 | 0.4724 | 293.89 | 291.35 | 0.1452 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.49 |  | 27.0399 | -2.0338 | 28.05 | 27.6 | 0.1133 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.14 |  | 35.73 | -1.6513 | 37.365 | 36.4 | 0.0569 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.04 |  | 21.3609 | -1.5024 | 22.18 | 21.78 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1454.88 |  | 1475.4183 | -1.392 | 1549.47 | 1482.06 | 4.9489 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 463.01 |  | 477.4785 | -3.0302 | 498.04 | 480.14 | 1.7473 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 755.85 |  | 769.3095 | -1.7496 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.755 |  | 255.4415 | 0.1227 | 258.07 | 252.62 | 0.0235 | watch_only | none |
| META | cloud_ai_capex | 669.32 |  | 673.4686 | -0.616 | 680.09 | 667.1 | 1.9378 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 254.61 |  | 257.6319 | -1.173 | 265.96 | 258.1 | 2.6315 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 160.55 |  | 163.2997 | -1.6838 | 168.11 | 162.41 | 2.479 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
