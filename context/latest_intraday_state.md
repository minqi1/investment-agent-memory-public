# Intraday State

- Generated at: `2026-07-18T00:14:49+08:00`
- Market time ET: `2026-07-17T12:14:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'spread_too_wide_or_missing': 34, 'below_opening_15m_low': 5, 'watch_only': 1, 'price_stale_or_missing': 1, 'below_vwap': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.43 |  | 693.7818 | 0.8141 | 693.36 | 686.78 | 0.0558 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 529.12 |  | 514.6847 | 2.8047 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 563.88 |  | 551.296 | 2.2826 | 550 | 536.9 | 0.0621 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.1 |  | 744.6472 | 0.1951 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 563.88 |  | 551.296 | 2.2826 | 550 | 536.9 | 0.0621 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 529.12 |  | 514.6847 | 2.8047 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 294.46 |  | 294.0286 | 0.1467 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 699.43 |  | 693.7818 | 0.8141 | 693.36 | 686.78 | 0.0558 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.05 |  | 45.364 | 1.5122 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 746.1 |  | 744.6472 | 0.1951 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 480.25 |  | 454.7067 | 5.6175 | 453.35 | 431.78 | 0.2874 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 247.98 |  | 247.8799 | 0.0404 | 247.72 | 243.725 | 0.0202 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 127.28 |  | 125.1953 | 1.6652 | 125.02 | 121.79 | 0.0629 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.57 |  | 24.0574 | 2.1306 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.9 |  | 20.4912 | 1.9949 | 20.445 | 19.92 | 0.0957 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.525 |  | 24.867 | 2.6459 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.31 |  | 33.4918 | 2.4429 | 34 | 32.26 | 0.0874 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.68 |  | 66.8468 | 2.7425 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.46 |  | 294.0286 | 0.1467 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 247.98 |  | 247.8799 | 0.0404 | 247.72 | 243.725 | 0.0202 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 746.1 |  | 744.6472 | 0.1951 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 346.27 |  | 346.0765 | 0.0559 | 348.47 | 341.42 | 0.1011 | watch_only | none |
| 5 | QQQ | market_regime | 699.43 |  | 693.7818 | 0.8141 | 693.36 | 686.78 | 0.0558 | buy_precheck_manual_confirm | none |
| 6 | APLD | high_beta_ai_infrastructure | 25.525 |  | 24.867 | 2.6459 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.57 |  | 24.0574 | 2.1306 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 8 | SMH | semiconductor_index | 563.88 |  | 551.296 | 2.2826 | 550 | 536.9 | 0.0621 | buy_precheck_manual_confirm | none |
| 9 | SOXX | semiconductor_index | 529.12 |  | 514.6847 | 2.8047 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| 10 | IREN | high_beta_ai_infrastructure | 34.31 |  | 33.4918 | 2.4429 | 34 | 32.26 | 0.0874 | buy_precheck_manual_confirm | none |
| 11 | HPE | ai_server_oem | 46.05 |  | 45.364 | 1.5122 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 12 | ORCL | cloud_ai_capex | 127.28 |  | 125.1953 | 1.6652 | 125.02 | 121.79 | 0.0629 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.9 |  | 20.4912 | 1.9949 | 20.445 | 19.92 | 0.0957 | buy_precheck_manual_confirm | none |
| 14 | WDC | memory_hbm_storage | 480.25 |  | 454.7067 | 5.6175 | 453.35 | 431.78 | 0.2874 | buy_precheck_manual_confirm | none |
| 15 | TT | data_center_power_cooling | 473.67 |  | 469.2643 | 0.9389 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | JCI | data_center_power_cooling | 142.29 |  | 140.7127 | 1.121 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | NVDA | ai_accelerator | 204.89 |  | 202.5138 | 1.1734 | 203.41 | 197.98 | 0.6296 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | ETN | data_center_power_cooling | 403.685 |  | 398.5085 | 1.299 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 372.78 |  | 368.2251 | 1.237 | 368.42 | 357.97 | 0.6626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 563.88 |  | 551.296 | 2.2826 | 550 | 536.9 | 0.0621 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 529.12 |  | 514.6847 | 2.8047 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 294.46 |  | 294.0286 | 0.1467 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 699.43 |  | 693.7818 | 0.8141 | 693.36 | 686.78 | 0.0558 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.05 |  | 45.364 | 1.5122 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 746.1 |  | 744.6472 | 0.1951 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 7 | WDC | memory_hbm_storage | 480.25 |  | 454.7067 | 5.6175 | 453.35 | 431.78 | 0.2874 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 247.98 |  | 247.8799 | 0.0404 | 247.72 | 243.725 | 0.0202 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 127.28 |  | 125.1953 | 1.6652 | 125.02 | 121.79 | 0.0629 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.57 |  | 24.0574 | 2.1306 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.9 |  | 20.4912 | 1.9949 | 20.445 | 19.92 | 0.0957 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.525 |  | 24.867 | 2.6459 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.31 |  | 33.4918 | 2.4429 | 34 | 32.26 | 0.0874 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.68 |  | 66.8468 | 2.7425 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 168.1 |  | 163.5619 | 2.7745 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | NVDA | ai_accelerator | 204.89 |  | 202.5138 | 1.1734 | 203.41 | 197.98 | 0.6296 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TSM | foundry | 404 |  | 396.2628 | 1.9525 | 394.11 | 386.02 | 1.0941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AVGO | custom_silicon_networking | 372.78 |  | 368.2251 | 1.237 | 368.42 | 357.97 | 0.6626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 550.96 |  | 530.5095 | 3.8549 | 535.095 | 513.34 | 4.1455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 502.2 |  | 482.7515 | 4.0287 | 482.43 | 461.04 | 1.129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.43 |  | 693.7818 | 0.8141 | 693.36 | 686.78 | 0.0558 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.68 |  | 66.8468 | 2.7425 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.89 |  | 202.5138 | 1.1734 | 203.41 | 197.98 | 0.6296 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 391.62 |  | 392.9704 | -0.3436 | 398.39 | 393.52 | 0.0255 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.18 |  | 332.383 | -0.6628 | 334.98 | 331.295 | 0.2181 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.27 |  | 346.0765 | 0.0559 | 348.47 | 341.42 | 0.1011 | watch_only | none |
| AMD | ai_accelerator | 502.2 |  | 482.7515 | 4.0287 | 482.43 | 461.04 | 1.129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 404 |  | 396.2628 | 1.9525 | 394.11 | 386.02 | 1.0941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.12 |  | 514.6847 | 2.8047 | 511.83 | 498.665 | 0.0718 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 563.88 |  | 551.296 | 2.2826 | 550 | 536.9 | 0.0621 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.78 |  | 368.2251 | 1.237 | 368.42 | 357.97 | 0.6626 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 886.38 |  | 853.97 | 3.7952 | 835.82 | 804.09 | 0.9477 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 191.325 |  | 185.0693 | 3.3802 | 185.03 | 178.09 | 2.5611 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 397.5 |  | 388.0047 | 2.4472 | 384 | 368.28 | 3.1648 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.05 |  | 45.364 | 1.5122 | 44.92 | 43.715 | 0.0434 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.57 |  | 24.0574 | 2.1306 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.1 |  | 744.6472 | 0.1951 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.46 |  | 294.0286 | 0.1467 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.28 |  | 125.1953 | 1.6652 | 125.02 | 121.79 | 0.0629 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 74.22 |  | 71.7041 | 3.5088 | 71.24 | 68.65 | 1.8728 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 296.18 |  | 283.5853 | 4.4412 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 403.685 |  | 398.5085 | 1.299 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 637.03 |  | 626.2609 | 1.7196 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1062.77 |  | 1039.0364 | 2.2842 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 473.67 |  | 469.2643 | 0.9389 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.29 |  | 140.7127 | 1.121 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 168.1 |  | 163.5619 | 2.7745 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 282.7 |  | 270.9531 | 4.3354 | 269.59 | 256.24 | 4.2731 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 735.4 |  | 704.6082 | 4.3701 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 384.625 |  | 374.4305 | 2.7227 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 103.58 |  | 98.8312 | 4.805 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 307.755 |  | 301.2756 | 2.1506 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1786.11 |  | 1744.3254 | 2.3955 | 1741.99 | 1704.935 | 1.1864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 550.96 |  | 530.5095 | 3.8549 | 535.095 | 513.34 | 4.1455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.69 |  | 309.8679 | 3.8152 | 306.51 | 298.89 | 4.5665 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 215.87 |  | 211.0086 | 2.3039 | 210.82 | 204.71 | 1.9595 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 323.845 |  | 310.7497 | 4.2141 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 279.54 |  | 268.0347 | 4.2925 | 265.71 | 258.355 | 4.9796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 63.15 |  | 60.8002 | 3.8648 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.96 |  | 49.3745 | 3.2111 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.03 |  | 133.1461 | 3.668 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.81 |  | 316.2566 | 3.0208 | 315.89 | 307.13 | 4.7267 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 516.885 |  | 521.4446 | -0.8744 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 299.08 |  | 301.0923 | -0.6683 | 304.36 | 299.62 | 3.7114 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.525 |  | 24.867 | 2.6459 | 25.45 | 24.1 | 0.0392 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.31 |  | 33.4918 | 2.4429 | 34 | 32.26 | 0.0874 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.9 |  | 20.4912 | 1.9949 | 20.445 | 19.92 | 0.0957 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1491.24 |  | 1414.955 | 5.3913 | 1393.96 | 1325.48 | 4.9053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 480.25 |  | 454.7067 | 5.6175 | 453.35 | 431.78 | 0.2874 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 780.43 |  | 741.7881 | 5.2093 | 724.57 | 702.24 | 3.3866 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 247.98 |  | 247.8799 | 0.0404 | 247.72 | 243.725 | 0.0202 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 633.34 |  | 635.0468 | -0.2688 | 649.07 | 638.97 | 0.2732 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 267.17 |  | 256.6755 | 4.0886 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 165.97 |  | 156.6296 | 5.9634 | 151.99 | 145.6 | 3.0126 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
