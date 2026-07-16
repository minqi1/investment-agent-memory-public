# Intraday State

- Generated at: `2026-07-16T22:43:14+08:00`
- Market time ET: `2026-07-16T10:43:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 7, 'below_vwap': 13, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 18, 'price_stale_or_missing': 1, 'below_opening_15m_low': 13}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.62 |  | 710.5624 | 0.1488 | 713.55 | 708.25 | 0.0492 | watch_only | none |
| SOXX | semiconductor_index | 538.07 |  | 538.395 | -0.0604 | 543.4 | 535.47 | 0.0818 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.42 |  | 576.2427 | -0.1428 | 580.31 | 572.21 | 0.1043 | below_vwap | below_vwap |
| SPY | market_regime | 753.85 |  | 752.4913 | 0.1806 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.59 |  | 473.7901 | 0.3799 | 474.085 | 467.64 | 0.1724 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.85 |  | 752.4913 | 0.1806 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 297.045 |  | 296.4791 | 0.1909 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.31 |  | 329.0864 | 0.3718 | 328.98 | 326.885 | 0.2664 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.85 |  | 752.4913 | 0.1806 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.045 |  | 296.4791 | 0.1909 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 711.62 |  | 710.5624 | 0.1488 | 713.55 | 708.25 | 0.0492 | watch_only | none |
| 4 | TT | data_center_power_cooling | 475.59 |  | 473.7901 | 0.3799 | 474.085 | 467.64 | 0.1724 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 372.91 |  | 371.8516 | 0.2846 | 375.18 | 369.2 | 0.1368 | watch_only | none |
| 6 | AMD | ai_accelerator | 511.54 |  | 511.1379 | 0.0787 | 518.33 | 507.62 | 0.2287 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 330.31 |  | 329.0864 | 0.3718 | 328.98 | 326.885 | 0.2664 | buy_precheck_manual_confirm | none |
| 8 | MSFT | cloud_ai_capex | 396.91 |  | 395.1402 | 0.4479 | 398.69 | 392.2 | 0.0806 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 256.63 |  | 255.0302 | 0.6273 | 258.07 | 252.62 | 0.0818 | watch_only | none |
| 10 | META | cloud_ai_capex | 677.09 |  | 673.4966 | 0.5335 | 680.09 | 667.1 | 0.0458 | watch_only | none |
| 11 | LIN | industrial_gases | 514.035 |  | 513.2038 | 0.162 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | JCI | data_center_power_cooling | 141.19 |  | 140.5878 | 0.4284 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 382.365 |  | 382.1341 | 0.0604 | 386.58 | 378.53 | 0.4184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 298.14 |  | 296.786 | 0.4562 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 635.265 |  | 633.4778 | 0.2821 | 640.25 | 631.005 | 0.3715 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ASML | semiconductor_equipment | 1829.74 |  | 1827.5152 | 0.1217 | 1823.13 | 1796.26 | 0.7241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ONTO | semiconductor_test_packaging | 292 |  | 290.4884 | 0.5204 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 223.41 |  | 222.9484 | 0.2071 | 222.19 | 218.09 | 0.649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | DELL | ai_server_oem | 408.09 |  | 405.695 | 0.5903 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 136.42 |  | 135.9299 | 0.3606 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.59 |  | 473.7901 | 0.3799 | 474.085 | 467.64 | 0.1724 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.85 |  | 752.4913 | 0.1806 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 297.045 |  | 296.4791 | 0.1909 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.31 |  | 329.0864 | 0.3718 | 328.98 | 326.885 | 0.2664 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 141.19 |  | 140.5878 | 0.4284 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1039.8 |  | 1029.6397 | 0.9868 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ASML | semiconductor_equipment | 1829.74 |  | 1827.5152 | 0.1217 | 1823.13 | 1796.26 | 0.7241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AMAT | semiconductor_equipment | 579.12 |  | 575.6243 | 0.6073 | 572.69 | 562.32 | 1.4574 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | KLAC | semiconductor_equipment | 223.41 |  | 222.9484 | 0.2071 | 222.19 | 218.09 | 0.649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | COHU | semiconductor_test_packaging | 53.135 |  | 52.6409 | 0.9387 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TER | semiconductor_test_packaging | 332.84 |  | 328.4912 | 1.3239 | 332.49 | 326.685 | 4.3114 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | QQQ | market_regime | 711.62 |  | 710.5624 | 0.1488 | 713.55 | 708.25 | 0.0492 | watch_only | none |
| 13 | AMD | ai_accelerator | 511.54 |  | 511.1379 | 0.0787 | 518.33 | 507.62 | 0.2287 | watch_only | none |
| 14 | MSFT | cloud_ai_capex | 396.91 |  | 395.1402 | 0.4479 | 398.69 | 392.2 | 0.0806 | watch_only | none |
| 15 | GOOGL | cloud_ai_capex | 372.91 |  | 371.8516 | 0.2846 | 375.18 | 369.2 | 0.1368 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 256.63 |  | 255.0302 | 0.6273 | 258.07 | 252.62 | 0.0818 | watch_only | none |
| 17 | META | cloud_ai_capex | 677.09 |  | 673.4966 | 0.5335 | 680.09 | 667.1 | 0.0458 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 72.49 |  | 72.2099 | 0.3878 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| 19 | ANET | ai_networking_optical | 166.28 |  | 166.3935 | -0.0682 | 169.91 | 165.6 | 0.1864 | below_vwap | below_vwap |
| 20 | SOXX | semiconductor_index | 538.07 |  | 538.395 | -0.0604 | 543.4 | 535.47 | 0.0818 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.62 |  | 710.5624 | 0.1488 | 713.55 | 708.25 | 0.0492 | watch_only | none |
| TQQQ | leveraged_tool | 72.49 |  | 72.2099 | 0.3878 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| NVDA | ai_accelerator | 207.86 |  | 208.4601 | -0.2879 | 211.03 | 207.49 | 0.0192 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 396.91 |  | 395.1402 | 0.4479 | 398.69 | 392.2 | 0.0806 | watch_only | none |
| AAPL | mega_cap_platform | 330.31 |  | 329.0864 | 0.3718 | 328.98 | 326.885 | 0.2664 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.91 |  | 371.8516 | 0.2846 | 375.18 | 369.2 | 0.1368 | watch_only | none |
| AMD | ai_accelerator | 511.54 |  | 511.1379 | 0.0787 | 518.33 | 507.62 | 0.2287 | watch_only | none |
| TSM | foundry | 413.45 |  | 411.2 | 0.5472 | 414.385 | 406.61 | 1.0231 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 538.07 |  | 538.395 | -0.0604 | 543.4 | 535.47 | 0.0818 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.42 |  | 576.2427 | -0.1428 | 580.31 | 572.21 | 0.1043 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.365 |  | 382.1341 | 0.0604 | 386.58 | 378.53 | 0.4184 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 861.78 |  | 867.3736 | -0.6449 | 887.1 | 866.765 | 0.7751 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 193.195 |  | 195.3366 | -1.0964 | 201.61 | 194.19 | 0.2381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 408.09 |  | 405.695 | 0.5903 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.55 |  | 46.7825 | -0.497 | 47.65 | 46.165 | 0.043 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.675 |  | 25.9207 | -0.9478 | 26.71 | 25.74 | 0.0779 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.85 |  | 752.4913 | 0.1806 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.045 |  | 296.4791 | 0.1909 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.12 |  | 127.4168 | -1.0177 | 131.36 | 126.665 | 0.0714 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.89 |  | 74.1305 | -0.3245 | 75.54 | 73.985 | 1.5428 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 298.14 |  | 296.786 | 0.4562 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.45 |  | 402.5709 | -0.03 | 406.24 | 399.495 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635.265 |  | 633.4778 | 0.2821 | 640.25 | 631.005 | 0.3715 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1039.8 |  | 1029.6397 | 0.9868 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 475.59 |  | 473.7901 | 0.3799 | 474.085 | 467.64 | 0.1724 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 141.19 |  | 140.5878 | 0.4284 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.28 |  | 166.3935 | -0.0682 | 169.91 | 165.6 | 0.1864 | below_vwap | below_vwap |
| COHR | ai_networking_optical | 282.77 |  | 285.0571 | -0.8023 | 288.48 | 280.67 | 1.6338 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 717.865 |  | 722.0841 | -0.5843 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 395.34 |  | 399.9785 | -1.1597 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.49 |  | 103.8885 | -1.3462 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.12 |  | 329.615 | -0.757 | 337.59 | 326.16 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1829.74 |  | 1827.5152 | 0.1217 | 1823.13 | 1796.26 | 0.7241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 579.12 |  | 575.6243 | 0.6073 | 572.69 | 562.32 | 1.4574 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 327.79 |  | 328.0307 | -0.0734 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 223.41 |  | 222.9484 | 0.2071 | 222.19 | 218.09 | 0.649 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 332.84 |  | 328.4912 | 1.3239 | 332.49 | 326.685 | 4.3114 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 292 |  | 290.4884 | 0.5204 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.59 |  | 64.8381 | -0.3827 | 66.19 | 63.93 | 4.9543 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 53.135 |  | 52.6409 | 0.9387 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.42 |  | 135.9299 | 0.3606 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 341.52 |  | 341.7629 | -0.0711 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 514.035 |  | 513.2038 | 0.162 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 293.4 |  | 291.7541 | 0.5641 | 293.89 | 291.35 | 4.7205 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 27.41 |  | 27.4925 | -0.3001 | 28.05 | 27.6 | 0.1459 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.43 |  | 36.3612 | -2.5609 | 37.365 | 36.4 | 0.0564 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.36 |  | 21.6563 | -1.3682 | 22.18 | 21.78 | 0.0468 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1483.12 |  | 1501.4171 | -1.2187 | 1549.47 | 1482.06 | 3.3713 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 485.875 |  | 483.8358 | 0.4215 | 498.04 | 480.14 | 2.0581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 785.38 |  | 777.3917 | 1.0276 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 256.63 |  | 255.0302 | 0.6273 | 258.07 | 252.62 | 0.0818 | watch_only | none |
| META | cloud_ai_capex | 677.09 |  | 673.4966 | 0.5335 | 680.09 | 667.1 | 0.0458 | watch_only | none |
| ARM | ai_accelerator | 258 |  | 259.6601 | -0.6393 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.96 |  | 164.6719 | -1.6468 | 168.11 | 162.41 | 2.7723 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
