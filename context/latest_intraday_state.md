# Intraday State

- Generated at: `2026-07-16T22:16:47+08:00`
- Market time ET: `2026-07-16T10:16:49-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'below_vwap': 8, 'spread_too_wide_or_missing': 30, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 4, 'below_opening_15m_low': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.44 |  | 710.2868 | 0.3032 | 713.55 | 708.25 | 0.0112 | watch_only | none |
| SOXX | semiconductor_index | 542.77 |  | 538.0806 | 0.8715 | 543.4 | 535.47 | 0.1032 | watch_only | none |
| SMH | semiconductor_index | 579.57 |  | 575.914 | 0.6348 | 580.31 | 572.21 | 0.1104 | watch_only | none |
| SPY | market_regime | 753.47 |  | 752.1195 | 0.1796 | 753.51 | 751.13 | 0.0053 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.72 |  | 140.2902 | 1.0192 | 140.83 | 139.43 | 0.2329 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1829.25 |  | 1827.8057 | 0.079 | 1823.13 | 1796.26 | 0.3324 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 226.19 |  | 222.4978 | 1.6594 | 222.19 | 218.09 | 0.1415 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 297.46 |  | 296.3574 | 0.372 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1829.25 |  | 1827.8057 | 0.079 | 1823.13 | 1796.26 | 0.3324 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 410.445 |  | 410.4261 | 0.0046 | 414.385 | 406.61 | 0.0658 | watch_only | none |
| 3 | QQQ | market_regime | 712.44 |  | 710.2868 | 0.3032 | 713.55 | 708.25 | 0.0112 | watch_only | none |
| 4 | IWM | market_regime | 297.46 |  | 296.3574 | 0.372 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 208.91 |  | 208.4178 | 0.2362 | 211.03 | 207.49 | 0.0191 | watch_only | none |
| 6 | SPY | market_regime | 753.47 |  | 752.1195 | 0.1796 | 753.51 | 751.13 | 0.0053 | watch_only | none |
| 7 | HPE | ai_server_oem | 47.01 |  | 46.8835 | 0.2698 | 47.65 | 46.165 | 0.0425 | watch_only | none |
| 8 | SMH | semiconductor_index | 579.57 |  | 575.914 | 0.6348 | 580.31 | 572.21 | 0.1104 | watch_only | none |
| 9 | JCI | data_center_power_cooling | 141.72 |  | 140.2902 | 1.0192 | 140.83 | 139.43 | 0.2329 | buy_precheck_manual_confirm | none |
| 10 | CIEN | ai_networking_optical | 401.55 |  | 401.3471 | 0.0505 | 410 | 397.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 542.77 |  | 538.0806 | 0.8715 | 543.4 | 535.47 | 0.1032 | watch_only | none |
| 12 | ARM | ai_accelerator | 260.66 |  | 260.1628 | 0.1911 | 265.96 | 258.1 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TT | data_center_power_cooling | 475.53 |  | 472.8243 | 0.5722 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ANET | ai_networking_optical | 166.725 |  | 166.5435 | 0.109 | 169.91 | 165.6 | 1.7994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 634.42 |  | 633.0043 | 0.2237 | 640.25 | 631.005 | 1.7244 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ETN | data_center_power_cooling | 405.42 |  | 402.2779 | 0.7811 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MRVL | custom_silicon_networking | 196.05 |  | 195.539 | 0.2613 | 201.61 | 194.19 | 1.7343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMKR | semiconductor_test_packaging | 65.18 |  | 64.837 | 0.5291 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | SKHY | memory_hbm_storage | 165.33 |  | 164.899 | 0.2613 | 168.11 | 162.41 | 1.3851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | KLAC | semiconductor_equipment | 226.19 |  | 222.4978 | 1.6594 | 222.19 | 218.09 | 0.1415 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.72 |  | 140.2902 | 1.0192 | 140.83 | 139.43 | 0.2329 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1829.25 |  | 1827.8057 | 0.079 | 1823.13 | 1796.26 | 0.3324 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 226.19 |  | 222.4978 | 1.6594 | 222.19 | 218.09 | 0.1415 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 297.46 |  | 296.3574 | 0.372 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 475.53 |  | 472.8243 | 0.5722 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1045.71 |  | 1027.4171 | 1.7805 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | AMAT | semiconductor_equipment | 584.83 |  | 573.9934 | 1.8879 | 572.69 | 562.32 | 2.7683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | LRCX | semiconductor_equipment | 332.07 |  | 327.825 | 1.2949 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | COHU | semiconductor_test_packaging | 53.78 |  | 52.4034 | 2.627 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 542.77 |  | 538.0806 | 0.8715 | 543.4 | 535.47 | 0.1032 | watch_only | none |
| 12 | TSM | foundry | 410.445 |  | 410.4261 | 0.0046 | 414.385 | 406.61 | 0.0658 | watch_only | none |
| 13 | QQQ | market_regime | 712.44 |  | 710.2868 | 0.3032 | 713.55 | 708.25 | 0.0112 | watch_only | none |
| 14 | NVDA | ai_accelerator | 208.91 |  | 208.4178 | 0.2362 | 211.03 | 207.49 | 0.0191 | watch_only | none |
| 15 | SMH | semiconductor_index | 579.57 |  | 575.914 | 0.6348 | 580.31 | 572.21 | 0.1104 | watch_only | none |
| 16 | SPY | market_regime | 753.47 |  | 752.1195 | 0.1796 | 753.51 | 751.13 | 0.0053 | watch_only | none |
| 17 | HPE | ai_server_oem | 47.01 |  | 46.8835 | 0.2698 | 47.65 | 46.165 | 0.0425 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 72.735 |  | 72.1079 | 0.8697 | 73.09 | 71.45 | 0.0137 | watch_only | none |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | MSFT | cloud_ai_capex | 394.34 |  | 395.0698 | -0.1847 | 398.69 | 392.2 | 0.1116 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.44 |  | 710.2868 | 0.3032 | 713.55 | 708.25 | 0.0112 | watch_only | none |
| TQQQ | leveraged_tool | 72.735 |  | 72.1079 | 0.8697 | 73.09 | 71.45 | 0.0137 | watch_only | none |
| NVDA | ai_accelerator | 208.91 |  | 208.4178 | 0.2362 | 211.03 | 207.49 | 0.0191 | watch_only | none |
| MSFT | cloud_ai_capex | 394.34 |  | 395.0698 | -0.1847 | 398.69 | 392.2 | 0.1116 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.45 |  | 328.7946 | -0.1048 | 328.98 | 326.885 | 0.0183 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 370.955 |  | 371.3266 | -0.1001 | 375.18 | 369.2 | 0.1402 | below_vwap | below_vwap |
| AMD | ai_accelerator | 516.51 |  | 512.4102 | 0.8001 | 518.33 | 507.62 | 0.666 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 410.445 |  | 410.4261 | 0.0046 | 414.385 | 406.61 | 0.0658 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 542.77 |  | 538.0806 | 0.8715 | 543.4 | 535.47 | 0.1032 | watch_only | none |
| SMH | semiconductor_index | 579.57 |  | 575.914 | 0.6348 | 580.31 | 572.21 | 0.1104 | watch_only | none |
| AVGO | custom_silicon_networking | 384.69 |  | 381.9011 | 0.7303 | 386.58 | 378.53 | 3.7953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 875.53 |  | 867.2073 | 0.9597 | 887.1 | 866.765 | 0.5471 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 196.05 |  | 195.539 | 0.2613 | 201.61 | 194.19 | 1.7343 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 408.885 |  | 404.85 | 0.9967 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 47.01 |  | 46.8835 | 0.2698 | 47.65 | 46.165 | 0.0425 | watch_only | none |
| SMCI | ai_server_oem | 25.905 |  | 25.9582 | -0.2048 | 26.71 | 25.74 | 0.0772 | below_vwap | below_vwap |
| SPY | market_regime | 753.47 |  | 752.1195 | 0.1796 | 753.51 | 751.13 | 0.0053 | watch_only | none |
| IWM | market_regime | 297.46 |  | 296.3574 | 0.372 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.35 |  | 127.5857 | -0.1847 | 131.36 | 126.665 | 2.2772 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.64 |  | 74.2017 | 0.5907 | 75.54 | 73.985 | 4.381 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 299.44 |  | 296.2745 | 1.0684 | 300.385 | 293.64 | 4.5418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 405.42 |  | 402.2779 | 0.7811 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.42 |  | 633.0043 | 0.2237 | 640.25 | 631.005 | 1.7244 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1045.71 |  | 1027.4171 | 1.7805 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 475.53 |  | 472.8243 | 0.5722 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.72 |  | 140.2902 | 1.0192 | 140.83 | 139.43 | 0.2329 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 166.725 |  | 166.5435 | 0.109 | 169.91 | 165.6 | 1.7994 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 288.09 |  | 285.2115 | 1.0093 | 288.48 | 280.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 733.57 |  | 722.9106 | 1.4745 | 737.175 | 720.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 401.55 |  | 401.3471 | 0.0505 | 410 | 397.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 105.69 |  | 103.9935 | 1.6313 | 106.975 | 102.85 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 332.17 |  | 329.4807 | 0.8162 | 337.59 | 326.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1829.25 |  | 1827.8057 | 0.079 | 1823.13 | 1796.26 | 0.3324 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 584.83 |  | 573.9934 | 1.8879 | 572.69 | 562.32 | 2.7683 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 332.07 |  | 327.825 | 1.2949 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 226.19 |  | 222.4978 | 1.6594 | 222.19 | 218.09 | 0.1415 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 332.32 |  | 327.8555 | 1.3617 | 332.49 | 326.685 | 4.4806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.38 |  | 289.6427 | 1.9808 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.18 |  | 64.837 | 0.5291 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.78 |  | 52.4034 | 2.627 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.9 |  | 135.8245 | 0.7918 | 138.07 | 133.73 | 4.6092 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 511.05 |  | 513.4807 | -0.4734 | 515.825 | 512.23 | 3.6493 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 290.64 |  | 291.4021 | -0.2615 | 293.89 | 291.35 | 4.294 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.595 |  | 27.5137 | 0.2955 | 28.05 | 27.6 | 0.0362 | below_opening_15m_low | below_opening_15m_low |
| IREN | high_beta_ai_infrastructure | 36.22 |  | 36.4904 | -0.7409 | 37.365 | 36.4 | 0.0552 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.59 |  | 21.711 | -0.5572 | 22.18 | 21.78 | 0.5558 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SNDK | memory_hbm_storage | 1523.53 |  | 1501.9255 | 1.4385 | 1549.47 | 1482.06 | 4.2008 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 489.84 |  | 483.2683 | 1.3598 | 498.04 | 480.14 | 1.0146 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 790.18 |  | 776.3096 | 1.7867 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 254.23 |  | 254.6756 | -0.175 | 258.07 | 252.62 | 0.0393 | below_vwap | below_vwap |
| META | cloud_ai_capex | 671.99 |  | 672.3163 | -0.0485 | 680.09 | 667.1 | 0.1443 | below_vwap | below_vwap |
| ARM | ai_accelerator | 260.66 |  | 260.1628 | 0.1911 | 265.96 | 258.1 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 165.33 |  | 164.899 | 0.2613 | 168.11 | 162.41 | 1.3851 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
