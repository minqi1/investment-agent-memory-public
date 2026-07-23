# Intraday State

- Generated at: `2026-07-23T21:54:32+08:00`
- Market time ET: `2026-07-23T09:54:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 24, 'watch_only': 5, 'below_opening_15m_low': 1, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 2, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.95 |  | 696.3191 | -0.053 | 698.65 | 693.24 | 0.0747 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 554.71 |  | 552.8589 | 0.3348 | 557.38 | 545.965 | 0.1028 | watch_only | none |
| SMH | semiconductor_index | 584 |  | 581.8982 | 0.3612 | 585.98 | 576.635 | 0.101 | watch_only | none |
| SPY | market_regime | 740.27 |  | 740.7889 | -0.07 | 742.515 | 738.54 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.53 |  | 31.0974 | 1.3912 | 31.52 | 30.23 | 0.2854 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 554.71 |  | 552.8589 | 0.3348 | 557.38 | 545.965 | 0.1028 | watch_only | none |
| 2 | NVDA | ai_accelerator | 209.68 |  | 209.3842 | 0.1413 | 210.85 | 208.49 | 0.0286 | watch_only | none |
| 3 | AVGO | custom_silicon_networking | 394.75 |  | 394.0969 | 0.1657 | 397.34 | 390.54 | 0.1343 | watch_only | none |
| 4 | SMH | semiconductor_index | 584 |  | 581.8982 | 0.3612 | 585.98 | 576.635 | 0.101 | watch_only | none |
| 5 | SMCI | ai_server_oem | 31.53 |  | 31.0974 | 1.3912 | 31.52 | 30.23 | 0.2854 | buy_precheck_manual_confirm | none |
| 6 | ETN | data_center_power_cooling | 413.54 |  | 412.6086 | 0.2257 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | MKSI | semiconductor_materials | 345 |  | 344.4145 | 0.17 | 347.59 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ASML | semiconductor_equipment | 1797.895 |  | 1796.8494 | 0.0582 | 1806.11 | 1780.9 | 0.703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | PWR | data_center_power_cooling | 654.27 |  | 653.0742 | 0.1831 | 656.38 | 642.37 | 4.4217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | VRT | data_center_power_cooling | 309.27 |  | 307.5539 | 0.558 | 311.13 | 303.96 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ARM | ai_accelerator | 281.67 |  | 279.6696 | 0.7153 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | HPE | ai_server_oem | 48.6 |  | 48.4951 | 0.2163 | 48.88 | 47.635 | 4.4239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | META | cloud_ai_capex | 610.96 |  | 610.2826 | 0.111 | 614.15 | 605.39 | 1.1588 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 124.08 |  | 123.2923 | 0.6389 | 124.22 | 122.07 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | IREN | high_beta_ai_infrastructure | 42.31 |  | 42.3037 | 0.0148 | 43.21 | 40.51 | 4.3725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ANET | ai_networking_optical | 177.955 |  | 176.921 | 0.5845 | 177.84 | 173.19 | 0.9722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TSM | foundry | 419.17 |  | 417.6566 | 0.3623 | 420.72 | 412.69 | 1.67 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CORZ | high_beta_ai_infrastructure | 24.235 |  | 24.058 | 0.7359 | 24.46 | 23.265 | 0.2476 | watch_only | none |
| 19 | AMD | ai_accelerator | 553.96 |  | 549.9813 | 0.7234 | 556.12 | 542.33 | 0.4892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CIEN | ai_networking_optical | 406.25 |  | 404.2272 | 0.5004 | 408.58 | 397.9 | 3.6135 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.53 |  | 31.0974 | 1.3912 | 31.52 | 30.23 | 0.2854 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 177.955 |  | 176.921 | 0.5845 | 177.84 | 173.19 | 0.9722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | COHR | ai_networking_optical | 322.475 |  | 318.0941 | 1.3772 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LITE | ai_networking_optical | 883.19 |  | 868.74 | 1.6633 | 880.26 | 833 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ALAB | ai_networking_optical | 336.81 |  | 333.2572 | 1.0661 | 336.81 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | SMH | semiconductor_index | 584 |  | 581.8982 | 0.3612 | 585.98 | 576.635 | 0.101 | watch_only | none |
| 7 | SOXX | semiconductor_index | 554.71 |  | 552.8589 | 0.3348 | 557.38 | 545.965 | 0.1028 | watch_only | none |
| 8 | NVDA | ai_accelerator | 209.68 |  | 209.3842 | 0.1413 | 210.85 | 208.49 | 0.0286 | watch_only | none |
| 9 | AVGO | custom_silicon_networking | 394.75 |  | 394.0969 | 0.1657 | 397.34 | 390.54 | 0.1343 | watch_only | none |
| 10 | CORZ | high_beta_ai_infrastructure | 24.235 |  | 24.058 | 0.7359 | 24.46 | 23.265 | 0.2476 | watch_only | none |
| 11 | MU | memory_hbm_storage | 985.51 |  | 985.8661 | -0.0361 | 999.04 | 964.86 | 0.2527 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 560.25 |  | 560.6722 | -0.0753 | 566.18 | 548.47 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | TT | data_center_power_cooling | 475.92 |  | 476.8204 | -0.1888 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 143.6 |  | 144.0403 | -0.3057 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 215.02 |  | 216.1315 | -0.5143 | 217.88 | 212.99 | 2.7858 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.73 |  | 291.8892 | -0.0545 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 318.85 |  | 320.4076 | -0.4861 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | QQQ | market_regime | 695.95 |  | 696.3191 | -0.053 | 698.65 | 693.24 | 0.0747 | below_vwap | below_vwap |
| 19 | SPY | market_regime | 740.27 |  | 740.7889 | -0.07 | 742.515 | 738.54 | 0.0054 | below_vwap | below_vwap |
| 20 | WDC | memory_hbm_storage | 564.98 |  | 570.0654 | -0.8921 | 576.24 | 556.3 | 0.1044 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.95 |  | 696.3191 | -0.053 | 698.65 | 693.24 | 0.0747 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.45 |  | 67.476 | -0.0386 | 68.245 | 66.7 | 0.0297 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 209.68 |  | 209.3842 | 0.1413 | 210.85 | 208.49 | 0.0286 | watch_only | none |
| MSFT | cloud_ai_capex | 388.43 |  | 389.0464 | -0.1584 | 391.71 | 387.245 | 0.1751 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 319.365 |  | 321.3003 | -0.6023 | 323.25 | 320.82 | 0.2035 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 320.995 |  | 321.1787 | -0.0572 | 324.42 | 320.24 | 0.4175 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 553.96 |  | 549.9813 | 0.7234 | 556.12 | 542.33 | 0.4892 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 419.17 |  | 417.6566 | 0.3623 | 420.72 | 412.69 | 1.67 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.71 |  | 552.8589 | 0.3348 | 557.38 | 545.965 | 0.1028 | watch_only | none |
| SMH | semiconductor_index | 584 |  | 581.8982 | 0.3612 | 585.98 | 576.635 | 0.101 | watch_only | none |
| AVGO | custom_silicon_networking | 394.75 |  | 394.0969 | 0.1657 | 397.34 | 390.54 | 0.1343 | watch_only | none |
| MU | memory_hbm_storage | 985.51 |  | 985.8661 | -0.0361 | 999.04 | 964.86 | 0.2527 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 212.89 |  | 211.5941 | 0.6125 | 213.785 | 207.665 | 4.2886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.235 |  | 443.7675 | -0.12 | 450.07 | 438.55 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.6 |  | 48.4951 | 0.2163 | 48.88 | 47.635 | 4.4239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SMCI | ai_server_oem | 31.53 |  | 31.0974 | 1.3912 | 31.52 | 30.23 | 0.2854 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 740.27 |  | 740.7889 | -0.07 | 742.515 | 738.54 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 291.73 |  | 291.8892 | -0.0545 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.08 |  | 123.2923 | 0.6389 | 124.22 | 122.07 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 82.79 |  | 83.084 | -0.3539 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 309.27 |  | 307.5539 | 0.558 | 311.13 | 303.96 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 413.54 |  | 412.6086 | 0.2257 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 654.27 |  | 653.0742 | 0.1831 | 656.38 | 642.37 | 4.4217 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1018.94 |  | 1004.2682 | 1.4609 | 1023.33 | 979.08 | 3.5586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.92 |  | 476.8204 | -0.1888 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.6 |  | 144.0403 | -0.3057 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 177.955 |  | 176.921 | 0.5845 | 177.84 | 173.19 | 0.9722 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 322.475 |  | 318.0941 | 1.3772 | 320.13 | 307.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 883.19 |  | 868.74 | 1.6633 | 880.26 | 833 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 406.25 |  | 404.2272 | 0.5004 | 408.58 | 397.9 | 3.6135 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 117.45 |  | 115.4617 | 1.7221 | 118.01 | 108.505 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 336.81 |  | 333.2572 | 1.0661 | 336.81 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1797.895 |  | 1796.8494 | 0.0582 | 1806.11 | 1780.9 | 0.703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 560.25 |  | 560.6722 | -0.0753 | 566.18 | 548.47 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 318.85 |  | 320.4076 | -0.4861 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.02 |  | 216.1315 | -0.5143 | 217.88 | 212.99 | 2.7858 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 371.51 |  | 372.4165 | -0.2434 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 298.22 |  | 298.7117 | -0.1646 | 301.235 | 293.685 | 0.8685 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 66.385 |  | 66.5905 | -0.3086 | 67.185 | 65.81 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.195 |  | 54.8181 | 0.6875 | 55.195 | 54.445 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 136.19 |  | 136.9436 | -0.5503 | 137.81 | 135.66 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345 |  | 344.4145 | 0.17 | 347.59 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 506.41 |  | 506.9648 | -0.1094 | 510.71 | 502.72 | 0.0889 | below_vwap | below_vwap |
| APD | industrial_gases | 296.85 |  | 297.5261 | -0.2272 | 299.26 | 295.795 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.5 |  | 30.3644 | 0.4467 | 31.13 | 29.12 | 4.918 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 42.31 |  | 42.3037 | 0.0148 | 43.21 | 40.51 | 4.3725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CORZ | high_beta_ai_infrastructure | 24.235 |  | 24.058 | 0.7359 | 24.46 | 23.265 | 0.2476 | watch_only | none |
| SNDK | memory_hbm_storage | 1632.87 |  | 1618.0301 | 0.9172 | 1651.355 | 1560 | 0.5953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 564.98 |  | 570.0654 | -0.8921 | 576.24 | 556.3 | 0.1044 | below_vwap | below_vwap |
| STX | memory_hbm_storage | 924.14 |  | 926.1642 | -0.2186 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 236.305 |  | 236.9848 | -0.2868 | 238.285 | 235.71 | 0.0254 | below_vwap | below_vwap |
| META | cloud_ai_capex | 610.96 |  | 610.2826 | 0.111 | 614.15 | 605.39 | 1.1588 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 281.67 |  | 279.6696 | 0.7153 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 174.905 |  | 173.8761 | 0.5918 | 177.88 | 168.18 | 1.4293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
