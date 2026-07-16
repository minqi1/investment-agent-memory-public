# Intraday State

- Generated at: `2026-07-17T01:27:53+08:00`
- Market time ET: `2026-07-16T13:27:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'manual_confirm_candidate': 4, 'below_vwap': 9, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.54 |  | 709.8631 | -0.3273 | 713.55 | 708.25 | 0.0396 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.68 |  | 535.3799 | -1.2514 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.755 |  | 573.1692 | -0.9446 | 580.31 | 572.21 | 0.0352 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.43 |  | 752.7212 | -0.0387 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.1 |  | 474.2873 | 0.1713 | 474.085 | 467.64 | 0.1705 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.16 |  | 294.8637 | 0.1005 | 293.89 | 291.35 | 0.1118 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 403.265 |  | 398.0088 | 1.3206 | 398.69 | 392.2 | 0.0694 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 332.755 |  | 330.1944 | 0.7755 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.1 |  | 474.2873 | 0.1713 | 474.085 | 467.64 | 0.1705 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.16 |  | 294.8637 | 0.1005 | 293.89 | 291.35 | 0.1118 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 332.755 |  | 330.1944 | 0.7755 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 256.525 |  | 255.5291 | 0.3897 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 403.265 |  | 398.0088 | 1.3206 | 398.69 | 392.2 | 0.0694 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 140.63 |  | 140.544 | 0.0612 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | LIN | industrial_gases | 515.61 |  | 514.9303 | 0.132 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ANET | ai_networking_optical | 167.215 |  | 166.4486 | 0.4604 | 169.91 | 165.6 | 1.1781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | ASML | semiconductor_equipment | 1801.12 |  | 1821.5238 | -1.1202 | 1823.13 | 1796.26 | 0.0961 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 752.43 |  | 752.7212 | -0.0387 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 11 | IWM | market_regime | 295.55 |  | 296.3738 | -0.2779 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GOOGL | cloud_ai_capex | 371.68 |  | 371.8549 | -0.047 | 375.18 | 369.2 | 0.3255 | below_vwap | below_vwap |
| 14 | ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | AMAT | semiconductor_equipment | 563.54 |  | 572.2771 | -1.5267 | 572.69 | 562.32 | 1.9999 | below_vwap | below_vwap,spread_too_wide |
| 16 | KLAC | semiconductor_equipment | 218.81 |  | 221.4078 | -1.1733 | 222.19 | 218.09 | 0.6581 | below_vwap | below_vwap,spread_too_wide |
| 17 | META | cloud_ai_capex | 669.705 |  | 672.8566 | -0.4684 | 680.09 | 667.1 | 1.9994 | below_vwap | below_vwap,spread_too_wide |
| 18 | SOXX | semiconductor_index | 528.68 |  | 535.3799 | -1.2514 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | TSM | foundry | 405.91 |  | 410.0095 | -0.9999 | 414.385 | 406.61 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 707.54 |  | 709.8631 | -0.3273 | 713.55 | 708.25 | 0.0396 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.1 |  | 474.2873 | 0.1713 | 474.085 | 467.64 | 0.1705 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 295.16 |  | 294.8637 | 0.1005 | 293.89 | 291.35 | 0.1118 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 403.265 |  | 398.0088 | 1.3206 | 398.69 | 392.2 | 0.0694 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 332.755 |  | 330.1944 | 0.7755 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 256.525 |  | 255.5291 | 0.3897 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| 6 | ASML | semiconductor_equipment | 1801.12 |  | 1821.5238 | -1.1202 | 1823.13 | 1796.26 | 0.0961 | below_vwap | below_vwap |
| 7 | AMAT | semiconductor_equipment | 563.54 |  | 572.2771 | -1.5267 | 572.69 | 562.32 | 1.9999 | below_vwap | below_vwap,spread_too_wide |
| 8 | KLAC | semiconductor_equipment | 218.81 |  | 221.4078 | -1.1733 | 222.19 | 218.09 | 0.6581 | below_vwap | below_vwap,spread_too_wide |
| 9 | SPY | market_regime | 752.43 |  | 752.7212 | -0.0387 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.55 |  | 296.3738 | -0.2779 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GOOGL | cloud_ai_capex | 371.68 |  | 371.8549 | -0.047 | 375.18 | 369.2 | 0.3255 | below_vwap | below_vwap |
| 14 | META | cloud_ai_capex | 669.705 |  | 672.8566 | -0.4684 | 680.09 | 667.1 | 1.9994 | below_vwap | below_vwap,spread_too_wide |
| 15 | ANET | ai_networking_optical | 167.215 |  | 166.4486 | 0.4604 | 169.91 | 165.6 | 1.1781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | JCI | data_center_power_cooling | 140.63 |  | 140.544 | 0.0612 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | LIN | industrial_gases | 515.61 |  | 514.9303 | 0.132 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SOXX | semiconductor_index | 528.68 |  | 535.3799 | -1.2514 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | TSM | foundry | 405.91 |  | 410.0095 | -0.9999 | 414.385 | 406.61 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | CIEN | ai_networking_optical | 390.35 |  | 396.0854 | -1.448 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.54 |  | 709.8631 | -0.3273 | 713.55 | 708.25 | 0.0396 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.36 |  | 72.0033 | -0.8934 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.265 |  | 207.4857 | -0.1064 | 211.03 | 207.49 | 0.4246 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 403.265 |  | 398.0088 | 1.3206 | 398.69 | 392.2 | 0.0694 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 332.755 |  | 330.1944 | 0.7755 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.68 |  | 371.8549 | -0.047 | 375.18 | 369.2 | 0.3255 | below_vwap | below_vwap |
| AMD | ai_accelerator | 497.13 |  | 506.5346 | -1.8567 | 518.33 | 507.62 | 1.1224 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.91 |  | 410.0095 | -0.9999 | 414.385 | 406.61 | 0.0739 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.68 |  | 535.3799 | -1.2514 | 543.4 | 535.47 | 0.0681 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.755 |  | 573.1692 | -0.9446 | 580.31 | 572.21 | 0.0352 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 377.52 |  | 380.8773 | -0.8815 | 386.58 | 378.53 | 0.9298 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.62 |  | 859.2794 | -1.2405 | 887.1 | 866.765 | 1.2703 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.67 |  | 192.127 | -2.3198 | 201.61 | 194.19 | 0.5062 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 400.62 |  | 403.2215 | -0.6452 | 411.65 | 400.635 | 4.0487 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.45 |  | 45.983 | -1.159 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.13 |  | 25.4518 | -1.2642 | 26.71 | 25.74 | 0.0398 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.43 |  | 752.7212 | -0.0387 | 753.51 | 751.13 | 0.0053 | below_vwap | below_vwap |
| IWM | market_regime | 295.55 |  | 296.3738 | -0.2779 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.48 |  | 126.7416 | -0.2064 | 131.36 | 126.665 | 0.0395 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.18 |  | 73.4925 | -0.4252 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 291.19 |  | 294.5649 | -1.1457 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 394.25 |  | 399.7551 | -1.3771 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.925 |  | 631.9819 | -0.6419 | 640.25 | 631.005 | 0.7373 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1019.41 |  | 1028.8501 | -0.9175 | 1035.07 | 1021.09 | 4.79 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.1 |  | 474.2873 | 0.1713 | 474.085 | 467.64 | 0.1705 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 140.63 |  | 140.544 | 0.0612 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.215 |  | 166.4486 | 0.4604 | 169.91 | 165.6 | 1.1781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.13 |  | 281.8379 | -1.6704 | 288.48 | 280.67 | 2.1614 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.33 |  | 710.5092 | -1.8549 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 390.35 |  | 396.0854 | -1.448 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.83 |  | 101.9672 | -3.0767 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 315.18 |  | 324.099 | -2.752 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1801.12 |  | 1821.5238 | -1.1202 | 1823.13 | 1796.26 | 0.0961 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 563.54 |  | 572.2771 | -1.5267 | 572.69 | 562.32 | 1.9999 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.81 |  | 324.7421 | -1.8267 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.81 |  | 221.4078 | -1.1733 | 222.19 | 218.09 | 0.6581 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.7 |  | 327.3746 | -1.4279 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 282.045 |  | 288.8133 | -2.3435 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.645 |  | 64.2455 | -2.4912 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.16 |  | 52.2255 | -2.0401 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.8 |  | 135.123 | -0.9791 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 331.915 |  | 338.2811 | -1.8819 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 515.61 |  | 514.9303 | 0.132 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.16 |  | 294.8637 | 0.1005 | 293.89 | 291.35 | 0.1118 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.24 |  | 26.9897 | -2.7778 | 28.05 | 27.6 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.76 |  | 35.6675 | -2.5444 | 37.365 | 36.4 | 0.0288 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.79 |  | 21.2909 | -2.3526 | 22.18 | 21.78 | 0.0962 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1431.26 |  | 1472.8602 | -2.8245 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 456.92 |  | 476.6969 | -4.1487 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 748.04 |  | 768.1618 | -2.6195 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 256.525 |  | 255.5291 | 0.3897 | 258.07 | 252.62 | 0.0156 | watch_only | none |
| META | cloud_ai_capex | 669.705 |  | 672.8566 | -0.4684 | 680.09 | 667.1 | 1.9994 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 254.54 |  | 257.4119 | -1.1157 | 265.96 | 258.1 | 3.9287 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.22 |  | 162.7947 | -4.0387 | 168.11 | 162.41 | 0.6337 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
