# Intraday State

- Generated at: `2026-07-23T01:17:57+08:00`
- Market time ET: `2026-07-22T13:17:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_opening_15m_low': 7, 'watch_only': 1, 'spread_too_wide_or_missing': 22, 'price_stale_or_missing': 1, 'below_vwap': 13}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.695 |  | 707.3689 | 0.1875 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.18 |  | 552.884 | 1.1388 | 551.02 | 540.105 | 0.0429 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.345 |  | 585.1428 | 0.889 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.24 |  | 748.4776 | 0.1019 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.34 |  | 211.0654 | 1.0777 | 207.4 | 205.01 | 0.0328 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 975.45 |  | 967.3153 | 0.841 | 963.41 | 936.99 | 0.2389 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 914.775 |  | 908.5945 | 0.6802 | 899.59 | 860.605 | 0.117 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.18 |  | 552.884 | 1.1388 | 551.02 | 540.105 | 0.0429 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.345 |  | 585.1428 | 0.889 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 213.655 |  | 211.14 | 1.1912 | 207.06 | 202.18 | 0.1264 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 708.695 |  | 707.3689 | 0.1875 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 749.24 |  | 748.4776 | 0.1019 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1807.855 |  | 1796.9838 | 0.605 | 1786.525 | 1767.54 | 0.0531 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 300.65 |  | 298.8821 | 0.5915 | 297.69 | 293.905 | 0.1264 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.28 |  | 31.1782 | 0.3266 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.28 |  | 70.8411 | 0.6196 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.24 |  | 748.4776 | 0.1019 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.695 |  | 707.3689 | 0.1875 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 348.305 |  | 347.9453 | 0.1034 | 348.76 | 346.23 | 0.0545 | watch_only | none |
| 4 | SMCI | ai_server_oem | 31.28 |  | 31.1782 | 0.3266 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1807.855 |  | 1796.9838 | 0.605 | 1786.525 | 1767.54 | 0.0531 | buy_precheck_manual_confirm | none |
| 6 | VRT | data_center_power_cooling | 300.65 |  | 298.8821 | 0.5915 | 297.69 | 293.905 | 0.1264 | buy_precheck_manual_confirm | none |
| 7 | STX | memory_hbm_storage | 914.775 |  | 908.5945 | 0.6802 | 899.59 | 860.605 | 0.117 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 559.18 |  | 552.884 | 1.1388 | 551.02 | 540.105 | 0.0429 | buy_precheck_manual_confirm | none |
| 9 | SMH | semiconductor_index | 590.345 |  | 585.1428 | 0.889 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| 10 | MU | memory_hbm_storage | 975.45 |  | 967.3153 | 0.841 | 963.41 | 936.99 | 0.2389 | buy_precheck_manual_confirm | none |
| 11 | NVDA | ai_accelerator | 213.34 |  | 211.0654 | 1.0777 | 207.4 | 205.01 | 0.0328 | buy_precheck_manual_confirm | none |
| 12 | LRCX | semiconductor_equipment | 320.07 |  | 318.9754 | 0.3432 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 143.06 |  | 142.8999 | 0.112 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ETN | data_center_power_cooling | 408.57 |  | 407.9042 | 0.1632 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | MRVL | custom_silicon_networking | 213.655 |  | 211.14 | 1.1912 | 207.06 | 202.18 | 0.1264 | buy_precheck_manual_confirm | none |
| 17 | TT | data_center_power_cooling | 475.51 |  | 473.4734 | 0.4301 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 643.34 |  | 640.4078 | 0.4579 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TSM | foundry | 421.635 |  | 420.6806 | 0.2269 | 419.42 | 414.87 | 0.9605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | MKSI | semiconductor_materials | 346.39 |  | 343.7929 | 0.7554 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.34 |  | 211.0654 | 1.0777 | 207.4 | 205.01 | 0.0328 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 975.45 |  | 967.3153 | 0.841 | 963.41 | 936.99 | 0.2389 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 914.775 |  | 908.5945 | 0.6802 | 899.59 | 860.605 | 0.117 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 559.18 |  | 552.884 | 1.1388 | 551.02 | 540.105 | 0.0429 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 590.345 |  | 585.1428 | 0.889 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 213.655 |  | 211.14 | 1.1912 | 207.06 | 202.18 | 0.1264 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 708.695 |  | 707.3689 | 0.1875 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 749.24 |  | 748.4776 | 0.1019 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 9 | ASML | semiconductor_equipment | 1807.855 |  | 1796.9838 | 0.605 | 1786.525 | 1767.54 | 0.0531 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 300.65 |  | 298.8821 | 0.5915 | 297.69 | 293.905 | 0.1264 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 31.28 |  | 31.1782 | 0.3266 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 71.28 |  | 70.8411 | 0.6196 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 13 | DELL | ai_server_oem | 442.51 |  | 442.7187 | -0.0471 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | CRWV | gpu_cloud_ai_factory | 83.49 |  | 83.522 | -0.0383 | 83.22 | 79.6 | 4.8149 | below_vwap | below_vwap,spread_too_wide |
| 15 | TSM | foundry | 421.635 |  | 420.6806 | 0.2269 | 419.42 | 414.87 | 0.9605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 556.23 |  | 551.4026 | 0.8755 | 548.755 | 526.6 | 0.6508 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TT | data_center_power_cooling | 475.51 |  | 473.4734 | 0.4301 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SNDK | memory_hbm_storage | 1613.3 |  | 1577.3085 | 2.2818 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | WDC | memory_hbm_storage | 558.74 |  | 555.6495 | 0.5562 | 548.14 | 526.22 | 5.0685 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 371.685 |  | 371.5312 | 0.0414 | 369.53 | 365 | 5.1011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.695 |  | 707.3689 | 0.1875 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.28 |  | 70.8411 | 0.6196 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.34 |  | 211.0654 | 1.0777 | 207.4 | 205.01 | 0.0328 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.44 |  | 390.413 | -0.5054 | 400.89 | 392.26 | 0.103 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.81 |  | 325.2005 | -0.4276 | 328.865 | 325.74 | 0.2162 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.305 |  | 347.9453 | 0.1034 | 348.76 | 346.23 | 0.0545 | watch_only | none |
| AMD | ai_accelerator | 556.23 |  | 551.4026 | 0.8755 | 548.755 | 526.6 | 0.6508 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.635 |  | 420.6806 | 0.2269 | 419.42 | 414.87 | 0.9605 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.18 |  | 552.884 | 1.1388 | 551.02 | 540.105 | 0.0429 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.345 |  | 585.1428 | 0.889 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.04 |  | 389.9887 | 1.5517 | 387.635 | 380.205 | 4.3935 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 975.45 |  | 967.3153 | 0.841 | 963.41 | 936.99 | 0.2389 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 213.655 |  | 211.14 | 1.1912 | 207.06 | 202.18 | 0.1264 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 442.51 |  | 442.7187 | -0.0471 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.79 |  | 49.0313 | -0.4921 | 48.96 | 47.01 | 0.0615 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.28 |  | 31.1782 | 0.3266 | 30.66 | 28.52 | 0.032 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.24 |  | 748.4776 | 0.1019 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.355 |  | 295.1488 | -0.2689 | 296.39 | 295.22 | 0.0102 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.435 |  | 126.6863 | -0.1983 | 128.79 | 125.83 | 1.8824 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.49 |  | 83.522 | -0.0383 | 83.22 | 79.6 | 4.8149 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 300.65 |  | 298.8821 | 0.5915 | 297.69 | 293.905 | 0.1264 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 408.57 |  | 407.9042 | 0.1632 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.34 |  | 640.4078 | 0.4579 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 990.1 |  | 1007.7495 | -1.7514 | 1036.605 | 998.94 | 1.1221 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.51 |  | 473.4734 | 0.4301 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.06 |  | 142.8999 | 0.112 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.21 |  | 174.8526 | 0.2044 | 175.265 | 171.06 | 2.6711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.46 |  | 316.1681 | -0.224 | 317.93 | 306.89 | 2.5265 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 832.49 |  | 840.5832 | -0.9628 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 402.12 |  | 405.9179 | -0.9356 | 407.12 | 397.835 | 1.9223 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.815 |  | 114.6004 | -2.4305 | 117.185 | 113.68 | 4.6148 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 333.24 |  | 329.2893 | 1.1998 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1807.855 |  | 1796.9838 | 0.605 | 1786.525 | 1767.54 | 0.0531 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.185 |  | 558.428 | 0.1356 | 559.22 | 544.305 | 0.524 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 320.07 |  | 318.9754 | 0.3432 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.455 |  | 216.0818 | 0.1727 | 215.465 | 210.975 | 4.3335 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 371.685 |  | 371.5312 | 0.0414 | 369.53 | 365 | 5.1011 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 295.265 |  | 295.3329 | -0.023 | 298.42 | 288.335 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.72 |  | 67.4749 | 0.3632 | 66.73 | 64.98 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.11 |  | 138.7448 | 0.2632 | 140.09 | 135.555 | 4.7373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 346.39 |  | 343.7929 | 0.7554 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.61 |  | 507.2126 | 0.4727 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.64 |  | 297.7588 | -0.0399 | 300.24 | 297.585 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.24 |  | 30.7802 | -1.7549 | 30.78 | 29.46 | 0.0661 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.91 |  | 42.6826 | -1.8101 | 42.29 | 40.305 | 0.0716 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.88 |  | 24.1302 | -1.0367 | 24.255 | 23.58 | 0.0838 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1613.3 |  | 1577.3085 | 2.2818 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 558.74 |  | 555.6495 | 0.5562 | 548.14 | 526.22 | 5.0685 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 914.775 |  | 908.5945 | 0.6802 | 899.59 | 860.605 | 0.117 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 243.255 |  | 244.4822 | -0.502 | 248.43 | 244.47 | 0.0164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 630.03 |  | 631.271 | -0.1966 | 647.02 | 632.77 | 0.1 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 286.08 |  | 285.6434 | 0.1529 | 286.39 | 280.275 | 2.6251 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 168.36 |  | 166.76 | 0.9594 | 166.63 | 162.08 | 3.6885 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
