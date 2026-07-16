# Intraday State

- Generated at: `2026-07-17T03:51:15+08:00`
- Market time ET: `2026-07-16T15:51:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'spread_too_wide_or_missing': 6, 'below_vwap': 5, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.97 |  | 708.2863 | -0.6094 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.92 |  | 532.5054 | -1.0489 | 543.4 | 535.47 | 0.074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.75 |  | 571.0475 | -0.9277 | 580.31 | 572.21 | 0.0389 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.99 |  | 751.3546 | -0.3147 | 753.51 | 751.13 | 0.008 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.03 |  | 140.608 | 0.3001 | 140.83 | 139.43 | 0.0425 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.03 |  | 140.608 | 0.3001 | 140.83 | 139.43 | 0.0425 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 167.46 |  | 166.6204 | 0.5039 | 169.91 | 165.6 | 0.2448 | watch_only | none |
| 3 | TT | data_center_power_cooling | 476.195 |  | 474.3795 | 0.3827 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | GEV | data_center_power_cooling | 1030.43 |  | 1027.4226 | 0.2927 | 1035.07 | 1021.09 | 3.5199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | MSFT | cloud_ai_capex | 400.32 |  | 400.0928 | 0.0568 | 398.69 | 392.2 | 0.617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ARM | ai_accelerator | 259.345 |  | 257.29 | 0.7987 | 265.96 | 258.1 | 1.3496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 297.36 |  | 295.2231 | 0.7238 | 293.89 | 291.35 | 0.3766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | LIN | industrial_gases | 520.985 |  | 515.8346 | 0.9985 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | IWM | market_regime | 294.86 |  | 295.8699 | -0.3413 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | AAPL | mega_cap_platform | 331.205 |  | 331.4676 | -0.0792 | 328.98 | 326.885 | 0.0604 | below_vwap | below_vwap |
| 12 | TSM | foundry | 406.76 |  | 408.3384 | -0.3865 | 414.385 | 406.61 | 2.4339 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 218.96 |  | 220.2132 | -0.5691 | 222.19 | 218.09 | 0.5389 | below_vwap | below_vwap,spread_too_wide |
| 14 | SOXX | semiconductor_index | 526.92 |  | 532.5054 | -1.0489 | 543.4 | 535.47 | 0.074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | QQQ | market_regime | 703.97 |  | 708.2863 | -0.6094 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | AVGO | custom_silicon_networking | 373.05 |  | 378.4114 | -1.4168 | 386.58 | 378.53 | 0.0563 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.23 |  | 207.2526 | -0.4934 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | AMD | ai_accelerator | 497.85 |  | 502.1074 | -0.8479 | 518.33 | 507.62 | 0.1044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | ASML | semiconductor_equipment | 1784.605 |  | 1810.6204 | -1.4368 | 1823.13 | 1796.26 | 0.0633 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SMH | semiconductor_index | 565.75 |  | 571.0475 | -0.9277 | 580.31 | 572.21 | 0.0389 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | JCI | data_center_power_cooling | 141.03 |  | 140.608 | 0.3001 | 140.83 | 139.43 | 0.0425 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.205 |  | 331.4676 | -0.0792 | 328.98 | 326.885 | 0.0604 | below_vwap | below_vwap |
| 3 | TT | data_center_power_cooling | 476.195 |  | 474.3795 | 0.3827 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 520.985 |  | 515.8346 | 0.9985 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 297.36 |  | 295.2231 | 0.7238 | 293.89 | 291.35 | 0.3766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | MSFT | cloud_ai_capex | 400.32 |  | 400.0928 | 0.0568 | 398.69 | 392.2 | 0.617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 167.46 |  | 166.6204 | 0.5039 | 169.91 | 165.6 | 0.2448 | watch_only | none |
| 8 | TSM | foundry | 406.76 |  | 408.3384 | -0.3865 | 414.385 | 406.61 | 2.4339 | below_vwap | below_vwap,spread_too_wide |
| 9 | KLAC | semiconductor_equipment | 218.96 |  | 220.2132 | -0.5691 | 222.19 | 218.09 | 0.5389 | below_vwap | below_vwap,spread_too_wide |
| 10 | IWM | market_regime | 294.86 |  | 295.8699 | -0.3413 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | GEV | data_center_power_cooling | 1030.43 |  | 1027.4226 | 0.2927 | 1035.07 | 1021.09 | 3.5199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ARM | ai_accelerator | 259.345 |  | 257.29 | 0.7987 | 265.96 | 258.1 | 1.3496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SOXX | semiconductor_index | 526.92 |  | 532.5054 | -1.0489 | 543.4 | 535.47 | 0.074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | CIEN | ai_networking_optical | 387.92 |  | 392.7044 | -1.2183 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 16 | QQQ | market_regime | 703.97 |  | 708.2863 | -0.6094 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | AVGO | custom_silicon_networking | 373.05 |  | 378.4114 | -1.4168 | 386.58 | 378.53 | 0.0563 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | MU | memory_hbm_storage | 849.045 |  | 855.1782 | -0.7172 | 887.1 | 866.765 | 0.3239 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | VRT | data_center_power_cooling | 292.46 |  | 292.9924 | -0.1817 | 300.385 | 293.64 | 1.9798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | NVDA | ai_accelerator | 206.23 |  | 207.2526 | -0.4934 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.97 |  | 708.2863 | -0.6094 | 713.55 | 708.25 | 0.0071 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.11 |  | 71.5477 | -2.0095 | 73.09 | 71.45 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.23 |  | 207.2526 | -0.4934 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.32 |  | 400.0928 | 0.0568 | 398.69 | 392.2 | 0.617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 331.205 |  | 331.4676 | -0.0792 | 328.98 | 326.885 | 0.0604 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 354.25 |  | 364.8998 | -2.9185 | 375.18 | 369.2 | 0.1383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 497.85 |  | 502.1074 | -0.8479 | 518.33 | 507.62 | 0.1044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 406.76 |  | 408.3384 | -0.3865 | 414.385 | 406.61 | 2.4339 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.92 |  | 532.5054 | -1.0489 | 543.4 | 535.47 | 0.074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.75 |  | 571.0475 | -0.9277 | 580.31 | 572.21 | 0.0389 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 373.05 |  | 378.4114 | -1.4168 | 386.58 | 378.53 | 0.0563 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 849.045 |  | 855.1782 | -0.7172 | 887.1 | 866.765 | 0.3239 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 187.665 |  | 190.2779 | -1.3732 | 201.61 | 194.19 | 0.5648 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 392.77 |  | 400.6366 | -1.9635 | 411.65 | 400.635 | 4.7381 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.095 |  | 45.7028 | -1.3299 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.785 |  | 25.242 | -1.8106 | 26.71 | 25.74 | 0.0403 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 748.99 |  | 751.3546 | -0.3147 | 753.51 | 751.13 | 0.008 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.86 |  | 295.8699 | -0.3413 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 123.85 |  | 126.0932 | -1.779 | 131.36 | 126.665 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 72.65 |  | 73.2524 | -0.8224 | 75.54 | 73.985 | 0.0964 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 292.46 |  | 292.9924 | -0.1817 | 300.385 | 293.64 | 1.9798 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 397.17 |  | 399.0429 | -0.4693 | 406.24 | 399.495 | 0.3676 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 628.73 |  | 630.9352 | -0.3495 | 640.25 | 631.005 | 0.1575 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1030.43 |  | 1027.4226 | 0.2927 | 1035.07 | 1021.09 | 3.5199 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.195 |  | 474.3795 | 0.3827 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.03 |  | 140.608 | 0.3001 | 140.83 | 139.43 | 0.0425 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 167.46 |  | 166.6204 | 0.5039 | 169.91 | 165.6 | 0.2448 | watch_only | none |
| COHR | ai_networking_optical | 275.32 |  | 280.038 | -1.6848 | 288.48 | 280.67 | 0.1271 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LITE | ai_networking_optical | 700 |  | 706.75 | -0.9551 | 737.175 | 720.21 | 4.1429 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 387.92 |  | 392.7044 | -1.2183 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.64 |  | 100.8591 | -1.2087 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.85 |  | 322.2149 | -1.665 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1784.605 |  | 1810.6204 | -1.4368 | 1823.13 | 1796.26 | 0.0633 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 558.52 |  | 567.8008 | -1.6345 | 572.69 | 562.32 | 0.6052 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.66 |  | 321.5806 | -1.2192 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.96 |  | 220.2132 | -0.5691 | 222.19 | 218.09 | 0.5389 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 318.935 |  | 324.8113 | -1.8091 | 332.49 | 326.685 | 0.6616 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.06 |  | 284.7887 | -1.6604 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.7 |  | 63.7126 | -1.5893 | 66.19 | 63.93 | 0.9729 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 51.11 |  | 51.6669 | -1.0779 | 52.72 | 51.735 | 0.137 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ENTG | semiconductor_materials | 132.855 |  | 134.2344 | -1.0276 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 328.445 |  | 333.2546 | -1.4432 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 520.985 |  | 515.8346 | 0.9985 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.36 |  | 295.2231 | 0.7238 | 293.89 | 291.35 | 0.3766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.12 |  | 26.7191 | -2.2422 | 28.05 | 27.6 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.88 |  | 35.4656 | -1.6511 | 37.365 | 36.4 | 0.0573 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.96 |  | 21.1713 | -0.9981 | 22.18 | 21.78 | 0.0954 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1410.14 |  | 1448.9357 | -2.6775 | 1549.47 | 1482.06 | 1.1375 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 463.455 |  | 471.6166 | -1.7306 | 498.04 | 480.14 | 0.6926 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 743.25 |  | 759.3232 | -2.1168 | 797.155 | 768.7 | 0.4279 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 248.85 |  | 254.3013 | -2.1436 | 258.07 | 252.62 | 0.0241 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 662.845 |  | 669.8936 | -1.0522 | 680.09 | 667.1 | 0.092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 259.345 |  | 257.29 | 0.7987 | 265.96 | 258.1 | 1.3496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 156.005 |  | 161.0199 | -3.1144 | 168.11 | 162.41 | 0.0256 | below_opening_15m_low | below_opening_15m_low,below_vwap |
