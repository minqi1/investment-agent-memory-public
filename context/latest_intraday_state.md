# Intraday State

- Generated at: `2026-07-17T00:36:14+08:00`
- Market time ET: `2026-07-16T12:36:15-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 36, 'manual_confirm_candidate': 3, 'below_vwap': 14, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.86 |  | 710.1469 | -0.322 | 713.55 | 708.25 | 0.0438 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.86 |  | 536.4411 | -1.2268 | 543.4 | 535.47 | 0.0812 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.79 |  | 574.5924 | -1.0098 | 580.31 | 572.21 | 0.0686 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.08 |  | 752.792 | -0.0946 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.605 |  | 294.7349 | 0.6345 | 293.89 | 291.35 | 0.1922 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.545 |  | 396.8314 | 1.1878 | 398.69 | 392.2 | 0.1942 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.96 |  | 329.9076 | 0.319 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 330.96 |  | 329.9076 | 0.319 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.53 |  | 255.3974 | 0.0519 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 3 | APD | industrial_gases | 296.605 |  | 294.7349 | 0.6345 | 293.89 | 291.35 | 0.1922 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 401.545 |  | 396.8314 | 1.1878 | 398.69 | 392.2 | 0.1942 | buy_precheck_manual_confirm | none |
| 5 | LIN | industrial_gases | 515.53 |  | 514.7878 | 0.1442 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ASML | semiconductor_equipment | 1805.07 |  | 1823.7007 | -1.0216 | 1823.13 | 1796.26 | 0.0942 | below_vwap | below_vwap |
| 7 | SPY | market_regime | 752.08 |  | 752.792 | -0.0946 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.995 |  | 296.4726 | -0.1611 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 9 | GOOGL | cloud_ai_capex | 371.685 |  | 371.893 | -0.0559 | 375.18 | 369.2 | 0.1076 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | TT | data_center_power_cooling | 472.04 |  | 474.1631 | -0.4478 | 474.085 | 467.64 | 0.25 | below_vwap | below_vwap |
| 12 | KLAC | semiconductor_equipment | 218.26 |  | 221.9222 | -1.6502 | 222.19 | 218.09 | 0.1512 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 166.18 |  | 166.3229 | -0.0859 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 139.75 |  | 140.5619 | -0.5776 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 134.29 |  | 135.2893 | -0.7386 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 51.75 |  | 52.3092 | -1.0689 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | AVGO | custom_silicon_networking | 380.275 |  | 381.6601 | -0.3629 | 386.58 | 378.53 | 0.7836 | below_vwap | below_vwap,spread_too_wide |
| 18 | AMAT | semiconductor_equipment | 565.9 |  | 573.7147 | -1.3621 | 572.69 | 562.32 | 2.329 | below_vwap | below_vwap,spread_too_wide |
| 19 | META | cloud_ai_capex | 670.465 |  | 673.985 | -0.5223 | 680.09 | 667.1 | 2.0478 | below_vwap | below_vwap,spread_too_wide |
| 20 | SOXX | semiconductor_index | 529.86 |  | 536.4411 | -1.2268 | 543.4 | 535.47 | 0.0812 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | APD | industrial_gases | 296.605 |  | 294.7349 | 0.6345 | 293.89 | 291.35 | 0.1922 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 401.545 |  | 396.8314 | 1.1878 | 398.69 | 392.2 | 0.1942 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.96 |  | 329.9076 | 0.319 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.53 |  | 255.3974 | 0.0519 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| 5 | ANET | ai_networking_optical | 166.18 |  | 166.3229 | -0.0859 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | AVGO | custom_silicon_networking | 380.275 |  | 381.6601 | -0.3629 | 386.58 | 378.53 | 0.7836 | below_vwap | below_vwap,spread_too_wide |
| 7 | TT | data_center_power_cooling | 472.04 |  | 474.1631 | -0.4478 | 474.085 | 467.64 | 0.25 | below_vwap | below_vwap |
| 8 | JCI | data_center_power_cooling | 139.75 |  | 140.5619 | -0.5776 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ASML | semiconductor_equipment | 1805.07 |  | 1823.7007 | -1.0216 | 1823.13 | 1796.26 | 0.0942 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 565.9 |  | 573.7147 | -1.3621 | 572.69 | 562.32 | 2.329 | below_vwap | below_vwap,spread_too_wide |
| 11 | KLAC | semiconductor_equipment | 218.26 |  | 221.9222 | -1.6502 | 222.19 | 218.09 | 0.1512 | below_vwap | below_vwap |
| 12 | SPY | market_regime | 752.08 |  | 752.792 | -0.0946 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 295.995 |  | 296.4726 | -0.1611 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 134.29 |  | 135.2893 | -0.7386 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | GOOGL | cloud_ai_capex | 371.685 |  | 371.893 | -0.0559 | 375.18 | 369.2 | 0.1076 | below_vwap | below_vwap |
| 17 | COHU | semiconductor_test_packaging | 51.75 |  | 52.3092 | -1.0689 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | META | cloud_ai_capex | 670.465 |  | 673.985 | -0.5223 | 680.09 | 667.1 | 2.0478 | below_vwap | below_vwap,spread_too_wide |
| 19 | LIN | industrial_gases | 515.53 |  | 514.7878 | 0.1442 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SOXX | semiconductor_index | 529.86 |  | 536.4411 | -1.2268 | 543.4 | 535.47 | 0.0812 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.86 |  | 710.1469 | -0.322 | 713.55 | 708.25 | 0.0438 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.355 |  | 72.0843 | -1.0118 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.3 |  | 207.5546 | -0.1227 | 211.03 | 207.49 | 0.3377 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.545 |  | 396.8314 | 1.1878 | 398.69 | 392.2 | 0.1942 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.96 |  | 329.9076 | 0.319 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.685 |  | 371.893 | -0.0559 | 375.18 | 369.2 | 0.1076 | below_vwap | below_vwap |
| AMD | ai_accelerator | 499.72 |  | 508.2725 | -1.6827 | 518.33 | 507.62 | 2.7716 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 406.38 |  | 410.6596 | -1.0421 | 414.385 | 406.61 | 0.1353 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.86 |  | 536.4411 | -1.2268 | 543.4 | 535.47 | 0.0812 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.79 |  | 574.5924 | -1.0098 | 580.31 | 572.21 | 0.0686 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.275 |  | 381.6601 | -0.3629 | 386.58 | 378.53 | 0.7836 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 851.36 |  | 861.8459 | -1.2167 | 887.1 | 866.765 | 1.231 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.48 |  | 192.6043 | -2.1413 | 201.61 | 194.19 | 0.6473 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.09 |  | 403.8098 | -0.9212 | 411.65 | 400.635 | 1.1647 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.28 |  | 46.099 | -1.7767 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.02 |  | 25.5448 | -2.0543 | 26.71 | 25.74 | 0.04 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.08 |  | 752.792 | -0.0946 | 753.51 | 751.13 | 0.0093 | below_vwap | below_vwap |
| IWM | market_regime | 295.995 |  | 296.4726 | -0.1611 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.465 |  | 126.7776 | -0.2466 | 131.36 | 126.665 | 0.3875 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.69 |  | 73.5494 | -1.1685 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 289.87 |  | 295.205 | -1.8072 | 300.385 | 293.64 | 1.6594 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 391.36 |  | 400.4151 | -2.2614 | 406.24 | 399.495 | 3.2119 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 627.05 |  | 632.5668 | -0.8721 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1018.4 |  | 1030.5898 | -1.1828 | 1035.07 | 1021.09 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 472.04 |  | 474.1631 | -0.4478 | 474.085 | 467.64 | 0.25 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 139.75 |  | 140.5619 | -0.5776 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.18 |  | 166.3229 | -0.0859 | 169.91 | 165.6 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 276.805 |  | 282.6073 | -2.0531 | 288.48 | 280.67 | 1.3836 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 700.57 |  | 712.6641 | -1.697 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 390.765 |  | 396.8841 | -1.5418 | 410 | 397.68 | 0.1996 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.42 |  | 102.4264 | -2.9351 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.35 |  | 325.1899 | -2.4109 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1805.07 |  | 1823.7007 | -1.0216 | 1823.13 | 1796.26 | 0.0942 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.9 |  | 573.7147 | -1.3621 | 572.69 | 562.32 | 2.329 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.02 |  | 325.5366 | -1.6946 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.26 |  | 221.9222 | -1.6502 | 222.19 | 218.09 | 0.1512 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.73 |  | 327.9845 | -1.9069 | 332.49 | 326.685 | 0.9107 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 284.95 |  | 289.8288 | -1.6833 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.06 |  | 64.445 | -2.1491 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.75 |  | 52.3092 | -1.0689 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.29 |  | 135.2893 | -0.7386 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.06 |  | 339.1474 | -1.2052 | 346.26 | 338 | 3.9247 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 515.53 |  | 514.7878 | 0.1442 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.605 |  | 294.7349 | 0.6345 | 293.89 | 291.35 | 0.1922 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.35 |  | 27.1273 | -2.8653 | 28.05 | 27.6 | 0.0759 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.85 |  | 35.7786 | -2.5955 | 37.365 | 36.4 | 0.0574 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.86 |  | 21.4347 | -2.6811 | 22.18 | 21.78 | 0.0479 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1441.17 |  | 1478.4547 | -2.5219 | 1549.47 | 1482.06 | 3.8163 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 458.94 |  | 479.0649 | -4.2009 | 498.04 | 480.14 | 0.3203 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 753.89 |  | 769.6366 | -2.046 | 797.155 | 768.7 | 3.8016 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.53 |  | 255.3974 | 0.0519 | 258.07 | 252.62 | 0.0117 | watch_only | none |
| META | cloud_ai_capex | 670.465 |  | 673.985 | -0.5223 | 680.09 | 667.1 | 2.0478 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 253.5 |  | 257.9684 | -1.7321 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.37 |  | 163.4319 | -1.8735 | 168.11 | 162.41 | 0.9042 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
