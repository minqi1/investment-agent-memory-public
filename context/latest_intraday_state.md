# Intraday State

- Generated at: `2026-07-18T02:48:12+08:00`
- Market time ET: `2026-07-17T14:48:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_vwap': 14, 'watch_only': 3, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 24, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.83 |  | 695.5621 | 0.1823 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.2 |  | 518.4901 | 0.9084 | 511.83 | 498.665 | 0.0344 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.66 |  | 555.113 | 0.2787 | 550 | 536.9 | 0.0683 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.58 |  | 744.8885 | -0.1757 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.66 |  | 555.113 | 0.2787 | 550 | 536.9 | 0.0683 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 495.5 |  | 486.8184 | 1.7833 | 482.43 | 461.04 | 0.1574 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 523.2 |  | 518.4901 | 0.9084 | 511.83 | 498.665 | 0.0344 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 212.9 |  | 212.2043 | 0.3279 | 210.82 | 204.71 | 0.1362 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 870.61 |  | 864.3405 | 0.7254 | 835.82 | 804.09 | 0.1068 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.83 |  | 695.5621 | 0.1823 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.315 |  | 45.6726 | 1.4065 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 189.5 |  | 187.1748 | 1.2422 | 185.03 | 178.09 | 0.3377 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.56 |  | 24.3116 | 1.0218 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.995 |  | 20.6633 | 1.6052 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.78 |  | 67.2148 | 0.8408 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.83 |  | 695.5621 | 0.1823 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 556.66 |  | 555.113 | 0.2787 | 550 | 536.9 | 0.0683 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 212.9 |  | 212.2043 | 0.3279 | 210.82 | 204.71 | 0.1362 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.23 |  | 393.4073 | 0.2091 | 398.39 | 393.52 | 0.0152 | watch_only | none |
| 5 | MU | memory_hbm_storage | 870.61 |  | 864.3405 | 0.7254 | 835.82 | 804.09 | 0.1068 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 334.055 |  | 332.0622 | 0.6001 | 334.98 | 331.295 | 0.1227 | watch_only | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.21 |  | 25.0919 | 0.4709 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.56 |  | 24.3116 | 1.0218 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 9 | SOXX | semiconductor_index | 523.2 |  | 518.4901 | 0.9084 | 511.83 | 498.665 | 0.0344 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 46.315 |  | 45.6726 | 1.4065 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 11 | MRVL | custom_silicon_networking | 189.5 |  | 187.1748 | 1.2422 | 185.03 | 178.09 | 0.3377 | buy_precheck_manual_confirm | none |
| 12 | ONTO | semiconductor_test_packaging | 277.82 |  | 277.6707 | 0.0538 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ASML | semiconductor_equipment | 1760.16 |  | 1757.0599 | 0.1764 | 1741.99 | 1704.935 | 2.9009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 126.24 |  | 126.0296 | 0.167 | 125.02 | 121.79 | 1.4734 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 495.5 |  | 486.8184 | 1.7833 | 482.43 | 461.04 | 0.1574 | buy_precheck_manual_confirm | none |
| 16 | ETN | data_center_power_cooling | 399.9 |  | 399.7751 | 0.0312 | 389.4 | 382.38 | 3.8985 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | PWR | data_center_power_cooling | 632.52 |  | 630.0985 | 0.3843 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | CORZ | high_beta_ai_infrastructure | 20.995 |  | 20.6633 | 1.6052 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| 19 | META | cloud_ai_capex | 646.41 |  | 642.4328 | 0.6191 | 649.07 | 638.97 | 0.6111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AVGO | custom_silicon_networking | 372.57 |  | 370.2588 | 0.6242 | 368.42 | 357.97 | 1.9191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.66 |  | 555.113 | 0.2787 | 550 | 536.9 | 0.0683 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 495.5 |  | 486.8184 | 1.7833 | 482.43 | 461.04 | 0.1574 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 523.2 |  | 518.4901 | 0.9084 | 511.83 | 498.665 | 0.0344 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 212.9 |  | 212.2043 | 0.3279 | 210.82 | 204.71 | 0.1362 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 870.61 |  | 864.3405 | 0.7254 | 835.82 | 804.09 | 0.1068 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 696.83 |  | 695.5621 | 0.1823 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.315 |  | 45.6726 | 1.4065 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 189.5 |  | 187.1748 | 1.2422 | 185.03 | 178.09 | 0.3377 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 24.56 |  | 24.3116 | 1.0218 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.995 |  | 20.6633 | 1.6052 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.78 |  | 67.2148 | 0.8408 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 12 | TSM | foundry | 397.02 |  | 398.072 | -0.2643 | 394.11 | 386.02 | 1.0226 | below_vwap | below_vwap,spread_too_wide |
| 13 | TT | data_center_power_cooling | 469.13 |  | 469.7833 | -0.1391 | 469.08 | 460.78 | 0.13 | below_vwap | below_vwap |
| 14 | CIEN | ai_networking_optical | 376.91 |  | 377.8315 | -0.2439 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | LRCX | semiconductor_equipment | 311.745 |  | 312.122 | -0.1208 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | SPY | market_regime | 743.58 |  | 744.8885 | -0.1757 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 17 | SNDK | memory_hbm_storage | 1416.5 |  | 1428.0954 | -0.8119 | 1393.96 | 1325.48 | 1.4119 | below_vwap | below_vwap,spread_too_wide |
| 18 | ANET | ai_networking_optical | 168.56 |  | 166.175 | 1.4352 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 372.57 |  | 370.2588 | 0.6242 | 368.42 | 357.97 | 1.9191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1760.16 |  | 1757.0599 | 0.1764 | 1741.99 | 1704.935 | 2.9009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.83 |  | 695.5621 | 0.1823 | 693.36 | 686.78 | 0.0057 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.78 |  | 67.2148 | 0.8408 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.23 |  | 203.2413 | -0.0056 | 203.41 | 197.98 | 0.0443 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.23 |  | 393.4073 | 0.2091 | 398.39 | 393.52 | 0.0152 | watch_only | none |
| AAPL | mega_cap_platform | 334.055 |  | 332.0622 | 0.6001 | 334.98 | 331.295 | 0.1227 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.4 |  | 345.814 | -0.4089 | 348.47 | 341.42 | 0.0174 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.5 |  | 486.8184 | 1.7833 | 482.43 | 461.04 | 0.1574 | buy_precheck_manual_confirm | none |
| TSM | foundry | 397.02 |  | 398.072 | -0.2643 | 394.11 | 386.02 | 1.0226 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.2 |  | 518.4901 | 0.9084 | 511.83 | 498.665 | 0.0344 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.66 |  | 555.113 | 0.2787 | 550 | 536.9 | 0.0683 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.57 |  | 370.2588 | 0.6242 | 368.42 | 357.97 | 1.9191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 870.61 |  | 864.3405 | 0.7254 | 835.82 | 804.09 | 0.1068 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 189.5 |  | 187.1748 | 1.2422 | 185.03 | 178.09 | 0.3377 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 400.94 |  | 393.111 | 1.9916 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.315 |  | 45.6726 | 1.4065 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.56 |  | 24.3116 | 1.0218 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.58 |  | 744.8885 | -0.1757 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.6 |  | 294.1598 | -0.1903 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.24 |  | 126.0296 | 0.167 | 125.02 | 121.79 | 1.4734 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.505 |  | 72.2234 | 1.7744 | 71.24 | 68.65 | 2.6801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 291.37 |  | 287.3455 | 1.4006 | 280.565 | 273.17 | 4.5578 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 399.9 |  | 399.7751 | 0.0312 | 389.4 | 382.38 | 3.8985 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 632.52 |  | 630.0985 | 0.3843 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1053.705 |  | 1045.207 | 0.813 | 1001.82 | 982.21 | 4.3921 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.13 |  | 469.7833 | -0.1391 | 469.08 | 460.78 | 0.13 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 140.835 |  | 140.9586 | -0.0877 | 140.765 | 137.165 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ANET | ai_networking_optical | 168.56 |  | 166.175 | 1.4352 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 277.2 |  | 274.0385 | 1.1537 | 269.59 | 256.24 | 0.6133 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 734.89 |  | 717.9165 | 2.3643 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 376.91 |  | 377.8315 | -0.2439 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.47 |  | 100.5751 | 1.8841 | 97.585 | 91.92 | 4.4013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 304.3 |  | 305.1925 | -0.2924 | 305.21 | 289.97 | 4.9852 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1760.16 |  | 1757.0599 | 0.1764 | 1741.99 | 1704.935 | 2.9009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 532.47 |  | 535.1684 | -0.5042 | 535.095 | 513.34 | 0.4019 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 311.745 |  | 312.122 | -0.1208 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 212.9 |  | 212.2043 | 0.3279 | 210.82 | 204.71 | 0.1362 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 323.8 |  | 320.0438 | 1.1737 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 277.82 |  | 277.6707 | 0.0538 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.21 |  | 61.5132 | 1.1328 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.86 |  | 49.9145 | 1.8942 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.85 |  | 134.8427 | 1.4886 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 323.515 |  | 318.827 | 1.4704 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 515.155 |  | 519.7952 | -0.8927 | 526.74 | 522.205 | 0.1475 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 296.28 |  | 298.9066 | -0.8787 | 304.36 | 299.62 | 4.7624 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.21 |  | 25.0919 | 0.4709 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.655 |  | 33.7864 | -0.3889 | 34 | 32.26 | 0.0297 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.995 |  | 20.6633 | 1.6052 | 20.445 | 19.92 | 0.0953 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1416.5 |  | 1428.0954 | -0.8119 | 1393.96 | 1325.48 | 1.4119 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 479.365 |  | 467.245 | 2.5939 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 786.96 |  | 760.9829 | 3.4136 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.5 |  | 247.9997 | -0.2015 | 247.72 | 243.725 | 0.0242 | below_vwap | below_vwap |
| META | cloud_ai_capex | 646.41 |  | 642.4328 | 0.6191 | 649.07 | 638.97 | 0.6111 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.79 |  | 261.205 | 2.1382 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 160.93 |  | 158.8632 | 1.301 | 151.99 | 145.6 | 3.7283 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
