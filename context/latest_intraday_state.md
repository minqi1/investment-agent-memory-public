# Intraday State

- Generated at: `2026-07-24T02:00:28+08:00`
- Market time ET: `2026-07-23T14:00:29-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 17, 'watch_only': 3, 'below_vwap': 28, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 5, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.05 |  | 693.0696 | -0.2914 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 547.23 |  | 550.9112 | -0.6682 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.46 |  | 581.1105 | -0.6282 | 585.98 | 576.635 | 0.071 | below_vwap | below_vwap |
| SPY | market_regime | 737.195 |  | 738.7527 | -0.2109 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1668.88 |  | 1642.0196 | 1.6358 | 1651.355 | 1560 | 0.1887 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 209.08 |  | 208.5869 | 0.2364 | 210.85 | 208.49 | 0.0191 | watch_only | none |
| 2 | MU | memory_hbm_storage | 992.96 |  | 991.7155 | 0.1255 | 999.04 | 964.86 | 0.289 | watch_only | none |
| 3 | WDC | memory_hbm_storage | 564.88 |  | 564.3203 | 0.0992 | 576.24 | 556.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | CORZ | high_beta_ai_infrastructure | 24.15 |  | 24.0691 | 0.3362 | 24.46 | 23.265 | 0.0828 | watch_only | none |
| 5 | ANET | ai_networking_optical | 176.905 |  | 176.7547 | 0.085 | 177.84 | 173.19 | 1.905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ARM | ai_accelerator | 279.845 |  | 279.6785 | 0.0595 | 283 | 276.24 | 2.7837 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SNDK | memory_hbm_storage | 1668.88 |  | 1642.0196 | 1.6358 | 1651.355 | 1560 | 0.1887 | buy_precheck_manual_confirm | none |
| 8 | META | cloud_ai_capex | 606.47 |  | 604.2671 | 0.3646 | 614.15 | 605.39 | 1.3191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 577.46 |  | 581.1105 | -0.6282 | 585.98 | 576.635 | 0.071 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 547.23 |  | 550.9112 | -0.6682 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1793.01 |  | 1803.7248 | -0.594 | 1806.11 | 1780.9 | 0.1021 | below_vwap | below_vwap |
| 12 | KLAC | semiconductor_equipment | 213.77 |  | 215.6402 | -0.8673 | 217.88 | 212.99 | 0.0655 | below_vwap | below_vwap |
| 13 | IWM | market_regime | 291.04 |  | 291.6621 | -0.2133 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 14 | HPE | ai_server_oem | 48.17 |  | 48.3533 | -0.3791 | 48.88 | 47.635 | 0.0415 | below_vwap | below_vwap |
| 15 | MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| 16 | GEV | data_center_power_cooling | 1028.45 |  | 1013.6908 | 1.456 | 1023.33 | 979.08 | 2.0264 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SMCI | ai_server_oem | 31.44 |  | 31.7014 | -0.8246 | 31.52 | 30.23 | 0.0318 | below_vwap | below_vwap |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | IREN | high_beta_ai_infrastructure | 40.9 |  | 41.7073 | -1.9356 | 43.21 | 40.51 | 0.0733 | below_vwap | below_vwap |
| 20 | CIEN | ai_networking_optical | 407.755 |  | 408.3178 | -0.1378 | 408.58 | 397.9 | 0.2551 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SNDK | memory_hbm_storage | 1668.88 |  | 1642.0196 | 1.6358 | 1651.355 | 1560 | 0.1887 | buy_precheck_manual_confirm | none |
| 2 | GEV | data_center_power_cooling | 1028.45 |  | 1013.6908 | 1.456 | 1023.33 | 979.08 | 2.0264 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | NVDA | ai_accelerator | 209.08 |  | 208.5869 | 0.2364 | 210.85 | 208.49 | 0.0191 | watch_only | none |
| 4 | MU | memory_hbm_storage | 992.96 |  | 991.7155 | 0.1255 | 999.04 | 964.86 | 0.289 | watch_only | none |
| 5 | CORZ | high_beta_ai_infrastructure | 24.15 |  | 24.0691 | 0.3362 | 24.46 | 23.265 | 0.0828 | watch_only | none |
| 6 | TSM | foundry | 415.57 |  | 416.6965 | -0.2703 | 420.72 | 412.69 | 1.4919 | below_vwap | below_vwap,spread_too_wide |
| 7 | SMH | semiconductor_index | 577.46 |  | 581.1105 | -0.6282 | 585.98 | 576.635 | 0.071 | below_vwap | below_vwap |
| 8 | SOXX | semiconductor_index | 547.23 |  | 550.9112 | -0.6682 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1793.01 |  | 1803.7248 | -0.594 | 1806.11 | 1780.9 | 0.1021 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 558.54 |  | 565.7515 | -1.2747 | 566.18 | 548.47 | 4.2898 | below_vwap | below_vwap,spread_too_wide |
| 11 | TT | data_center_power_cooling | 476.26 |  | 476.782 | -0.1095 | 480 | 472.33 | 1.9359 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.52 |  | 143.9429 | -0.2938 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 648.715 |  | 651.9326 | -0.4936 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | KLAC | semiconductor_equipment | 213.77 |  | 215.6402 | -0.8673 | 217.88 | 212.99 | 0.0655 | below_vwap | below_vwap |
| 15 | ETN | data_center_power_cooling | 412.43 |  | 413.3814 | -0.2302 | 415.53 | 406.545 | 0.9505 | below_vwap | below_vwap,spread_too_wide |
| 16 | IWM | market_regime | 291.04 |  | 291.6621 | -0.2133 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 17 | LRCX | semiconductor_equipment | 317.43 |  | 321.0071 | -1.1143 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LIN | industrial_gases | 505.3 |  | 507.4635 | -0.4263 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | HPE | ai_server_oem | 48.17 |  | 48.3533 | -0.3791 | 48.88 | 47.635 | 0.0415 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 691.05 |  | 693.0696 | -0.2914 | 698.65 | 693.24 | 0.0087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.99 |  | 66.5606 | -0.8572 | 68.245 | 66.7 | 0.0303 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.08 |  | 208.5869 | 0.2364 | 210.85 | 208.49 | 0.0191 | watch_only | none |
| MSFT | cloud_ai_capex | 380.945 |  | 382.6354 | -0.4418 | 391.71 | 387.245 | 0.0368 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 320.54 |  | 321.0981 | -0.1738 | 323.25 | 320.82 | 0.0437 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.49 |  | 319.5499 | -0.0187 | 324.42 | 320.24 | 0.0438 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 534.51 |  | 540.6326 | -1.1325 | 556.12 | 542.33 | 2.1216 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 415.57 |  | 416.6965 | -0.2703 | 420.72 | 412.69 | 1.4919 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 547.23 |  | 550.9112 | -0.6682 | 557.38 | 545.965 | 0.0566 | below_vwap | below_vwap |
| SMH | semiconductor_index | 577.46 |  | 581.1105 | -0.6282 | 585.98 | 576.635 | 0.071 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.415 |  | 392.3848 | -0.502 | 397.34 | 390.54 | 1.5138 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.96 |  | 991.7155 | 0.1255 | 999.04 | 964.86 | 0.289 | watch_only | none |
| MRVL | custom_silicon_networking | 206.82 |  | 209.6797 | -1.3638 | 213.785 | 207.665 | 0.1789 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 440.22 |  | 443.9734 | -0.8454 | 450.07 | 438.55 | 0.2999 | below_vwap | below_vwap |
| HPE | ai_server_oem | 48.17 |  | 48.3533 | -0.3791 | 48.88 | 47.635 | 0.0415 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.44 |  | 31.7014 | -0.8246 | 31.52 | 30.23 | 0.0318 | below_vwap | below_vwap |
| SPY | market_regime | 737.195 |  | 738.7527 | -0.2109 | 742.515 | 738.54 | 0.0054 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.04 |  | 291.6621 | -0.2133 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.185 |  | 121.9406 | -1.4397 | 124.22 | 122.07 | 0.0499 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.26 |  | 82.8361 | -0.6955 | 84.415 | 80.64 | 0.4376 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.55 |  | 306.2472 | -1.2073 | 311.13 | 303.96 | 1.3056 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 412.43 |  | 413.3814 | -0.2302 | 415.53 | 406.545 | 0.9505 | below_vwap | below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 648.715 |  | 651.9326 | -0.4936 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1028.45 |  | 1013.6908 | 1.456 | 1023.33 | 979.08 | 2.0264 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 476.26 |  | 476.782 | -0.1095 | 480 | 472.33 | 1.9359 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 143.52 |  | 143.9429 | -0.2938 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 176.905 |  | 176.7547 | 0.085 | 177.84 | 173.19 | 1.905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 313.29 |  | 318.0426 | -1.4943 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 835.455 |  | 857.6651 | -2.5896 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 407.755 |  | 408.3178 | -0.1378 | 408.58 | 397.9 | 0.2551 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 113.485 |  | 114.6089 | -0.9806 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 324.76 |  | 327.7453 | -0.9109 | 341.68 | 327.43 | 4.6742 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1793.01 |  | 1803.7248 | -0.594 | 1806.11 | 1780.9 | 0.1021 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 558.54 |  | 565.7515 | -1.2747 | 566.18 | 548.47 | 4.2898 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.43 |  | 321.0071 | -1.1143 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 213.77 |  | 215.6402 | -0.8673 | 217.88 | 212.99 | 0.0655 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 370.41 |  | 372.2641 | -0.4981 | 376.78 | 363.37 | 3.7769 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 288.915 |  | 294.4769 | -1.8887 | 301.305 | 293.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.64 |  | 65.2657 | -0.9587 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.18 |  | 54.5671 | -0.7093 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.1 |  | 135.2847 | -0.8757 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.02 |  | 342.9003 | 0.0349 | 347.92 | 341.755 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 505.3 |  | 507.4635 | -0.4263 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.095 |  | 295.8149 | -0.2433 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.02 |  | 30.0601 | -0.1333 | 31.13 | 29.12 | 0.0999 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.9 |  | 41.7073 | -1.9356 | 43.21 | 40.51 | 0.0733 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.15 |  | 24.0691 | 0.3362 | 24.46 | 23.265 | 0.0828 | watch_only | none |
| SNDK | memory_hbm_storage | 1668.88 |  | 1642.0196 | 1.6358 | 1651.355 | 1560 | 0.1887 | buy_precheck_manual_confirm | none |
| WDC | memory_hbm_storage | 564.88 |  | 564.3203 | 0.0992 | 576.24 | 556.3 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 921.69 |  | 924.6685 | -0.3221 | 933.5 | 908.955 |  | below_vwap | below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 234.245 |  | 234.3536 | -0.0463 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.47 |  | 604.2671 | 0.3646 | 614.15 | 605.39 | 1.3191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 279.845 |  | 279.6785 | 0.0595 | 283 | 276.24 | 2.7837 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.03 |  | 173.6109 | -0.3346 | 177.88 | 168.18 | 1.0692 | below_vwap | below_vwap,spread_too_wide |
