# Intraday State

- Generated at: `2026-07-16T02:32:44+08:00`
- Market time ET: `2026-07-15T14:32:45-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 7, 'price_stale_or_missing': 1, 'below_vwap': 2, 'watch_only': 4, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.22 |  | 716.3538 | 0.2605 | 724.31 | 721.08 | 0.0014 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 554.465 |  | 551.43 | 0.5504 | 575.7 | 565.33 | 0.0523 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.83 |  | 587.327 | 0.2559 | 606.85 | 597.81 | 0.0374 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.72 |  | 753.2669 | 0.1929 | 755.54 | 754.215 | 0.0026 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.57 |  | 395.3131 | 0.318 | 391.33 | 387.05 | 0.0857 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.145 |  | 368.8427 | 0.8953 | 364.41 | 357.885 | 0.3466 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.6 |  | 325.6278 | 0.6056 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 133.79 |  | 131.7984 | 1.5111 | 132.925 | 129.92 | 0.1271 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.83 |  | 21.8838 | 4.3237 | 22.36 | 21.94 | 0.0438 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.3 |  | 39.2336 | 2.718 | 40.01 | 38.815 | 0.0496 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.22 |  | 28.28 | 3.3239 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.57 |  | 395.3131 | 0.318 | 391.33 | 387.05 | 0.0857 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.72 |  | 753.2669 | 0.1929 | 755.54 | 754.215 | 0.0026 | watch_only | none |
| 3 | IWM | market_regime | 295.92 |  | 295.6465 | 0.0925 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 327.6 |  | 325.6278 | 0.6056 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 394.12 |  | 392.0025 | 0.5402 | 397.94 | 392.62 | 0.2766 | watch_only | none |
| 6 | ASML | semiconductor_equipment | 1788.65 |  | 1772.3176 | 0.9215 | 1829.9 | 1759.045 | 0.0794 | watch_only | none |
| 7 | ORCL | cloud_ai_capex | 133.79 |  | 131.7984 | 1.5111 | 132.925 | 129.92 | 0.1271 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 372.145 |  | 368.8427 | 0.8953 | 364.41 | 357.885 | 0.3466 | buy_precheck_manual_confirm | none |
| 9 | IREN | high_beta_ai_infrastructure | 40.3 |  | 39.2336 | 2.718 | 40.01 | 38.815 | 0.0496 | buy_precheck_manual_confirm | none |
| 10 | APLD | high_beta_ai_infrastructure | 29.22 |  | 28.28 | 3.3239 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 420.405 |  | 418.9902 | 0.3377 | 428.59 | 422.945 | 0.0309 | below_opening_15m_low | below_opening_15m_low |
| 12 | CORZ | high_beta_ai_infrastructure | 22.83 |  | 21.8838 | 4.3237 | 22.36 | 21.94 | 0.0438 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 588.83 |  | 587.327 | 0.2559 | 606.85 | 597.81 | 0.0374 | below_opening_15m_low | below_opening_15m_low |
| 14 | QQQ | market_regime | 718.22 |  | 716.3538 | 0.2605 | 724.31 | 721.08 | 0.0014 | below_opening_15m_low | below_opening_15m_low |
| 15 | META | cloud_ai_capex | 676.95 |  | 675.5538 | 0.2067 | 664.875 | 657.17 | 0.7696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | HPE | ai_server_oem | 47.035 |  | 46.9275 | 0.2291 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| 17 | NVDA | ai_accelerator | 210.585 |  | 209.2381 | 0.6437 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 18 | LRCX | semiconductor_equipment | 331.93 |  | 331.4567 | 0.1428 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 19 | SOXX | semiconductor_index | 554.465 |  | 551.43 | 0.5504 | 575.7 | 565.33 | 0.0523 | below_opening_15m_low | below_opening_15m_low |
| 20 | AMD | ai_accelerator | 531.22 |  | 527.3973 | 0.7248 | 558.62 | 548.745 | 0.1337 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.57 |  | 395.3131 | 0.318 | 391.33 | 387.05 | 0.0857 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 372.145 |  | 368.8427 | 0.8953 | 364.41 | 357.885 | 0.3466 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.6 |  | 325.6278 | 0.6056 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 133.79 |  | 131.7984 | 1.5111 | 132.925 | 129.92 | 0.1271 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 22.83 |  | 21.8838 | 4.3237 | 22.36 | 21.94 | 0.0438 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 40.3 |  | 39.2336 | 2.718 | 40.01 | 38.815 | 0.0496 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 29.22 |  | 28.28 | 3.3239 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 254.38 |  | 254.4836 | -0.0407 | 252.89 | 249.98 | 0.0354 | below_vwap | below_vwap |
| 9 | AVGO | custom_silicon_networking | 394.12 |  | 392.0025 | 0.5402 | 397.94 | 392.62 | 0.2766 | watch_only | none |
| 10 | META | cloud_ai_capex | 676.95 |  | 675.5538 | 0.2067 | 664.875 | 657.17 | 0.7696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | ASML | semiconductor_equipment | 1788.65 |  | 1772.3176 | 0.9215 | 1829.9 | 1759.045 | 0.0794 | watch_only | none |
| 12 | SPY | market_regime | 754.72 |  | 753.2669 | 0.1929 | 755.54 | 754.215 | 0.0026 | watch_only | none |
| 13 | IWM | market_regime | 295.92 |  | 295.6465 | 0.0925 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 179.53 |  | 175.8347 | 2.1016 | 183.63 | 176.08 | 1.6655 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 210.585 |  | 209.2381 | 0.6437 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| 17 | MU | memory_hbm_storage | 914.05 |  | 910.2653 | 0.4158 | 977.7 | 953.67 | 0.5284 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | CIEN | ai_networking_optical | 426.01 |  | 419.3739 | 1.5824 | 438.14 | 427.54 | 3.7839 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | SOXX | semiconductor_index | 554.465 |  | 551.43 | 0.5504 | 575.7 | 565.33 | 0.0523 | below_opening_15m_low | below_opening_15m_low |
| 20 | ANET | ai_networking_optical | 171.93 |  | 171.8704 | 0.0347 | 186.095 | 178.355 | 2.9896 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 718.22 |  | 716.3538 | 0.2605 | 724.31 | 721.08 | 0.0014 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.56 |  | 74.2073 | 0.4752 | 76.46 | 75.39 | 0.0134 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.585 |  | 209.2381 | 0.6437 | 213.775 | 211.225 | 0.0142 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.57 |  | 395.3131 | 0.318 | 391.33 | 387.05 | 0.0857 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.6 |  | 325.6278 | 0.6056 | 321.14 | 317.4 | 0.0092 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.145 |  | 368.8427 | 0.8953 | 364.41 | 357.885 | 0.3466 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 531.22 |  | 527.3973 | 0.7248 | 558.62 | 548.745 | 0.1337 | below_opening_15m_low | below_opening_15m_low |
| TSM | foundry | 420.405 |  | 418.9902 | 0.3377 | 428.59 | 422.945 | 0.0309 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.465 |  | 551.43 | 0.5504 | 575.7 | 565.33 | 0.0523 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 588.83 |  | 587.327 | 0.2559 | 606.85 | 597.81 | 0.0374 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.12 |  | 392.0025 | 0.5402 | 397.94 | 392.62 | 0.2766 | watch_only | none |
| MU | memory_hbm_storage | 914.05 |  | 910.2653 | 0.4158 | 977.7 | 953.67 | 0.5284 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MRVL | custom_silicon_networking | 208.235 |  | 208.4156 | -0.0866 | 223.02 | 214.85 | 0.1681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 406.29 |  | 407.1871 | -0.2203 | 457.935 | 442.67 | 4.738 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.035 |  | 46.9275 | 0.2291 | 50.2 | 48.995 | 0.0213 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.095 |  | 26.8813 | 0.795 | 28.295 | 27.55 | 0.0369 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 754.72 |  | 753.2669 | 0.1929 | 755.54 | 754.215 | 0.0026 | watch_only | none |
| IWM | market_regime | 295.92 |  | 295.6465 | 0.0925 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 133.79 |  | 131.7984 | 1.5111 | 132.925 | 129.92 | 0.1271 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 78.18 |  | 77.4729 | 0.9128 | 80.585 | 78.73 | 3.8117 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| VRT | data_center_power_cooling | 302.555 |  | 299.2548 | 1.1028 | 309.345 | 304.67 | 0.1256 | below_opening_15m_low | below_opening_15m_low |
| ETN | data_center_power_cooling | 411.11 |  | 408.5524 | 0.626 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 651.415 |  | 645.2078 | 0.9621 | 663.475 | 653.94 | 5.1196 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 1058.98 |  | 1033.6612 | 2.4494 | 1073.34 | 1059.27 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| TT | data_center_power_cooling | 478.66 |  | 478.7308 | -0.0148 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.54 |  | 141.7489 | 0.5581 | 145.99 | 144.625 | 0.2035 | below_opening_15m_low | below_opening_15m_low |
| ANET | ai_networking_optical | 171.93 |  | 171.8704 | 0.0347 | 186.095 | 178.355 | 2.9896 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 295.57 |  | 294.035 | 0.522 | 315.74 | 303.34 | 0.2368 | below_opening_15m_low | below_opening_15m_low |
| LITE | ai_networking_optical | 754.15 |  | 749.0551 | 0.6802 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| CIEN | ai_networking_optical | 426.01 |  | 419.3739 | 1.5824 | 438.14 | 427.54 | 3.7839 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 110.72 |  | 112.2746 | -1.3846 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 350.66 |  | 344.7064 | 1.7272 | 369.23 | 356.615 | 4.5942 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1788.65 |  | 1772.3176 | 0.9215 | 1829.9 | 1759.045 | 0.0794 | watch_only | none |
| AMAT | semiconductor_equipment | 577.29 |  | 577.7408 | -0.078 | 610.62 | 586.86 | 0.1871 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 331.93 |  | 331.4567 | 0.1428 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.67 |  | 222.6637 | 0.4519 | 236.49 | 225.11 | 0.0805 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 340.61 |  | 335.858 | 1.4149 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 306.14 |  | 307.4558 | -0.428 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.92 |  | 66.9364 | 1.4695 | 70.42 | 68.43 | 4.1519 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.75 |  | 54.3578 | 0.7216 | 57.92 | 55.2 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ENTG | semiconductor_materials | 138.16 |  | 137.6925 | 0.3395 | 143.15 | 140.4 | 5.0376 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MKSI | semiconductor_materials | 351.595 |  | 348.7565 | 0.8139 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 515.92 |  | 516.0907 | -0.0331 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.13 |  | 294.5325 | -0.4762 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.22 |  | 28.28 | 3.3239 | 29.055 | 28.28 | 0.1027 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 40.3 |  | 39.2336 | 2.718 | 40.01 | 38.815 | 0.0496 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.83 |  | 21.8838 | 4.3237 | 22.36 | 21.94 | 0.0438 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1648.61 |  | 1576.8885 | 4.5483 | 1726.34 | 1665.91 | 2.1837 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 516.35 |  | 516.5715 | -0.0429 | 568.16 | 542.4 | 0.6023 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 823.04 |  | 817.5877 | 0.6669 | 889.1 | 850.01 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AMZN | cloud_ai_capex | 254.38 |  | 254.4836 | -0.0407 | 252.89 | 249.98 | 0.0354 | below_vwap | below_vwap |
| META | cloud_ai_capex | 676.95 |  | 675.5538 | 0.2067 | 664.875 | 657.17 | 0.7696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 274.65 |  | 275.8135 | -0.4218 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 179.53 |  | 175.8347 | 2.1016 | 183.63 | 176.08 | 1.6655 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
