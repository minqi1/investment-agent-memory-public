# Intraday State

- Generated at: `2026-07-21T22:23:39+08:00`
- Market time ET: `2026-07-21T10:23:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'below_vwap': 19, 'below_opening_15m_low': 13, 'manual_confirm_candidate': 2, 'spread_too_wide_or_missing': 13, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.8 |  | 704.586 | 0.0304 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| SOXX | semiconductor_index | 543.93 |  | 546.0946 | -0.3964 | 550.77 | 545.11 | 0.1158 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.38 |  | 576.9234 | -0.2675 | 582.03 | 576.57 | 0.0348 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 745.92 |  | 745.2794 | 0.086 | 746.6 | 744.3 | 0.0054 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.435 |  | 23.3211 | 0.4884 | 23.32 | 22.79 | 0.128 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 326.18 |  | 324.1765 | 0.618 | 325.59 | 322.63 | 0.0215 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 326.18 |  | 324.1765 | 0.618 | 325.59 | 322.63 | 0.0215 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 704.8 |  | 704.586 | 0.0304 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| 3 | SPY | market_regime | 745.92 |  | 745.2794 | 0.086 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| 4 | IWM | market_regime | 294.35 |  | 293.8265 | 0.1782 | 294.51 | 292.72 | 0.0102 | watch_only | none |
| 5 | HPE | ai_server_oem | 46.235 |  | 46.2207 | 0.031 | 46.685 | 45.835 | 0.1081 | watch_only | none |
| 6 | CORZ | high_beta_ai_infrastructure | 23.435 |  | 23.3211 | 0.4884 | 23.32 | 22.79 | 0.128 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 216.01 |  | 215.8625 | 0.0683 | 220.76 | 214.41 | 0.2315 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 399.875 |  | 399.4743 | 0.1003 | 401.45 | 396.36 | 0.3476 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 41.615 |  | 41.4437 | 0.4132 | 41.65 | 40.435 | 0.0481 | watch_only | none |
| 10 | AMAT | semiconductor_equipment | 563.965 |  | 560.3196 | 0.6506 | 564.91 | 552.71 | 0.3387 | watch_only | none |
| 11 | COHU | semiconductor_test_packaging | 54.44 |  | 54.2793 | 0.296 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | APD | industrial_gases | 299.8 |  | 298.8887 | 0.3049 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | WDC | memory_hbm_storage | 533.65 |  | 532.9803 | 0.1256 | 533.56 | 517.335 | 0.4329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | LITE | ai_networking_optical | 814.78 |  | 812.0008 | 0.3423 | 823.31 | 800.37 | 1.112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | CIEN | ai_networking_optical | 401.69 |  | 400.5219 | 0.2916 | 401.91 | 397.18 | 0.6298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | GOOGL | cloud_ai_capex | 350.07 |  | 349.4972 | 0.1639 | 350.985 | 347.69 | 0.3599 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TER | semiconductor_test_packaging | 365.08 |  | 363.3267 | 0.4826 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ALAB | ai_networking_optical | 325.5 |  | 324.3109 | 0.3666 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | COHR | ai_networking_optical | 306.71 |  | 305.1164 | 0.5223 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 293 |  | 292.9511 | 0.0167 | 296.68 | 291.36 | 1.785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | CORZ | high_beta_ai_infrastructure | 23.435 |  | 23.3211 | 0.4884 | 23.32 | 22.79 | 0.128 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 326.18 |  | 324.1765 | 0.618 | 325.59 | 322.63 | 0.0215 | buy_precheck_manual_confirm | none |
| 3 | ARM | ai_accelerator | 286.55 |  | 282.1294 | 1.5669 | 286.39 | 275.86 | 3.3118 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | WDC | memory_hbm_storage | 533.65 |  | 532.9803 | 0.1256 | 533.56 | 517.335 | 0.4329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | QQQ | market_regime | 704.8 |  | 704.586 | 0.0304 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| 6 | SPY | market_regime | 745.92 |  | 745.2794 | 0.086 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| 7 | AMAT | semiconductor_equipment | 563.965 |  | 560.3196 | 0.6506 | 564.91 | 552.71 | 0.3387 | watch_only | none |
| 8 | AAOI | ai_networking_optical | 111.66 |  | 110.0369 | 1.4751 | 109.39 | 107.58 | 4.4241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | IWM | market_regime | 294.35 |  | 293.8265 | 0.1782 | 294.51 | 292.72 | 0.0102 | watch_only | none |
| 10 | KLAC | semiconductor_equipment | 216.01 |  | 215.8625 | 0.0683 | 220.76 | 214.41 | 0.2315 | watch_only | none |
| 11 | HPE | ai_server_oem | 46.235 |  | 46.2207 | 0.031 | 46.685 | 45.835 | 0.1081 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 399.875 |  | 399.4743 | 0.1003 | 401.45 | 396.36 | 0.3476 | watch_only | none |
| 13 | IREN | high_beta_ai_infrastructure | 41.615 |  | 41.4437 | 0.4132 | 41.65 | 40.435 | 0.0481 | watch_only | none |
| 14 | ANET | ai_networking_optical | 174.405 |  | 174.8958 | -0.2806 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TSM | foundry | 416.115 |  | 416.3636 | -0.0597 | 418.76 | 415.025 | 1.0117 | below_vwap | below_vwap,spread_too_wide |
| 16 | AVGO | custom_silicon_networking | 382.56 |  | 383.8111 | -0.326 | 390.11 | 382.13 | 0.2326 | below_vwap | below_vwap |
| 17 | AMD | ai_accelerator | 529.115 |  | 529.2894 | -0.033 | 532.365 | 524.72 | 1.7028 | below_vwap | below_vwap,spread_too_wide |
| 18 | ASML | semiconductor_equipment | 1792.335 |  | 1796.5198 | -0.2329 | 1804.54 | 1786.51 | 0.8341 | below_vwap | below_vwap,spread_too_wide |
| 19 | TT | data_center_power_cooling | 467.05 |  | 469.5231 | -0.5267 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 404.49 |  | 405.539 | -0.2587 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 704.8 |  | 704.586 | 0.0304 | 707.09 | 704.52 | 0.0383 | watch_only | none |
| TQQQ | leveraged_tool | 70.22 |  | 70.2291 | -0.0129 | 70.84 | 70.09 | 0.0285 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 204.985 |  | 206.3292 | -0.6515 | 208.61 | 206.275 | 0.0146 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.875 |  | 399.4743 | 0.1003 | 401.45 | 396.36 | 0.3476 | watch_only | none |
| AAPL | mega_cap_platform | 326.18 |  | 324.1765 | 0.618 | 325.59 | 322.63 | 0.0215 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 350.07 |  | 349.4972 | 0.1639 | 350.985 | 347.69 | 0.3599 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 529.115 |  | 529.2894 | -0.033 | 532.365 | 524.72 | 1.7028 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 416.115 |  | 416.3636 | -0.0597 | 418.76 | 415.025 | 1.0117 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1879277.8872 | -2.3029 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 543.93 |  | 546.0946 | -0.3964 | 550.77 | 545.11 | 0.1158 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 575.38 |  | 576.9234 | -0.2675 | 582.03 | 576.57 | 0.0348 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 382.56 |  | 383.8111 | -0.326 | 390.11 | 382.13 | 0.2326 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 921.6 |  | 931.2316 | -1.0343 | 944.99 | 923 | 1.5734 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 204.965 |  | 206.1221 | -0.5613 | 208.61 | 205.31 | 0.8343 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.63 |  | 402.422 | -0.6938 | 405.78 | 397.185 | 0.7107 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.235 |  | 46.2207 | 0.031 | 46.685 | 45.835 | 0.1081 | watch_only | none |
| SMCI | ai_server_oem | 24.48 |  | 24.5725 | -0.3764 | 24.77 | 24.34 | 0.0408 | below_vwap | below_vwap |
| SPY | market_regime | 745.92 |  | 745.2794 | 0.086 | 746.6 | 744.3 | 0.0054 | watch_only | none |
| IWM | market_regime | 294.35 |  | 293.8265 | 0.1782 | 294.51 | 292.72 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 124.96 |  | 124.9805 | -0.0164 | 126.01 | 122.48 | 0.088 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 76.28 |  | 76.3413 | -0.0803 | 76.615 | 74.55 | 2.4646 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 297.85 |  | 299.5691 | -0.5739 | 305.09 | 299.13 | 0.4062 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 404.49 |  | 405.539 | -0.2587 | 411.01 | 404.21 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635.135 |  | 637.2568 | -0.333 | 645.815 | 635.91 | 4.7864 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1080.98 |  | 1104.6491 | -2.1427 | 1140.63 | 1103.815 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 467.05 |  | 469.5231 | -0.5267 | 475.98 | 467.01 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 139.97 |  | 140.2941 | -0.231 | 142.15 | 140.105 | 0.3072 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ANET | ai_networking_optical | 174.405 |  | 174.8958 | -0.2806 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 306.71 |  | 305.1164 | 0.5223 | 309.72 | 302.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 814.78 |  | 812.0008 | 0.3423 | 823.31 | 800.37 | 1.112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 401.69 |  | 400.5219 | 0.2916 | 401.91 | 397.18 | 0.6298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 111.66 |  | 110.0369 | 1.4751 | 109.39 | 107.58 | 4.4241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 325.5 |  | 324.3109 | 0.3666 | 329.97 | 323.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1792.335 |  | 1796.5198 | -0.2329 | 1804.54 | 1786.51 | 0.8341 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 563.965 |  | 560.3196 | 0.6506 | 564.91 | 552.71 | 0.3387 | watch_only | none |
| LRCX | semiconductor_equipment | 317.13 |  | 318.2206 | -0.3427 | 328.135 | 317.17 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 216.01 |  | 215.8625 | 0.0683 | 220.76 | 214.41 | 0.2315 | watch_only | none |
| TER | semiconductor_test_packaging | 365.08 |  | 363.3267 | 0.4826 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 293 |  | 292.9511 | 0.0167 | 296.68 | 291.36 | 1.785 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 65.14 |  | 65.2465 | -0.1632 | 66.54 | 65 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.2793 | 0.296 | 54.45 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.4 |  | 140.1639 | -0.545 | 142.09 | 139.41 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.73 |  | 337.6271 | -0.5619 | 340.205 | 336.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 507.89 |  | 509.397 | -0.2958 | 512.83 | 507.675 | 1.1262 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 299.8 |  | 298.8887 | 0.3049 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.73 |  | 29.7454 | -0.0518 | 29.735 | 28.785 | 0.1009 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.615 |  | 41.4437 | 0.4132 | 41.65 | 40.435 | 0.0481 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 23.435 |  | 23.3211 | 0.4884 | 23.32 | 22.79 | 0.128 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1503.05 |  | 1517.7418 | -0.968 | 1540.85 | 1490.29 | 1.0332 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 533.65 |  | 532.9803 | 0.1256 | 533.56 | 517.335 | 0.4329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 862.95 |  | 864.0023 | -0.1218 | 866.73 | 845.78 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 247.21 |  | 247.6811 | -0.1902 | 248.915 | 247.32 | 0.0445 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 646.93 |  | 647.2719 | -0.0528 | 655.425 | 643.54 | 1.1732 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 286.55 |  | 282.1294 | 1.5669 | 286.39 | 275.86 | 3.3118 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 164.55 |  | 163.6933 | 0.5233 | 165.88 | 160.77 | 1.2823 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
