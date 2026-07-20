# Intraday State

- Generated at: `2026-07-21T03:28:08+08:00`
- Market time ET: `2026-07-20T15:28:08-04:00`
- Session open: `None`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `54`
- coverage_vwap: `54`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 2, 'below_vwap': 13, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.59 |  | 701.0656 | -0.6384 | 705.51 | 701.82 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 524.6 |  | 532.1759 | -1.4236 | 538.59 | 532.55 | 0.0553 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 557.78 |  | 565.4612 | -1.3584 | 572.46 | 567.02 | 0.0592 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 741.98 |  | 744.9717 | -0.4016 | 748.69 | 746.87 | 0.0229 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.05 |  | 397.5105 | 0.8904 | 392.89 | 389.74 | 0.0224 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 39.7 |  | 39.6894 | 0.0266 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IREN | high_beta_ai_infrastructure | 39.7 |  | 39.6894 | 0.0266 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.62 |  | 296.5049 | 0.0388 | 296.26 | 293.84 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 3 | MSFT | cloud_ai_capex | 401.05 |  | 397.5105 | 0.8904 | 392.89 | 389.74 | 0.0224 | buy_precheck_manual_confirm | none |
| 4 | META | cloud_ai_capex | 648.67 |  | 646.3984 | 0.3514 | 646.57 | 638.875 | 0.5858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | AVGO | custom_silicon_networking | 378.32 |  | 380.3653 | -0.5377 | 382.67 | 377.47 | 0.1031 | below_vwap | below_vwap |
| 6 | AMZN | cloud_ai_capex | 249.47 |  | 250.3914 | -0.368 | 250.2 | 248.195 | 0.008 | below_vwap | below_vwap |
| 7 | AAPL | mega_cap_platform | 328.6 |  | 326.6052 | 0.6108 | 333.63 | 330.03 | 0.0304 | below_opening_15m_low | below_opening_15m_low |
| 8 | LIN | industrial_gases | 512.56 |  | 513.1463 | -0.1143 | 514.7 | 511.78 | 0.0234 | below_vwap | below_vwap |
| 9 | GOOGL | cloud_ai_capex | 351.925 |  | 355.2141 | -0.926 | 358.795 | 350.875 | 0.1222 | below_vwap | below_vwap |
| 10 | 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | CORZ | high_beta_ai_infrastructure | 22.07 |  | 22.316 | -1.1025 | 22.565 | 21.85 | 0.0453 | below_vwap | below_vwap |
| 13 | APLD | high_beta_ai_infrastructure | 27.695 |  | 27.8564 | -0.5793 | 28.39 | 27.11 | 0.0722 | below_vwap | below_vwap |
| 14 | CIEN | ai_networking_optical | 378.54 |  | 386.3429 | -2.0197 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ALAB | ai_networking_optical | 309.13 |  | 313.7858 | -1.4837 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ANET | ai_networking_optical | 169.4 |  | 170.7233 | -0.7751 | 171.39 | 168.79 | 3.7898 | below_vwap | below_vwap,spread_too_wide |
| 17 | LITE | ai_networking_optical | 770.97 |  | 786.6378 | -1.9917 | 790.59 | 767.2 | 3.9262 | below_vwap | below_vwap,spread_too_wide |
| 18 | MRVL | custom_silicon_networking | 194.11 |  | 197.2997 | -1.6167 | 196.86 | 192.09 | 2.1843 | below_vwap | below_vwap,spread_too_wide |
| 19 | NVDA | ai_accelerator | 202.54 |  | 205.245 | -1.3179 | 207.71 | 205.095 | 0.0148 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 696.59 |  | 701.0656 | -0.6384 | 705.51 | 701.82 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 401.05 |  | 397.5105 | 0.8904 | 392.89 | 389.74 | 0.0224 | buy_precheck_manual_confirm | none |
| 2 | IREN | high_beta_ai_infrastructure | 39.7 |  | 39.6894 | 0.0266 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.62 |  | 296.5049 | 0.0388 | 296.26 | 293.84 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | META | cloud_ai_capex | 648.67 |  | 646.3984 | 0.3514 | 646.57 | 638.875 | 0.5858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 169.4 |  | 170.7233 | -0.7751 | 171.39 | 168.79 | 3.7898 | below_vwap | below_vwap,spread_too_wide |
| 6 | AVGO | custom_silicon_networking | 378.32 |  | 380.3653 | -0.5377 | 382.67 | 377.47 | 0.1031 | below_vwap | below_vwap |
| 7 | AMZN | cloud_ai_capex | 249.47 |  | 250.3914 | -0.368 | 250.2 | 248.195 | 0.008 | below_vwap | below_vwap |
| 8 | LITE | ai_networking_optical | 770.97 |  | 786.6378 | -1.9917 | 790.59 | 767.2 | 3.9262 | below_vwap | below_vwap,spread_too_wide |
| 9 | CIEN | ai_networking_optical | 378.54 |  | 386.3429 | -2.0197 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | LIN | industrial_gases | 512.56 |  | 513.1463 | -0.1143 | 514.7 | 511.78 | 0.0234 | below_vwap | below_vwap |
| 11 | 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GOOGL | cloud_ai_capex | 351.925 |  | 355.2141 | -0.926 | 358.795 | 350.875 | 0.1222 | below_vwap | below_vwap |
| 14 | MRVL | custom_silicon_networking | 194.11 |  | 197.2997 | -1.6167 | 196.86 | 192.09 | 2.1843 | below_vwap | below_vwap,spread_too_wide |
| 15 | ALAB | ai_networking_optical | 309.13 |  | 313.7858 | -1.4837 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 22.07 |  | 22.316 | -1.1025 | 22.565 | 21.85 | 0.0453 | below_vwap | below_vwap |
| 17 | APLD | high_beta_ai_infrastructure | 27.695 |  | 27.8564 | -0.5793 | 28.39 | 27.11 | 0.0722 | below_vwap | below_vwap |
| 18 | AAPL | mega_cap_platform | 328.6 |  | 326.6052 | 0.6108 | 333.63 | 330.03 | 0.0304 | below_opening_15m_low | below_opening_15m_low |
| 19 | TSM | foundry | 401.225 |  | 404.2067 | -0.7377 | 409.82 | 405.51 | 0.2293 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | NVDA | ai_accelerator | 202.54 |  | 205.245 | -1.3179 | 207.71 | 205.095 | 0.0148 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.59 |  | 701.0656 | -0.6384 | 705.51 | 701.82 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 67.82 |  | 69.1536 | -1.9284 | 70.43 | 69.35 | 0.0147 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 202.54 |  | 205.245 | -1.3179 | 207.71 | 205.095 | 0.0148 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 401.05 |  | 397.5105 | 0.8904 | 392.89 | 389.74 | 0.0224 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 328.6 |  | 326.6052 | 0.6108 | 333.63 | 330.03 | 0.0304 | below_opening_15m_low | below_opening_15m_low |
| GOOGL | cloud_ai_capex | 351.925 |  | 355.2141 | -0.926 | 358.795 | 350.875 | 0.1222 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.11 |  | 513.9005 | -1.3214 | 522.26 | 510.97 | 0.4181 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 401.225 |  | 404.2067 | -0.7377 | 409.82 | 405.51 | 0.2293 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524.6 |  | 532.1759 | -1.4236 | 538.59 | 532.55 | 0.0553 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 557.78 |  | 565.4612 | -1.3584 | 572.46 | 567.02 | 0.0592 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 378.32 |  | 380.3653 | -0.5377 | 382.67 | 377.47 | 0.1031 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 861.5 |  | 883.196 | -2.4565 | 898.57 | 878.92 | 0.1648 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 194.11 |  | 197.2997 | -1.6167 | 196.86 | 192.09 | 2.1843 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 383.05 |  | 389.9401 | -1.767 | 402.76 | 392.82 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 44.815 |  | 45.5215 | -1.5521 | 46.21 | 45.305 | 0.0669 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 23.99 |  | 24.168 | -0.7365 | 24.51 | 24.22 | 0.0417 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 741.98 |  | 744.9717 | -0.4016 | 748.69 | 746.87 | 0.0229 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 292.595 |  | 293.9056 | -0.4459 | 295.97 | 294.88 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 122.005 |  | 122.4111 | -0.3317 | 125.41 | 123.57 | 0.0574 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.59 |  | 76.0133 | -3.1881 | 79.23 | 75.17 | 4.1718 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 291.87 |  | 295.5726 | -1.2527 | 300.96 | 297.175 | 0.9696 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 399.86 |  | 403.2404 | -0.8383 | 413.44 | 406.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 631.43 |  | 636.6533 | -0.8204 | 644.7 | 636.38 | 0.057 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1073.28 |  | 1077.4584 | -0.3878 | 1103.11 | 1081.14 | 2.4001 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 466.365 |  | 466.4682 | -0.0221 | 477.865 | 468.805 | 0.1265 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| JCI | data_center_power_cooling | 138.96 |  | 140.1983 | -0.8833 | 143.075 | 141.14 | 3.7781 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 169.4 |  | 170.7233 | -0.7751 | 171.39 | 168.79 | 3.7898 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 286.74 |  | 293.1561 | -2.1886 | 296.46 | 286.91 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 770.97 |  | 786.6378 | -1.9917 | 790.59 | 767.2 | 3.9262 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 378.54 |  | 386.3429 | -2.0197 | 393.855 | 377.005 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.19 |  | 104.7285 | -2.4239 | 107.28 | 104.215 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 309.13 |  | 313.7858 | -1.4837 | 322.065 | 308.955 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1734.83 |  | 1751.3131 | -0.9412 | 1797.04 | 1768.805 | 0.0473 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 525.72 |  | 535.4814 | -1.8229 | 554.8 | 543 | 4.7554 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 306.23 |  | 311.5887 | -1.7198 | 324.32 | 319.39 | 4.8232 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 208.26 |  | 211.4392 | -1.5036 | 220.28 | 216.62 | 0.0768 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 333.62 |  | 339.9244 | -1.8546 | 349.43 | 335.335 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 276.73 |  | 281.5568 | -1.7143 | 288.94 | 284 | 4.1015 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.02 |  | 63.2733 | -1.9807 | 64.96 | 63.98 | 0.1129 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 51.26 |  | 51.5516 | -0.5656 | 52.74 | 50.72 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.1 |  | 137.2784 | -2.3153 | 141.89 | 138.545 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 323.61 |  | 329.0451 | -1.6518 | 338.1 | 328.505 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 512.56 |  | 513.1463 | -0.1143 | 514.7 | 511.78 | 0.0234 | below_vwap | below_vwap |
| APD | industrial_gases | 296.62 |  | 296.5049 | 0.0388 | 296.26 | 293.84 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.695 |  | 27.8564 | -0.5793 | 28.39 | 27.11 | 0.0722 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 39.7 |  | 39.6894 | 0.0266 | 39.16 | 36.335 | 0.0252 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 22.07 |  | 22.316 | -1.1025 | 22.565 | 21.85 | 0.0453 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1379.6 |  | 1421.8961 | -2.9746 | 1449.57 | 1394.24 | 5.1218 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 487.18 |  | 498.5152 | -2.2738 | 504.53 | 490.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 802.36 |  | 814.0573 | -1.4369 | 830.62 | 811.99 | 4.1714 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 249.47 |  | 250.3914 | -0.368 | 250.2 | 248.195 | 0.008 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.67 |  | 646.3984 | 0.3514 | 646.57 | 638.875 | 0.5858 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.53 |  | 272.208 | -1.3512 | 277.4 | 271.455 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 152.91 |  | 157.3274 | -2.8078 | 163.02 | 159.54 | 1.8965 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
