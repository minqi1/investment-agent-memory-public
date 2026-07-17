# Intraday State

- Generated at: `2026-07-17T23:38:34+08:00`
- Market time ET: `2026-07-17T11:38:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 3, 'watch_only': 4, 'spread_too_wide_or_missing': 31, 'price_stale_or_missing': 1, 'below_vwap': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.13 |  | 693.3239 | 0.4047 | 693.36 | 686.78 | 0.0474 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 519.475 |  | 512.6132 | 1.3386 | 511.83 | 498.665 | 0.104 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.18 |  | 549.9231 | 0.9559 | 550 | 536.9 | 0.0883 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.18 |  | 744.429 | 0.1009 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.705 |  | 202.25 | 1.2138 | 203.41 | 197.98 | 0.044 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 398.68 |  | 395.1984 | 0.881 | 394.11 | 386.02 | 0.1179 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.18 |  | 549.9231 | 0.9559 | 550 | 536.9 | 0.0883 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 519.475 |  | 512.6132 | 1.3386 | 511.83 | 498.665 | 0.104 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1761.22 |  | 1738.793 | 1.2898 | 1741.99 | 1704.935 | 0.1675 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 211.11 |  | 210.2131 | 0.4267 | 210.82 | 204.71 | 0.1184 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.13 |  | 693.3239 | 0.4047 | 693.36 | 686.78 | 0.0474 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.49 |  | 45.289 | 0.4438 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.18 |  | 744.429 | 0.1009 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 754.57 |  | 735.8583 | 2.5428 | 724.57 | 702.24 | 0.163 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.27 |  | 247.8237 | 0.1801 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 12 | ORCL | cloud_ai_capex | 125.825 |  | 124.9336 | 0.7135 | 125.02 | 121.79 | 0.2543 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.73 |  | 20.387 | 1.6822 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 67.75 |  | 66.6927 | 1.5853 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.18 |  | 744.429 | 0.1009 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.27 |  | 247.8237 | 0.1801 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 211.11 |  | 210.2131 | 0.4267 | 210.82 | 204.71 | 0.1184 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 696.13 |  | 693.3239 | 0.4047 | 693.36 | 686.78 | 0.0474 | buy_precheck_manual_confirm | none |
| 5 | SMCI | ai_server_oem | 24.06 |  | 24.0125 | 0.1978 | 24.3 | 23.46 | 0.0416 | watch_only | none |
| 6 | HPE | ai_server_oem | 45.49 |  | 45.289 | 0.4438 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| 7 | IREN | high_beta_ai_infrastructure | 33.52 |  | 33.4252 | 0.2836 | 34 | 32.26 | 0.0298 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 125.825 |  | 124.9336 | 0.7135 | 125.02 | 121.79 | 0.2543 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 204.705 |  | 202.25 | 1.2138 | 203.41 | 197.98 | 0.044 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 333.81 |  | 332.4429 | 0.4112 | 334.98 | 331.295 | 0.033 | watch_only | none |
| 11 | APLD | high_beta_ai_infrastructure | 24.945 |  | 24.8096 | 0.5458 | 25.45 | 24.1 | 0.0802 | watch_only | none |
| 12 | TSM | foundry | 398.68 |  | 395.1984 | 0.881 | 394.11 | 386.02 | 0.1179 | buy_precheck_manual_confirm | none |
| 13 | SMH | semiconductor_index | 555.18 |  | 549.9231 | 0.9559 | 550 | 536.9 | 0.0883 | buy_precheck_manual_confirm | none |
| 14 | TT | data_center_power_cooling | 469.7 |  | 469.0217 | 0.1446 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SOXX | semiconductor_index | 519.475 |  | 512.6132 | 1.3386 | 511.83 | 498.665 | 0.104 | buy_precheck_manual_confirm | none |
| 16 | ASML | semiconductor_equipment | 1761.22 |  | 1738.793 | 1.2898 | 1741.99 | 1704.935 | 0.1675 | buy_precheck_manual_confirm | none |
| 17 | ALAB | ai_networking_optical | 300.905 |  | 300.1512 | 0.2511 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 141.16 |  | 140.4966 | 0.4722 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | CORZ | high_beta_ai_infrastructure | 20.73 |  | 20.387 | 1.6822 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 20 | AVGO | custom_silicon_networking | 370.09 |  | 368.0255 | 0.561 | 368.42 | 357.97 | 3.2019 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.705 |  | 202.25 | 1.2138 | 203.41 | 197.98 | 0.044 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 398.68 |  | 395.1984 | 0.881 | 394.11 | 386.02 | 0.1179 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 555.18 |  | 549.9231 | 0.9559 | 550 | 536.9 | 0.0883 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 519.475 |  | 512.6132 | 1.3386 | 511.83 | 498.665 | 0.104 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1761.22 |  | 1738.793 | 1.2898 | 1741.99 | 1704.935 | 0.1675 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 211.11 |  | 210.2131 | 0.4267 | 210.82 | 204.71 | 0.1184 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 696.13 |  | 693.3239 | 0.4047 | 693.36 | 686.78 | 0.0474 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.49 |  | 45.289 | 0.4438 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| 9 | SPY | market_regime | 745.18 |  | 744.429 | 0.1009 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 754.57 |  | 735.8583 | 2.5428 | 724.57 | 702.24 | 0.163 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.27 |  | 247.8237 | 0.1801 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| 12 | ORCL | cloud_ai_capex | 125.825 |  | 124.9336 | 0.7135 | 125.02 | 121.79 | 0.2543 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.73 |  | 20.387 | 1.6822 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 67.75 |  | 66.6927 | 1.5853 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 164.95 |  | 162.9857 | 1.2052 | 163.275 | 157.34 | 4.9409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 370.09 |  | 368.0255 | 0.561 | 368.42 | 357.97 | 3.2019 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 536.51 |  | 528.8959 | 1.4396 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 491.415 |  | 479.2287 | 2.5429 | 482.43 | 461.04 | 0.816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 469.7 |  | 469.0217 | 0.1446 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 864.48 |  | 849.252 | 1.7931 | 835.82 | 804.09 | 1.3881 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.13 |  | 693.3239 | 0.4047 | 693.36 | 686.78 | 0.0474 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.75 |  | 66.6927 | 1.5853 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.705 |  | 202.25 | 1.2138 | 203.41 | 197.98 | 0.044 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 391.32 |  | 393.1215 | -0.4582 | 398.39 | 393.52 | 0.0537 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.81 |  | 332.4429 | 0.4112 | 334.98 | 331.295 | 0.033 | watch_only | none |
| GOOGL | cloud_ai_capex | 347.15 |  | 345.7001 | 0.4194 | 348.47 | 341.42 | 0.8527 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 491.415 |  | 479.2287 | 2.5429 | 482.43 | 461.04 | 0.816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 398.68 |  | 395.1984 | 0.881 | 394.11 | 386.02 | 0.1179 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 519.475 |  | 512.6132 | 1.3386 | 511.83 | 498.665 | 0.104 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.18 |  | 549.9231 | 0.9559 | 550 | 536.9 | 0.0883 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 370.09 |  | 368.0255 | 0.561 | 368.42 | 357.97 | 3.2019 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 864.48 |  | 849.252 | 1.7931 | 835.82 | 804.09 | 1.3881 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 186.15 |  | 184.4924 | 0.8985 | 185.03 | 178.09 | 0.8273 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 390.58 |  | 386.9548 | 0.9368 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.49 |  | 45.289 | 0.4438 | 44.92 | 43.715 | 0.022 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.06 |  | 24.0125 | 0.1978 | 24.3 | 23.46 | 0.0416 | watch_only | none |
| SPY | market_regime | 745.18 |  | 744.429 | 0.1009 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.61 |  | 294.0343 | -0.1443 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.825 |  | 124.9336 | 0.7135 | 125.02 | 121.79 | 0.2543 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.105 |  | 71.3922 | 2.3991 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 287.99 |  | 282.7098 | 1.8677 | 280.565 | 273.17 | 4.6113 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 398.96 |  | 396.1028 | 0.7213 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 628.9 |  | 624.2754 | 0.7408 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1042.03 |  | 1027.2252 | 1.4412 | 1001.82 | 982.21 | 1.1823 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.7 |  | 469.0217 | 0.1446 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.16 |  | 140.4966 | 0.4722 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.95 |  | 162.9857 | 1.2052 | 163.275 | 157.34 | 4.9409 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.33 |  | 269.1559 | 2.6654 | 269.59 | 256.24 | 4.7697 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 722.225 |  | 700.0775 | 3.1636 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 376.81 |  | 373.3671 | 0.9221 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.08 |  | 98.2506 | 2.8797 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 300.905 |  | 300.1512 | 0.2511 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1761.22 |  | 1738.793 | 1.2898 | 1741.99 | 1704.935 | 0.1675 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 536.51 |  | 528.8959 | 1.4396 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 313.96 |  | 307.7343 | 2.0231 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 211.11 |  | 210.2131 | 0.4267 | 210.82 | 204.71 | 0.1184 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 314.99 |  | 309.7781 | 1.6825 | 308.03 | 297.18 | 5.0383 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 269.225 |  | 267.0096 | 0.8297 | 265.71 | 258.355 | 0.5052 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 61.51 |  | 60.3518 | 1.9192 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.87 |  | 48.7613 | 2.2737 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.96 |  | 132.9119 | 2.2933 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 317.73 |  | 314.9647 | 0.878 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 520.53 |  | 521.7696 | -0.2376 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 300.13 |  | 301.4484 | -0.4374 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 24.945 |  | 24.8096 | 0.5458 | 25.45 | 24.1 | 0.0802 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.52 |  | 33.4252 | 0.2836 | 34 | 32.26 | 0.0298 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.73 |  | 20.387 | 1.6822 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1432.43 |  | 1401.794 | 2.1855 | 1393.96 | 1325.48 | 2.4357 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 463.28 |  | 452.2355 | 2.4422 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 754.57 |  | 735.8583 | 2.5428 | 724.57 | 702.24 | 0.163 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 248.27 |  | 247.8237 | 0.1801 | 247.72 | 243.725 | 0.0201 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 629.29 |  | 635.7343 | -1.0137 | 649.07 | 638.97 | 0.7135 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 260.18 |  | 255.1277 | 1.9803 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 161.045 |  | 155.3348 | 3.6761 | 151.99 | 145.6 | 3.7878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
