# Intraday State

- Generated at: `2026-07-18T00:02:40+08:00`
- Market time ET: `2026-07-17T12:02:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'spread_too_wide_or_missing': 34, 'below_opening_15m_low': 4, 'below_vwap': 3, 'watch_only': 3, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.6 |  | 693.6582 | 0.7124 | 693.36 | 686.78 | 0.0887 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 526.43 |  | 513.9045 | 2.4373 | 511.83 | 498.665 | 0.0912 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 562.01 |  | 550.9111 | 2.0146 | 550 | 536.9 | 0.0907 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.91 |  | 744.5874 | 0.1776 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 562.01 |  | 550.9111 | 2.0146 | 550 | 536.9 | 0.0907 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 526.43 |  | 513.9045 | 2.4373 | 511.83 | 498.665 | 0.0912 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1776.65 |  | 1742.6197 | 1.9528 | 1741.99 | 1704.935 | 0.1362 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 215.815 |  | 210.538 | 2.5065 | 210.82 | 204.71 | 0.1853 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 698.6 |  | 693.6582 | 0.7124 | 693.36 | 686.78 | 0.0887 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.055 |  | 45.3312 | 1.5968 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.91 |  | 744.5874 | 0.1776 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.39 |  | 24.04 | 1.4559 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.4768 | 1.4805 | 20.445 | 19.92 | 0.1444 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 34.075 |  | 33.4462 | 1.8799 | 34 | 32.26 | 0.088 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 68.38 |  | 66.7923 | 2.3771 | 66.9 | 64.92 | 0.0439 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.91 |  | 744.5874 | 0.1776 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 698.6 |  | 693.6582 | 0.7124 | 693.36 | 686.78 | 0.0887 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 294.2 |  | 294.0076 | 0.0655 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 346.73 |  | 346.0264 | 0.2033 | 348.47 | 341.42 | 0.2307 | watch_only | none |
| 5 | SMCI | ai_server_oem | 24.39 |  | 24.04 | 1.4559 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 6 | IREN | high_beta_ai_infrastructure | 34.075 |  | 33.4462 | 1.8799 | 34 | 32.26 | 0.088 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.4768 | 1.4805 | 20.445 | 19.92 | 0.1444 | buy_precheck_manual_confirm | none |
| 8 | SMH | semiconductor_index | 562.01 |  | 550.9111 | 2.0146 | 550 | 536.9 | 0.0907 | buy_precheck_manual_confirm | none |
| 9 | SOXX | semiconductor_index | 526.43 |  | 513.9045 | 2.4373 | 511.83 | 498.665 | 0.0912 | buy_precheck_manual_confirm | none |
| 10 | ASML | semiconductor_equipment | 1776.65 |  | 1742.6197 | 1.9528 | 1741.99 | 1704.935 | 0.1362 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 46.055 |  | 45.3312 | 1.5968 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 215.815 |  | 210.538 | 2.5065 | 210.82 | 204.71 | 0.1853 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 25.41 |  | 24.8338 | 2.3204 | 25.45 | 24.1 | 0.1181 | watch_only | none |
| 14 | TT | data_center_power_cooling | 473.33 |  | 469.2321 | 0.8733 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | JCI | data_center_power_cooling | 142.23 |  | 140.652 | 1.1219 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AMZN | cloud_ai_capex | 247.76 |  | 247.8826 | -0.0495 | 247.72 | 243.725 | 0.113 | below_vwap | below_vwap |
| 17 | NVDA | ai_accelerator | 204.85 |  | 202.4418 | 1.1896 | 203.41 | 197.98 | 0.4393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AAPL | mega_cap_platform | 331.38 |  | 332.5324 | -0.3465 | 334.98 | 331.295 | 0.0151 | below_vwap | below_vwap |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ETN | data_center_power_cooling | 403.25 |  | 397.6914 | 1.3977 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 562.01 |  | 550.9111 | 2.0146 | 550 | 536.9 | 0.0907 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 526.43 |  | 513.9045 | 2.4373 | 511.83 | 498.665 | 0.0912 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1776.65 |  | 1742.6197 | 1.9528 | 1741.99 | 1704.935 | 0.1362 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 215.815 |  | 210.538 | 2.5065 | 210.82 | 204.71 | 0.1853 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 698.6 |  | 693.6582 | 0.7124 | 693.36 | 686.78 | 0.0887 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.055 |  | 45.3312 | 1.5968 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 745.91 |  | 744.5874 | 0.1776 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.39 |  | 24.04 | 1.4559 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.4768 | 1.4805 | 20.445 | 19.92 | 0.1444 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 34.075 |  | 33.4462 | 1.8799 | 34 | 32.26 | 0.088 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 68.38 |  | 66.7923 | 2.3771 | 66.9 | 64.92 | 0.0439 | buy_precheck_manual_confirm | none |
| 12 | AMZN | cloud_ai_capex | 247.76 |  | 247.8826 | -0.0495 | 247.72 | 243.725 | 0.113 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 167.77 |  | 163.4256 | 2.6584 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | NVDA | ai_accelerator | 204.85 |  | 202.4418 | 1.1896 | 203.41 | 197.98 | 0.4393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TSM | foundry | 402.71 |  | 395.8233 | 1.7398 | 394.11 | 386.02 | 0.6829 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 371.43 |  | 368.1648 | 0.8869 | 368.42 | 357.97 | 3.5 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 545.49 |  | 529.7764 | 2.9661 | 535.095 | 513.34 | 1.2668 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 498.82 |  | 481.9095 | 3.5091 | 482.43 | 461.04 | 0.9182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 473.33 |  | 469.2321 | 0.8733 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 886.14 |  | 852.3354 | 3.9661 | 835.82 | 804.09 | 1.7119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.6 |  | 693.6582 | 0.7124 | 693.36 | 686.78 | 0.0887 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.38 |  | 66.7923 | 2.3771 | 66.9 | 64.92 | 0.0439 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.85 |  | 202.4418 | 1.1896 | 203.41 | 197.98 | 0.4393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 392.12 |  | 393.0259 | -0.2305 | 398.39 | 393.52 | 0.3519 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 331.38 |  | 332.5324 | -0.3465 | 334.98 | 331.295 | 0.0151 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 346.73 |  | 346.0264 | 0.2033 | 348.47 | 341.42 | 0.2307 | watch_only | none |
| AMD | ai_accelerator | 498.82 |  | 481.9095 | 3.5091 | 482.43 | 461.04 | 0.9182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 402.71 |  | 395.8233 | 1.7398 | 394.11 | 386.02 | 0.6829 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.43 |  | 513.9045 | 2.4373 | 511.83 | 498.665 | 0.0912 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 562.01 |  | 550.9111 | 2.0146 | 550 | 536.9 | 0.0907 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.43 |  | 368.1648 | 0.8869 | 368.42 | 357.97 | 3.5 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 886.14 |  | 852.3354 | 3.9661 | 835.82 | 804.09 | 1.7119 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.18 |  | 184.7916 | 2.3748 | 185.03 | 178.09 | 3.2667 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 397.02 |  | 387.6486 | 2.4175 | 384 | 368.28 | 4.1056 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.055 |  | 45.3312 | 1.5968 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.39 |  | 24.04 | 1.4559 | 24.3 | 23.46 | 0.041 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.91 |  | 744.5874 | 0.1776 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.2 |  | 294.0076 | 0.0655 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 127.095 |  | 125.1217 | 1.5771 | 125.02 | 121.79 | 2.0221 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 74.185 |  | 71.6482 | 3.5406 | 71.24 | 68.65 | 2.9656 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 294.36 |  | 283.3826 | 3.8737 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 403.25 |  | 397.6914 | 1.3977 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 636.46 |  | 625.5411 | 1.7455 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1060.9 |  | 1037.8668 | 2.2193 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 473.33 |  | 469.2321 | 0.8733 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.23 |  | 140.652 | 1.1219 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.77 |  | 163.4256 | 2.6584 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 282.44 |  | 270.2691 | 4.5032 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 735.89 |  | 703.3616 | 4.6247 | 694.98 | 653.305 | 3.6187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 384.68 |  | 374.0936 | 2.8299 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.84 |  | 98.6262 | 5.2864 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 306.87 |  | 300.5303 | 2.1095 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1776.65 |  | 1742.6197 | 1.9528 | 1741.99 | 1704.935 | 0.1362 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 545.49 |  | 529.7764 | 2.9661 | 535.095 | 513.34 | 1.2668 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 319.515 |  | 309.0743 | 3.3781 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.815 |  | 210.538 | 2.5065 | 210.82 | 204.71 | 0.1853 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 321.92 |  | 310.2453 | 3.763 | 308.03 | 297.18 | 4.7993 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 276.41 |  | 267.717 | 3.2471 | 265.71 | 258.355 | 4.5765 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.75 |  | 60.6462 | 3.469 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.145 |  | 49.1657 | 4.0259 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.1 |  | 133.1044 | 3.7532 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 323.26 |  | 315.4154 | 2.4871 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 517.65 |  | 521.5494 | -0.7477 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 299.315 |  | 301.1543 | -0.6107 | 304.36 | 299.62 | 3.9891 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.41 |  | 24.8338 | 2.3204 | 25.45 | 24.1 | 0.1181 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.075 |  | 33.4462 | 1.8799 | 34 | 32.26 | 0.088 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.4768 | 1.4805 | 20.445 | 19.92 | 0.1444 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1495.24 |  | 1410.0651 | 6.0405 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 477.64 |  | 453.2713 | 5.3762 | 453.35 | 431.78 | 4.8363 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 772.605 |  | 738.7101 | 4.5884 | 724.57 | 702.24 | 0.5113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.76 |  | 247.8826 | -0.0495 | 247.72 | 243.725 | 0.113 | below_vwap | below_vwap |
| META | cloud_ai_capex | 630.9 |  | 635.2359 | -0.6826 | 649.07 | 638.97 | 0.9574 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 265.58 |  | 255.9181 | 3.7754 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 164.515 |  | 156.095 | 5.3941 | 151.99 | 145.6 | 3.4039 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
