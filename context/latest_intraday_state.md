# Intraday State

- Generated at: `2026-07-17T02:39:38+08:00`
- Market time ET: `2026-07-16T14:39:39-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_vwap': 8, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.48 |  | 709.428 | -0.4156 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 528.56 |  | 533.8983 | -0.9999 | 543.4 | 535.47 | 0.053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.36 |  | 571.9644 | -0.805 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.61 |  | 752.4121 | -0.2395 | 753.51 | 751.13 | 0.0187 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.66 |  | 399.302 | 1.3418 | 398.69 | 392.2 | 0.1087 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.81 |  | 330.6191 | 0.3602 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.81 |  | 330.6191 | 0.3602 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 404.66 |  | 399.302 | 1.3418 | 398.69 | 392.2 | 0.1087 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 140.52 |  | 140.5166 | 0.0024 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | LIN | industrial_gases | 517.67 |  | 515.1268 | 0.4937 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 296.035 |  | 294.9417 | 0.3707 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ANET | ai_networking_optical | 167.44 |  | 166.5743 | 0.5197 | 169.91 | 165.6 | 3.5177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1796.46 |  | 1818.5363 | -1.214 | 1823.13 | 1796.26 | 0.103 | below_vwap | below_vwap |
| 8 | IWM | market_regime | 295.33 |  | 296.162 | -0.2809 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 9 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 10 | TT | data_center_power_cooling | 473.18 |  | 474.1684 | -0.2084 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 133.83 |  | 134.9765 | -0.8494 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | GEV | data_center_power_cooling | 1021.68 |  | 1027.559 | -0.5721 | 1035.07 | 1021.09 | 2.1983 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 219.95 |  | 221.0042 | -0.477 | 222.19 | 218.09 | 1.2139 | below_vwap | below_vwap,spread_too_wide |
| 14 | META | cloud_ai_capex | 667.81 |  | 671.6224 | -0.5676 | 680.09 | 667.1 | 2.5546 | below_vwap | below_vwap,spread_too_wide |
| 15 | SOXX | semiconductor_index | 528.56 |  | 533.8983 | -0.9999 | 543.4 | 535.47 | 0.053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | QQQ | market_regime | 706.48 |  | 709.428 | -0.4156 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | NVDA | ai_accelerator | 206.83 |  | 207.3588 | -0.255 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | ETN | data_center_power_cooling | 394.79 |  | 399.3414 | -1.1397 | 406.24 | 399.495 | 0.1317 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMH | semiconductor_index | 567.36 |  | 571.9644 | -0.805 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | SPY | market_regime | 750.61 |  | 752.4121 | -0.2395 | 753.51 | 751.13 | 0.0187 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 404.66 |  | 399.302 | 1.3418 | 398.69 | 392.2 | 0.1087 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.81 |  | 330.6191 | 0.3602 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 517.67 |  | 515.1268 | 0.4937 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.035 |  | 294.9417 | 0.3707 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 473.18 |  | 474.1684 | -0.2084 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 6 | GEV | data_center_power_cooling | 1021.68 |  | 1027.559 | -0.5721 | 1035.07 | 1021.09 | 2.1983 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1796.46 |  | 1818.5363 | -1.214 | 1823.13 | 1796.26 | 0.103 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 219.95 |  | 221.0042 | -0.477 | 222.19 | 218.09 | 1.2139 | below_vwap | below_vwap,spread_too_wide |
| 9 | IWM | market_regime | 295.33 |  | 296.162 | -0.2809 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ENTG | semiconductor_materials | 133.83 |  | 134.9765 | -0.8494 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 12 | META | cloud_ai_capex | 667.81 |  | 671.6224 | -0.5676 | 680.09 | 667.1 | 2.5546 | below_vwap | below_vwap,spread_too_wide |
| 13 | ANET | ai_networking_optical | 167.44 |  | 166.5743 | 0.5197 | 169.91 | 165.6 | 3.5177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | JCI | data_center_power_cooling | 140.52 |  | 140.5166 | 0.0024 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SOXX | semiconductor_index | 528.56 |  | 533.8983 | -0.9999 | 543.4 | 535.47 | 0.053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | TSM | foundry | 404.79 |  | 408.937 | -1.0141 | 414.385 | 406.61 | 1.1463 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | CIEN | ai_networking_optical | 390.87 |  | 394.8571 | -1.0098 | 410 | 397.68 | 0.1791 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | QQQ | market_regime | 706.48 |  | 709.428 | -0.4156 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AVGO | custom_silicon_networking | 376.32 |  | 380.0317 | -0.9767 | 386.58 | 378.53 | 0.4172 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 20 | MU | memory_hbm_storage | 849.24 |  | 857.4586 | -0.9585 | 887.1 | 866.765 | 1.7274 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.48 |  | 709.428 | -0.4156 | 713.55 | 708.25 | 0.0226 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.89 |  | 71.8373 | -1.3186 | 73.09 | 71.45 | 0.0141 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.83 |  | 207.3588 | -0.255 | 211.03 | 207.49 | 0.0145 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 404.66 |  | 399.302 | 1.3418 | 398.69 | 392.2 | 0.1087 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.81 |  | 330.6191 | 0.3602 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 359.35 |  | 369.1555 | -2.6562 | 375.18 | 369.2 | 0.7013 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMD | ai_accelerator | 495.51 |  | 504.192 | -1.722 | 518.33 | 507.62 | 1.3521 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 404.79 |  | 408.937 | -1.0141 | 414.385 | 406.61 | 1.1463 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 528.56 |  | 533.8983 | -0.9999 | 543.4 | 535.47 | 0.053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.36 |  | 571.9644 | -0.805 | 580.31 | 572.21 | 0.0476 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 376.32 |  | 380.0317 | -0.9767 | 386.58 | 378.53 | 0.4172 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 849.24 |  | 857.4586 | -0.9585 | 887.1 | 866.765 | 1.7274 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.67 |  | 191.0962 | -1.7929 | 201.61 | 194.19 | 0.1652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 396.62 |  | 402.3213 | -1.4171 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.4 |  | 45.8118 | -0.899 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.89 |  | 25.3383 | -1.7694 | 26.71 | 25.74 | 0.0402 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.61 |  | 752.4121 | -0.2395 | 753.51 | 751.13 | 0.0187 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.33 |  | 296.162 | -0.2809 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.17 |  | 126.6451 | -0.3752 | 131.36 | 126.665 | 0.111 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.9 |  | 73.3103 | -0.5596 | 75.54 | 73.985 | 0.439 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.3 |  | 293.4225 | -1.405 | 300.385 | 293.64 | 1.514 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 394.79 |  | 399.3414 | -1.1397 | 406.24 | 399.495 | 0.1317 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| PWR | data_center_power_cooling | 627.085 |  | 631.4369 | -0.6892 | 640.25 | 631.005 | 4.6182 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1021.68 |  | 1027.559 | -0.5721 | 1035.07 | 1021.09 | 2.1983 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.18 |  | 474.1684 | -0.2084 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.52 |  | 140.5166 | 0.0024 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.44 |  | 166.5743 | 0.5197 | 169.91 | 165.6 | 3.5177 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.06 |  | 280.7828 | -1.682 | 288.48 | 280.67 | 0.3695 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 703.71 |  | 708.514 | -0.678 | 737.175 | 720.21 | 2.2282 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.87 |  | 394.8571 | -1.0098 | 410 | 397.68 | 0.1791 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 99.12 |  | 101.3914 | -2.2402 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.98 |  | 323.5237 | -1.0953 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1796.46 |  | 1818.5363 | -1.214 | 1823.13 | 1796.26 | 0.103 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 560.22 |  | 570.2043 | -1.751 | 572.69 | 562.32 | 1.5637 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.67 |  | 322.9927 | -1.6479 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.95 |  | 221.0042 | -0.477 | 222.19 | 218.09 | 1.2139 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.56 |  | 326.7409 | -1.2796 | 332.49 | 326.685 | 3.6024 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.45 |  | 286.7045 | -2.1815 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.97 |  | 63.969 | -1.5616 | 66.19 | 63.93 | 4.8118 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 50.76 |  | 51.8391 | -2.0817 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.83 |  | 134.9765 | -0.8494 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.17 |  | 334.988 | -1.7368 | 346.26 | 338 | 4.2076 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 517.67 |  | 515.1268 | 0.4937 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.035 |  | 294.9417 | 0.3707 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.04 |  | 26.8054 | -2.8554 | 28.05 | 27.6 | 0.0384 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.225 |  | 35.5035 | -0.7844 | 37.365 | 36.4 | 0.0284 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.87 |  | 21.2231 | -1.6638 | 22.18 | 21.78 | 0.0958 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1417.82 |  | 1463.6323 | -3.13 | 1549.47 | 1482.06 | 2.5391 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 461.58 |  | 474.3302 | -2.688 | 498.04 | 480.14 | 0.3076 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 747.16 |  | 765.443 | -2.3885 | 797.155 | 768.7 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMZN | cloud_ai_capex | 252.34 |  | 255.3419 | -1.1757 | 258.07 | 252.62 | 0.0198 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 667.81 |  | 671.6224 | -0.5676 | 680.09 | 667.1 | 2.5546 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 257.25 |  | 257.2987 | -0.0189 | 265.96 | 258.1 | 3.8873 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 156.49 |  | 161.7489 | -3.2513 | 168.11 | 162.41 | 0.8627 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
