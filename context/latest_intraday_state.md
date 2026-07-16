# Intraday State

- Generated at: `2026-07-16T22:59:10+08:00`
- Market time ET: `2026-07-16T10:59:11-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 4, 'below_vwap': 18, 'below_opening_15m_low': 19, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 9, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.72 |  | 710.5884 | 0.0185 | 713.55 | 708.25 | 0.0619 | watch_only | none |
| SOXX | semiconductor_index | 536.07 |  | 538.1971 | -0.3952 | 543.4 | 535.47 | 0.0653 | below_vwap | below_vwap |
| SMH | semiconductor_index | 573.685 |  | 576.1465 | -0.4272 | 580.31 | 572.21 | 0.1028 | below_vwap | below_vwap |
| SPY | market_regime | 753.78 |  | 752.6332 | 0.1524 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.84 |  | 474.0202 | 0.3839 | 474.085 | 467.64 | 0.3194 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.78 |  | 752.6332 | 0.1524 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 297.03 |  | 296.5615 | 0.158 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.09 |  | 329.2099 | 0.2673 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.78 |  | 752.6332 | 0.1524 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 297.03 |  | 296.5615 | 0.158 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.09 |  | 329.2099 | 0.2673 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 710.72 |  | 710.5884 | 0.0185 | 713.55 | 708.25 | 0.0619 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 372.24 |  | 372.0384 | 0.0542 | 375.18 | 369.2 | 0.051 | watch_only | none |
| 6 | TT | data_center_power_cooling | 475.84 |  | 474.0202 | 0.3839 | 474.085 | 467.64 | 0.3194 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 397.275 |  | 395.3802 | 0.4792 | 398.69 | 392.2 | 0.0654 | watch_only | none |
| 8 | MKSI | semiconductor_materials | 341.9 |  | 341.1283 | 0.2262 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ENTG | semiconductor_materials | 136.36 |  | 135.9778 | 0.281 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | LIN | industrial_gases | 515.62 |  | 513.3539 | 0.4414 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | META | cloud_ai_capex | 679.96 |  | 674.1467 | 0.8623 | 680.09 | 667.1 | 0.2485 | watch_only | none |
| 12 | TER | semiconductor_test_packaging | 331.235 |  | 328.752 | 0.7553 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | GEV | data_center_power_cooling | 1038.37 |  | 1030.6202 | 0.752 | 1035.07 | 1021.09 | 4.5803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TSM | foundry | 413.045 |  | 411.4841 | 0.3793 | 414.385 | 406.61 | 0.9418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 141.475 |  | 140.6437 | 0.5911 | 140.83 | 139.43 | 4.9832 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 781.615 |  | 778.247 | 0.4328 | 797.155 | 768.7 | 1.2551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | APD | industrial_gases | 294.755 |  | 292.2182 | 0.8681 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SOXX | semiconductor_index | 536.07 |  | 538.1971 | -0.3952 | 543.4 | 535.47 | 0.0653 | below_vwap | below_vwap |
| 19 | SMH | semiconductor_index | 573.685 |  | 576.1465 | -0.4272 | 580.31 | 572.21 | 0.1028 | below_vwap | below_vwap |
| 20 | KLAC | semiconductor_equipment | 222.375 |  | 222.9663 | -0.2652 | 222.19 | 218.09 | 0.2069 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 475.84 |  | 474.0202 | 0.3839 | 474.085 | 467.64 | 0.3194 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.78 |  | 752.6332 | 0.1524 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 297.03 |  | 296.5615 | 0.158 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.09 |  | 329.2099 | 0.2673 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |
| 5 | AMAT | semiconductor_equipment | 575.58 |  | 575.6273 | -0.0082 | 572.69 | 562.32 | 3.0491 | below_vwap | below_vwap,spread_too_wide |
| 6 | KLAC | semiconductor_equipment | 222.375 |  | 222.9663 | -0.2652 | 222.19 | 218.09 | 0.2069 | below_vwap | below_vwap |
| 7 | JCI | data_center_power_cooling | 141.475 |  | 140.6437 | 0.5911 | 140.83 | 139.43 | 4.9832 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | GEV | data_center_power_cooling | 1038.37 |  | 1030.6202 | 0.752 | 1035.07 | 1021.09 | 4.5803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APD | industrial_gases | 294.755 |  | 292.2182 | 0.8681 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | QQQ | market_regime | 710.72 |  | 710.5884 | 0.0185 | 713.55 | 708.25 | 0.0619 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 397.275 |  | 395.3802 | 0.4792 | 398.69 | 392.2 | 0.0654 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 372.24 |  | 372.0384 | 0.0542 | 375.18 | 369.2 | 0.051 | watch_only | none |
| 13 | META | cloud_ai_capex | 679.96 |  | 674.1467 | 0.8623 | 680.09 | 667.1 | 0.2485 | watch_only | none |
| 14 | SOXX | semiconductor_index | 536.07 |  | 538.1971 | -0.3952 | 543.4 | 535.47 | 0.0653 | below_vwap | below_vwap |
| 15 | AVGO | custom_silicon_networking | 381.42 |  | 382.127 | -0.185 | 386.58 | 378.53 | 0.3723 | below_vwap | below_vwap,spread_too_wide |
| 16 | VRT | data_center_power_cooling | 296.17 |  | 296.7428 | -0.193 | 300.385 | 293.64 | 4.0078 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMD | ai_accelerator | 508.21 |  | 510.8622 | -0.5192 | 518.33 | 507.62 | 1.0783 | below_vwap | below_vwap,spread_too_wide |
| 18 | PWR | data_center_power_cooling | 633.275 |  | 633.5556 | -0.0443 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ASML | semiconductor_equipment | 1821.43 |  | 1827.1081 | -0.3108 | 1823.13 | 1796.26 | 0.3936 | below_vwap | below_vwap,spread_too_wide |
| 20 | ONTO | semiconductor_test_packaging | 290.39 |  | 290.4576 | -0.0233 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.72 |  | 710.5884 | 0.0185 | 713.55 | 708.25 | 0.0619 | watch_only | none |
| TQQQ | leveraged_tool | 72.18 |  | 72.2099 | -0.0414 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 206.4 |  | 208.1618 | -0.8464 | 211.03 | 207.49 | 0.0194 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 397.275 |  | 395.3802 | 0.4792 | 398.69 | 392.2 | 0.0654 | watch_only | none |
| AAPL | mega_cap_platform | 330.09 |  | 329.2099 | 0.2673 | 328.98 | 326.885 | 0.0576 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.24 |  | 372.0384 | 0.0542 | 375.18 | 369.2 | 0.051 | watch_only | none |
| AMD | ai_accelerator | 508.21 |  | 510.8622 | -0.5192 | 518.33 | 507.62 | 1.0783 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 413.045 |  | 411.4841 | 0.3793 | 414.385 | 406.61 | 0.9418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 536.07 |  | 538.1971 | -0.3952 | 543.4 | 535.47 | 0.0653 | below_vwap | below_vwap |
| SMH | semiconductor_index | 573.685 |  | 576.1465 | -0.4272 | 580.31 | 572.21 | 0.1028 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.42 |  | 382.127 | -0.185 | 386.58 | 378.53 | 0.3723 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 859.77 |  | 866.5769 | -0.7855 | 887.1 | 866.765 | 0.9782 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 191.83 |  | 194.9362 | -1.5934 | 201.61 | 194.19 | 0.662 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 402.86 |  | 405.7039 | -0.701 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.97 |  | 46.6153 | -1.3843 | 47.65 | 46.165 | 0.0218 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.63 |  | 25.8768 | -0.9536 | 26.71 | 25.74 | 0.078 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.78 |  | 752.6332 | 0.1524 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 297.03 |  | 296.5615 | 0.158 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.525 |  | 127.2039 | -0.5337 | 131.36 | 126.665 | 3.9518 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.75 |  | 74.0593 | -0.4177 | 75.54 | 73.985 | 0.2712 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 296.17 |  | 296.7428 | -0.193 | 300.385 | 293.64 | 4.0078 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 397.82 |  | 402.3553 | -1.1272 | 406.24 | 399.495 | 4.957 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 633.275 |  | 633.5556 | -0.0443 | 640.25 | 631.005 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1038.37 |  | 1030.6202 | 0.752 | 1035.07 | 1021.09 | 4.5803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.84 |  | 474.0202 | 0.3839 | 474.085 | 467.64 | 0.3194 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 141.475 |  | 140.6437 | 0.5911 | 140.83 | 139.43 | 4.9832 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 165.18 |  | 166.3436 | -0.6995 | 169.91 | 165.6 | 3.8382 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 280 |  | 284.704 | -1.6522 | 288.48 | 280.67 | 4.3821 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 713.135 |  | 721.4371 | -1.1508 | 737.175 | 720.21 | 0.2496 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 395.46 |  | 399.1797 | -0.9318 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.01 |  | 103.6515 | -1.5836 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 327.54 |  | 329.3528 | -0.5504 | 337.59 | 326.16 | 0.4885 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1821.43 |  | 1827.1081 | -0.3108 | 1823.13 | 1796.26 | 0.3936 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 575.58 |  | 575.6273 | -0.0082 | 572.69 | 562.32 | 3.0491 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 325.305 |  | 327.7576 | -0.7483 | 328.96 | 324.11 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 222.375 |  | 222.9663 | -0.2652 | 222.19 | 218.09 | 0.2069 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 331.235 |  | 328.752 | 0.7553 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 290.39 |  | 290.4576 | -0.0233 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.44 |  | 64.7323 | -0.4516 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.92 |  | 52.6526 | 0.5079 | 52.72 | 51.735 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 136.36 |  | 135.9778 | 0.281 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 341.9 |  | 341.1283 | 0.2262 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 515.62 |  | 513.3539 | 0.4414 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 294.755 |  | 292.2182 | 0.8681 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.415 |  | 27.4824 | -0.2454 | 28.05 | 27.6 | 0.1459 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.67 |  | 36.242 | -1.5783 | 37.365 | 36.4 | 0.0561 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.325 |  | 21.6009 | -1.2771 | 22.18 | 21.78 | 0.0938 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1472.085 |  | 1498.9024 | -1.7891 | 1549.47 | 1482.06 | 3.3965 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 482.45 |  | 484.0463 | -0.3298 | 498.04 | 480.14 | 0.825 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 781.615 |  | 778.247 | 0.4328 | 797.155 | 768.7 | 1.2551 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 254.93 |  | 255.1889 | -0.1014 | 258.07 | 252.62 | 0.0824 | below_vwap | below_vwap |
| META | cloud_ai_capex | 679.96 |  | 674.1467 | 0.8623 | 680.09 | 667.1 | 0.2485 | watch_only | none |
| ARM | ai_accelerator | 256.59 |  | 259.2977 | -1.0443 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.765 |  | 164.5308 | -1.681 | 168.11 | 162.41 | 2.5345 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
