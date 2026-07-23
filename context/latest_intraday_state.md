# Intraday State

- Generated at: `2026-07-24T00:52:16+08:00`
- Market time ET: `2026-07-23T12:52:17-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 13, 'watch_only': 6, 'spread_too_wide_or_missing': 13, 'price_stale_or_missing': 3, 'below_vwap': 20, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.72 |  | 693.1552 | -0.0628 | 698.65 | 693.24 | 0.0188 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.62 |  | 551.0348 | -0.0753 | 557.38 | 545.965 | 0.0745 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.84 |  | 581.2277 | -0.0667 | 585.98 | 576.635 | 0.0758 | below_vwap | below_vwap |
| SPY | market_regime | 738.09 |  | 738.8296 | -0.1001 | 742.515 | 738.54 | 0.0108 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.14 |  | 31.5811 | 1.7696 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1805.35 |  | 1804.0259 | 0.0734 | 1806.11 | 1780.9 | 0.0582 | watch_only | none |
| 2 | NVDA | ai_accelerator | 209.67 |  | 208.4075 | 0.6058 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 3 | MU | memory_hbm_storage | 995.67 |  | 990.7529 | 0.4963 | 999.04 | 964.86 | 0.0763 | watch_only | none |
| 4 | GEV | data_center_power_cooling | 1019.5 |  | 1011.8315 | 0.7579 | 1023.33 | 979.08 | 0.1726 | watch_only | none |
| 5 | TT | data_center_power_cooling | 477.41 |  | 476.7565 | 0.1371 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | COHU | semiconductor_test_packaging | 54.65 |  | 54.6081 | 0.0768 | 55.76 | 53.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TSM | foundry | 417.59 |  | 416.6549 | 0.2244 | 420.72 | 412.69 | 0.5053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | CIEN | ai_networking_optical | 408.77 |  | 408.1975 | 0.1403 | 408.58 | 397.9 | 4.4377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ARM | ai_accelerator | 281.59 |  | 279.3215 | 0.8122 | 283 | 276.24 | 0.2166 | watch_only | none |
| 10 | ANET | ai_networking_optical | 177.19 |  | 176.7085 | 0.2725 | 177.84 | 173.19 | 2.2575 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | KLAC | semiconductor_equipment | 216.04 |  | 215.7145 | 0.1509 | 217.88 | 212.99 | 2.8374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | HPE | ai_server_oem | 48.42 |  | 48.3581 | 0.1281 | 48.88 | 47.635 | 1.4663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ALAB | ai_networking_optical | 329.12 |  | 327.8072 | 0.4005 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | DELL | ai_server_oem | 444.1 |  | 444.098 | 0.0004 | 450.07 | 438.55 | 1.7766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CORZ | high_beta_ai_infrastructure | 24.135 |  | 24.0464 | 0.3685 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| 16 | STX | memory_hbm_storage | 927.43 |  | 924.7023 | 0.295 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SMCI | ai_server_oem | 32.14 |  | 31.5811 | 1.7696 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |
| 18 | TER | semiconductor_test_packaging | 373.79 |  | 372.0123 | 0.4779 | 376.78 | 363.37 | 4.4249 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ENTG | semiconductor_materials | 135.42 |  | 135.4058 | 0.0105 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 20 | SMH | semiconductor_index | 580.84 |  | 581.2277 | -0.0667 | 585.98 | 576.635 | 0.0758 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 32.14 |  | 31.5811 | 1.7696 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |
| 2 | CIEN | ai_networking_optical | 408.77 |  | 408.1975 | 0.1403 | 408.58 | 397.9 | 4.4377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | SNDK | memory_hbm_storage | 1680.57 |  | 1636.7493 | 2.6773 | 1651.355 | 1560 | 3.5542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | NVDA | ai_accelerator | 209.67 |  | 208.4075 | 0.6058 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 5 | MU | memory_hbm_storage | 995.67 |  | 990.7529 | 0.4963 | 999.04 | 964.86 | 0.0763 | watch_only | none |
| 6 | ASML | semiconductor_equipment | 1805.35 |  | 1804.0259 | 0.0734 | 1806.11 | 1780.9 | 0.0582 | watch_only | none |
| 7 | GEV | data_center_power_cooling | 1019.5 |  | 1011.8315 | 0.7579 | 1023.33 | 979.08 | 0.1726 | watch_only | none |
| 8 | ARM | ai_accelerator | 281.59 |  | 279.3215 | 0.8122 | 283 | 276.24 | 0.2166 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 24.135 |  | 24.0464 | 0.3685 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| 10 | SMH | semiconductor_index | 580.84 |  | 581.2277 | -0.0667 | 585.98 | 576.635 | 0.0758 | below_vwap | below_vwap |
| 11 | SOXX | semiconductor_index | 550.62 |  | 551.0348 | -0.0753 | 557.38 | 545.965 | 0.0745 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 390.745 |  | 392.6637 | -0.4886 | 397.34 | 390.54 | 1.5279 | below_vwap | below_vwap,spread_too_wide |
| 13 | AMAT | semiconductor_equipment | 565.74 |  | 566.4132 | -0.1189 | 566.18 | 548.47 | 4.2475 | below_vwap | below_vwap,spread_too_wide |
| 14 | JCI | data_center_power_cooling | 143.775 |  | 143.9571 | -0.1265 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 648.5 |  | 652.2987 | -0.5823 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | VRT | data_center_power_cooling | 304.51 |  | 306.3886 | -0.6131 | 311.13 | 303.96 | 1.1198 | below_vwap | below_vwap,spread_too_wide |
| 17 | ETN | data_center_power_cooling | 412.94 |  | 413.3559 | -0.1006 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | IWM | market_regime | 291.28 |  | 291.6957 | -0.1425 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 19 | LRCX | semiconductor_equipment | 320.7 |  | 321.3693 | -0.2083 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.72 |  | 693.1552 | -0.0628 | 698.65 | 693.24 | 0.0188 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.42 |  | 66.5841 | -0.2464 | 68.245 | 66.7 | 0.0151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.67 |  | 208.4075 | 0.6058 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.14 |  | 382.88 | -0.7156 | 391.71 | 387.245 | 0.8365 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.53 |  | 321.1551 | -0.1946 | 323.25 | 320.82 | 0.0094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.1 |  | 319.5329 | -0.1355 | 324.42 | 320.24 | 0.047 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 538.87 |  | 545.8823 | -1.2846 | 556.12 | 542.33 | 0.7182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 417.59 |  | 416.6549 | 0.2244 | 420.72 | 412.69 | 0.5053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.62 |  | 551.0348 | -0.0753 | 557.38 | 545.965 | 0.0745 | below_vwap | below_vwap |
| SMH | semiconductor_index | 580.84 |  | 581.2277 | -0.0667 | 585.98 | 576.635 | 0.0758 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.745 |  | 392.6637 | -0.4886 | 397.34 | 390.54 | 1.5279 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 995.67 |  | 990.7529 | 0.4963 | 999.04 | 964.86 | 0.0763 | watch_only | none |
| MRVL | custom_silicon_networking | 209.035 |  | 209.9713 | -0.4459 | 213.785 | 207.665 | 0.1052 | below_vwap | below_vwap |
| DELL | ai_server_oem | 444.1 |  | 444.098 | 0.0004 | 450.07 | 438.55 | 1.7766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.42 |  | 48.3581 | 0.1281 | 48.88 | 47.635 | 1.4663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SMCI | ai_server_oem | 32.14 |  | 31.5811 | 1.7696 | 31.52 | 30.23 | 0.0311 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.09 |  | 738.8296 | -0.1001 | 742.515 | 738.54 | 0.0108 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.28 |  | 291.6957 | -0.1425 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.65 |  | 122.1657 | -1.2407 | 124.22 | 122.07 | 0.1492 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.41 |  | 82.922 | -0.6175 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 304.51 |  | 306.3886 | -0.6131 | 311.13 | 303.96 | 1.1198 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.94 |  | 413.3559 | -0.1006 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 648.5 |  | 652.2987 | -0.5823 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1019.5 |  | 1011.8315 | 0.7579 | 1023.33 | 979.08 | 0.1726 | watch_only | none |
| TT | data_center_power_cooling | 477.41 |  | 476.7565 | 0.1371 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.775 |  | 143.9571 | -0.1265 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.19 |  | 176.7085 | 0.2725 | 177.84 | 173.19 | 2.2575 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316.035 |  | 318.3348 | -0.7224 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 849.17 |  | 858.6349 | -1.1023 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 408.77 |  | 408.1975 | 0.1403 | 408.58 | 397.9 | 4.4377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.405 |  | 114.7709 | -1.1901 | 118.01 | 108.505 | 4.6735 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 329.12 |  | 327.8072 | 0.4005 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1805.35 |  | 1804.0259 | 0.0734 | 1806.11 | 1780.9 | 0.0582 | watch_only | none |
| AMAT | semiconductor_equipment | 565.74 |  | 566.4132 | -0.1189 | 566.18 | 548.47 | 4.2475 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.7 |  | 321.3693 | -0.2083 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.04 |  | 215.7145 | 0.1509 | 217.88 | 212.99 | 2.8374 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 373.79 |  | 372.0123 | 0.4779 | 376.78 | 363.37 | 4.4249 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 293.18 |  | 295.3768 | -0.7437 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.57 |  | 65.3218 | 0.38 | 67.455 | 65.81 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.65 |  | 54.6081 | 0.0768 | 55.76 | 53.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.42 |  | 135.4058 | 0.0105 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| MKSI | semiconductor_materials | 345.93 |  | 342.8795 | 0.8897 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.02 |  | 507.6433 | -0.3198 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.83 |  | 296.2555 | -0.4812 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.8 |  | 30.0587 | -0.8606 | 31.13 | 29.12 | 0.1007 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.725 |  | 41.8173 | -2.612 | 43.21 | 40.51 | 0.0491 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.135 |  | 24.0464 | 0.3685 | 24.46 | 23.265 | 0.0414 | watch_only | none |
| SNDK | memory_hbm_storage | 1680.57 |  | 1636.7493 | 2.6773 | 1651.355 | 1560 | 3.5542 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 570.14 |  | 564.0376 | 1.0819 | 576.24 | 556.3 | 1.2681 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 927.43 |  | 924.7023 | 0.295 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234.095 |  | 234.3379 | -0.1036 | 238.285 | 235.71 | 0.0983 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 603.395 |  | 603.7631 | -0.061 | 614.15 | 605.39 | 0.1458 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 281.59 |  | 279.3215 | 0.8122 | 283 | 276.24 | 0.2166 | watch_only | none |
| SKHY | memory_hbm_storage | 173.05 |  | 173.6235 | -0.3303 | 177.88 | 168.18 | 1.0691 | below_vwap | below_vwap,spread_too_wide |
