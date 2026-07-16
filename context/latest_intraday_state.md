# Intraday State

- Generated at: `2026-07-17T03:59:12+08:00`
- Market time ET: `2026-07-16T15:59:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 40, 'manual_confirm_candidate': 2, 'below_vwap': 4, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 9}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.6 |  | 707.8843 | -0.3227 | 713.55 | 708.25 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.39 |  | 531.8902 | -0.4701 | 543.4 | 535.47 | 0.0019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.845 |  | 570.6055 | -0.4838 | 580.31 | 572.21 | 0.037 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.51 |  | 751.1361 | -0.0834 | 753.51 | 751.13 | 0.0053 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.61 |  | 400.1367 | 0.1183 | 398.69 | 392.2 | 0.01 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.14 |  | 331.5443 | 0.4813 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.61 |  | 400.1367 | 0.1183 | 398.69 | 392.2 | 0.01 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.14 |  | 331.5443 | 0.4813 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 141.12 |  | 140.6545 | 0.3309 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | ENTG | semiconductor_materials | 134.39 |  | 134.1412 | 0.1855 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 474.995 |  | 474.4134 | 0.1226 | 474.085 | 467.64 | 4.779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | VRT | data_center_power_cooling | 293.92 |  | 293.0748 | 0.2884 | 300.385 | 293.64 | 4.2018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | APD | industrial_gases | 297.595 |  | 295.5064 | 0.7068 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ANET | ai_networking_optical | 168.08 |  | 166.8027 | 0.7658 | 169.91 | 165.6 | 3.9208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | GEV | data_center_power_cooling | 1034.98 |  | 1027.7602 | 0.7025 | 1035.07 | 1021.09 | 3.4126 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | NVDA | ai_accelerator | 207.32 |  | 207.2282 | 0.0443 | 211.03 | 207.49 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| 11 | TSM | foundry | 408.11 |  | 408.4158 | -0.0749 | 414.385 | 406.61 | 0.1152 | below_vwap | below_vwap |
| 12 | LIN | industrial_gases | 520.84 |  | 516.52 | 0.8364 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 219.15 |  | 220.0718 | -0.4189 | 222.19 | 218.09 | 0.0593 | below_vwap | below_vwap |
| 14 | IWM | market_regime | 295.265 |  | 295.8154 | -0.1861 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 15 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ARM | ai_accelerator | 261.32 |  | 257.6102 | 1.4401 | 265.96 | 258.1 | 3.3293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LITE | ai_networking_optical | 707.46 |  | 706.636 | 0.1166 | 737.175 | 720.21 | 4.0992 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SOXX | semiconductor_index | 529.39 |  | 531.8902 | -0.4701 | 543.4 | 535.47 | 0.0019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | CIEN | ai_networking_optical | 389.22 |  | 392.0981 | -0.734 | 410 | 397.68 | 0.0796 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 705.6 |  | 707.8843 | -0.3227 | 713.55 | 708.25 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.61 |  | 400.1367 | 0.1183 | 398.69 | 392.2 | 0.01 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 333.14 |  | 331.5443 | 0.4813 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.995 |  | 474.4134 | 0.1226 | 474.085 | 467.64 | 4.779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | JCI | data_center_power_cooling | 141.12 |  | 140.6545 | 0.3309 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 520.84 |  | 516.52 | 0.8364 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 297.595 |  | 295.5064 | 0.7068 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TSM | foundry | 408.11 |  | 408.4158 | -0.0749 | 414.385 | 406.61 | 0.1152 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 219.15 |  | 220.0718 | -0.4189 | 222.19 | 218.09 | 0.0593 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.265 |  | 295.8154 | -0.1861 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ANET | ai_networking_optical | 168.08 |  | 166.8027 | 0.7658 | 169.91 | 165.6 | 3.9208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | VRT | data_center_power_cooling | 293.92 |  | 293.0748 | 0.2884 | 300.385 | 293.64 | 4.2018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | GEV | data_center_power_cooling | 1034.98 |  | 1027.7602 | 0.7025 | 1035.07 | 1021.09 | 3.4126 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ENTG | semiconductor_materials | 134.39 |  | 134.1412 | 0.1855 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ARM | ai_accelerator | 261.32 |  | 257.6102 | 1.4401 | 265.96 | 258.1 | 3.3293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 207.32 |  | 207.2282 | 0.0443 | 211.03 | 207.49 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| 17 | LITE | ai_networking_optical | 707.46 |  | 706.636 | 0.1166 | 737.175 | 720.21 | 4.0992 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SOXX | semiconductor_index | 529.39 |  | 531.8902 | -0.4701 | 543.4 | 535.47 | 0.0019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | CIEN | ai_networking_optical | 389.22 |  | 392.0981 | -0.734 | 410 | 397.68 | 0.0796 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 705.6 |  | 707.8843 | -0.3227 | 713.55 | 708.25 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.6 |  | 707.8843 | -0.3227 | 713.55 | 708.25 | 0.0227 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.61 |  | 71.5064 | -1.2536 | 73.09 | 71.45 | 0.0142 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.32 |  | 207.2282 | 0.0443 | 211.03 | 207.49 | 0.0724 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 400.61 |  | 400.1367 | 0.1183 | 398.69 | 392.2 | 0.01 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.14 |  | 331.5443 | 0.4813 | 328.98 | 326.885 | 0.009 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 353.835 |  | 364.1386 | -2.8296 | 375.18 | 369.2 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 500.43 |  | 501.8501 | -0.283 | 518.33 | 507.62 | 0.2698 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 408.11 |  | 408.4158 | -0.0749 | 414.385 | 406.61 | 0.1152 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.39 |  | 531.8902 | -0.4701 | 543.4 | 535.47 | 0.0019 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 567.845 |  | 570.6055 | -0.4838 | 580.31 | 572.21 | 0.037 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 374.69 |  | 377.8137 | -0.8268 | 386.58 | 378.53 | 0.1121 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MU | memory_hbm_storage | 850.26 |  | 854.9721 | -0.5511 | 887.1 | 866.765 | 0.3034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 188.325 |  | 190.0294 | -0.8969 | 201.61 | 194.19 | 0.1009 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 391.705 |  | 399.8534 | -2.0378 | 411.65 | 400.635 | 0.2093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 45.08 |  | 45.6824 | -1.3187 | 47.65 | 46.165 | 0.0222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.69 |  | 25.1995 | -2.0218 | 26.71 | 25.74 | 0.0405 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 750.51 |  | 751.1361 | -0.0834 | 753.51 | 751.13 | 0.0053 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 295.265 |  | 295.8154 | -0.1861 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.32 |  | 125.8924 | -1.249 | 131.36 | 126.665 | 4.0943 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.805 |  | 73.225 | -0.5736 | 75.54 | 73.985 | 4.7936 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 293.92 |  | 293.0748 | 0.2884 | 300.385 | 293.64 | 4.2018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 396.31 |  | 398.8718 | -0.6423 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 629.9 |  | 630.8692 | -0.1536 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1034.98 |  | 1027.7602 | 0.7025 | 1035.07 | 1021.09 | 3.4126 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 474.995 |  | 474.4134 | 0.1226 | 474.085 | 467.64 | 4.779 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.12 |  | 140.6545 | 0.3309 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.08 |  | 166.8027 | 0.7658 | 169.91 | 165.6 | 3.9208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.93 |  | 279.7217 | -0.998 | 288.48 | 280.67 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 707.46 |  | 706.636 | 0.1166 | 737.175 | 720.21 | 4.0992 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 389.22 |  | 392.0981 | -0.734 | 410 | 397.68 | 0.0796 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAOI | ai_networking_optical | 100.16 |  | 100.8049 | -0.6398 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 319.09 |  | 321.7738 | -0.8341 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1781.91 |  | 1806.6193 | -1.3677 | 1823.13 | 1796.26 | 1.8542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 560.3 |  | 566.6426 | -1.1193 | 572.69 | 562.32 | 0.075 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 320.18 |  | 321.3951 | -0.3781 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.15 |  | 220.0718 | -0.4189 | 222.19 | 218.09 | 0.0593 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 321.89 |  | 324.3048 | -0.7446 | 332.49 | 326.685 | 0.1771 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ONTO | semiconductor_test_packaging | 281.64 |  | 284.4557 | -0.9899 | 295.83 | 285.02 | 4.7507 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 62.955 |  | 63.6307 | -1.0618 | 66.19 | 63.93 | 0.2383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 51.585 |  | 51.6467 | -0.1194 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.39 |  | 134.1412 | 0.1855 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 330.3 |  | 332.9393 | -0.7927 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 520.84 |  | 516.52 | 0.8364 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.595 |  | 295.5064 | 0.7068 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.425 |  | 26.705 | -1.0486 | 28.05 | 27.6 | 0.0378 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.945 |  | 35.4275 | -1.3619 | 37.365 | 36.4 | 0.0286 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.98 |  | 21.158 | -0.8415 | 22.18 | 21.78 | 0.0477 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1408.26 |  | 1445.8453 | -2.5995 | 1549.47 | 1482.06 | 0.0589 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| WDC | memory_hbm_storage | 465.26 |  | 471.0935 | -1.2383 | 498.04 | 480.14 | 0.0365 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| STX | memory_hbm_storage | 745.2 |  | 757.4306 | -1.6147 | 797.155 | 768.7 | 0.0362 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 250.065 |  | 253.9656 | -1.5359 | 258.07 | 252.62 | 0.02 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 662.68 |  | 669.405 | -1.0046 | 680.09 | 667.1 | 0.0196 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 261.32 |  | 257.6102 | 1.4401 | 265.96 | 258.1 | 3.3293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 152.27 |  | 160.2489 | -4.9791 | 168.11 | 162.41 | 3.7631 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
