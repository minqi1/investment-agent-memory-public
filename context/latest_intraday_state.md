# Intraday State

- Generated at: `2026-07-16T22:53:57+08:00`
- Market time ET: `2026-07-16T10:53:59-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 17, 'below_opening_15m_low': 21, 'watch_only': 3, 'manual_confirm_candidate': 3, 'spread_too_wide_or_missing': 11, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.37 |  | 710.6002 | -0.0324 | 713.55 | 708.25 | 0.0084 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 535.17 |  | 538.294 | -0.5804 | 543.4 | 535.47 | 0.0803 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 573.1 |  | 576.2065 | -0.5391 | 580.31 | 572.21 | 0.0646 | below_vwap | below_vwap |
| SPY | market_regime | 753.8 |  | 752.6047 | 0.1588 | 753.51 | 751.13 | 0.0279 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.8 |  | 752.6047 | 0.1588 | 753.51 | 751.13 | 0.0279 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.06 |  | 296.5518 | 0.1714 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.28 |  | 329.185 | 0.3326 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.8 |  | 752.6047 | 0.1588 | 753.51 | 751.13 | 0.0279 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.06 |  | 296.5518 | 0.1714 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.28 |  | 329.185 | 0.3326 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 373.1 |  | 372.0211 | 0.29 | 375.18 | 369.2 | 0.2546 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 396.82 |  | 395.3198 | 0.3795 | 398.69 | 392.2 | 0.189 | watch_only | none |
| 6 | META | cloud_ai_capex | 678.115 |  | 673.9604 | 0.6164 | 680.09 | 667.1 | 0.3451 | watch_only | none |
| 7 | PWR | data_center_power_cooling | 635 |  | 633.5495 | 0.2289 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | LIN | industrial_gases | 513.535 |  | 513.2332 | 0.0588 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ENTG | semiconductor_materials | 136.16 |  | 135.9426 | 0.1599 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TT | data_center_power_cooling | 475.58 |  | 474.0142 | 0.3303 | 474.085 | 467.64 | 4.7458 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | JCI | data_center_power_cooling | 141.23 |  | 140.6273 | 0.4285 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | GEV | data_center_power_cooling | 1037.85 |  | 1030.2175 | 0.7409 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TSM | foundry | 412.885 |  | 411.4763 | 0.3424 | 414.385 | 406.61 | 2.4704 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 329.85 |  | 328.7089 | 0.3472 | 332.49 | 326.685 | 0.5396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | APD | industrial_gases | 293.46 |  | 291.9923 | 0.5027 | 293.89 | 291.35 | 4.7979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | QQQ | market_regime | 710.37 |  | 710.6002 | -0.0324 | 713.55 | 708.25 | 0.0084 | below_vwap | below_vwap |
| 18 | SMH | semiconductor_index | 573.1 |  | 576.2065 | -0.5391 | 580.31 | 572.21 | 0.0646 | below_vwap | below_vwap |
| 19 | AMZN | cloud_ai_capex | 254.76 |  | 255.1975 | -0.1714 | 258.07 | 252.62 | 0.0236 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.8 |  | 752.6047 | 0.1588 | 753.51 | 751.13 | 0.0279 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.06 |  | 296.5518 | 0.1714 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.28 |  | 329.185 | 0.3326 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | AMAT | semiconductor_equipment | 574.47 |  | 575.7073 | -0.2149 | 572.69 | 562.32 | 0.3882 | below_vwap | below_vwap,spread_too_wide |
| 5 | TT | data_center_power_cooling | 475.58 |  | 474.0142 | 0.3303 | 474.085 | 467.64 | 4.7458 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | JCI | data_center_power_cooling | 141.23 |  | 140.6273 | 0.4285 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | GEV | data_center_power_cooling | 1037.85 |  | 1030.2175 | 0.7409 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | MSFT | cloud_ai_capex | 396.82 |  | 395.3198 | 0.3795 | 398.69 | 392.2 | 0.189 | watch_only | none |
| 10 | GOOGL | cloud_ai_capex | 373.1 |  | 372.0211 | 0.29 | 375.18 | 369.2 | 0.2546 | watch_only | none |
| 11 | META | cloud_ai_capex | 678.115 |  | 673.9604 | 0.6164 | 680.09 | 667.1 | 0.3451 | watch_only | none |
| 12 | QQQ | market_regime | 710.37 |  | 710.6002 | -0.0324 | 713.55 | 708.25 | 0.0084 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 381.54 |  | 382.1459 | -0.1585 | 386.58 | 378.53 | 0.7863 | below_vwap | below_vwap,spread_too_wide |
| 14 | VRT | data_center_power_cooling | 296.09 |  | 296.8116 | -0.2431 | 300.385 | 293.64 | 3.8671 | below_vwap | below_vwap,spread_too_wide |
| 15 | ASML | semiconductor_equipment | 1813.425 |  | 1827.3144 | -0.7601 | 1823.13 | 1796.26 | 0.6882 | below_vwap | below_vwap,spread_too_wide |
| 16 | ONTO | semiconductor_test_packaging | 290.445 |  | 290.5368 | -0.0316 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | KLAC | semiconductor_equipment | 222.04 |  | 222.984 | -0.4233 | 222.19 | 218.09 | 2.0942 | below_vwap | below_vwap,spread_too_wide |
| 18 | LRCX | semiconductor_equipment | 325.79 |  | 327.9072 | -0.6457 | 328.96 | 324.11 | 0.2026 | below_vwap | below_vwap |
| 19 | SMH | semiconductor_index | 573.1 |  | 576.2065 | -0.5391 | 580.31 | 572.21 | 0.0646 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.37 |  | 710.6002 | -0.0324 | 713.55 | 708.25 | 0.0084 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 72.06 |  | 72.2159 | -0.2158 | 73.09 | 71.45 | 0.0278 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 206.99 |  | 208.3286 | -0.6425 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 396.82 |  | 395.3198 | 0.3795 | 398.69 | 392.2 | 0.189 | watch_only | none |
| AAPL | mega_cap_platform | 330.28 |  | 329.185 | 0.3326 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 373.1 |  | 372.0211 | 0.29 | 375.18 | 369.2 | 0.2546 | watch_only | none |
| AMD | ai_accelerator | 507.29 |  | 511.0241 | -0.7307 | 518.33 | 507.62 | 1.2715 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 412.885 |  | 411.4763 | 0.3424 | 414.385 | 406.61 | 2.4704 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 535.17 |  | 538.294 | -0.5804 | 543.4 | 535.47 | 0.0803 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 573.1 |  | 576.2065 | -0.5391 | 580.31 | 572.21 | 0.0646 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.54 |  | 382.1459 | -0.1585 | 386.58 | 378.53 | 0.7863 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 859.29 |  | 867.1118 | -0.9021 | 887.1 | 866.765 | 1.3069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 191.505 |  | 195.0532 | -1.8191 | 201.61 | 194.19 | 2.7258 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 404.99 |  | 405.7663 | -0.1913 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46 |  | 46.6501 | -1.3935 | 47.65 | 46.165 | 0.0435 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.6 |  | 25.897 | -1.147 | 26.71 | 25.74 | 0.0391 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.8 |  | 752.6047 | 0.1588 | 753.51 | 751.13 | 0.0279 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.06 |  | 296.5518 | 0.1714 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.43 |  | 127.3022 | -0.6852 | 131.36 | 126.665 | 0.3006 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.65 |  | 74.0748 | -0.5735 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 296.09 |  | 296.8116 | -0.2431 | 300.385 | 293.64 | 3.8671 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 398.585 |  | 402.4786 | -0.9674 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635 |  | 633.5495 | 0.2289 | 640.25 | 631.005 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1037.85 |  | 1030.2175 | 0.7409 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 475.58 |  | 474.0142 | 0.3303 | 474.085 | 467.64 | 4.7458 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.23 |  | 140.6273 | 0.4285 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.44 |  | 166.3722 | -0.5603 | 169.91 | 165.6 | 1.8133 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 280.07 |  | 284.8306 | -1.6714 | 288.48 | 280.67 | 2.6351 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 715.085 |  | 721.8174 | -0.9327 | 737.175 | 720.21 | 0.1035 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 394.69 |  | 399.7183 | -1.258 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.775 |  | 103.7692 | -1.9217 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.39 |  | 329.4619 | -0.9324 | 337.59 | 326.16 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1813.425 |  | 1827.3144 | -0.7601 | 1823.13 | 1796.26 | 0.6882 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 574.47 |  | 575.7073 | -0.2149 | 572.69 | 562.32 | 0.3882 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 325.79 |  | 327.9072 | -0.6457 | 328.96 | 324.11 | 0.2026 | below_vwap | below_vwap |
| KLAC | semiconductor_equipment | 222.04 |  | 222.984 | -0.4233 | 222.19 | 218.09 | 2.0942 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 329.85 |  | 328.7089 | 0.3472 | 332.49 | 326.685 | 0.5396 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 290.445 |  | 290.5368 | -0.0316 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.22 |  | 64.7848 | -0.8718 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.16 |  | 135.9426 | 0.1599 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 340.69 |  | 341.6368 | -0.2771 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 513.535 |  | 513.2332 | 0.0588 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 293.46 |  | 291.9923 | 0.5027 | 293.89 | 291.35 | 4.7979 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 27.35 |  | 27.486 | -0.4946 | 28.05 | 27.6 | 0.1828 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.47 |  | 36.2902 | -2.2602 | 37.365 | 36.4 | 0.0282 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.29 |  | 21.6119 | -1.4895 | 22.18 | 21.78 | 0.0939 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1474.94 |  | 1500.0751 | -1.6756 | 1549.47 | 1482.06 | 1.0122 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 483.56 |  | 484.1101 | -0.1136 | 498.04 | 480.14 | 0.9203 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 786.01 |  | 778.0769 | 1.0196 | 797.155 | 768.7 | 0.7379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 254.76 |  | 255.1975 | -0.1714 | 258.07 | 252.62 | 0.0236 | below_vwap | below_vwap |
| META | cloud_ai_capex | 678.115 |  | 673.9604 | 0.6164 | 680.09 | 667.1 | 0.3451 | watch_only | none |
| ARM | ai_accelerator | 256.295 |  | 259.4045 | -1.1987 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.715 |  | 164.588 | -1.7456 | 168.11 | 162.41 | 1.5892 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
