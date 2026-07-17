# Intraday State

- Generated at: `2026-07-18T03:56:43+08:00`
- Market time ET: `2026-07-17T15:56:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 17, 'watch_only': 4, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 1, 'below_vwap': 13, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.92 |  | 695.698 | 0.1756 | 693.36 | 686.78 | 0.0115 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.45 |  | 519.4361 | 0.7727 | 511.83 | 498.665 | 0.0401 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.16 |  | 555.4267 | 0.4921 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.03 |  | 744.4501 | -0.0564 | 742.66 | 740.8 | 0.0134 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.5 |  | 203.1777 | 0.1586 | 203.41 | 197.98 | 0.0393 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.16 |  | 555.4267 | 0.4921 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 372.325 |  | 370.5958 | 0.4666 | 368.42 | 357.97 | 0.0645 | buy_precheck_manual_confirm | none |
| 4 | AMD | ai_accelerator | 499.32 |  | 489.1348 | 2.0823 | 482.43 | 461.04 | 0.1562 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 523.45 |  | 519.4361 | 0.7727 | 511.83 | 498.665 | 0.0401 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 213.61 |  | 212.3634 | 0.587 | 210.82 | 204.71 | 0.0421 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 289.845 |  | 288.0618 | 0.619 | 280.565 | 273.17 | 0.0759 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 696.92 |  | 695.698 | 0.1756 | 693.36 | 686.78 | 0.0115 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.075 |  | 45.7375 | 0.738 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 790.59 |  | 771.0391 | 2.5357 | 724.57 | 702.24 | 0.0329 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 477.51 |  | 468.7769 | 1.863 | 453.35 | 431.78 | 0.0796 | buy_precheck_manual_confirm | none |
| 12 | MRVL | custom_silicon_networking | 189.315 |  | 187.3714 | 1.0373 | 185.03 | 178.09 | 0.1849 | buy_precheck_manual_confirm | none |
| 13 | ORCL | cloud_ai_capex | 126.64 |  | 126.1304 | 0.404 | 125.02 | 121.79 | 0.1895 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 24.355 |  | 24.3308 | 0.0994 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 15 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6926 | 1.099 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| 16 | APLD | high_beta_ai_infrastructure | 25.585 |  | 25.1416 | 1.7634 | 25.45 | 24.1 | 0.0391 | buy_precheck_manual_confirm | none |
| 17 | TQQQ | leveraged_tool | 67.95 |  | 67.2894 | 0.9818 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.5 |  | 203.1777 | 0.1586 | 203.41 | 197.98 | 0.0393 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 24.355 |  | 24.3308 | 0.0994 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.92 |  | 695.698 | 0.1756 | 693.36 | 686.78 | 0.0115 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 558.16 |  | 555.4267 | 0.4921 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 372.325 |  | 370.5958 | 0.4666 | 368.42 | 357.97 | 0.0645 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 394.405 |  | 393.78 | 0.1587 | 398.39 | 393.52 | 0.0127 | watch_only | none |
| 7 | KLAC | semiconductor_equipment | 213.61 |  | 212.3634 | 0.587 | 210.82 | 204.71 | 0.0421 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 523.45 |  | 519.4361 | 0.7727 | 511.83 | 498.665 | 0.0401 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 289.845 |  | 288.0618 | 0.619 | 280.565 | 273.17 | 0.0759 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.075 |  | 45.7375 | 0.738 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 11 | GOOGL | cloud_ai_capex | 346.93 |  | 345.7082 | 0.3534 | 348.47 | 341.42 | 0.0663 | watch_only | none |
| 12 | META | cloud_ai_capex | 646.725 |  | 642.764 | 0.6163 | 649.07 | 638.97 | 0.0912 | watch_only | none |
| 13 | ORCL | cloud_ai_capex | 126.64 |  | 126.1304 | 0.404 | 125.02 | 121.79 | 0.1895 | buy_precheck_manual_confirm | none |
| 14 | AAPL | mega_cap_platform | 333.895 |  | 332.5217 | 0.413 | 334.98 | 331.295 | 0.009 | watch_only | none |
| 15 | TT | data_center_power_cooling | 470.94 |  | 469.8366 | 0.2348 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6926 | 1.099 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| 17 | MRVL | custom_silicon_networking | 189.315 |  | 187.3714 | 1.0373 | 185.03 | 178.09 | 0.1849 | buy_precheck_manual_confirm | none |
| 18 | APLD | high_beta_ai_infrastructure | 25.585 |  | 25.1416 | 1.7634 | 25.45 | 24.1 | 0.0391 | buy_precheck_manual_confirm | none |
| 19 | PWR | data_center_power_cooling | 630.66 |  | 630.3998 | 0.0413 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TSM | foundry | 398.34 |  | 397.8892 | 0.1133 | 394.11 | 386.02 | 0.5021 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.5 |  | 203.1777 | 0.1586 | 203.41 | 197.98 | 0.0393 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.16 |  | 555.4267 | 0.4921 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 372.325 |  | 370.5958 | 0.4666 | 368.42 | 357.97 | 0.0645 | buy_precheck_manual_confirm | none |
| 4 | AMD | ai_accelerator | 499.32 |  | 489.1348 | 2.0823 | 482.43 | 461.04 | 0.1562 | buy_precheck_manual_confirm | none |
| 5 | SOXX | semiconductor_index | 523.45 |  | 519.4361 | 0.7727 | 511.83 | 498.665 | 0.0401 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 213.61 |  | 212.3634 | 0.587 | 210.82 | 204.71 | 0.0421 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 289.845 |  | 288.0618 | 0.619 | 280.565 | 273.17 | 0.0759 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 696.92 |  | 695.698 | 0.1756 | 693.36 | 686.78 | 0.0115 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.075 |  | 45.7375 | 0.738 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 790.59 |  | 771.0391 | 2.5357 | 724.57 | 702.24 | 0.0329 | buy_precheck_manual_confirm | none |
| 11 | WDC | memory_hbm_storage | 477.51 |  | 468.7769 | 1.863 | 453.35 | 431.78 | 0.0796 | buy_precheck_manual_confirm | none |
| 12 | MRVL | custom_silicon_networking | 189.315 |  | 187.3714 | 1.0373 | 185.03 | 178.09 | 0.1849 | buy_precheck_manual_confirm | none |
| 13 | ORCL | cloud_ai_capex | 126.64 |  | 126.1304 | 0.404 | 125.02 | 121.79 | 0.1895 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 24.355 |  | 24.3308 | 0.0994 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| 15 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6926 | 1.099 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| 16 | APLD | high_beta_ai_infrastructure | 25.585 |  | 25.1416 | 1.7634 | 25.45 | 24.1 | 0.0391 | buy_precheck_manual_confirm | none |
| 17 | TQQQ | leveraged_tool | 67.95 |  | 67.2894 | 0.9818 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 18 | ASML | semiconductor_equipment | 1750.89 |  | 1756.8643 | -0.3401 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | MU | memory_hbm_storage | 854.4 |  | 864.4006 | -1.1569 | 835.82 | 804.09 | 0.096 | below_vwap | below_vwap |
| 20 | SPY | market_regime | 744.03 |  | 744.4501 | -0.0564 | 742.66 | 740.8 | 0.0134 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.92 |  | 695.698 | 0.1756 | 693.36 | 686.78 | 0.0115 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.95 |  | 67.2894 | 0.9818 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.5 |  | 203.1777 | 0.1586 | 203.41 | 197.98 | 0.0393 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 394.405 |  | 393.78 | 0.1587 | 398.39 | 393.52 | 0.0127 | watch_only | none |
| AAPL | mega_cap_platform | 333.895 |  | 332.5217 | 0.413 | 334.98 | 331.295 | 0.009 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.93 |  | 345.7082 | 0.3534 | 348.47 | 341.42 | 0.0663 | watch_only | none |
| AMD | ai_accelerator | 499.32 |  | 489.1348 | 2.0823 | 482.43 | 461.04 | 0.1562 | buy_precheck_manual_confirm | none |
| TSM | foundry | 398.34 |  | 397.8892 | 0.1133 | 394.11 | 386.02 | 0.5021 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.45 |  | 519.4361 | 0.7727 | 511.83 | 498.665 | 0.0401 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.16 |  | 555.4267 | 0.4921 | 550 | 536.9 | 0.0502 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.325 |  | 370.5958 | 0.4666 | 368.42 | 357.97 | 0.0645 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 854.4 |  | 864.4006 | -1.1569 | 835.82 | 804.09 | 0.096 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 189.315 |  | 187.3714 | 1.0373 | 185.03 | 178.09 | 0.1849 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 399.71 |  | 394.1395 | 1.4133 | 384 | 368.28 | 0.5579 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.075 |  | 45.7375 | 0.738 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.355 |  | 24.3308 | 0.0994 | 24.3 | 23.46 | 0.0411 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.03 |  | 744.4501 | -0.0564 | 742.66 | 740.8 | 0.0134 | below_vwap | below_vwap |
| IWM | market_regime | 294.015 |  | 294.0708 | -0.019 | 294.205 | 291.675 | 0.0136 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.64 |  | 126.1304 | 0.404 | 125.02 | 121.79 | 0.1895 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.29 |  | 72.3544 | 1.2931 | 71.24 | 68.65 | 4.2025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 289.845 |  | 288.0618 | 0.619 | 280.565 | 273.17 | 0.0759 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 402.145 |  | 399.877 | 0.5672 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 630.66 |  | 630.3998 | 0.0413 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1057.88 |  | 1047.448 | 0.9959 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 470.94 |  | 469.8366 | 0.2348 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.54 |  | 140.8359 | -0.2101 | 140.765 | 137.165 | 0.0498 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 168.89 |  | 166.6769 | 1.3278 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 279.39 |  | 274.9552 | 1.6129 | 269.59 | 256.24 | 1.2384 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 736.13 |  | 721.4591 | 2.0335 | 694.98 | 653.305 | 4.2941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.49 |  | 377.4681 | -0.524 | 375.52 | 359.81 | 3.9442 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.93 |  | 100.9578 | 1.9535 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.17 |  | 304.5882 | -0.1373 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1750.89 |  | 1756.8643 | -0.3401 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 530.91 |  | 533.4087 | -0.4684 | 535.095 | 513.34 |  | below_vwap | below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 314.08 |  | 312.1426 | 0.6207 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.61 |  | 212.3634 | 0.587 | 210.82 | 204.71 | 0.0421 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.89 |  | 321.0193 | 1.2057 | 308.03 | 297.18 | 3.8536 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 278.595 |  | 277.7049 | 0.3205 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.11 |  | 61.8503 | 2.0368 | 60.51 | 57.99 | 4.7378 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 51.37 |  | 50.1582 | 2.4159 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.93 |  | 135.9189 | 2.2153 | 129.93 | 126.945 | 0.4463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.66 |  | 320.7585 | 1.5281 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 512.12 |  | 516.4522 | -0.8388 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.24 |  | 297.8543 | -0.8777 | 304.36 | 299.62 | 0.0813 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 25.585 |  | 25.1416 | 1.7634 | 25.45 | 24.1 | 0.0391 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 33.57 |  | 33.7072 | -0.407 | 34 | 32.26 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6926 | 1.099 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1360.37 |  | 1423.1689 | -4.4126 | 1393.96 | 1325.48 | 0.1308 | below_vwap | below_vwap |
| WDC | memory_hbm_storage | 477.51 |  | 468.7769 | 1.863 | 453.35 | 431.78 | 0.0796 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 790.59 |  | 771.0391 | 2.5357 | 724.57 | 702.24 | 0.0329 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.48 |  | 247.8846 | -0.1632 | 247.72 | 243.725 | 0.0202 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.725 |  | 642.764 | 0.6163 | 649.07 | 638.97 | 0.0912 | watch_only | none |
| ARM | ai_accelerator | 267.93 |  | 261.9604 | 2.2788 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 153.34 |  | 158.4419 | -3.22 | 151.99 | 145.6 | 0.1956 | below_vwap | below_vwap |
