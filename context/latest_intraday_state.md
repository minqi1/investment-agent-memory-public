# Intraday State

- Generated at: `2026-07-16T22:22:08+08:00`
- Market time ET: `2026-07-16T10:22:10-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'below_vwap': 13, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 2, 'below_opening_15m_low': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.545 |  | 710.4188 | 0.1585 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| SOXX | semiconductor_index | 539.745 |  | 538.2822 | 0.2718 | 543.4 | 535.47 | 0.1019 | watch_only | none |
| SMH | semiconductor_index | 577.37 |  | 576.1842 | 0.2058 | 580.31 | 572.21 | 0.045 | watch_only | none |
| SPY | market_regime | 753.55 |  | 752.184 | 0.1816 | 753.51 | 751.13 | 0.0398 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 224.61 |  | 222.7764 | 0.8231 | 222.19 | 218.09 | 0.1692 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.55 |  | 752.184 | 0.1816 | 753.51 | 751.13 | 0.0398 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 297.11 |  | 296.4179 | 0.2335 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 329.315 |  | 328.8084 | 0.1541 | 328.98 | 326.885 | 0.0152 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.55 |  | 752.184 | 0.1816 | 753.51 | 751.13 | 0.0398 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.11 |  | 296.4179 | 0.2335 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 329.315 |  | 328.8084 | 0.1541 | 328.98 | 326.885 | 0.0152 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 539.745 |  | 538.2822 | 0.2718 | 543.4 | 535.47 | 0.1019 | watch_only | none |
| 5 | QQQ | market_regime | 711.545 |  | 710.4188 | 0.1585 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| 6 | NVDA | ai_accelerator | 208.475 |  | 208.4461 | 0.0139 | 211.03 | 207.49 | 0.0144 | watch_only | none |
| 7 | SMH | semiconductor_index | 577.37 |  | 576.1842 | 0.2058 | 580.31 | 572.21 | 0.045 | watch_only | none |
| 8 | GOOGL | cloud_ai_capex | 371.9 |  | 371.329 | 0.1538 | 375.18 | 369.2 | 0.0699 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 255.015 |  | 254.6777 | 0.1324 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 10 | AMD | ai_accelerator | 513.03 |  | 512.5278 | 0.098 | 518.33 | 507.62 | 0.2183 | watch_only | none |
| 11 | ENTG | semiconductor_materials | 136.12 |  | 135.8665 | 0.1866 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 224.61 |  | 222.7764 | 0.8231 | 222.19 | 218.09 | 0.1692 | buy_precheck_manual_confirm | none |
| 13 | SNDK | memory_hbm_storage | 1507 |  | 1503.2688 | 0.2482 | 1549.47 | 1482.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AMKR | semiconductor_test_packaging | 64.89 |  | 64.8631 | 0.0415 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | LRCX | semiconductor_equipment | 329.985 |  | 328.0215 | 0.5986 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TSM | foundry | 411.49 |  | 410.5325 | 0.2332 | 414.385 | 406.61 | 1.446 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 476.17 |  | 472.9202 | 0.6872 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 141.41 |  | 140.3682 | 0.7422 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 634.455 |  | 633.048 | 0.2223 | 640.25 | 631.005 | 1.5115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ETN | data_center_power_cooling | 404.93 |  | 402.381 | 0.6335 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 224.61 |  | 222.7764 | 0.8231 | 222.19 | 218.09 | 0.1692 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.55 |  | 752.184 | 0.1816 | 753.51 | 751.13 | 0.0398 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 297.11 |  | 296.4179 | 0.2335 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 329.315 |  | 328.8084 | 0.1541 | 328.98 | 326.885 | 0.0152 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1827.18 |  | 1827.6767 | -0.0272 | 1823.13 | 1796.26 | 0.7416 | below_vwap | below_vwap,spread_too_wide |
| 6 | TT | data_center_power_cooling | 476.17 |  | 472.9202 | 0.6872 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | JCI | data_center_power_cooling | 141.41 |  | 140.3682 | 0.7422 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 1043.22 |  | 1029.146 | 1.3675 | 1035.07 | 1021.09 | 4.4986 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | AMAT | semiconductor_equipment | 580.7 |  | 574.8831 | 1.0118 | 572.69 | 562.32 | 0.8869 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | LRCX | semiconductor_equipment | 329.985 |  | 328.0215 | 0.5986 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | COHU | semiconductor_test_packaging | 53.78 |  | 52.4034 | 2.627 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SOXX | semiconductor_index | 539.745 |  | 538.2822 | 0.2718 | 543.4 | 535.47 | 0.1019 | watch_only | none |
| 13 | QQQ | market_regime | 711.545 |  | 710.4188 | 0.1585 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| 14 | NVDA | ai_accelerator | 208.475 |  | 208.4461 | 0.0139 | 211.03 | 207.49 | 0.0144 | watch_only | none |
| 15 | AMD | ai_accelerator | 513.03 |  | 512.5278 | 0.098 | 518.33 | 507.62 | 0.2183 | watch_only | none |
| 16 | SMH | semiconductor_index | 577.37 |  | 576.1842 | 0.2058 | 580.31 | 572.21 | 0.045 | watch_only | none |
| 17 | GOOGL | cloud_ai_capex | 371.9 |  | 371.329 | 0.1538 | 375.18 | 369.2 | 0.0699 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 255.015 |  | 254.6777 | 0.1324 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 72.485 |  | 72.148 | 0.4671 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| 20 | ANET | ai_networking_optical | 165.64 |  | 166.5322 | -0.5357 | 169.91 | 165.6 | 2.7228 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.545 |  | 710.4188 | 0.1585 | 713.55 | 708.25 | 0.0098 | watch_only | none |
| TQQQ | leveraged_tool | 72.485 |  | 72.148 | 0.4671 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| NVDA | ai_accelerator | 208.475 |  | 208.4461 | 0.0139 | 211.03 | 207.49 | 0.0144 | watch_only | none |
| MSFT | cloud_ai_capex | 394.87 |  | 394.9519 | -0.0207 | 398.69 | 392.2 | 0.1444 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 329.315 |  | 328.8084 | 0.1541 | 328.98 | 326.885 | 0.0152 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.9 |  | 371.329 | 0.1538 | 375.18 | 369.2 | 0.0699 | watch_only | none |
| AMD | ai_accelerator | 513.03 |  | 512.5278 | 0.098 | 518.33 | 507.62 | 0.2183 | watch_only | none |
| TSM | foundry | 411.49 |  | 410.5325 | 0.2332 | 414.385 | 406.61 | 1.446 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 539.745 |  | 538.2822 | 0.2718 | 543.4 | 535.47 | 0.1019 | watch_only | none |
| SMH | semiconductor_index | 577.37 |  | 576.1842 | 0.2058 | 580.31 | 572.21 | 0.045 | watch_only | none |
| AVGO | custom_silicon_networking | 383.68 |  | 382.0183 | 0.435 | 386.58 | 378.53 | 4.1363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 870.79 |  | 867.4187 | 0.3887 | 887.1 | 866.765 | 1.0048 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 194.73 |  | 195.5338 | -0.4111 | 201.61 | 194.19 | 2.0798 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 407.19 |  | 405.232 | 0.4832 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.61 |  | 46.8839 | -0.5842 | 47.65 | 46.165 | 0.0429 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.75 |  | 25.9534 | -0.7836 | 26.71 | 25.74 | 0.0777 | below_vwap | below_vwap |
| SPY | market_regime | 753.55 |  | 752.184 | 0.1816 | 753.51 | 751.13 | 0.0398 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.11 |  | 296.4179 | 0.2335 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.17 |  | 127.5683 | -0.3123 | 131.36 | 126.665 | 3.1454 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.43 |  | 74.2446 | 0.2497 | 75.54 | 73.985 | 2.4184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 297.495 |  | 296.4505 | 0.3523 | 300.385 | 293.64 | 4.4639 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 404.93 |  | 402.381 | 0.6335 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.455 |  | 633.048 | 0.2223 | 640.25 | 631.005 | 1.5115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1043.22 |  | 1029.146 | 1.3675 | 1035.07 | 1021.09 | 4.4986 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.17 |  | 472.9202 | 0.6872 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.41 |  | 140.3682 | 0.7422 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.64 |  | 166.5322 | -0.5357 | 169.91 | 165.6 | 2.7228 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 285.08 |  | 285.3447 | -0.0928 | 288.48 | 280.67 | 3.613 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 722.03 |  | 723.4288 | -0.1934 | 737.175 | 720.21 | 3.9721 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.8 |  | 401.2058 | -1.3474 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 104.02 |  | 104.0235 | -0.0034 | 106.975 | 102.85 | 4.0665 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 332.48 |  | 329.6731 | 0.8514 | 337.59 | 326.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1827.18 |  | 1827.6767 | -0.0272 | 1823.13 | 1796.26 | 0.7416 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 580.7 |  | 574.8831 | 1.0118 | 572.69 | 562.32 | 0.8869 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 329.985 |  | 328.0215 | 0.5986 | 328.96 | 324.11 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 224.61 |  | 222.7764 | 0.8231 | 222.19 | 218.09 | 0.1692 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 331.64 |  | 328.0203 | 1.1035 | 332.49 | 326.685 | 0.3739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 294.97 |  | 289.902 | 1.7482 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.89 |  | 64.8631 | 0.0415 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.78 |  | 52.4034 | 2.627 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.12 |  | 135.8665 | 0.1866 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 511.71 |  | 513.2125 | -0.2928 | 515.825 | 512.23 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 291.58 |  | 291.3512 | 0.0785 | 293.89 | 291.35 | 3.92 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 27.5 |  | 27.5156 | -0.0568 | 28.05 | 27.6 | 0.1091 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 36.18 |  | 36.4802 | -0.8228 | 37.365 | 36.4 | 0.1106 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.61 |  | 21.6889 | -0.364 | 22.18 | 21.78 | 0.4165 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SNDK | memory_hbm_storage | 1507 |  | 1503.2688 | 0.2482 | 1549.47 | 1482.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 485.79 |  | 483.5543 | 0.4623 | 498.04 | 480.14 | 1.2207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 788.14 |  | 776.6783 | 1.4757 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 255.015 |  | 254.6777 | 0.1324 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| META | cloud_ai_capex | 674.8 |  | 672.3677 | 0.3617 | 680.09 | 667.1 | 1.3234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 258.55 |  | 260.1543 | -0.6167 | 265.96 | 258.1 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 162.85 |  | 164.8892 | -1.2367 | 168.11 | 162.41 | 1.4615 | below_vwap | below_vwap,spread_too_wide |
