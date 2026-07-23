# Intraday State

- Generated at: `2026-07-23T23:29:04+08:00`
- Market time ET: `2026-07-23T11:29:04-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 24, 'watch_only': 1, 'price_stale_or_missing': 1, 'below_vwap': 29, 'spread_too_wide_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 688.55 |  | 693.9604 | -0.7796 | 698.65 | 693.24 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545 |  | 552.375 | -1.3351 | 557.38 | 545.965 | 0.0734 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 574.76 |  | 581.7718 | -1.2053 | 585.98 | 576.635 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 736.12 |  | 739.4146 | -0.4456 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.52 |  | 321.2921 | 0.0709 | 323.25 | 320.82 | 0.0156 | watch_only | none |
| 2 | LIN | industrial_gases | 508.52 |  | 507.6987 | 0.1618 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MU | memory_hbm_storage | 980.43 |  | 989.0316 | -0.8697 | 999.04 | 964.86 | 0.0806 | below_vwap | below_vwap |
| 4 | KLAC | semiconductor_equipment | 214.28 |  | 216.0076 | -0.7998 | 217.88 | 212.99 | 0.1073 | below_vwap | below_vwap |
| 5 | IWM | market_regime | 290.53 |  | 291.8209 | -0.4424 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 6 | SMCI | ai_server_oem | 30.89 |  | 31.4843 | -1.8877 | 31.52 | 30.23 | 0.0647 | below_vwap | below_vwap |
| 7 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 8 | IREN | high_beta_ai_infrastructure | 40.79 |  | 42.0929 | -3.0954 | 43.21 | 40.51 | 0.049 | below_vwap | below_vwap |
| 9 | TT | data_center_power_cooling | 474.13 |  | 476.6586 | -0.5305 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | JCI | data_center_power_cooling | 143.01 |  | 143.9996 | -0.6872 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | PWR | data_center_power_cooling | 644.9 |  | 653.9529 | -1.3843 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 411.22 |  | 413.4229 | -0.5328 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 317.72 |  | 321.6766 | -1.23 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | COHR | ai_networking_optical | 311.98 |  | 319.2215 | -2.2685 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 367.83 |  | 372.3782 | -1.2214 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 54.09 |  | 55.0016 | -1.6574 | 55.76 | 54.09 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | CRWV | gpu_cloud_ai_factory | 81.035 |  | 83.1671 | -2.5636 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AAOI | ai_networking_optical | 111.225 |  | 115.2436 | -3.4871 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ASML | semiconductor_equipment | 1791.42 |  | 1805.6778 | -0.7896 | 1806.11 | 1780.9 | 0.3896 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 561.59 |  | 566.8707 | -0.9316 | 566.18 | 548.47 | 1.4263 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 321.52 |  | 321.2921 | 0.0709 | 323.25 | 320.82 | 0.0156 | watch_only | none |
| 2 | MU | memory_hbm_storage | 980.43 |  | 989.0316 | -0.8697 | 999.04 | 964.86 | 0.0806 | below_vwap | below_vwap |
| 3 | ASML | semiconductor_equipment | 1791.42 |  | 1805.6778 | -0.7896 | 1806.11 | 1780.9 | 0.3896 | below_vwap | below_vwap,spread_too_wide |
| 4 | AMAT | semiconductor_equipment | 561.59 |  | 566.8707 | -0.9316 | 566.18 | 548.47 | 1.4263 | below_vwap | below_vwap,spread_too_wide |
| 5 | TT | data_center_power_cooling | 474.13 |  | 476.6586 | -0.5305 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | ANET | ai_networking_optical | 174.19 |  | 176.8617 | -1.5106 | 177.84 | 173.19 | 3.4904 | below_vwap | below_vwap,spread_too_wide |
| 7 | JCI | data_center_power_cooling | 143.01 |  | 143.9996 | -0.6872 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | PWR | data_center_power_cooling | 644.9 |  | 653.9529 | -1.3843 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | KLAC | semiconductor_equipment | 214.28 |  | 216.0076 | -0.7998 | 217.88 | 212.99 | 0.1073 | below_vwap | below_vwap |
| 10 | ETN | data_center_power_cooling | 411.22 |  | 413.4229 | -0.5328 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | GEV | data_center_power_cooling | 1001.78 |  | 1011.6075 | -0.9715 | 1023.33 | 979.08 | 2.261 | below_vwap | below_vwap,spread_too_wide |
| 12 | IWM | market_regime | 290.53 |  | 291.8209 | -0.4424 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 317.72 |  | 321.6766 | -1.23 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | WDC | memory_hbm_storage | 559.89 |  | 562.8184 | -0.5203 | 576.24 | 556.3 | 4.2294 | below_vwap | below_vwap,spread_too_wide |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | APD | industrial_gases | 296.59 |  | 296.8765 | -0.0965 | 299.26 | 295.795 | 4.9833 | below_vwap | below_vwap,spread_too_wide |
| 17 | HPE | ai_server_oem | 47.98 |  | 48.5017 | -1.0757 | 48.88 | 47.635 | 4.2726 | below_vwap | below_vwap,spread_too_wide |
| 18 | COHR | ai_networking_optical | 311.98 |  | 319.2215 | -2.2685 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | CIEN | ai_networking_optical | 403.29 |  | 409.1795 | -1.4393 | 408.58 | 397.9 | 0.605 | below_vwap | below_vwap,spread_too_wide |
| 20 | TER | semiconductor_test_packaging | 367.83 |  | 372.3782 | -1.2214 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 688.55 |  | 693.9604 | -0.7796 | 698.65 | 693.24 | 0.0116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.205 |  | 66.7597 | -2.3288 | 68.245 | 66.7 | 0.0153 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.32 |  | 208.3883 | -0.9925 | 210.85 | 208.49 | 0.5816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 378.685 |  | 384.1107 | -1.4125 | 391.71 | 387.245 | 0.1716 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.52 |  | 321.2921 | 0.0709 | 323.25 | 320.82 | 0.0156 | watch_only | none |
| GOOGL | cloud_ai_capex | 316.07 |  | 319.5874 | -1.1006 | 324.42 | 320.24 | 1.2307 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 538.105 |  | 548.1974 | -1.841 | 556.12 | 542.33 | 2.1018 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 412.65 |  | 417.272 | -1.1077 | 420.72 | 412.69 | 0.1018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545 |  | 552.375 | -1.3351 | 557.38 | 545.965 | 0.0734 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 574.76 |  | 581.7718 | -1.2053 | 585.98 | 576.635 | 0.0661 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 387.96 |  | 393.464 | -1.3989 | 397.34 | 390.54 | 0.6959 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 980.43 |  | 989.0316 | -0.8697 | 999.04 | 964.86 | 0.0806 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 205.63 |  | 210.5874 | -2.3541 | 213.785 | 207.665 | 1.989 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 440.13 |  | 444.5801 | -1.001 | 450.07 | 438.55 | 0.4976 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.98 |  | 48.5017 | -1.0757 | 48.88 | 47.635 | 4.2726 | below_vwap | below_vwap,spread_too_wide |
| SMCI | ai_server_oem | 30.89 |  | 31.4843 | -1.8877 | 31.52 | 30.23 | 0.0647 | below_vwap | below_vwap |
| SPY | market_regime | 736.12 |  | 739.4146 | -0.4456 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 290.53 |  | 291.8209 | -0.4424 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.96 |  | 122.847 | -2.3501 | 124.22 | 122.07 | 0.1751 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 81.035 |  | 83.1671 | -2.5636 | 84.415 | 80.64 |  | below_vwap | below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 301.29 |  | 307.8402 | -2.1278 | 311.13 | 303.96 | 0.5974 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 411.22 |  | 413.4229 | -0.5328 | 415.53 | 406.545 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 644.9 |  | 653.9529 | -1.3843 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1001.78 |  | 1011.6075 | -0.9715 | 1023.33 | 979.08 | 2.261 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.13 |  | 476.6586 | -0.5305 | 480 | 472.33 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 143.01 |  | 143.9996 | -0.6872 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 174.19 |  | 176.8617 | -1.5106 | 177.84 | 173.19 | 3.4904 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.98 |  | 319.2215 | -2.2685 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 828.63 |  | 863.2348 | -4.0087 | 880.26 | 833 | 0.6794 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 403.29 |  | 409.1795 | -1.4393 | 408.58 | 397.9 | 0.605 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.225 |  | 115.2436 | -3.4871 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 322.33 |  | 330.1362 | -2.3645 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1791.42 |  | 1805.6778 | -0.7896 | 1806.11 | 1780.9 | 0.3896 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 561.59 |  | 566.8707 | -0.9316 | 566.18 | 548.47 | 1.4263 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.72 |  | 321.6766 | -1.23 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.28 |  | 216.0076 | -0.7998 | 217.88 | 212.99 | 0.1073 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 367.83 |  | 372.3782 | -1.2214 | 376.78 | 363.37 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.02 |  | 296.4492 | -1.8314 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.08 |  | 65.6172 | -2.3427 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.09 |  | 55.0016 | -1.6574 | 55.76 | 54.09 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.555 |  | 135.7443 | -1.6128 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.325 |  | 344.4459 | -1.4867 | 347.92 | 341.755 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 508.52 |  | 507.6987 | 0.1618 | 510.71 | 502.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.59 |  | 296.8765 | -0.0965 | 299.26 | 295.795 | 4.9833 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 29.38 |  | 30.1474 | -2.5456 | 31.13 | 29.12 | 4.9694 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 40.79 |  | 42.0929 | -3.0954 | 43.21 | 40.51 | 0.049 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.75 |  | 24.0834 | -1.3843 | 24.46 | 23.265 | 0.0842 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1615.74 |  | 1624.8791 | -0.5624 | 1651.355 | 1560 | 1.2818 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 559.89 |  | 562.8184 | -0.5203 | 576.24 | 556.3 | 4.2294 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 915.8 |  | 923.7425 | -0.8598 | 933.5 | 908.955 | 1.7799 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 232.415 |  | 234.6739 | -0.9626 | 238.285 | 235.71 | 0.1463 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 600.095 |  | 605.5934 | -0.9079 | 614.15 | 605.39 | 0.3516 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 275.575 |  | 279.4445 | -1.3847 | 283 | 276.24 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 168.08 |  | 173.8857 | -3.3388 | 177.88 | 168.18 | 2.9748 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
