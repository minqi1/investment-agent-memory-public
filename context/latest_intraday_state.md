# Intraday State

- Generated at: `2026-07-16T23:48:38+08:00`
- Market time ET: `2026-07-16T11:48:39-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 16, 'below_opening_15m_low': 28, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 2, 'watch_only': 2, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.69 |  | 710.5187 | -0.1166 | 713.55 | 708.25 | 0.0211 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 532.99 |  | 537.4165 | -0.8237 | 543.4 | 535.47 | 0.0582 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 571.575 |  | 575.2326 | -0.6358 | 580.31 | 572.21 | 0.0682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.16 |  | 752.8456 | 0.0418 | 753.51 | 751.13 | 0.0066 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.115 |  | 396.0214 | 0.7812 | 398.69 | 392.2 | 0.1428 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.535 |  | 329.5437 | 0.6043 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.115 |  | 396.0214 | 0.7812 | 398.69 | 392.2 | 0.1428 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.16 |  | 752.8456 | 0.0418 | 753.51 | 751.13 | 0.0066 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 331.535 |  | 329.5437 | 0.6043 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.8 |  | 255.2472 | 0.2166 | 258.07 | 252.62 | 0.0899 | watch_only | none |
| 5 | TT | data_center_power_cooling | 475.27 |  | 474.4082 | 0.1817 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | LIN | industrial_gases | 517.46 |  | 514.5536 | 0.5648 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ONTO | semiconductor_test_packaging | 292.7 |  | 290.6109 | 0.7189 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | META | cloud_ai_capex | 676.78 |  | 675.0235 | 0.2602 | 680.09 | 667.1 | 0.9604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APD | industrial_gases | 296.585 |  | 294.4962 | 0.7093 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ANET | ai_networking_optical | 167.27 |  | 166.2916 | 0.5884 | 169.91 | 165.6 | 4.5196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | IWM | market_regime | 296.315 |  | 296.6215 | -0.1033 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 12 | TSM | foundry | 410.37 |  | 411.3516 | -0.2386 | 414.385 | 406.61 | 0.1267 | below_vwap | below_vwap |
| 13 | QQQ | market_regime | 709.69 |  | 710.5187 | -0.1166 | 713.55 | 708.25 | 0.0211 | below_vwap | below_vwap |
| 14 | ASML | semiconductor_equipment | 1817.68 |  | 1825.6602 | -0.4371 | 1823.13 | 1796.26 | 0.1161 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 140.565 |  | 140.7065 | -0.1006 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 371.58 |  | 371.9941 | -0.1113 | 375.18 | 369.2 | 0.2584 | below_vwap | below_vwap |
| 18 | MKSI | semiconductor_materials | 338.96 |  | 341.203 | -0.6574 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ENTG | semiconductor_materials | 135.155 |  | 135.9787 | -0.6057 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | AMKR | semiconductor_test_packaging | 64.08 |  | 64.6012 | -0.8069 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.115 |  | 396.0214 | 0.7812 | 398.69 | 392.2 | 0.1428 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.535 |  | 329.5437 | 0.6043 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.315 |  | 296.6215 | -0.1033 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 4 | TT | data_center_power_cooling | 475.27 |  | 474.4082 | 0.1817 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 517.46 |  | 514.5536 | 0.5648 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 296.585 |  | 294.4962 | 0.7093 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SPY | market_regime | 753.16 |  | 752.8456 | 0.0418 | 753.51 | 751.13 | 0.0066 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 255.8 |  | 255.2472 | 0.2166 | 258.07 | 252.62 | 0.0899 | watch_only | none |
| 9 | TSM | foundry | 410.37 |  | 411.3516 | -0.2386 | 414.385 | 406.61 | 0.1267 | below_vwap | below_vwap |
| 10 | QQQ | market_regime | 709.69 |  | 710.5187 | -0.1166 | 713.55 | 708.25 | 0.0211 | below_vwap | below_vwap |
| 11 | AVGO | custom_silicon_networking | 381.25 |  | 381.8585 | -0.1594 | 386.58 | 378.53 | 0.9941 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 140.565 |  | 140.7065 | -0.1006 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1027.575 |  | 1032.8165 | -0.5075 | 1035.07 | 1021.09 | 2.8066 | below_vwap | below_vwap,spread_too_wide |
| 14 | ASML | semiconductor_equipment | 1817.68 |  | 1825.6602 | -0.4371 | 1823.13 | 1796.26 | 0.1161 | below_vwap | below_vwap |
| 15 | AMAT | semiconductor_equipment | 569.96 |  | 575.0743 | -0.8893 | 572.69 | 562.32 | 3.1002 | below_vwap | below_vwap,spread_too_wide |
| 16 | KLAC | semiconductor_equipment | 220.8 |  | 222.7693 | -0.884 | 222.19 | 218.09 | 0.4121 | below_vwap | below_vwap,spread_too_wide |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 338.96 |  | 341.203 | -0.6574 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | DELL | ai_server_oem | 401.32 |  | 404.8078 | -0.8616 | 411.65 | 400.635 | 4.7618 | below_vwap | below_vwap,spread_too_wide |
| 20 | ENTG | semiconductor_materials | 135.155 |  | 135.9787 | -0.6057 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.69 |  | 710.5187 | -0.1166 | 713.55 | 708.25 | 0.0211 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.86 |  | 72.2001 | -0.4711 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.2 |  | 207.6281 | -0.2062 | 211.03 | 207.49 | 0.1351 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 399.115 |  | 396.0214 | 0.7812 | 398.69 | 392.2 | 0.1428 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.535 |  | 329.5437 | 0.6043 | 328.98 | 326.885 | 0.0151 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.58 |  | 371.9941 | -0.1113 | 375.18 | 369.2 | 0.2584 | below_vwap | below_vwap |
| AMD | ai_accelerator | 505.74 |  | 510.3245 | -0.8983 | 518.33 | 507.62 | 0.2135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 410.37 |  | 411.3516 | -0.2386 | 414.385 | 406.61 | 0.1267 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 532.99 |  | 537.4165 | -0.8237 | 543.4 | 535.47 | 0.0582 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 571.575 |  | 575.2326 | -0.6358 | 580.31 | 572.21 | 0.0682 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 381.25 |  | 381.8585 | -0.1594 | 386.58 | 378.53 | 0.9941 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.88 |  | 864.0949 | -1.7608 | 887.1 | 866.765 | 0.7657 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 189.95 |  | 193.7631 | -1.9679 | 201.61 | 194.19 | 0.8318 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.32 |  | 404.8078 | -0.8616 | 411.65 | 400.635 | 4.7618 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.58 |  | 46.2695 | -1.4901 | 47.65 | 46.165 | 0.0439 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.185 |  | 25.6951 | -1.9852 | 26.71 | 25.74 | 0.0397 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.16 |  | 752.8456 | 0.0418 | 753.51 | 751.13 | 0.0066 | watch_only | none |
| IWM | market_regime | 296.315 |  | 296.6215 | -0.1033 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.06 |  | 127.0901 | -0.8105 | 131.36 | 126.665 | 3.2921 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.49 |  | 73.8579 | -1.8521 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 292.205 |  | 296.2934 | -1.3798 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 395.585 |  | 401.4536 | -1.4618 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 630.85 |  | 633.1918 | -0.3698 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1027.575 |  | 1032.8165 | -0.5075 | 1035.07 | 1021.09 | 2.8066 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.27 |  | 474.4082 | 0.1817 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.565 |  | 140.7065 | -0.1006 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.27 |  | 166.2916 | 0.5884 | 169.91 | 165.6 | 4.5196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 277.86 |  | 283.7589 | -2.0788 | 288.48 | 280.67 | 3.6241 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 698.96 |  | 716.0467 | -2.3863 | 737.175 | 720.21 | 2.8385 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 393.75 |  | 398.2728 | -1.1356 | 410 | 397.68 | 5.0083 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 100.34 |  | 103.1131 | -2.6894 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.37 |  | 328.1226 | -2.6675 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1817.68 |  | 1825.6602 | -0.4371 | 1823.13 | 1796.26 | 0.1161 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 569.96 |  | 575.0743 | -0.8893 | 572.69 | 562.32 | 3.1002 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 323.58 |  | 327.1464 | -1.0901 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 220.8 |  | 222.7693 | -0.884 | 222.19 | 218.09 | 0.4121 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 326.4 |  | 328.9819 | -0.7848 | 332.49 | 326.685 | 3.5815 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 292.7 |  | 290.6109 | 0.7189 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.08 |  | 64.6012 | -0.8069 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.64 |  | 52.6741 | -0.0647 | 52.72 | 51.735 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.155 |  | 135.9787 | -0.6057 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 338.96 |  | 341.203 | -0.6574 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.46 |  | 514.5536 | 0.5648 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.585 |  | 294.4962 | 0.7093 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.57 |  | 27.3276 | -2.7722 | 28.05 | 27.6 | 0.0753 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.21 |  | 36.011 | -2.2243 | 37.365 | 36.4 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.04 |  | 21.5418 | -2.3293 | 22.18 | 21.78 | 0.0475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1440.96 |  | 1487.2373 | -3.1116 | 1549.47 | 1482.06 | 2.9085 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 467.57 |  | 482.129 | -3.0197 | 498.04 | 480.14 | 1.4287 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 762.26 |  | 776.6643 | -1.8546 | 797.155 | 768.7 | 0.2873 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 255.8 |  | 255.2472 | 0.2166 | 258.07 | 252.62 | 0.0899 | watch_only | none |
| META | cloud_ai_capex | 676.78 |  | 675.0235 | 0.2602 | 680.09 | 667.1 | 0.9604 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 255.785 |  | 258.5436 | -1.067 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.71 |  | 163.6923 | -1.8219 | 168.11 | 162.41 | 1.2134 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
