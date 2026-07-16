# Intraday State

- Generated at: `2026-07-16T22:33:08+08:00`
- Market time ET: `2026-07-16T10:33:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 8, 'manual_confirm_candidate': 4, 'below_vwap': 15, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 2, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.94 |  | 710.485 | 0.2048 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| SOXX | semiconductor_index | 538.92 |  | 538.3561 | 0.1047 | 543.4 | 535.47 | 0.0965 | watch_only | none |
| SMH | semiconductor_index | 576.77 |  | 576.2257 | 0.0945 | 580.31 | 572.21 | 0.0399 | watch_only | none |
| SPY | market_regime | 754.04 |  | 752.3881 | 0.2196 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 223.77 |  | 222.9213 | 0.3807 | 222.19 | 218.09 | 0.1385 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.04 |  | 752.3881 | 0.2196 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.99 |  | 296.4491 | 0.1825 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.59 |  | 328.9215 | 0.5073 | 328.98 | 326.885 | 0.0302 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.04 |  | 752.3881 | 0.2196 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.99 |  | 296.4491 | 0.1825 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 538.92 |  | 538.3561 | 0.1047 | 543.4 | 535.47 | 0.0965 | watch_only | none |
| 4 | KLAC | semiconductor_equipment | 223.77 |  | 222.9213 | 0.3807 | 222.19 | 218.09 | 0.1385 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 711.94 |  | 710.485 | 0.2048 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| 6 | SMH | semiconductor_index | 576.77 |  | 576.2257 | 0.0945 | 580.31 | 572.21 | 0.0399 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 330.59 |  | 328.9215 | 0.5073 | 328.98 | 326.885 | 0.0302 | buy_precheck_manual_confirm | none |
| 8 | NVDA | ai_accelerator | 208.495 |  | 208.4584 | 0.0176 | 211.03 | 207.49 | 0.1535 | watch_only | none |
| 9 | GOOGL | cloud_ai_capex | 373.665 |  | 371.5027 | 0.582 | 375.18 | 369.2 | 0.1311 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 256.39 |  | 254.809 | 0.6204 | 258.07 | 252.62 | 0.0273 | watch_only | none |
| 11 | MSFT | cloud_ai_capex | 396.825 |  | 395.0171 | 0.4577 | 398.69 | 392.2 | 0.2444 | watch_only | none |
| 12 | LIN | industrial_gases | 513.68 |  | 513.2092 | 0.0917 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 382.19 |  | 382.1088 | 0.0212 | 386.58 | 378.53 | 0.5495 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 298.23 |  | 296.6296 | 0.5395 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 635.45 |  | 633.2715 | 0.344 | 640.25 | 631.005 | 1.5548 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ETN | data_center_power_cooling | 404.07 |  | 402.513 | 0.3868 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | STX | memory_hbm_storage | 782.58 |  | 777.1068 | 0.7043 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | DELL | ai_server_oem | 408.41 |  | 405.5524 | 0.7046 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ENTG | semiconductor_materials | 136.85 |  | 135.8733 | 0.7189 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TSM | foundry | 413.8 |  | 410.7817 | 0.7348 | 414.385 | 406.61 | 1.4379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 223.77 |  | 222.9213 | 0.3807 | 222.19 | 218.09 | 0.1385 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 754.04 |  | 752.3881 | 0.2196 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.99 |  | 296.4491 | 0.1825 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.59 |  | 328.9215 | 0.5073 | 328.98 | 326.885 | 0.0302 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1826.655 |  | 1827.5776 | -0.0505 | 1823.13 | 1796.26 | 0.2732 | below_vwap | below_vwap |
| 6 | TT | data_center_power_cooling | 476.48 |  | 473.4086 | 0.6488 | 474.085 | 467.64 | 4.6529 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | JCI | data_center_power_cooling | 141.73 |  | 140.4912 | 0.8817 | 140.83 | 139.43 | 4.8896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | GEV | data_center_power_cooling | 1047.29 |  | 1029.3358 | 1.7443 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | AMAT | semiconductor_equipment | 577.99 |  | 575.4928 | 0.4339 | 572.69 | 562.32 | 1.0848 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | COHU | semiconductor_test_packaging | 53.56 |  | 52.5428 | 1.9359 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 538.92 |  | 538.3561 | 0.1047 | 543.4 | 535.47 | 0.0965 | watch_only | none |
| 12 | QQQ | market_regime | 711.94 |  | 710.485 | 0.2048 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| 13 | NVDA | ai_accelerator | 208.495 |  | 208.4584 | 0.0176 | 211.03 | 207.49 | 0.1535 | watch_only | none |
| 14 | SMH | semiconductor_index | 576.77 |  | 576.2257 | 0.0945 | 580.31 | 572.21 | 0.0399 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 396.825 |  | 395.0171 | 0.4577 | 398.69 | 392.2 | 0.2444 | watch_only | none |
| 16 | GOOGL | cloud_ai_capex | 373.665 |  | 371.5027 | 0.582 | 375.18 | 369.2 | 0.1311 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 256.39 |  | 254.809 | 0.6204 | 258.07 | 252.62 | 0.0273 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 72.5 |  | 72.1928 | 0.4256 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| 19 | ANET | ai_networking_optical | 165.87 |  | 166.4227 | -0.3321 | 169.91 | 165.6 | 0.5848 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMD | ai_accelerator | 510.84 |  | 511.0822 | -0.0474 | 518.33 | 507.62 | 0.5873 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.94 |  | 710.485 | 0.2048 | 713.55 | 708.25 | 0.0421 | watch_only | none |
| TQQQ | leveraged_tool | 72.5 |  | 72.1928 | 0.4256 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| NVDA | ai_accelerator | 208.495 |  | 208.4584 | 0.0176 | 211.03 | 207.49 | 0.1535 | watch_only | none |
| MSFT | cloud_ai_capex | 396.825 |  | 395.0171 | 0.4577 | 398.69 | 392.2 | 0.2444 | watch_only | none |
| AAPL | mega_cap_platform | 330.59 |  | 328.9215 | 0.5073 | 328.98 | 326.885 | 0.0302 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 373.665 |  | 371.5027 | 0.582 | 375.18 | 369.2 | 0.1311 | watch_only | none |
| AMD | ai_accelerator | 510.84 |  | 511.0822 | -0.0474 | 518.33 | 507.62 | 0.5873 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 413.8 |  | 410.7817 | 0.7348 | 414.385 | 406.61 | 1.4379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 538.92 |  | 538.3561 | 0.1047 | 543.4 | 535.47 | 0.0965 | watch_only | none |
| SMH | semiconductor_index | 576.77 |  | 576.2257 | 0.0945 | 580.31 | 572.21 | 0.0399 | watch_only | none |
| AVGO | custom_silicon_networking | 382.19 |  | 382.1088 | 0.0212 | 386.58 | 378.53 | 0.5495 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 863.72 |  | 867.4879 | -0.4343 | 887.1 | 866.765 | 0.5766 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 193.67 |  | 195.4215 | -0.8962 | 201.61 | 194.19 | 2.7263 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 408.41 |  | 405.5524 | 0.7046 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.45 |  | 46.8407 | -0.834 | 47.65 | 46.165 | 0.0431 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.76 |  | 25.9335 | -0.669 | 26.71 | 25.74 | 0.0388 | below_vwap | below_vwap |
| SPY | market_regime | 754.04 |  | 752.3881 | 0.2196 | 753.51 | 751.13 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.99 |  | 296.4491 | 0.1825 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.995 |  | 127.4972 | -0.3939 | 131.36 | 126.665 | 0.7638 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.52 |  | 74.2103 | -0.9302 | 75.54 | 73.985 | 0.9793 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 298.23 |  | 296.6296 | 0.5395 | 300.385 | 293.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 404.07 |  | 402.513 | 0.3868 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 635.45 |  | 633.2715 | 0.344 | 640.25 | 631.005 | 1.5548 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1047.29 |  | 1029.3358 | 1.7443 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 476.48 |  | 473.4086 | 0.6488 | 474.085 | 467.64 | 4.6529 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.73 |  | 140.4912 | 0.8817 | 140.83 | 139.43 | 4.8896 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 165.87 |  | 166.4227 | -0.3321 | 169.91 | 165.6 | 0.5848 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 282.68 |  | 285.1927 | -0.8811 | 288.48 | 280.67 | 1.3797 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 717 |  | 722.6076 | -0.776 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 397.03 |  | 400.629 | -0.8983 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.91 |  | 103.9675 | -1.0172 | 106.975 | 102.85 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.95 |  | 329.7122 | 0.3754 | 337.59 | 326.16 | 4.5384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1826.655 |  | 1827.5776 | -0.0505 | 1823.13 | 1796.26 | 0.2732 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 577.99 |  | 575.4928 | 0.4339 | 572.69 | 562.32 | 1.0848 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 327.42 |  | 328.0947 | -0.2057 | 328.96 | 324.11 | 0.8888 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 223.77 |  | 222.9213 | 0.3807 | 222.19 | 218.09 | 0.1385 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 331.54 |  | 328.3059 | 0.9851 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 294.65 |  | 290.2926 | 1.501 | 295.83 | 285.02 | 4.1269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 64.61 |  | 64.8492 | -0.3688 | 66.19 | 63.93 | 4.9528 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 53.56 |  | 52.5428 | 1.9359 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.85 |  | 135.8733 | 0.7189 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 513.68 |  | 513.2092 | 0.0917 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 292.68 |  | 291.5771 | 0.3783 | 293.89 | 291.35 | 3.5295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 27.42 |  | 27.496 | -0.2763 | 28.05 | 27.6 | 0.1094 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.94 |  | 36.4316 | -1.3495 | 37.365 | 36.4 | 0.0556 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.54 |  | 21.6709 | -0.6039 | 22.18 | 21.78 | 0.0929 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1491.6 |  | 1502.4938 | -0.725 | 1549.47 | 1482.06 | 1.6392 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 483.585 |  | 483.6139 | -0.006 | 498.04 | 480.14 | 3.5154 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 782.58 |  | 777.1068 | 0.7043 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 256.39 |  | 254.809 | 0.6204 | 258.07 | 252.62 | 0.0273 | watch_only | none |
| META | cloud_ai_capex | 678.64 |  | 672.8696 | 0.8576 | 680.09 | 667.1 | 0.6719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 258.26 |  | 259.8445 | -0.6098 | 265.96 | 258.1 | 4.7123 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 162.5 |  | 164.7226 | -1.3493 | 168.11 | 162.41 | 1.5323 | below_vwap | below_vwap,spread_too_wide |
