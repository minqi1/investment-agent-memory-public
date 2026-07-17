# Intraday State

- Generated at: `2026-07-18T02:36:03+08:00`
- Market time ET: `2026-07-17T14:36:04-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'watch_only': 4, 'below_vwap': 13, 'spread_too_wide_or_missing': 27, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.99 |  | 695.5402 | 0.2084 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.3 |  | 518.3559 | 0.9538 | 511.83 | 498.665 | 0.0879 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.59 |  | 555.0685 | 0.4543 | 550 | 536.9 | 0.0789 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.67 |  | 744.917 | -0.1674 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.59 |  | 555.0685 | 0.4543 | 550 | 536.9 | 0.0789 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.3 |  | 518.3559 | 0.9538 | 511.83 | 498.665 | 0.0879 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.99 |  | 695.5402 | 0.2084 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| 4 | HPE | ai_server_oem | 46.3 |  | 45.659 | 1.4039 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 5 | WDC | memory_hbm_storage | 483.12 |  | 466.9522 | 3.4624 | 453.35 | 431.78 | 0.1884 | buy_precheck_manual_confirm | none |
| 6 | COHR | ai_networking_optical | 277.84 |  | 273.99 | 1.4052 | 269.59 | 256.24 | 0.1836 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.64 |  | 24.3019 | 1.3913 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 21.06 |  | 20.6598 | 1.9373 | 20.445 | 19.92 | 0.095 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.98 |  | 67.2072 | 1.1498 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.99 |  | 695.5402 | 0.2084 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 203.3 |  | 203.2431 | 0.028 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| 3 | SMH | semiconductor_index | 557.59 |  | 555.0685 | 0.4543 | 550 | 536.9 | 0.0789 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 394.7 |  | 393.3746 | 0.3369 | 398.39 | 393.52 | 0.0735 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 332.295 |  | 332.003 | 0.088 | 334.98 | 331.295 | 0.006 | watch_only | none |
| 6 | APLD | high_beta_ai_infrastructure | 25.27 |  | 25.0888 | 0.7223 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| 7 | SMCI | ai_server_oem | 24.64 |  | 24.3019 | 1.3913 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 523.3 |  | 518.3559 | 0.9538 | 511.83 | 498.665 | 0.0879 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.3 |  | 45.659 | 1.4039 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 10 | COHR | ai_networking_optical | 277.84 |  | 273.99 | 1.4052 | 269.59 | 256.24 | 0.1836 | buy_precheck_manual_confirm | none |
| 11 | ETN | data_center_power_cooling | 400.72 |  | 399.7618 | 0.2397 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | LRCX | semiconductor_equipment | 312.815 |  | 312.1181 | 0.2233 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ONTO | semiconductor_test_packaging | 278.09 |  | 277.6428 | 0.1611 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ASML | semiconductor_equipment | 1763.82 |  | 1756.9227 | 0.3926 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 634.26 |  | 630.0105 | 0.6745 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CORZ | high_beta_ai_infrastructure | 21.06 |  | 20.6598 | 1.9373 | 20.445 | 19.92 | 0.095 | buy_precheck_manual_confirm | none |
| 17 | AVGO | custom_silicon_networking | 372.855 |  | 370.218 | 0.7123 | 368.42 | 357.97 | 1.9364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | WDC | memory_hbm_storage | 483.12 |  | 466.9522 | 3.4624 | 453.35 | 431.78 | 0.1884 | buy_precheck_manual_confirm | none |
| 19 | KLAC | semiconductor_equipment | 213.17 |  | 212.192 | 0.4609 | 210.82 | 204.71 | 4.039 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ORCL | cloud_ai_capex | 126.77 |  | 126.0118 | 0.6017 | 125.02 | 121.79 | 1.1201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.59 |  | 555.0685 | 0.4543 | 550 | 536.9 | 0.0789 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.3 |  | 518.3559 | 0.9538 | 511.83 | 498.665 | 0.0879 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 696.99 |  | 695.5402 | 0.2084 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| 4 | HPE | ai_server_oem | 46.3 |  | 45.659 | 1.4039 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| 5 | WDC | memory_hbm_storage | 483.12 |  | 466.9522 | 3.4624 | 453.35 | 431.78 | 0.1884 | buy_precheck_manual_confirm | none |
| 6 | COHR | ai_networking_optical | 277.84 |  | 273.99 | 1.4052 | 269.59 | 256.24 | 0.1836 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 24.64 |  | 24.3019 | 1.3913 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| 8 | CORZ | high_beta_ai_infrastructure | 21.06 |  | 20.6598 | 1.9373 | 20.445 | 19.92 | 0.095 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.98 |  | 67.2072 | 1.1498 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 10 | TSM | foundry | 397.385 |  | 398.0979 | -0.1791 | 394.11 | 386.02 | 0.6216 | below_vwap | below_vwap,spread_too_wide |
| 11 | TT | data_center_power_cooling | 469.74 |  | 469.7851 | -0.0096 | 469.08 | 460.78 | 4.2151 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 140.835 |  | 140.9586 | -0.0877 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | CIEN | ai_networking_optical | 376.9 |  | 377.8507 | -0.2516 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | SPY | market_regime | 743.67 |  | 744.917 | -0.1674 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 15 | AMZN | cloud_ai_capex | 247.75 |  | 248.0073 | -0.1038 | 247.72 | 243.725 | 0.0161 | below_vwap | below_vwap |
| 16 | SNDK | memory_hbm_storage | 1420.58 |  | 1428.2923 | -0.54 | 1393.96 | 1325.48 | 4.6615 | below_vwap | below_vwap,spread_too_wide |
| 17 | ANET | ai_networking_optical | 168.56 |  | 166.1303 | 1.4625 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 372.855 |  | 370.218 | 0.7123 | 368.42 | 357.97 | 1.9364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 495.92 |  | 486.7544 | 1.883 | 482.43 | 461.04 | 3.19 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ASML | semiconductor_equipment | 1763.82 |  | 1756.9227 | 0.3926 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.99 |  | 695.5402 | 0.2084 | 693.36 | 686.78 | 0.0402 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.98 |  | 67.2072 | 1.1498 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.3 |  | 203.2431 | 0.028 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| MSFT | cloud_ai_capex | 394.7 |  | 393.3746 | 0.3369 | 398.39 | 393.52 | 0.0735 | watch_only | none |
| AAPL | mega_cap_platform | 332.295 |  | 332.003 | 0.088 | 334.98 | 331.295 | 0.006 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.77 |  | 345.8617 | -0.3156 | 348.47 | 341.42 | 0.1943 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.92 |  | 486.7544 | 1.883 | 482.43 | 461.04 | 3.19 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 397.385 |  | 398.0979 | -0.1791 | 394.11 | 386.02 | 0.6216 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.3 |  | 518.3559 | 0.9538 | 511.83 | 498.665 | 0.0879 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.59 |  | 555.0685 | 0.4543 | 550 | 536.9 | 0.0789 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.855 |  | 370.218 | 0.7123 | 368.42 | 357.97 | 1.9364 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 873.28 |  | 864.1871 | 1.0522 | 835.82 | 804.09 | 1.002 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.055 |  | 187.1397 | 1.0235 | 185.03 | 178.09 | 0.6294 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 401.06 |  | 392.88 | 2.0821 | 384 | 368.28 | 4.9519 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.3 |  | 45.659 | 1.4039 | 44.92 | 43.715 | 0.0216 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.64 |  | 24.3019 | 1.3913 | 24.3 | 23.46 | 0.0406 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.67 |  | 744.917 | -0.1674 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.62 |  | 294.1827 | -0.1913 | 294.205 | 291.675 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.77 |  | 126.0118 | 0.6017 | 125.02 | 121.79 | 1.1201 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.73 |  | 72.2101 | 2.1049 | 71.24 | 68.65 | 2.7262 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 292.11 |  | 287.2645 | 1.6868 | 280.565 | 273.17 | 4.7688 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 400.72 |  | 399.7618 | 0.2397 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.26 |  | 630.0105 | 0.6745 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1055.97 |  | 1045.0246 | 1.0474 | 1001.82 | 982.21 | 4.6981 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.74 |  | 469.7851 | -0.0096 | 469.08 | 460.78 | 4.2151 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.835 |  | 140.9586 | -0.0877 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.56 |  | 166.1303 | 1.4625 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 277.84 |  | 273.99 | 1.4052 | 269.59 | 256.24 | 0.1836 | buy_precheck_manual_confirm | none |
| LITE | ai_networking_optical | 733.85 |  | 717.5534 | 2.2711 | 694.98 | 653.305 | 2.2062 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 376.9 |  | 377.8507 | -0.2516 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.555 |  | 100.5226 | 2.0218 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 303.4 |  | 305.2229 | -0.5972 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1763.82 |  | 1756.9227 | 0.3926 | 1741.99 | 1704.935 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 532.565 |  | 535.284 | -0.5079 | 535.095 | 513.34 | 0.2122 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 312.815 |  | 312.1181 | 0.2233 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.17 |  | 212.192 | 0.4609 | 210.82 | 204.71 | 4.039 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 324.33 |  | 319.917 | 1.3794 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.09 |  | 277.6428 | 0.1611 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.365 |  | 61.4945 | 1.4155 | 60.51 | 57.99 | 3.7521 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 50.98 |  | 49.8958 | 2.173 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.08 |  | 134.7753 | 1.71 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 324.61 |  | 318.7695 | 1.8322 | 315.89 | 307.13 | 4.1311 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 514.92 |  | 519.9016 | -0.9582 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 296.33 |  | 298.9944 | -0.8911 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.27 |  | 25.0888 | 0.7223 | 25.45 | 24.1 | 0.0396 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.735 |  | 33.7947 | -0.1766 | 34 | 32.26 | 0.0296 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.06 |  | 20.6598 | 1.9373 | 20.445 | 19.92 | 0.095 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1420.58 |  | 1428.2923 | -0.54 | 1393.96 | 1325.48 | 4.6615 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 483.12 |  | 466.9522 | 3.4624 | 453.35 | 431.78 | 0.1884 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 788.87 |  | 760.4535 | 3.7368 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.75 |  | 248.0073 | -0.1038 | 247.72 | 243.725 | 0.0161 | below_vwap | below_vwap |
| META | cloud_ai_capex | 648.195 |  | 642.3181 | 0.915 | 649.07 | 638.97 | 0.6696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 268.34 |  | 261.1315 | 2.7605 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 161.18 |  | 158.7342 | 1.5408 | 151.99 | 145.6 | 2.4817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
