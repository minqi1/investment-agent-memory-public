# Intraday State

- Generated at: `2026-07-18T03:08:26+08:00`
- Market time ET: `2026-07-17T15:08:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'below_vwap': 19, 'watch_only': 4, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.71 |  | 695.6518 | 0.1521 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 521.82 |  | 518.6492 | 0.6113 | 511.83 | 498.665 | 0.0862 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.83 |  | 555.2263 | 0.1087 | 550 | 536.9 | 0.0594 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.55 |  | 744.8603 | -0.1759 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 555.83 |  | 555.2263 | 0.1087 | 550 | 536.9 | 0.0594 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 521.82 |  | 518.6492 | 0.6113 | 511.83 | 498.665 | 0.0862 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1051.02 |  | 1045.5122 | 0.5268 | 1001.82 | 982.21 | 0.1598 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 696.71 |  | 695.6518 | 0.1521 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.13 |  | 45.6982 | 0.9448 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 6 | STX | memory_hbm_storage | 787.31 |  | 762.8852 | 3.2016 | 724.57 | 702.24 | 0.1029 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 188.85 |  | 187.2443 | 0.8576 | 185.03 | 178.09 | 0.2648 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.52 |  | 24.3199 | 0.8228 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.93 |  | 20.6748 | 1.2341 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 67.87 |  | 67.2425 | 0.9333 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.71 |  | 695.6518 | 0.1521 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 555.83 |  | 555.2263 | 0.1087 | 550 | 536.9 | 0.0594 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 644.16 |  | 642.5749 | 0.2467 | 649.07 | 638.97 | 0.2142 | watch_only | none |
| 4 | SOXX | semiconductor_index | 521.82 |  | 518.6492 | 0.6113 | 511.83 | 498.665 | 0.0862 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 394.91 |  | 393.5064 | 0.3567 | 398.39 | 393.52 | 0.043 | watch_only | none |
| 6 | AAPL | mega_cap_platform | 334.05 |  | 332.2324 | 0.5471 | 334.98 | 331.295 | 0.006 | watch_only | none |
| 7 | GEV | data_center_power_cooling | 1051.02 |  | 1045.5122 | 0.5268 | 1001.82 | 982.21 | 0.1598 | buy_precheck_manual_confirm | none |
| 8 | APLD | high_beta_ai_infrastructure | 25.27 |  | 25.0988 | 0.6822 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| 9 | SMCI | ai_server_oem | 24.52 |  | 24.3199 | 0.8228 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.13 |  | 45.6982 | 0.9448 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.93 |  | 20.6748 | 1.2341 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| 12 | MRVL | custom_silicon_networking | 188.85 |  | 187.2443 | 0.8576 | 185.03 | 178.09 | 0.2648 | buy_precheck_manual_confirm | none |
| 13 | PWR | data_center_power_cooling | 631.42 |  | 630.3071 | 0.1766 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 278.01 |  | 277.768 | 0.0871 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ORCL | cloud_ai_capex | 126.05 |  | 126.0393 | 0.0085 | 125.02 | 121.79 | 3.4748 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 787.31 |  | 762.8852 | 3.2016 | 724.57 | 702.24 | 0.1029 | buy_precheck_manual_confirm | none |
| 17 | AVGO | custom_silicon_networking | 371.895 |  | 370.3771 | 0.4098 | 368.42 | 357.97 | 2.1942 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 322.255 |  | 320.2884 | 0.614 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | MU | memory_hbm_storage | 868.09 |  | 864.6894 | 0.3933 | 835.82 | 804.09 | 1.2671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SPY | market_regime | 743.55 |  | 744.8603 | -0.1759 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 555.83 |  | 555.2263 | 0.1087 | 550 | 536.9 | 0.0594 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 521.82 |  | 518.6492 | 0.6113 | 511.83 | 498.665 | 0.0862 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1051.02 |  | 1045.5122 | 0.5268 | 1001.82 | 982.21 | 0.1598 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 696.71 |  | 695.6518 | 0.1521 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| 5 | HPE | ai_server_oem | 46.13 |  | 45.6982 | 0.9448 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 6 | STX | memory_hbm_storage | 787.31 |  | 762.8852 | 3.2016 | 724.57 | 702.24 | 0.1029 | buy_precheck_manual_confirm | none |
| 7 | MRVL | custom_silicon_networking | 188.85 |  | 187.2443 | 0.8576 | 185.03 | 178.09 | 0.2648 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.52 |  | 24.3199 | 0.8228 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.93 |  | 20.6748 | 1.2341 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 67.87 |  | 67.2425 | 0.9333 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 395.785 |  | 398.0058 | -0.558 | 394.11 | 386.02 | 0.1567 | below_vwap | below_vwap |
| 12 | ASML | semiconductor_equipment | 1752.72 |  | 1757.1576 | -0.2525 | 1741.99 | 1704.935 | 2.5503 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 212.07 |  | 212.2435 | -0.0818 | 210.82 | 204.71 | 4.7626 | below_vwap | below_vwap,spread_too_wide |
| 14 | CIEN | ai_networking_optical | 375.78 |  | 377.8075 | -0.5367 | 375.52 | 359.81 | 0.3406 | below_vwap | below_vwap |
| 15 | ETN | data_center_power_cooling | 399 |  | 399.7792 | -0.1949 | 389.4 | 382.38 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | LRCX | semiconductor_equipment | 310.79 |  | 312.1325 | -0.4301 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | SPY | market_regime | 743.55 |  | 744.8603 | -0.1759 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 18 | SNDK | memory_hbm_storage | 1417.43 |  | 1427.8006 | -0.7263 | 1393.96 | 1325.48 | 1.1838 | below_vwap | below_vwap,spread_too_wide |
| 19 | SKHY | memory_hbm_storage | 157.33 |  | 158.9724 | -1.0331 | 151.99 | 145.6 | 3.1081 | below_vwap | below_vwap,spread_too_wide |
| 20 | ANET | ai_networking_optical | 168.6 |  | 166.2862 | 1.3914 | 163.275 | 157.34 | 4.573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.71 |  | 695.6518 | 0.1521 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.87 |  | 67.2425 | 0.9333 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.77 |  | 203.2386 | -0.2306 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.91 |  | 393.5064 | 0.3567 | 398.39 | 393.52 | 0.043 | watch_only | none |
| AAPL | mega_cap_platform | 334.05 |  | 332.2324 | 0.5471 | 334.98 | 331.295 | 0.006 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.805 |  | 345.7845 | -0.2833 | 348.47 | 341.42 | 0.1131 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.615 |  | 486.9847 | 1.7722 | 482.43 | 461.04 | 3.3009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 395.785 |  | 398.0058 | -0.558 | 394.11 | 386.02 | 0.1567 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 521.82 |  | 518.6492 | 0.6113 | 511.83 | 498.665 | 0.0862 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.83 |  | 555.2263 | 0.1087 | 550 | 536.9 | 0.0594 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.895 |  | 370.3771 | 0.4098 | 368.42 | 357.97 | 2.1942 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 868.09 |  | 864.6894 | 0.3933 | 835.82 | 804.09 | 1.2671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 188.85 |  | 187.2443 | 0.8576 | 185.03 | 178.09 | 0.2648 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 399.99 |  | 393.379 | 1.6806 | 384 | 368.28 | 1.125 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.13 |  | 45.6982 | 0.9448 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.52 |  | 24.3199 | 0.8228 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.55 |  | 744.8603 | -0.1759 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.45 |  | 294.1435 | -0.2358 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.05 |  | 126.0393 | 0.0085 | 125.02 | 121.79 | 3.4748 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.28 |  | 72.2642 | 1.4056 | 71.24 | 68.65 | 0.3957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.77 |  | 287.55 | 1.1198 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 399 |  | 399.7792 | -0.1949 | 389.4 | 382.38 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 631.42 |  | 630.3071 | 0.1766 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1051.02 |  | 1045.5122 | 0.5268 | 1001.82 | 982.21 | 0.1598 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 467.9 |  | 469.7273 | -0.389 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.705 |  | 140.9273 | -0.1578 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.6 |  | 166.2862 | 1.3914 | 163.275 | 157.34 | 4.573 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.705 |  | 274.1677 | 0.9254 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 733.86 |  | 718.7689 | 2.0996 | 694.98 | 653.305 | 1.7238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.78 |  | 377.8075 | -0.5367 | 375.52 | 359.81 | 0.3406 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 102.005 |  | 100.617 | 1.3795 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 301.05 |  | 304.8995 | -1.2626 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1752.72 |  | 1757.1576 | -0.2525 | 1741.99 | 1704.935 | 2.5503 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 530.33 |  | 534.9983 | -0.8726 | 535.095 | 513.34 | 0.413 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 310.79 |  | 312.1325 | -0.4301 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.07 |  | 212.2435 | -0.0818 | 210.82 | 204.71 | 4.7626 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 322.255 |  | 320.2884 | 0.614 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.01 |  | 277.768 | 0.0871 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.2 |  | 61.5965 | 0.9797 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.79 |  | 49.9574 | 1.6667 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.08 |  | 134.9765 | 1.5584 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324 |  | 319.0459 | 1.5528 | 315.89 | 307.13 | 4.3025 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.78 |  | 518.704 | -0.9493 | 526.74 | 522.205 | 3.7428 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 295.81 |  | 298.8442 | -1.0153 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.27 |  | 25.0988 | 0.6822 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.485 |  | 33.7813 | -0.877 | 34 | 32.26 | 0.0299 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.93 |  | 20.6748 | 1.2341 | 20.445 | 19.92 | 0.0478 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1417.43 |  | 1427.8006 | -0.7263 | 1393.96 | 1325.48 | 1.1838 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.18 |  | 467.5699 | 2.6969 | 453.35 | 431.78 | 0.6268 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 787.31 |  | 762.8852 | 3.2016 | 724.57 | 702.24 | 0.1029 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.715 |  | 247.9881 | -0.1101 | 247.72 | 243.725 | 0.1413 | below_vwap | below_vwap |
| META | cloud_ai_capex | 644.16 |  | 642.5749 | 0.2467 | 649.07 | 638.97 | 0.2142 | watch_only | none |
| ARM | ai_accelerator | 266.88 |  | 261.3305 | 2.1236 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 157.33 |  | 158.9724 | -1.0331 | 151.99 | 145.6 | 3.1081 | below_vwap | below_vwap,spread_too_wide |
