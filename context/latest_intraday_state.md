# Intraday State

- Generated at: `2026-07-16T23:28:30+08:00`
- Market time ET: `2026-07-16T11:28:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 4, 'below_opening_15m_low': 20, 'manual_confirm_candidate': 4, 'below_vwap': 17, 'spread_too_wide_or_missing': 9, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.25 |  | 710.4784 | 0.1086 | 713.55 | 708.25 | 0.0422 | watch_only | none |
| SOXX | semiconductor_index | 535.91 |  | 537.7406 | -0.3404 | 543.4 | 535.47 | 0.0933 | below_vwap | below_vwap |
| SMH | semiconductor_index | 574.02 |  | 575.6872 | -0.2896 | 580.31 | 572.21 | 0.0801 | below_vwap | below_vwap |
| SPY | market_regime | 754.22 |  | 752.7697 | 0.1927 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.22 |  | 752.7697 | 0.1927 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.18 |  | 296.6059 | 0.1935 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 399.23 |  | 395.7278 | 0.885 | 398.69 | 392.2 | 0.1403 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.77 |  | 329.3705 | 0.4249 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.22 |  | 752.7697 | 0.1927 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.18 |  | 296.6059 | 0.1935 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 711.25 |  | 710.4784 | 0.1086 | 713.55 | 708.25 | 0.0422 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 330.77 |  | 329.3705 | 0.4249 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 256.02 |  | 255.2111 | 0.317 | 258.07 | 252.62 | 0.0781 | watch_only | none |
| 6 | META | cloud_ai_capex | 675.89 |  | 674.8894 | 0.1483 | 680.09 | 667.1 | 0.2323 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 399.23 |  | 395.7278 | 0.885 | 398.69 | 392.2 | 0.1403 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 474.76 |  | 474.3254 | 0.0916 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 140.86 |  | 140.7024 | 0.112 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | COHU | semiconductor_test_packaging | 52.81 |  | 52.6715 | 0.2629 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 136.18 |  | 135.9801 | 0.147 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | LIN | industrial_gases | 517.49 |  | 513.962 | 0.6864 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 411.66 |  | 411.3957 | 0.0642 | 414.385 | 406.61 | 0.8308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | GEV | data_center_power_cooling | 1037.27 |  | 1032.8193 | 0.4309 | 1035.07 | 1021.09 | 1.9831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TER | semiconductor_test_packaging | 330.4 |  | 328.9857 | 0.4299 | 332.49 | 326.685 | 0.9171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMAT | semiconductor_equipment | 573.38 |  | 575.3903 | -0.3494 | 572.69 | 562.32 | 0.1308 | below_vwap | below_vwap |
| 17 | SOXX | semiconductor_index | 535.91 |  | 537.7406 | -0.3404 | 543.4 | 535.47 | 0.0933 | below_vwap | below_vwap |
| 18 | SMH | semiconductor_index | 574.02 |  | 575.6872 | -0.2896 | 580.31 | 572.21 | 0.0801 | below_vwap | below_vwap |
| 19 | ORCL | cloud_ai_capex | 127.06 |  | 127.1305 | -0.0554 | 131.36 | 126.665 | 0.0472 | below_vwap | below_vwap |
| 20 | GOOGL | cloud_ai_capex | 372 |  | 372.0326 | -0.0088 | 375.18 | 369.2 | 0.0753 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.22 |  | 752.7697 | 0.1927 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.18 |  | 296.6059 | 0.1935 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 399.23 |  | 395.7278 | 0.885 | 398.69 | 392.2 | 0.1403 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.77 |  | 329.3705 | 0.4249 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1824.18 |  | 1825.935 | -0.0961 | 1823.13 | 1796.26 | 0.7609 | below_vwap | below_vwap,spread_too_wide |
| 6 | AMAT | semiconductor_equipment | 573.38 |  | 575.3903 | -0.3494 | 572.69 | 562.32 | 0.1308 | below_vwap | below_vwap |
| 7 | TT | data_center_power_cooling | 474.76 |  | 474.3254 | 0.0916 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 140.86 |  | 140.7024 | 0.112 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | GEV | data_center_power_cooling | 1037.27 |  | 1032.8193 | 0.4309 | 1035.07 | 1021.09 | 1.9831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | LIN | industrial_gases | 517.49 |  | 513.962 | 0.6864 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | APD | industrial_gases | 296.64 |  | 293.4603 | 1.0835 | 293.89 | 291.35 | 3.7318 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | COHU | semiconductor_test_packaging | 52.81 |  | 52.6715 | 0.2629 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | QQQ | market_regime | 711.25 |  | 710.4784 | 0.1086 | 713.55 | 708.25 | 0.0422 | watch_only | none |
| 14 | AMZN | cloud_ai_capex | 256.02 |  | 255.2111 | 0.317 | 258.07 | 252.62 | 0.0781 | watch_only | none |
| 15 | META | cloud_ai_capex | 675.89 |  | 674.8894 | 0.1483 | 680.09 | 667.1 | 0.2323 | watch_only | none |
| 16 | TQQQ | leveraged_tool | 72.3 |  | 72.2008 | 0.1374 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| 17 | SOXX | semiconductor_index | 535.91 |  | 537.7406 | -0.3404 | 543.4 | 535.47 | 0.0933 | below_vwap | below_vwap |
| 18 | AVGO | custom_silicon_networking | 381.725 |  | 381.8705 | -0.0381 | 386.58 | 378.53 | 0.4244 | below_vwap | below_vwap,spread_too_wide |
| 19 | VRT | data_center_power_cooling | 294.27 |  | 296.5064 | -0.7542 | 300.385 | 293.64 | 3.1774 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMD | ai_accelerator | 508.75 |  | 510.5082 | -0.3444 | 518.33 | 507.62 | 0.8531 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.25 |  | 710.4784 | 0.1086 | 713.55 | 708.25 | 0.0422 | watch_only | none |
| TQQQ | leveraged_tool | 72.3 |  | 72.2008 | 0.1374 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| NVDA | ai_accelerator | 206.91 |  | 207.6664 | -0.3642 | 211.03 | 207.49 | 0.0483 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.23 |  | 395.7278 | 0.885 | 398.69 | 392.2 | 0.1403 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 330.77 |  | 329.3705 | 0.4249 | 328.98 | 326.885 | 0.0091 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372 |  | 372.0326 | -0.0088 | 375.18 | 369.2 | 0.0753 | below_vwap | below_vwap |
| AMD | ai_accelerator | 508.75 |  | 510.5082 | -0.3444 | 518.33 | 507.62 | 0.8531 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 411.66 |  | 411.3957 | 0.0642 | 414.385 | 406.61 | 0.8308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 535.91 |  | 537.7406 | -0.3404 | 543.4 | 535.47 | 0.0933 | below_vwap | below_vwap |
| SMH | semiconductor_index | 574.02 |  | 575.6872 | -0.2896 | 580.31 | 572.21 | 0.0801 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.725 |  | 381.8705 | -0.0381 | 386.58 | 378.53 | 0.4244 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 861.74 |  | 865.1848 | -0.3982 | 887.1 | 866.765 | 0.9202 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 191.99 |  | 194.0399 | -1.0564 | 201.61 | 194.19 | 0.5782 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 402.32 |  | 405.0446 | -0.6727 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.04 |  | 46.4167 | -0.8116 | 47.65 | 46.165 | 0.0434 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.33 |  | 25.7644 | -1.6859 | 26.71 | 25.74 | 0.0395 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.22 |  | 752.7697 | 0.1927 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.18 |  | 296.6059 | 0.1935 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.06 |  | 127.1305 | -0.0554 | 131.36 | 126.665 | 0.0472 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.33 |  | 73.9472 | -0.8346 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 294.27 |  | 296.5064 | -0.7542 | 300.385 | 293.64 | 3.1774 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 397.05 |  | 401.6604 | -1.1478 | 406.24 | 399.495 | 4.478 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 631.98 |  | 633.3074 | -0.2096 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1037.27 |  | 1032.8193 | 0.4309 | 1035.07 | 1021.09 | 1.9831 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 474.76 |  | 474.3254 | 0.0916 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.86 |  | 140.7024 | 0.112 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.52 |  | 166.272 | -0.4523 | 169.91 | 165.6 | 3.8304 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 278.8 |  | 284.0292 | -1.8411 | 288.48 | 280.67 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 706.88 |  | 717.8826 | -1.5327 | 737.175 | 720.21 | 3.8875 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 394.9 |  | 398.6579 | -0.9426 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.56 |  | 103.263 | -1.6492 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 323.83 |  | 328.7519 | -1.4971 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1824.18 |  | 1825.935 | -0.0961 | 1823.13 | 1796.26 | 0.7609 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 573.38 |  | 575.3903 | -0.3494 | 572.69 | 562.32 | 0.1308 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 325.98 |  | 327.3558 | -0.4203 | 328.96 | 324.11 | 3.6321 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 221.75 |  | 222.855 | -0.4958 | 222.19 | 218.09 | 4.5096 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 330.4 |  | 328.9857 | 0.4299 | 332.49 | 326.685 | 0.9171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 | 3.5681 | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| AMKR | semiconductor_test_packaging | 64.59 |  | 64.6238 | -0.0524 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.81 |  | 52.6715 | 0.2629 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.18 |  | 135.9801 | 0.147 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 339.905 |  | 341.2728 | -0.4008 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.49 |  | 513.962 | 0.6864 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.64 |  | 293.4603 | 1.0835 | 293.89 | 291.35 | 3.7318 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.93 |  | 27.4058 | -1.7361 | 28.05 | 27.6 | 0.1485 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.93 |  | 36.0833 | -0.4249 | 37.365 | 36.4 | 0.0835 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.31 |  | 21.5616 | -1.1667 | 22.18 | 21.78 | 0.0939 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1469.68 |  | 1490.6683 | -1.408 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 475.46 |  | 483.2415 | -1.6103 | 498.04 | 480.14 | 0.101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 771.74 |  | 777.6078 | -0.7546 | 797.155 | 768.7 | 1.6106 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.02 |  | 255.2111 | 0.317 | 258.07 | 252.62 | 0.0781 | watch_only | none |
| META | cloud_ai_capex | 675.89 |  | 674.8894 | 0.1483 | 680.09 | 667.1 | 0.2323 | watch_only | none |
| ARM | ai_accelerator | 257.15 |  | 258.7739 | -0.6275 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.69 |  | 163.8911 | -1.343 | 168.11 | 162.41 | 3.08 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
