# Intraday State

- Generated at: `2026-07-16T22:07:29+08:00`
- Market time ET: `2026-07-16T10:07:30-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'below_vwap': 11, 'spread_too_wide_or_missing': 29, 'price_stale_or_missing': 1, 'manual_confirm_candidate': 2, 'below_opening_15m_low': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.47 |  | 709.6386 | 0.2581 | 713.55 | 708.25 | 0.0394 | watch_only | none |
| SOXX | semiconductor_index | 541.98 |  | 537.3753 | 0.8569 | 543.4 | 535.47 | 0.072 | watch_only | none |
| SMH | semiconductor_index | 578.665 |  | 575.0186 | 0.6341 | 580.31 | 572.21 | 0.0588 | watch_only | none |
| SPY | market_regime | 752.855 |  | 751.974 | 0.1172 | 753.51 | 751.13 | 0.004 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 226.44 |  | 220.8627 | 2.5252 | 222.19 | 218.09 | 0.2031 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.06 |  | 296.1909 | 0.2934 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 297.06 |  | 296.1909 | 0.2934 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 711.47 |  | 709.6386 | 0.2581 | 713.55 | 708.25 | 0.0394 | watch_only | none |
| 3 | SPY | market_regime | 752.855 |  | 751.974 | 0.1172 | 753.51 | 751.13 | 0.004 | watch_only | none |
| 4 | HPE | ai_server_oem | 46.98 |  | 46.8534 | 0.2702 | 47.65 | 46.165 | 0.0426 | watch_only | none |
| 5 | SMCI | ai_server_oem | 26.015 |  | 25.9614 | 0.2065 | 26.71 | 25.74 | 0.0769 | watch_only | none |
| 6 | SMH | semiconductor_index | 578.665 |  | 575.0186 | 0.6341 | 580.31 | 572.21 | 0.0588 | watch_only | none |
| 7 | AMD | ai_accelerator | 515.18 |  | 511.8561 | 0.6494 | 518.33 | 507.62 | 0.2543 | watch_only | none |
| 8 | SOXX | semiconductor_index | 541.98 |  | 537.3753 | 0.8569 | 543.4 | 535.47 | 0.072 | watch_only | none |
| 9 | ENTG | semiconductor_materials | 135.515 |  | 134.5496 | 0.7175 | 135.515 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ANET | ai_networking_optical | 166.52 |  | 166.342 | 0.107 | 169.91 | 165.6 | 3.8074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | VRT | data_center_power_cooling | 295.92 |  | 294.7234 | 0.406 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 633.365 |  | 632.4557 | 0.1438 | 640.25 | 631.005 | 1.4478 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ETN | data_center_power_cooling | 403.58 |  | 401.8706 | 0.4253 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | MKSI | semiconductor_materials | 343.52 |  | 341.2665 | 0.6603 | 343.92 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ARM | ai_accelerator | 260.87 |  | 259.9572 | 0.3511 | 265.96 | 258.1 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MRVL | custom_silicon_networking | 195.94 |  | 195.3652 | 0.2942 | 201.61 | 194.19 | 0.8676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMKR | semiconductor_test_packaging | 64.98 |  | 64.7246 | 0.3946 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | CRWV | gpu_cloud_ai_factory | 74.295 |  | 74.1654 | 0.1748 | 75.54 | 73.985 | 1.7902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TSM | foundry | 412.645 |  | 410.098 | 0.6211 | 414.385 | 406.61 | 0.8385 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 475.63 |  | 471.2743 | 0.9242 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 226.44 |  | 220.8627 | 2.5252 | 222.19 | 218.09 | 0.2031 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.06 |  | 296.1909 | 0.2934 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 475.63 |  | 471.2743 | 0.9242 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | JCI | data_center_power_cooling | 141.2 |  | 140.0576 | 0.8156 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | GEV | data_center_power_cooling | 1039.03 |  | 1025.7326 | 1.2964 | 1035.07 | 1021.09 | 3.1221 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ASML | semiconductor_equipment | 1839.36 |  | 1812.9795 | 1.4551 | 1823.13 | 1796.26 | 0.766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AMAT | semiconductor_equipment | 586.545 |  | 570.4257 | 2.8258 | 572.69 | 562.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | LRCX | semiconductor_equipment | 332.495 |  | 326.2417 | 1.9168 | 328.96 | 324.11 | 4.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ENTG | semiconductor_materials | 135.515 |  | 134.5496 | 0.7175 | 135.515 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | COHU | semiconductor_test_packaging | 52.72 |  | 52.1874 | 1.0205 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 541.98 |  | 537.3753 | 0.8569 | 543.4 | 535.47 | 0.072 | watch_only | none |
| 12 | QQQ | market_regime | 711.47 |  | 709.6386 | 0.2581 | 713.55 | 708.25 | 0.0394 | watch_only | none |
| 13 | AMD | ai_accelerator | 515.18 |  | 511.8561 | 0.6494 | 518.33 | 507.62 | 0.2543 | watch_only | none |
| 14 | SMH | semiconductor_index | 578.665 |  | 575.0186 | 0.6341 | 580.31 | 572.21 | 0.0588 | watch_only | none |
| 15 | SPY | market_regime | 752.855 |  | 751.974 | 0.1172 | 753.51 | 751.13 | 0.004 | watch_only | none |
| 16 | HPE | ai_server_oem | 46.98 |  | 46.8534 | 0.2702 | 47.65 | 46.165 | 0.0426 | watch_only | none |
| 17 | SMCI | ai_server_oem | 26.015 |  | 25.9614 | 0.2065 | 26.71 | 25.74 | 0.0769 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 72.43 |  | 72.0226 | 0.5656 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| 19 | CIEN | ai_networking_optical | 400.745 |  | 401.2939 | -0.1368 | 410 | 397.68 | 0.6638 | below_vwap | below_vwap,spread_too_wide |
| 20 | NVDA | ai_accelerator | 208.06 |  | 208.4346 | -0.1797 | 211.03 | 207.49 | 0.0529 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.47 |  | 709.6386 | 0.2581 | 713.55 | 708.25 | 0.0394 | watch_only | none |
| TQQQ | leveraged_tool | 72.43 |  | 72.0226 | 0.5656 | 73.09 | 71.45 | 0.0138 | watch_only | none |
| NVDA | ai_accelerator | 208.06 |  | 208.4346 | -0.1797 | 211.03 | 207.49 | 0.0529 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 393.29 |  | 395.3251 | -0.5148 | 398.69 | 392.2 | 0.1602 | below_vwap | below_vwap |
| AAPL | mega_cap_platform | 328.865 |  | 328.8838 | -0.0057 | 328.98 | 326.885 | 0.0274 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 369.94 |  | 371.5615 | -0.4364 | 375.18 | 369.2 | 1.1272 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 515.18 |  | 511.8561 | 0.6494 | 518.33 | 507.62 | 0.2543 | watch_only | none |
| TSM | foundry | 412.645 |  | 410.098 | 0.6211 | 414.385 | 406.61 | 0.8385 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 541.98 |  | 537.3753 | 0.8569 | 543.4 | 535.47 | 0.072 | watch_only | none |
| SMH | semiconductor_index | 578.665 |  | 575.0186 | 0.6341 | 580.31 | 572.21 | 0.0588 | watch_only | none |
| AVGO | custom_silicon_networking | 384.02 |  | 380.9223 | 0.8132 | 386.58 | 378.53 | 3.8097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 875.97 |  | 866.0029 | 1.1509 | 887.1 | 866.765 | 3.1896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 195.94 |  | 195.3652 | 0.2942 | 201.61 | 194.19 | 0.8676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 409.255 |  | 403.351 | 1.4637 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.98 |  | 46.8534 | 0.2702 | 47.65 | 46.165 | 0.0426 | watch_only | none |
| SMCI | ai_server_oem | 26.015 |  | 25.9614 | 0.2065 | 26.71 | 25.74 | 0.0769 | watch_only | none |
| SPY | market_regime | 752.855 |  | 751.974 | 0.1172 | 753.51 | 751.13 | 0.004 | watch_only | none |
| IWM | market_regime | 297.06 |  | 296.1909 | 0.2934 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.53 |  | 127.6361 | -0.0832 | 131.36 | 126.665 | 1.5683 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 74.295 |  | 74.1654 | 0.1748 | 75.54 | 73.985 | 1.7902 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 295.92 |  | 294.7234 | 0.406 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 403.58 |  | 401.8706 | 0.4253 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 633.365 |  | 632.4557 | 0.1438 | 640.25 | 631.005 | 1.4478 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1039.03 |  | 1025.7326 | 1.2964 | 1035.07 | 1021.09 | 3.1221 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.63 |  | 471.2743 | 0.9242 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.2 |  | 140.0576 | 0.8156 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.52 |  | 166.342 | 0.107 | 169.91 | 165.6 | 3.8074 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 287.77 |  | 284.4552 | 1.1653 | 288.48 | 280.67 | 0.6255 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 727.67 |  | 721.6966 | 0.8277 | 737.175 | 720.21 | 0.3793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 400.745 |  | 401.2939 | -0.1368 | 410 | 397.68 | 0.6638 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 104.87 |  | 103.8216 | 1.0098 | 106.975 | 102.85 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 328.615 |  | 329.0783 | -0.1408 | 337.59 | 326.16 | 0.5325 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1839.36 |  | 1812.9795 | 1.4551 | 1823.13 | 1796.26 | 0.766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 586.545 |  | 570.4257 | 2.8258 | 572.69 | 562.32 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 332.495 |  | 326.2417 | 1.9168 | 328.96 | 324.11 | 4.6828 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 226.44 |  | 220.8627 | 2.5252 | 222.19 | 218.09 | 0.2031 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 331.79 |  | 327.0125 | 1.461 | 332.49 | 326.685 | 0.7143 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 291.24 |  | 288.7141 | 0.8749 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.98 |  | 64.7246 | 0.3946 | 66.19 | 63.93 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.72 |  | 52.1874 | 1.0205 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.515 |  | 134.5496 | 0.7175 | 135.515 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 343.52 |  | 341.2665 | 0.6603 | 343.92 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 511.91 |  | 513.648 | -0.3384 | 515.825 | 512.23 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 290.675 |  | 291.6536 | -0.3355 | 293.89 | 291.35 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.51 |  | 27.5012 | 0.032 | 28.05 | 27.6 | 0.0727 | below_opening_15m_low | below_opening_15m_low |
| IREN | high_beta_ai_infrastructure | 36.36 |  | 36.5028 | -0.3912 | 37.365 | 36.4 | 0.0825 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.54 |  | 21.7182 | -0.8205 | 22.18 | 21.78 | 0.0929 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1524.29 |  | 1499.8087 | 1.6323 | 1549.47 | 1482.06 | 0.5603 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 487.37 |  | 482.7801 | 0.9507 | 498.04 | 480.14 | 0.6299 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 782.26 |  | 774.7321 | 0.9717 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 253.58 |  | 254.8103 | -0.4828 | 258.07 | 252.62 | 0.0631 | below_vwap | below_vwap |
| META | cloud_ai_capex | 670.39 |  | 672.4307 | -0.3035 | 680.09 | 667.1 | 0.0895 | below_vwap | below_vwap |
| ARM | ai_accelerator | 260.87 |  | 259.9572 | 0.3511 | 265.96 | 258.1 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 164.88 |  | 164.8888 | -0.0054 | 168.11 | 162.41 | 2.1228 | below_vwap | below_vwap,spread_too_wide |
