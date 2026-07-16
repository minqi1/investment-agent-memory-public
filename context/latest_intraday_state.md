# Intraday State

- Generated at: `2026-07-16T23:20:01+08:00`
- Market time ET: `2026-07-16T11:20:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 23, 'below_opening_15m_low': 21, 'watch_only': 2, 'manual_confirm_candidate': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.94 |  | 710.4974 | -0.0784 | 713.55 | 708.25 | 0.0085 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 534.3 |  | 537.8458 | -0.6593 | 543.4 | 535.47 | 0.0805 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.72 |  | 575.7856 | -0.5324 | 580.31 | 572.21 | 0.0908 | below_vwap | below_vwap |
| SPY | market_regime | 753.52 |  | 752.7181 | 0.1065 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.52 |  | 752.7181 | 0.1065 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.94 |  | 296.5927 | 0.1171 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.275 |  | 329.3172 | 0.2909 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.52 |  | 752.7181 | 0.1065 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.94 |  | 296.5927 | 0.1171 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.275 |  | 329.3172 | 0.2909 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.29 |  | 255.1902 | 0.0391 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 5 | MSFT | cloud_ai_capex | 398.16 |  | 395.5869 | 0.6505 | 398.69 | 392.2 | 0.2512 | watch_only | none |
| 6 | TT | data_center_power_cooling | 475.26 |  | 474.1604 | 0.2319 | 474.085 | 467.64 | 4.7595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | TER | semiconductor_test_packaging | 331.08 |  | 328.9475 | 0.6483 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | META | cloud_ai_capex | 676.18 |  | 674.8296 | 0.2001 | 680.09 | 667.1 | 0.7394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | GEV | data_center_power_cooling | 1040.57 |  | 1032.5356 | 0.7781 | 1035.07 | 1021.09 | 4.929 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | LIN | industrial_gases | 517.995 |  | 513.8062 | 0.8152 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | QQQ | market_regime | 709.94 |  | 710.4974 | -0.0784 | 713.55 | 708.25 | 0.0085 | below_vwap | below_vwap |
| 12 | SMH | semiconductor_index | 572.72 |  | 575.7856 | -0.5324 | 580.31 | 572.21 | 0.0908 | below_vwap | below_vwap |
| 13 | ORCL | cloud_ai_capex | 127.14 |  | 127.1466 | -0.0052 | 131.36 | 126.665 | 0.0944 | below_vwap | below_vwap |
| 14 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 221.835 |  | 222.902 | -0.4787 | 222.19 | 218.09 | 0.302 | below_vwap | below_vwap |
| 16 | VRT | data_center_power_cooling | 295.51 |  | 296.6123 | -0.3716 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 140.665 |  | 140.6979 | -0.0234 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 371.98 |  | 372.0367 | -0.0152 | 375.18 | 369.2 | 0.3414 | below_vwap | below_vwap |
| 20 | LRCX | semiconductor_equipment | 326.15 |  | 327.4533 | -0.398 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.52 |  | 752.7181 | 0.1065 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.94 |  | 296.5927 | 0.1171 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.275 |  | 329.3172 | 0.2909 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |
| 4 | AMAT | semiconductor_equipment | 575.01 |  | 575.545 | -0.093 | 572.69 | 562.32 | 0.4904 | below_vwap | below_vwap,spread_too_wide |
| 5 | TT | data_center_power_cooling | 475.26 |  | 474.1604 | 0.2319 | 474.085 | 467.64 | 4.7595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | GEV | data_center_power_cooling | 1040.57 |  | 1032.5356 | 0.7781 | 1035.07 | 1021.09 | 4.929 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | LIN | industrial_gases | 517.995 |  | 513.8062 | 0.8152 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | APD | industrial_gases | 296.54 |  | 292.966 | 1.2199 | 293.89 | 291.35 | 3.76 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | MSFT | cloud_ai_capex | 398.16 |  | 395.5869 | 0.6505 | 398.69 | 392.2 | 0.2512 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 255.29 |  | 255.1902 | 0.0391 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| 11 | TSM | foundry | 411 |  | 411.4159 | -0.1011 | 414.385 | 406.61 | 1.1046 | below_vwap | below_vwap,spread_too_wide |
| 12 | QQQ | market_regime | 709.94 |  | 710.4974 | -0.0784 | 713.55 | 708.25 | 0.0085 | below_vwap | below_vwap |
| 13 | AVGO | custom_silicon_networking | 380.69 |  | 381.9668 | -0.3343 | 386.58 | 378.53 | 1.3397 | below_vwap | below_vwap,spread_too_wide |
| 14 | VRT | data_center_power_cooling | 295.51 |  | 296.6123 | -0.3716 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 140.665 |  | 140.6979 | -0.0234 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | AMD | ai_accelerator | 507.89 |  | 510.6254 | -0.5357 | 518.33 | 507.62 | 0.9943 | below_vwap | below_vwap,spread_too_wide |
| 17 | PWR | data_center_power_cooling | 632.91 |  | 633.4425 | -0.0841 | 640.25 | 631.005 | 0.9986 | below_vwap | below_vwap,spread_too_wide |
| 18 | ASML | semiconductor_equipment | 1821.91 |  | 1826.172 | -0.2334 | 1823.13 | 1796.26 | 0.7426 | below_vwap | below_vwap,spread_too_wide |
| 19 | ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 221.835 |  | 222.902 | -0.4787 | 222.19 | 218.09 | 0.302 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.94 |  | 710.4974 | -0.0784 | 713.55 | 708.25 | 0.0085 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.97 |  | 72.1991 | -0.3173 | 73.09 | 71.45 | 0.0278 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 206.255 |  | 207.7587 | -0.7238 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 398.16 |  | 395.5869 | 0.6505 | 398.69 | 392.2 | 0.2512 | watch_only | none |
| AAPL | mega_cap_platform | 330.275 |  | 329.3172 | 0.2909 | 328.98 | 326.885 | 0.0394 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.98 |  | 372.0367 | -0.0152 | 375.18 | 369.2 | 0.3414 | below_vwap | below_vwap |
| AMD | ai_accelerator | 507.89 |  | 510.6254 | -0.5357 | 518.33 | 507.62 | 0.9943 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 411 |  | 411.4159 | -0.1011 | 414.385 | 406.61 | 1.1046 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.3 |  | 537.8458 | -0.6593 | 543.4 | 535.47 | 0.0805 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.72 |  | 575.7856 | -0.5324 | 580.31 | 572.21 | 0.0908 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 380.69 |  | 381.9668 | -0.3343 | 386.58 | 378.53 | 1.3397 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 853.735 |  | 865.8811 | -1.4027 | 887.1 | 866.765 | 2.1646 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 190.84 |  | 194.2278 | -1.7442 | 201.61 | 194.19 | 0.8436 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 402.04 |  | 405.1942 | -0.7784 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.86 |  | 46.4443 | -1.2581 | 47.65 | 46.165 | 0.0654 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.335 |  | 25.795 | -1.7833 | 26.71 | 25.74 | 0.0395 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.52 |  | 752.7181 | 0.1065 | 753.51 | 751.13 | 0.0053 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.94 |  | 296.5927 | 0.1171 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.14 |  | 127.1466 | -0.0052 | 131.36 | 126.665 | 0.0944 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.55 |  | 73.9848 | -0.5877 | 75.54 | 73.985 | 0.9517 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 295.51 |  | 296.6123 | -0.3716 | 300.385 | 293.64 |  | below_vwap | below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 397.44 |  | 401.7628 | -1.076 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 632.91 |  | 633.4425 | -0.0841 | 640.25 | 631.005 | 0.9986 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1040.57 |  | 1032.5356 | 0.7781 | 1035.07 | 1021.09 | 4.929 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.26 |  | 474.1604 | 0.2319 | 474.085 | 467.64 | 4.7595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.665 |  | 140.6979 | -0.0234 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 165.115 |  | 166.2829 | -0.7024 | 169.91 | 165.6 | 3.8397 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 278.27 |  | 284.2015 | -2.0871 | 288.48 | 280.67 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 707.82 |  | 719.1599 | -1.5768 | 737.175 | 720.21 | 4.1126 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 394.46 |  | 398.7593 | -1.0782 | 410 | 397.68 | 4.7914 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 100.93 |  | 103.3507 | -2.3422 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 323.4 |  | 329.0227 | -1.7089 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1821.91 |  | 1826.172 | -0.2334 | 1823.13 | 1796.26 | 0.7426 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 575.01 |  | 575.545 | -0.093 | 572.69 | 562.32 | 0.4904 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 326.15 |  | 327.4533 | -0.398 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 221.835 |  | 222.902 | -0.4787 | 222.19 | 218.09 | 0.302 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 331.08 |  | 328.9475 | 0.6483 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 288.95 |  | 290.5577 | -0.5533 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.45 |  | 64.6563 | -0.319 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.57 |  | 52.6687 | -0.1873 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.58 |  | 135.9739 | -0.2897 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.725 |  | 341.3178 | -0.1737 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 517.995 |  | 513.8062 | 0.8152 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.54 |  | 292.966 | 1.2199 | 293.89 | 291.35 | 3.76 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.915 |  | 27.4313 | -1.8821 | 28.05 | 27.6 | 0.0743 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.61 |  | 36.1026 | -1.3646 | 37.365 | 36.4 | 0.0562 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.32 |  | 21.5742 | -1.1782 | 22.18 | 21.78 | 0.1407 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1455.45 |  | 1494.0671 | -2.5847 | 1549.47 | 1482.06 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 475.68 |  | 483.7198 | -1.6621 | 498.04 | 480.14 | 0.7253 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 771.115 |  | 778.1078 | -0.8987 | 797.155 | 768.7 | 1.5808 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.29 |  | 255.1902 | 0.0391 | 258.07 | 252.62 | 0.0157 | watch_only | none |
| META | cloud_ai_capex | 676.18 |  | 674.8296 | 0.2001 | 680.09 | 667.1 | 0.7394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 257 |  | 258.8847 | -0.728 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 160.22 |  | 164.0453 | -2.3318 | 168.11 | 162.41 | 1.6228 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
