# Intraday State

- Generated at: `2026-07-16T22:27:27+08:00`
- Market time ET: `2026-07-16T10:27:29-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 11, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 15, 'below_vwap': 15, 'price_stale_or_missing': 2, 'below_opening_15m_low': 9}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.16 |  | 710.4479 | 0.1002 | 713.55 | 708.25 | 0.0183 | watch_only | none |
| SOXX | semiconductor_index | 539.39 |  | 538.2957 | 0.2033 | 543.4 | 535.47 | 0.1112 | watch_only | none |
| SMH | semiconductor_index | 576.71 |  | 576.1689 | 0.0939 | 580.31 | 572.21 | 0.0486 | watch_only | none |
| SPY | market_regime | 753.76 |  | 752.2797 | 0.1968 | 753.51 | 751.13 | 0.0371 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 223.82 |  | 222.8707 | 0.4259 | 222.19 | 218.09 | 0.1742 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.76 |  | 752.2797 | 0.1968 | 753.51 | 751.13 | 0.0371 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.96 |  | 296.4346 | 0.1772 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.56 |  | 328.872 | 0.5133 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.76 |  | 752.2797 | 0.1968 | 753.51 | 751.13 | 0.0371 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.96 |  | 296.4346 | 0.1772 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 539.39 |  | 538.2957 | 0.2033 | 543.4 | 535.47 | 0.1112 | watch_only | none |
| 4 | QQQ | market_regime | 711.16 |  | 710.4479 | 0.1002 | 713.55 | 708.25 | 0.0183 | watch_only | none |
| 5 | MU | memory_hbm_storage | 868.69 |  | 867.4774 | 0.1398 | 887.1 | 866.765 | 0.1473 | watch_only | none |
| 6 | NVDA | ai_accelerator | 208.51 |  | 208.4383 | 0.0344 | 211.03 | 207.49 | 0.0192 | watch_only | none |
| 7 | SMH | semiconductor_index | 576.71 |  | 576.1689 | 0.0939 | 580.31 | 572.21 | 0.0486 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 395.07 |  | 394.9568 | 0.0287 | 398.69 | 392.2 | 0.0709 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 330.56 |  | 328.872 | 0.5133 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 255.345 |  | 254.7162 | 0.2468 | 258.07 | 252.62 | 0.1175 | watch_only | none |
| 11 | KLAC | semiconductor_equipment | 223.82 |  | 222.8707 | 0.4259 | 222.19 | 218.09 | 0.1742 | buy_precheck_manual_confirm | none |
| 12 | PWR | data_center_power_cooling | 634.945 |  | 633.122 | 0.2879 | 640.25 | 631.005 | 0.274 | watch_only | none |
| 13 | APD | industrial_gases | 293.315 |  | 291.5483 | 0.606 | 293.89 | 291.35 | 0.2796 | watch_only | none |
| 14 | META | cloud_ai_capex | 675.62 |  | 672.5262 | 0.46 | 680.09 | 667.1 | 0.1791 | watch_only | none |
| 15 | AVGO | custom_silicon_networking | 383.11 |  | 382.0777 | 0.2702 | 386.58 | 378.53 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ETN | data_center_power_cooling | 404.16 |  | 402.4657 | 0.421 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | STX | memory_hbm_storage | 782.345 |  | 776.9363 | 0.6962 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | DELL | ai_server_oem | 406.82 |  | 405.3482 | 0.3631 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 483.97 |  | 483.5829 | 0.08 | 498.04 | 480.14 | 0.7273 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | GOOGL | cloud_ai_capex | 371.755 |  | 371.3448 | 0.1105 | 375.18 | 369.2 | 0.5057 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 223.82 |  | 222.8707 | 0.4259 | 222.19 | 218.09 | 0.1742 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 753.76 |  | 752.2797 | 0.1968 | 753.51 | 751.13 | 0.0371 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.96 |  | 296.4346 | 0.1772 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 330.56 |  | 328.872 | 0.5133 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1826.47 |  | 1827.5997 | -0.0618 | 1823.13 | 1796.26 | 0.2874 | below_vwap | below_vwap |
| 6 | TT | data_center_power_cooling | 476.47 |  | 473.1941 | 0.6923 | 474.085 | 467.64 | 4.5669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | JCI | data_center_power_cooling | 141.67 |  | 140.4101 | 0.8973 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 1047.2 |  | 1029.2074 | 1.7482 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | AMAT | semiconductor_equipment | 577.555 |  | 575.0556 | 0.4346 | 572.69 | 562.32 | 0.4346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | COHU | semiconductor_test_packaging | 53.41 |  | 52.4192 | 1.8902 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 539.39 |  | 538.2957 | 0.2033 | 543.4 | 535.47 | 0.1112 | watch_only | none |
| 12 | QQQ | market_regime | 711.16 |  | 710.4479 | 0.1002 | 713.55 | 708.25 | 0.0183 | watch_only | none |
| 13 | MU | memory_hbm_storage | 868.69 |  | 867.4774 | 0.1398 | 887.1 | 866.765 | 0.1473 | watch_only | none |
| 14 | NVDA | ai_accelerator | 208.51 |  | 208.4383 | 0.0344 | 211.03 | 207.49 | 0.0192 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 634.945 |  | 633.122 | 0.2879 | 640.25 | 631.005 | 0.274 | watch_only | none |
| 16 | SMH | semiconductor_index | 576.71 |  | 576.1689 | 0.0939 | 580.31 | 572.21 | 0.0486 | watch_only | none |
| 17 | APD | industrial_gases | 293.315 |  | 291.5483 | 0.606 | 293.89 | 291.35 | 0.2796 | watch_only | none |
| 18 | MSFT | cloud_ai_capex | 395.07 |  | 394.9568 | 0.0287 | 398.69 | 392.2 | 0.0709 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 255.345 |  | 254.7162 | 0.2468 | 258.07 | 252.62 | 0.1175 | watch_only | none |
| 20 | META | cloud_ai_capex | 675.62 |  | 672.5262 | 0.46 | 680.09 | 667.1 | 0.1791 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.16 |  | 710.4479 | 0.1002 | 713.55 | 708.25 | 0.0183 | watch_only | none |
| TQQQ | leveraged_tool | 72.45 |  | 72.1785 | 0.3761 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| NVDA | ai_accelerator | 208.51 |  | 208.4383 | 0.0344 | 211.03 | 207.49 | 0.0192 | watch_only | none |
| MSFT | cloud_ai_capex | 395.07 |  | 394.9568 | 0.0287 | 398.69 | 392.2 | 0.0709 | watch_only | none |
| AAPL | mega_cap_platform | 330.56 |  | 328.872 | 0.5133 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.755 |  | 371.3448 | 0.1105 | 375.18 | 369.2 | 0.5057 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 509.6 |  | 511.0996 | -0.2934 | 518.33 | 507.62 | 0.3984 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 413.21 |  | 410.608 | 0.6337 | 414.385 | 406.61 | 1.0164 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 539.39 |  | 538.2957 | 0.2033 | 543.4 | 535.47 | 0.1112 | watch_only | none |
| SMH | semiconductor_index | 576.71 |  | 576.1689 | 0.0939 | 580.31 | 572.21 | 0.0486 | watch_only | none |
| AVGO | custom_silicon_networking | 383.11 |  | 382.0777 | 0.2702 | 386.58 | 378.53 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 868.69 |  | 867.4774 | 0.1398 | 887.1 | 866.765 | 0.1473 | watch_only | none |
| MRVL | custom_silicon_networking | 193.89 |  | 195.4606 | -0.8036 | 201.61 | 194.19 | 2.8315 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 406.82 |  | 405.3482 | 0.3631 | 411.65 | 400.635 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.68 |  | 46.8667 | -0.3984 | 47.65 | 46.165 | 0.0428 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 25.745 |  | 25.9399 | -0.7515 | 26.71 | 25.74 | 0.0777 | below_vwap | below_vwap |
| SPY | market_regime | 753.76 |  | 752.2797 | 0.1968 | 753.51 | 751.13 | 0.0371 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.96 |  | 296.4346 | 0.1772 | 296.28 | 294.65 | 0.0101 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.11 |  | 127.5276 | -0.3274 | 131.36 | 126.665 | 0.1888 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.94 |  | 74.2377 | -0.401 | 75.54 | 73.985 | 1.6229 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 298.05 |  | 296.5562 | 0.5037 | 300.385 | 293.64 | 4.8314 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 404.16 |  | 402.4657 | 0.421 | 406.24 | 399.495 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.945 |  | 633.122 | 0.2879 | 640.25 | 631.005 | 0.274 | watch_only | none |
| GEV | data_center_power_cooling | 1047.2 |  | 1029.2074 | 1.7482 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 476.47 |  | 473.1941 | 0.6923 | 474.085 | 467.64 | 4.5669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 141.67 |  | 140.4101 | 0.8973 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.65 |  | 166.4903 | -0.5047 | 169.91 | 165.6 | 2.1129 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 283.85 |  | 285.2448 | -0.489 | 288.48 | 280.67 | 3.6287 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 716.88 |  | 722.8534 | -0.8264 | 737.175 | 720.21 | 0.1995 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CIEN | ai_networking_optical | 394.215 |  | 400.7563 | -1.6322 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.95 |  | 103.9844 | -0.9947 | 106.975 | 102.85 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 329.67 |  | 329.6939 | -0.0073 | 337.59 | 326.16 | 0.6097 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1826.47 |  | 1827.5997 | -0.0618 | 1823.13 | 1796.26 | 0.2874 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 577.555 |  | 575.0556 | 0.4346 | 572.69 | 562.32 | 0.4346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 327.63 |  | 328.0368 | -0.124 | 328.96 | 324.11 | 0.9706 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 223.82 |  | 222.8707 | 0.4259 | 222.19 | 218.09 | 0.1742 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 330.78 |  | 328.1304 | 0.8075 | 332.49 | 326.685 | 3.4948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 292.14 |  | 290.1872 | 0.6729 | 295.83 | 285.02 | 5.0934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 64.445 |  | 64.8468 | -0.6197 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.41 |  | 52.4192 | 1.8902 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.375 |  | 135.8296 | -0.3347 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 346.26 |  | 341.618 | 1.3588 | 346.26 | 338 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 513.2 |  | 513.2056 | -0.0011 | 515.825 | 512.23 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 293.315 |  | 291.5483 | 0.606 | 293.89 | 291.35 | 0.2796 | watch_only | none |
| APLD | high_beta_ai_infrastructure | 27.37 |  | 27.4982 | -0.4663 | 28.05 | 27.6 | 0.1096 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.91 |  | 36.4579 | -1.5027 | 37.365 | 36.4 | 0.0835 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.49 |  | 21.6781 | -0.8676 | 22.18 | 21.78 | 0.2327 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1492.985 |  | 1502.83 | -0.6551 | 1549.47 | 1482.06 | 3.0831 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 483.97 |  | 483.5829 | 0.08 | 498.04 | 480.14 | 0.7273 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 782.345 |  | 776.9363 | 0.6962 | 797.155 | 768.7 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 255.345 |  | 254.7162 | 0.2468 | 258.07 | 252.62 | 0.1175 | watch_only | none |
| META | cloud_ai_capex | 675.62 |  | 672.5262 | 0.46 | 680.09 | 667.1 | 0.1791 | watch_only | none |
| ARM | ai_accelerator | 257.91 |  | 259.889 | -0.7615 | 265.96 | 258.1 | 4.8971 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 162.01 |  | 164.776 | -1.6786 | 168.11 | 162.41 | 2.7776 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
