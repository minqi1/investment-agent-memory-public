# Intraday State

- Generated at: `2026-07-16T22:38:05+08:00`
- Market time ET: `2026-07-16T10:38:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'manual_confirm_candidate': 6, 'spread_too_wide_or_missing': 16, 'price_stale_or_missing': 1, 'below_vwap': 13, 'below_opening_15m_low': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.08 |  | 710.516 | 0.2201 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| SOXX | semiconductor_index | 539.59 |  | 538.379 | 0.2249 | 543.4 | 535.47 | 0.0871 | watch_only | none |
| SMH | semiconductor_index | 576.87 |  | 576.2412 | 0.1091 | 580.31 | 572.21 | 0.0676 | watch_only | none |
| SPY | market_regime | 754.26 |  | 752.4428 | 0.2415 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 576.535 |  | 575.5529 | 0.1706 | 572.69 | 562.32 | 0.3035 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 223.025 |  | 222.9344 | 0.0406 | 222.19 | 218.09 | 0.2421 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 754.26 |  | 752.4428 | 0.2415 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 296.9 |  | 296.4678 | 0.1458 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | TER | semiconductor_test_packaging | 332.665 |  | 328.3897 | 1.3019 | 332.49 | 326.685 | 0.3307 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 330.92 |  | 329.0056 | 0.5819 | 328.98 | 326.885 | 0.0604 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.26 |  | 752.4428 | 0.2415 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.9 |  | 296.4678 | 0.1458 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 576.535 |  | 575.5529 | 0.1706 | 572.69 | 562.32 | 0.3035 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 223.025 |  | 222.9344 | 0.0406 | 222.19 | 218.09 | 0.2421 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 539.59 |  | 538.379 | 0.2249 | 543.4 | 535.47 | 0.0871 | watch_only | none |
| 6 | QQQ | market_regime | 712.08 |  | 710.516 | 0.2201 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| 7 | NVDA | ai_accelerator | 208.79 |  | 208.4732 | 0.1519 | 211.03 | 207.49 | 0.0958 | watch_only | none |
| 8 | SMH | semiconductor_index | 576.87 |  | 576.2412 | 0.1091 | 580.31 | 572.21 | 0.0676 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 330.92 |  | 329.0056 | 0.5819 | 328.98 | 326.885 | 0.0604 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 256.375 |  | 254.9551 | 0.5569 | 258.07 | 252.62 | 0.0546 | watch_only | none |
| 11 | VRT | data_center_power_cooling | 298.26 |  | 296.7094 | 0.5226 | 300.385 | 293.64 | 0.2179 | watch_only | none |
| 12 | APD | industrial_gases | 293.02 |  | 291.6854 | 0.4575 | 293.89 | 291.35 | 0.2491 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 397.1 |  | 395.0845 | 0.5102 | 398.69 | 392.2 | 0.3374 | watch_only | none |
| 14 | GOOGL | cloud_ai_capex | 373.53 |  | 371.6746 | 0.4992 | 375.18 | 369.2 | 0.3052 | watch_only | none |
| 15 | TER | semiconductor_test_packaging | 332.665 |  | 328.3897 | 1.3019 | 332.49 | 326.685 | 0.3307 | buy_precheck_manual_confirm | none |
| 16 | PWR | data_center_power_cooling | 634.8 |  | 633.4303 | 0.2162 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ETN | data_center_power_cooling | 403.425 |  | 402.5529 | 0.2166 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 342.86 |  | 341.6961 | 0.3406 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 141.315 |  | 140.5693 | 0.5305 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 382.97 |  | 382.1216 | 0.222 | 386.58 | 378.53 | 1.0445 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 576.535 |  | 575.5529 | 0.1706 | 572.69 | 562.32 | 0.3035 | buy_precheck_manual_confirm | none |
| 2 | KLAC | semiconductor_equipment | 223.025 |  | 222.9344 | 0.0406 | 222.19 | 218.09 | 0.2421 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 754.26 |  | 752.4428 | 0.2415 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 296.9 |  | 296.4678 | 0.1458 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | TER | semiconductor_test_packaging | 332.665 |  | 328.3897 | 1.3019 | 332.49 | 326.685 | 0.3307 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 330.92 |  | 329.0056 | 0.5819 | 328.98 | 326.885 | 0.0604 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 414.79 |  | 411.0238 | 0.9163 | 414.385 | 406.61 | 1.2151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | TT | data_center_power_cooling | 476.09 |  | 473.6387 | 0.5176 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 141.315 |  | 140.5693 | 0.5305 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | GEV | data_center_power_cooling | 1043.23 |  | 1029.4957 | 1.3341 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | COHU | semiconductor_test_packaging | 53.16 |  | 52.5914 | 1.0811 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SOXX | semiconductor_index | 539.59 |  | 538.379 | 0.2249 | 543.4 | 535.47 | 0.0871 | watch_only | none |
| 13 | QQQ | market_regime | 712.08 |  | 710.516 | 0.2201 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| 14 | VRT | data_center_power_cooling | 298.26 |  | 296.7094 | 0.5226 | 300.385 | 293.64 | 0.2179 | watch_only | none |
| 15 | NVDA | ai_accelerator | 208.79 |  | 208.4732 | 0.1519 | 211.03 | 207.49 | 0.0958 | watch_only | none |
| 16 | SMH | semiconductor_index | 576.87 |  | 576.2412 | 0.1091 | 580.31 | 572.21 | 0.0676 | watch_only | none |
| 17 | APD | industrial_gases | 293.02 |  | 291.6854 | 0.4575 | 293.89 | 291.35 | 0.2491 | watch_only | none |
| 18 | MSFT | cloud_ai_capex | 397.1 |  | 395.0845 | 0.5102 | 398.69 | 392.2 | 0.3374 | watch_only | none |
| 19 | GOOGL | cloud_ai_capex | 373.53 |  | 371.6746 | 0.4992 | 375.18 | 369.2 | 0.3052 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 256.375 |  | 254.9551 | 0.5569 | 258.07 | 252.62 | 0.0546 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 712.08 |  | 710.516 | 0.2201 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| TQQQ | leveraged_tool | 72.7 |  | 72.2001 | 0.6924 | 73.09 | 71.45 | 0.0275 | watch_only | none |
| NVDA | ai_accelerator | 208.79 |  | 208.4732 | 0.1519 | 211.03 | 207.49 | 0.0958 | watch_only | none |
| MSFT | cloud_ai_capex | 397.1 |  | 395.0845 | 0.5102 | 398.69 | 392.2 | 0.3374 | watch_only | none |
| AAPL | mega_cap_platform | 330.92 |  | 329.0056 | 0.5819 | 328.98 | 326.885 | 0.0604 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 373.53 |  | 371.6746 | 0.4992 | 375.18 | 369.2 | 0.3052 | watch_only | none |
| AMD | ai_accelerator | 512.385 |  | 511.1008 | 0.2513 | 518.33 | 507.62 | 1.1222 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 414.79 |  | 411.0238 | 0.9163 | 414.385 | 406.61 | 1.2151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 539.59 |  | 538.379 | 0.2249 | 543.4 | 535.47 | 0.0871 | watch_only | none |
| SMH | semiconductor_index | 576.87 |  | 576.2412 | 0.1091 | 580.31 | 572.21 | 0.0676 | watch_only | none |
| AVGO | custom_silicon_networking | 382.97 |  | 382.1216 | 0.222 | 386.58 | 378.53 | 1.0445 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 866.585 |  | 867.4798 | -0.1032 | 887.1 | 866.765 | 0.2193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 193.66 |  | 195.3904 | -0.8856 | 201.61 | 194.19 | 2.7264 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 407.44 |  | 405.6042 | 0.4526 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.32 |  | 46.8182 | -1.0641 | 47.65 | 46.165 | 0.0216 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.735 |  | 25.9288 | -0.7474 | 26.71 | 25.74 | 0.0389 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.26 |  | 752.4428 | 0.2415 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.9 |  | 296.4678 | 0.1458 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.775 |  | 127.4832 | -0.5555 | 131.36 | 126.665 | 0.7099 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.77 |  | 74.175 | -0.546 | 75.54 | 73.985 | 1.4098 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 298.26 |  | 296.7094 | 0.5226 | 300.385 | 293.64 | 0.2179 | watch_only | none |
| ETN | data_center_power_cooling | 403.425 |  | 402.5529 | 0.2166 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.8 |  | 633.4303 | 0.2162 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1043.23 |  | 1029.4957 | 1.3341 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 476.09 |  | 473.6387 | 0.5176 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.315 |  | 140.5693 | 0.5305 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.265 |  | 166.4002 | -0.0812 | 169.91 | 165.6 | 0.9142 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 283.41 |  | 285.1143 | -0.5978 | 288.48 | 280.67 | 2.0641 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 718.52 |  | 722.2696 | -0.5191 | 737.175 | 720.21 | 4.8001 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 394.03 |  | 400.4108 | -1.5936 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 103.13 |  | 103.9347 | -0.7742 | 106.975 | 102.85 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 328.905 |  | 329.6904 | -0.2382 | 337.59 | 326.16 | 4.6731 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1823 |  | 1827.6089 | -0.2522 | 1823.13 | 1796.26 | 0.571 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 576.535 |  | 575.5529 | 0.1706 | 572.69 | 562.32 | 0.3035 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 327.95 |  | 328.0376 | -0.0267 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 223.025 |  | 222.9344 | 0.0406 | 222.19 | 218.09 | 0.2421 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 332.665 |  | 328.3897 | 1.3019 | 332.49 | 326.685 | 0.3307 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 292.06 |  | 290.365 | 0.5837 | 295.83 | 285.02 | 0.3972 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 64.73 |  | 64.8433 | -0.1748 | 66.19 | 63.93 | 4.9436 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 53.16 |  | 52.5914 | 1.0811 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.46 |  | 135.895 | 0.4158 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 342.86 |  | 341.6961 | 0.3406 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.81 |  | 513.2082 | -0.0776 | 515.825 | 512.23 | 0.353 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 293.02 |  | 291.6854 | 0.4575 | 293.89 | 291.35 | 0.2491 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 27.47 |  | 27.497 | -0.0982 | 28.05 | 27.6 | 0.1456 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.94 |  | 36.415 | -1.3044 | 37.365 | 36.4 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.495 |  | 21.6665 | -0.7917 | 22.18 | 21.78 | 0.093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1489.655 |  | 1501.9247 | -0.8169 | 1549.47 | 1482.06 | 1.107 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 485.74 |  | 483.6804 | 0.4258 | 498.04 | 480.14 | 3.4998 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 784.29 |  | 777.1957 | 0.9128 | 797.155 | 768.7 | 5.1333 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 256.375 |  | 254.9551 | 0.5569 | 258.07 | 252.62 | 0.0546 | watch_only | none |
| META | cloud_ai_capex | 679.9 |  | 673.2817 | 0.983 | 680.09 | 667.1 | 0.4515 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 257.99 |  | 259.7468 | -0.6763 | 265.96 | 258.1 | 4.5428 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 163.46 |  | 164.7009 | -0.7535 | 168.11 | 162.41 | 1.2235 | below_vwap | below_vwap,spread_too_wide |
