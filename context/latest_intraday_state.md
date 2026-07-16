# Intraday State

- Generated at: `2026-07-16T23:24:27+08:00`
- Market time ET: `2026-07-16T11:24:28-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 18, 'below_opening_15m_low': 25, 'watch_only': 3, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.76 |  | 710.4625 | -0.0989 | 713.55 | 708.25 | 0.0409 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 534.06 |  | 537.7723 | -0.6903 | 543.4 | 535.47 | 0.0749 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.06 |  | 575.7434 | -0.6398 | 580.31 | 572.21 | 0.0629 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.345 |  | 752.7336 | 0.0812 | 753.51 | 751.13 | 0.0093 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.76 |  | 296.5977 | 0.0547 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 297.095 |  | 293.233 | 1.317 | 293.89 | 291.35 | 0.2087 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.54 |  | 329.3524 | 0.3606 | 328.98 | 326.885 | 0.0242 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.76 |  | 296.5977 | 0.0547 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.345 |  | 752.7336 | 0.0812 | 753.51 | 751.13 | 0.0093 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 330.54 |  | 329.3524 | 0.3606 | 328.98 | 326.885 | 0.0242 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.47 |  | 255.1986 | 0.1063 | 258.07 | 252.62 | 0.0274 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 398.61 |  | 395.6497 | 0.7482 | 398.69 | 392.2 | 0.1003 | watch_only | none |
| 6 | TT | data_center_power_cooling | 474.72 |  | 474.3011 | 0.0883 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ENTG | semiconductor_materials | 136.07 |  | 135.9783 | 0.0674 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 297.095 |  | 293.233 | 1.317 | 293.89 | 291.35 | 0.2087 | buy_precheck_manual_confirm | none |
| 9 | META | cloud_ai_capex | 675.555 |  | 674.8654 | 0.1022 | 680.09 | 667.1 | 0.5151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | GEV | data_center_power_cooling | 1036.37 |  | 1032.703 | 0.3551 | 1035.07 | 1021.09 | 1.1183 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | LIN | industrial_gases | 517.56 |  | 513.9177 | 0.7087 | 515.825 | 512.23 | 5.0893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 330.32 |  | 328.9677 | 0.4111 | 332.49 | 326.685 | 0.4026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 410.96 |  | 411.3934 | -0.1054 | 414.385 | 406.61 | 0.0487 | below_vwap | below_vwap |
| 14 | QQQ | market_regime | 709.76 |  | 710.4625 | -0.0989 | 713.55 | 708.25 | 0.0409 | below_vwap | below_vwap |
| 15 | ORCL | cloud_ai_capex | 126.75 |  | 127.1365 | -0.304 | 131.36 | 126.665 | 0.0789 | below_vwap | below_vwap |
| 16 | GOOGL | cloud_ai_capex | 371.73 |  | 372.0341 | -0.0817 | 375.18 | 369.2 | 0.0404 | below_vwap | below_vwap |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | VRT | data_center_power_cooling | 293.85 |  | 296.5393 | -0.9069 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | JCI | data_center_power_cooling | 140.665 |  | 140.6998 | -0.0247 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.76 |  | 296.5977 | 0.0547 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 297.095 |  | 293.233 | 1.317 | 293.89 | 291.35 | 0.2087 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.54 |  | 329.3524 | 0.3606 | 328.98 | 326.885 | 0.0242 | buy_precheck_manual_confirm | none |
| 4 | TT | data_center_power_cooling | 474.72 |  | 474.3011 | 0.0883 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | GEV | data_center_power_cooling | 1036.37 |  | 1032.703 | 0.3551 | 1035.07 | 1021.09 | 1.1183 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | LIN | industrial_gases | 517.56 |  | 513.9177 | 0.7087 | 515.825 | 512.23 | 5.0893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SPY | market_regime | 753.345 |  | 752.7336 | 0.0812 | 753.51 | 751.13 | 0.0093 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 398.61 |  | 395.6497 | 0.7482 | 398.69 | 392.2 | 0.1003 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 255.47 |  | 255.1986 | 0.1063 | 258.07 | 252.62 | 0.0274 | watch_only | none |
| 10 | TSM | foundry | 410.96 |  | 411.3934 | -0.1054 | 414.385 | 406.61 | 0.0487 | below_vwap | below_vwap |
| 11 | QQQ | market_regime | 709.76 |  | 710.4625 | -0.0989 | 713.55 | 708.25 | 0.0409 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 380.42 |  | 381.9029 | -0.3883 | 386.58 | 378.53 | 0.8017 | below_vwap | below_vwap,spread_too_wide |
| 13 | VRT | data_center_power_cooling | 293.85 |  | 296.5393 | -0.9069 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 140.665 |  | 140.6998 | -0.0247 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ASML | semiconductor_equipment | 1819.895 |  | 1826.0553 | -0.3374 | 1823.13 | 1796.26 | 0.7363 | below_vwap | below_vwap,spread_too_wide |
| 16 | AMAT | semiconductor_equipment | 570.875 |  | 575.4402 | -0.7933 | 572.69 | 562.32 | 3.7907 | below_vwap | below_vwap,spread_too_wide |
| 17 | ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | KLAC | semiconductor_equipment | 221.09 |  | 222.8761 | -0.8014 | 222.19 | 218.09 | 0.4885 | below_vwap | below_vwap,spread_too_wide |
| 19 | LRCX | semiconductor_equipment | 324.66 |  | 327.3819 | -0.8314 | 328.96 | 324.11 | 4.4416 | below_vwap | below_vwap,spread_too_wide |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.76 |  | 710.4625 | -0.0989 | 713.55 | 708.25 | 0.0409 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.9 |  | 72.1964 | -0.4106 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 206.42 |  | 207.6925 | -0.6127 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.61 |  | 395.6497 | 0.7482 | 398.69 | 392.2 | 0.1003 | watch_only | none |
| AAPL | mega_cap_platform | 330.54 |  | 329.3524 | 0.3606 | 328.98 | 326.885 | 0.0242 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.73 |  | 372.0341 | -0.0817 | 375.18 | 369.2 | 0.0404 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.03 |  | 510.5418 | -0.6879 | 518.33 | 507.62 | 0.4793 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 410.96 |  | 411.3934 | -0.1054 | 414.385 | 406.61 | 0.0487 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.06 |  | 537.7723 | -0.6903 | 543.4 | 535.47 | 0.0749 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.06 |  | 575.7434 | -0.6398 | 580.31 | 572.21 | 0.0629 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.42 |  | 381.9029 | -0.3883 | 386.58 | 378.53 | 0.8017 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 856.875 |  | 865.263 | -0.9694 | 887.1 | 866.765 | 0.7411 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 191.165 |  | 194.1064 | -1.5154 | 201.61 | 194.19 | 0.7533 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 403.49 |  | 405.0895 | -0.3949 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.96 |  | 46.4353 | -1.0235 | 47.65 | 46.165 | 0.0435 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.285 |  | 25.7756 | -1.9034 | 26.71 | 25.74 | 0.0395 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.345 |  | 752.7336 | 0.0812 | 753.51 | 751.13 | 0.0093 | watch_only | none |
| IWM | market_regime | 296.76 |  | 296.5977 | 0.0547 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.75 |  | 127.1365 | -0.304 | 131.36 | 126.665 | 0.0789 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.205 |  | 73.9567 | -1.0164 | 75.54 | 73.985 | 0.3688 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.85 |  | 296.5393 | -0.9069 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 396.46 |  | 401.6977 | -1.3039 | 406.24 | 399.495 | 0.116 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 630.055 |  | 633.3316 | -0.5174 | 640.25 | 631.005 | 0.1873 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GEV | data_center_power_cooling | 1036.37 |  | 1032.703 | 0.3551 | 1035.07 | 1021.09 | 1.1183 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 474.72 |  | 474.3011 | 0.0883 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.665 |  | 140.6998 | -0.0247 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 164.63 |  | 166.2746 | -0.9891 | 169.91 | 165.6 | 2.2535 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 276.96 |  | 284.1111 | -2.517 | 288.48 | 280.67 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 702.305 |  | 718.2831 | -2.2245 | 737.175 | 720.21 | 3.4031 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 394.35 |  | 398.689 | -1.0883 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.89 |  | 103.302 | -2.3349 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 323.73 |  | 328.775 | -1.5345 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1819.895 |  | 1826.0553 | -0.3374 | 1823.13 | 1796.26 | 0.7363 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 570.875 |  | 575.4402 | -0.7933 | 572.69 | 562.32 | 3.7907 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 324.66 |  | 327.3819 | -0.8314 | 328.96 | 324.11 | 4.4416 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 221.09 |  | 222.8761 | -0.8014 | 222.19 | 218.09 | 0.4885 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 330.32 |  | 328.9677 | 0.4111 | 332.49 | 326.685 | 0.4026 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.24 |  | 64.6353 | -0.6116 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.61 |  | 52.6668 | -0.1078 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 136.07 |  | 135.9783 | 0.0674 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 340.36 |  | 341.3012 | -0.2758 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.56 |  | 513.9177 | 0.7087 | 515.825 | 512.23 | 5.0893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.095 |  | 293.233 | 1.317 | 293.89 | 291.35 | 0.2087 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.91 |  | 27.4153 | -1.843 | 28.05 | 27.6 | 0.0743 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.615 |  | 36.0892 | -1.3139 | 37.365 | 36.4 | 0.0281 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.285 |  | 21.5662 | -1.3038 | 22.18 | 21.78 | 0.1409 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1460.525 |  | 1491.517 | -2.0779 | 1549.47 | 1482.06 | 4.7928 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 473.4 |  | 483.4747 | -2.0838 | 498.04 | 480.14 | 3.5002 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 768.005 |  | 777.8506 | -1.2657 | 797.155 | 768.7 | 0.25 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 255.47 |  | 255.1986 | 0.1063 | 258.07 | 252.62 | 0.0274 | watch_only | none |
| META | cloud_ai_capex | 675.555 |  | 674.8654 | 0.1022 | 680.09 | 667.1 | 0.5151 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 256.49 |  | 258.7963 | -0.8912 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.595 |  | 163.9293 | -2.034 | 168.11 | 162.41 | 2.1732 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
