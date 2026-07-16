# Intraday State

- Generated at: `2026-07-16T23:44:39+08:00`
- Market time ET: `2026-07-16T11:44:40-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'below_opening_15m_low': 23, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 5, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.23 |  | 710.5324 | -0.0426 | 713.55 | 708.25 | 0.0253 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 534.28 |  | 537.5156 | -0.602 | 543.4 | 535.47 | 0.0805 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.725 |  | 575.4288 | -0.4699 | 580.31 | 572.21 | 0.0716 | below_vwap | below_vwap |
| SPY | market_regime | 753.63 |  | 752.8357 | 0.1055 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.63 |  | 752.8357 | 0.1055 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.74 |  | 296.6247 | 0.0389 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 398.94 |  | 395.965 | 0.7513 | 398.69 | 392.2 | 0.1178 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.135 |  | 329.5181 | 0.4907 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.63 |  | 752.8357 | 0.1055 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.74 |  | 296.6247 | 0.0389 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 398.94 |  | 395.965 | 0.7513 | 398.69 | 392.2 | 0.1178 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.135 |  | 329.5181 | 0.4907 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 255.46 |  | 255.2438 | 0.0847 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 6 | META | cloud_ai_capex | 676.1 |  | 674.997 | 0.1634 | 680.09 | 667.1 | 0.3062 | watch_only | none |
| 7 | TT | data_center_power_cooling | 475.17 |  | 474.4023 | 0.1618 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | LIN | industrial_gases | 517.42 |  | 514.4816 | 0.5711 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ANET | ai_networking_optical | 167.57 |  | 166.2862 | 0.7721 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ONTO | semiconductor_test_packaging | 292.7 |  | 290.6109 | 0.7189 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | APD | industrial_gases | 296.69 |  | 294.4781 | 0.7511 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TSM | foundry | 410.12 |  | 411.3768 | -0.3055 | 414.385 | 406.61 | 0.061 | below_vwap | below_vwap |
| 13 | QQQ | market_regime | 710.23 |  | 710.5324 | -0.0426 | 713.55 | 708.25 | 0.0253 | below_vwap | below_vwap |
| 14 | SMH | semiconductor_index | 572.725 |  | 575.4288 | -0.4699 | 580.31 | 572.21 | 0.0716 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | AVGO | custom_silicon_networking | 381.84 |  | 381.8658 | -0.0068 | 386.58 | 378.53 | 0.3457 | below_vwap | below_vwap |
| 17 | KLAC | semiconductor_equipment | 221.19 |  | 222.7987 | -0.722 | 222.19 | 218.09 | 0.1673 | below_vwap | below_vwap |
| 18 | JCI | data_center_power_cooling | 140.695 |  | 140.7094 | -0.0102 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 632.51 |  | 633.2274 | -0.1133 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | GEV | data_center_power_cooling | 1030.765 |  | 1032.9449 | -0.211 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.63 |  | 752.8357 | 0.1055 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.74 |  | 296.6247 | 0.0389 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 398.94 |  | 395.965 | 0.7513 | 398.69 | 392.2 | 0.1178 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 331.135 |  | 329.5181 | 0.4907 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 475.17 |  | 474.4023 | 0.1618 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | LIN | industrial_gases | 517.42 |  | 514.4816 | 0.5711 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | APD | industrial_gases | 296.69 |  | 294.4781 | 0.7511 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | AMZN | cloud_ai_capex | 255.46 |  | 255.2438 | 0.0847 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 9 | META | cloud_ai_capex | 676.1 |  | 674.997 | 0.1634 | 680.09 | 667.1 | 0.3062 | watch_only | none |
| 10 | TSM | foundry | 410.12 |  | 411.3768 | -0.3055 | 414.385 | 406.61 | 0.061 | below_vwap | below_vwap |
| 11 | QQQ | market_regime | 710.23 |  | 710.5324 | -0.0426 | 713.55 | 708.25 | 0.0253 | below_vwap | below_vwap |
| 12 | AVGO | custom_silicon_networking | 381.84 |  | 381.8658 | -0.0068 | 386.58 | 378.53 | 0.3457 | below_vwap | below_vwap |
| 13 | VRT | data_center_power_cooling | 293.86 |  | 296.3659 | -0.8455 | 300.385 | 293.64 | 0.5275 | below_vwap | below_vwap,spread_too_wide |
| 14 | JCI | data_center_power_cooling | 140.695 |  | 140.7094 | -0.0102 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 632.51 |  | 633.2274 | -0.1133 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | GEV | data_center_power_cooling | 1030.765 |  | 1032.9449 | -0.211 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ASML | semiconductor_equipment | 1821.62 |  | 1825.7527 | -0.2264 | 1823.13 | 1796.26 | 4.754 | below_vwap | below_vwap,spread_too_wide |
| 18 | AMAT | semiconductor_equipment | 571.115 |  | 575.2305 | -0.7155 | 572.69 | 562.32 | 3.1062 | below_vwap | below_vwap,spread_too_wide |
| 19 | KLAC | semiconductor_equipment | 221.19 |  | 222.7987 | -0.722 | 222.19 | 218.09 | 0.1673 | below_vwap | below_vwap |
| 20 | LRCX | semiconductor_equipment | 324.385 |  | 327.1992 | -0.8601 | 328.96 | 324.11 | 3.3263 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.23 |  | 710.5324 | -0.0426 | 713.55 | 708.25 | 0.0253 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 72.07 |  | 72.2053 | -0.1874 | 73.09 | 71.45 | 0.0278 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.335 |  | 207.6371 | -0.1455 | 211.03 | 207.49 | 0.164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.94 |  | 395.965 | 0.7513 | 398.69 | 392.2 | 0.1178 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.135 |  | 329.5181 | 0.4907 | 328.98 | 326.885 | 0.0181 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.485 |  | 371.9968 | -0.1376 | 375.18 | 369.2 | 0.2692 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.5 |  | 510.3953 | -0.5673 | 518.33 | 507.62 | 0.2778 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 410.12 |  | 411.3768 | -0.3055 | 414.385 | 406.61 | 0.061 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.28 |  | 537.5156 | -0.602 | 543.4 | 535.47 | 0.0805 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.725 |  | 575.4288 | -0.4699 | 580.31 | 572.21 | 0.0716 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.84 |  | 381.8658 | -0.0068 | 386.58 | 378.53 | 0.3457 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 856.3 |  | 864.5682 | -0.9563 | 887.1 | 866.765 | 1.8685 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 190.86 |  | 193.8161 | -1.5252 | 201.61 | 194.19 | 0.1781 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 401.87 |  | 404.939 | -0.7579 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.66 |  | 46.3261 | -1.4378 | 47.65 | 46.165 | 0.0657 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.255 |  | 25.7206 | -1.8101 | 26.71 | 25.74 | 0.0396 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.63 |  | 752.8357 | 0.1055 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.74 |  | 296.6247 | 0.0389 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.465 |  | 127.1114 | -0.5085 | 131.36 | 126.665 | 0.4665 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.935 |  | 73.8996 | -1.3053 | 75.54 | 73.985 | 4.7988 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.86 |  | 296.3659 | -0.8455 | 300.385 | 293.64 | 0.5275 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 396.29 |  | 401.4879 | -1.2947 | 406.24 | 399.495 | 4.2797 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 632.51 |  | 633.2274 | -0.1133 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1030.765 |  | 1032.9449 | -0.211 | 1035.07 | 1021.09 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 475.17 |  | 474.4023 | 0.1618 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.695 |  | 140.7094 | -0.0102 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.57 |  | 166.2862 | 0.7721 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 279.07 |  | 283.8247 | -1.6752 | 288.48 | 280.67 | 3.7195 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 705.03 |  | 716.4673 | -1.5963 | 737.175 | 720.21 | 2.4112 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 394.84 |  | 398.3857 | -0.89 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 101.11 |  | 103.1504 | -1.9781 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.63 |  | 328.3609 | -2.6589 | 337.59 | 326.16 | 4.0641 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1821.62 |  | 1825.7527 | -0.2264 | 1823.13 | 1796.26 | 4.754 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 571.115 |  | 575.2305 | -0.7155 | 572.69 | 562.32 | 3.1062 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 324.385 |  | 327.1992 | -0.8601 | 328.96 | 324.11 | 3.3263 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 221.19 |  | 222.7987 | -0.722 | 222.19 | 218.09 | 0.1673 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 327.59 |  | 329.0069 | -0.4306 | 332.49 | 326.685 | 3.7883 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 292.7 |  | 290.6109 | 0.7189 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.36 |  | 64.6084 | -0.3844 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.64 |  | 52.6741 | -0.0647 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.98 |  | 136.0027 | -0.0167 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.89 |  | 341.2732 | -0.4053 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.42 |  | 514.4816 | 0.5711 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.69 |  | 294.4781 | 0.7511 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.7 |  | 27.3442 | -2.3559 | 28.05 | 27.6 | 0.0375 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.39 |  | 36.0551 | -1.8448 | 37.365 | 36.4 | 0.0848 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.205 |  | 21.5478 | -1.5911 | 22.18 | 21.78 | 0.1415 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1449.235 |  | 1488.916 | -2.6651 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 468.34 |  | 482.4358 | -2.9218 | 498.04 | 480.14 | 2.2526 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 765.31 |  | 776.9879 | -1.503 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 255.46 |  | 255.2438 | 0.0847 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| META | cloud_ai_capex | 676.1 |  | 674.997 | 0.1634 | 680.09 | 667.1 | 0.3062 | watch_only | none |
| ARM | ai_accelerator | 256.9 |  | 258.6094 | -0.661 | 265.96 | 258.1 | 3.8926 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 161.82 |  | 163.7805 | -1.197 | 168.11 | 162.41 | 3.7016 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
