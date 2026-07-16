# Intraday State

- Generated at: `2026-07-17T00:00:34+08:00`
- Market time ET: `2026-07-16T12:00:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 17, 'manual_confirm_candidate': 3, 'spread_too_wide_or_missing': 6, 'below_opening_15m_low': 27, 'price_stale_or_missing': 2, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.25 |  | 710.5149 | -0.0373 | 713.55 | 708.25 | 0.0169 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 533.93 |  | 537.3272 | -0.6322 | 543.4 | 535.47 | 0.088 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.79 |  | 575.1834 | -0.4161 | 580.31 | 572.21 | 0.0803 | below_vwap | below_vwap |
| SPY | market_regime | 753.57 |  | 752.8714 | 0.0928 | 753.51 | 751.13 | 0.0265 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.57 |  | 752.8714 | 0.0928 | 753.51 | 751.13 | 0.0265 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.72 |  | 514.6242 | 0.4073 | 515.825 | 512.23 | 0.1316 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 400.445 |  | 396.1684 | 1.0795 | 398.69 | 392.2 | 0.0924 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.57 |  | 752.8714 | 0.0928 | 753.51 | 751.13 | 0.0265 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.72 |  | 514.6242 | 0.4073 | 515.825 | 512.23 | 0.1316 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 256.29 |  | 255.2939 | 0.3902 | 258.07 | 252.62 | 0.0546 | watch_only | none |
| 4 | MSFT | cloud_ai_capex | 400.445 |  | 396.1684 | 1.0795 | 398.69 | 392.2 | 0.0924 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 475.215 |  | 474.4263 | 0.1662 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ONTO | semiconductor_test_packaging | 290.87 |  | 290.6458 | 0.0771 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ANET | ai_networking_optical | 167.39 |  | 166.3004 | 0.6552 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | AVGO | custom_silicon_networking | 382.02 |  | 381.8627 | 0.0412 | 386.58 | 378.53 | 1.3298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APD | industrial_gases | 296.28 |  | 294.5563 | 0.5852 | 293.89 | 291.35 | 3.9321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | AAPL | mega_cap_platform | 331.83 |  | 329.6882 | 0.6497 | 328.98 | 326.885 | 0.452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | IWM | market_regime | 296.4 |  | 296.6131 | -0.0718 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 12 | QQQ | market_regime | 710.25 |  | 710.5149 | -0.0373 | 713.55 | 708.25 | 0.0169 | below_vwap | below_vwap |
| 13 | NVDA | ai_accelerator | 207.6 |  | 207.6259 | -0.0125 | 211.03 | 207.49 | 0.0145 | below_vwap | below_vwap |
| 14 | ASML | semiconductor_equipment | 1817.68 |  | 1825.5111 | -0.429 | 1823.13 | 1796.26 | 0.1282 | below_vwap | below_vwap |
| 15 | SMH | semiconductor_index | 572.79 |  | 575.1834 | -0.4161 | 580.31 | 572.21 | 0.0803 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 140.325 |  | 140.6903 | -0.2597 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 631.835 |  | 633.1309 | -0.2047 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | KLAC | semiconductor_equipment | 221.065 |  | 222.7126 | -0.7398 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | META | cloud_ai_capex | 674.6 |  | 675.0659 | -0.069 | 680.09 | 667.1 | 0.292 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.57 |  | 752.8714 | 0.0928 | 753.51 | 751.13 | 0.0265 | buy_precheck_manual_confirm | none |
| 2 | LIN | industrial_gases | 516.72 |  | 514.6242 | 0.4073 | 515.825 | 512.23 | 0.1316 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 400.445 |  | 396.1684 | 1.0795 | 398.69 | 392.2 | 0.0924 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 296.4 |  | 296.6131 | -0.0718 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 5 | TT | data_center_power_cooling | 475.215 |  | 474.4263 | 0.1662 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.28 |  | 294.5563 | 0.5852 | 293.89 | 291.35 | 3.9321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | AAPL | mega_cap_platform | 331.83 |  | 329.6882 | 0.6497 | 328.98 | 326.885 | 0.452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AMZN | cloud_ai_capex | 256.29 |  | 255.2939 | 0.3902 | 258.07 | 252.62 | 0.0546 | watch_only | none |
| 9 | TSM | foundry | 408.32 |  | 411.2344 | -0.7087 | 414.385 | 406.61 | 2.9389 | below_vwap | below_vwap,spread_too_wide |
| 10 | QQQ | market_regime | 710.25 |  | 710.5149 | -0.0373 | 713.55 | 708.25 | 0.0169 | below_vwap | below_vwap |
| 11 | NVDA | ai_accelerator | 207.6 |  | 207.6259 | -0.0125 | 211.03 | 207.49 | 0.0145 | below_vwap | below_vwap |
| 12 | JCI | data_center_power_cooling | 140.325 |  | 140.6903 | -0.2597 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 631.835 |  | 633.1309 | -0.2047 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1032.07 |  | 1032.5435 | -0.0459 | 1035.07 | 1021.09 | 1.2974 | below_vwap | below_vwap,spread_too_wide |
| 15 | ASML | semiconductor_equipment | 1817.68 |  | 1825.5111 | -0.429 | 1823.13 | 1796.26 | 0.1282 | below_vwap | below_vwap |
| 16 | AMAT | semiconductor_equipment | 570.58 |  | 574.7605 | -0.7273 | 572.69 | 562.32 | 0.6537 | below_vwap | below_vwap,spread_too_wide |
| 17 | KLAC | semiconductor_equipment | 221.065 |  | 222.7126 | -0.7398 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | SMH | semiconductor_index | 572.79 |  | 575.1834 | -0.4161 | 580.31 | 572.21 | 0.0803 | below_vwap | below_vwap |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 135.54 |  | 135.9611 | -0.3097 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.25 |  | 710.5149 | -0.0373 | 713.55 | 708.25 | 0.0169 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 72.05 |  | 72.1978 | -0.2047 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.6 |  | 207.6259 | -0.0125 | 211.03 | 207.49 | 0.0145 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 400.445 |  | 396.1684 | 1.0795 | 398.69 | 392.2 | 0.0924 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.83 |  | 329.6882 | 0.6497 | 328.98 | 326.885 | 0.452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 371.29 |  | 371.9931 | -0.189 | 375.18 | 369.2 | 0.5225 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 506.88 |  | 510.197 | -0.6501 | 518.33 | 507.62 | 1.4145 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 408.32 |  | 411.2344 | -0.7087 | 414.385 | 406.61 | 2.9389 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 533.93 |  | 537.3272 | -0.6322 | 543.4 | 535.47 | 0.088 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.79 |  | 575.1834 | -0.4161 | 580.31 | 572.21 | 0.0803 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.02 |  | 381.8627 | 0.0412 | 386.58 | 378.53 | 1.3298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 853.41 |  | 863.6189 | -1.1821 | 887.1 | 866.765 | 1.4061 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 190.37 |  | 193.5539 | -1.645 | 201.61 | 194.19 | 0.1944 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 400.21 |  | 404.5884 | -1.0822 | 411.65 | 400.635 | 4.5676 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.59 |  | 46.2041 | -1.329 | 47.65 | 46.165 | 0.0219 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.23 |  | 25.6696 | -1.7124 | 26.71 | 25.74 | 0.0396 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.57 |  | 752.8714 | 0.0928 | 753.51 | 751.13 | 0.0265 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.4 |  | 296.6131 | -0.0718 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.53 |  | 127.027 | -0.3912 | 131.36 | 126.665 | 2.8926 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.85 |  | 73.7428 | -1.2107 | 75.54 | 73.985 | 4.9966 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.41 |  | 296.1523 | -0.926 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.68 |  | 401.3212 | -1.4057 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 631.835 |  | 633.1309 | -0.2047 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1032.07 |  | 1032.5435 | -0.0459 | 1035.07 | 1021.09 | 1.2974 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.215 |  | 474.4263 | 0.1662 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.325 |  | 140.6903 | -0.2597 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.39 |  | 166.3004 | 0.6552 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.795 |  | 283.6058 | -1.6963 | 288.48 | 280.67 | 4.541 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 702.48 |  | 715.0169 | -1.7534 | 737.175 | 720.21 | 3.2713 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 395.145 |  | 397.7555 | -0.6563 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.94 |  | 103.0285 | -2.0271 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.99 |  | 326.9989 | -2.1434 | 337.59 | 326.16 | 0.3344 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ASML | semiconductor_equipment | 1817.68 |  | 1825.5111 | -0.429 | 1823.13 | 1796.26 | 0.1282 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 570.58 |  | 574.7605 | -0.7273 | 572.69 | 562.32 | 0.6537 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 323.32 |  | 326.9 | -1.0951 | 328.96 | 324.11 | 1.4537 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 221.065 |  | 222.7126 | -0.7398 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 326.44 |  | 328.9 | -0.7479 | 332.49 | 326.685 | 0.2543 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ONTO | semiconductor_test_packaging | 290.87 |  | 290.6458 | 0.0771 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.22 |  | 64.5785 | -0.5551 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.25 |  | 52.6601 | -0.7788 | 52.72 | 51.735 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.54 |  | 135.9611 | -0.3097 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 336.8 |  | 340.8422 | -1.186 | 346.26 | 338 | 4.6437 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.72 |  | 514.6242 | 0.4073 | 515.825 | 512.23 | 0.1316 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.28 |  | 294.5563 | 0.5852 | 293.89 | 291.35 | 3.9321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.61 |  | 27.2802 | -2.4568 | 28.05 | 27.6 | 0.1503 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.195 |  | 35.9424 | -2.0794 | 37.365 | 36.4 | 0.0852 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.065 |  | 21.5025 | -2.0346 | 22.18 | 21.78 | 0.0949 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1447.12 |  | 1485.5038 | -2.5839 | 1549.47 | 1482.06 | 0.548 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 469.77 |  | 481.5762 | -2.4516 | 498.04 | 480.14 | 2.4927 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 760.08 |  | 773.5071 | -1.7359 | 797.155 | 768.7 | 2.6905 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.29 |  | 255.2939 | 0.3902 | 258.07 | 252.62 | 0.0546 | watch_only | none |
| META | cloud_ai_capex | 674.6 |  | 675.0659 | -0.069 | 680.09 | 667.1 | 0.292 | below_vwap | below_vwap |
| ARM | ai_accelerator | 256.47 |  | 258.4496 | -0.766 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.57 |  | 163.6169 | -1.251 | 168.11 | 162.41 | 1.6897 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
