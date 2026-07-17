# Intraday State

- Generated at: `2026-07-18T03:36:40+08:00`
- Market time ET: `2026-07-17T15:36:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_vwap': 14, 'watch_only': 3, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.03 |  | 695.6424 | 0.0557 | 693.36 | 686.78 | 0.0216 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 523.33 |  | 518.881 | 0.8574 | 511.83 | 498.665 | 0.1013 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.34 |  | 555.2046 | 0.3846 | 550 | 536.9 | 0.0861 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.97 |  | 744.6218 | -0.2218 | 742.66 | 740.8 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.34 |  | 555.2046 | 0.3846 | 550 | 536.9 | 0.0861 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.33 |  | 518.881 | 0.8574 | 511.83 | 498.665 | 0.1013 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.37 |  | 212.2324 | 0.536 | 210.82 | 204.71 | 0.1922 | buy_precheck_manual_confirm | none |
| 4 | PWR | data_center_power_cooling | 630.65 |  | 630.3101 | 0.0539 | 616.75 | 609.05 | 0.1491 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.03 |  | 695.6424 | 0.0557 | 693.36 | 686.78 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.01 |  | 45.7157 | 0.6439 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.3 |  | 126.0518 | 0.1969 | 125.02 | 121.79 | 0.0396 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.5 |  | 24.3254 | 0.7176 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.095 |  | 72.3103 | 1.0852 | 71.24 | 68.65 | 0.2599 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.74 |  | 20.6855 | 0.2633 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.76 |  | 67.2644 | 0.7368 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 696.03 |  | 695.6424 | 0.0557 | 693.36 | 686.78 | 0.0216 | buy_precheck_manual_confirm | none |
| 2 | ORCL | cloud_ai_capex | 126.3 |  | 126.0518 | 0.1969 | 125.02 | 121.79 | 0.0396 | buy_precheck_manual_confirm | none |
| 3 | CORZ | high_beta_ai_infrastructure | 20.74 |  | 20.6855 | 0.2633 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 4 | PWR | data_center_power_cooling | 630.65 |  | 630.3101 | 0.0539 | 616.75 | 609.05 | 0.1491 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 557.34 |  | 555.2046 | 0.3846 | 550 | 536.9 | 0.0861 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 332.47 |  | 332.3367 | 0.0401 | 334.98 | 331.295 | 0.015 | watch_only | none |
| 7 | SMCI | ai_server_oem | 24.5 |  | 24.3254 | 0.7176 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 8 | KLAC | semiconductor_equipment | 213.37 |  | 212.2324 | 0.536 | 210.82 | 204.71 | 0.1922 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.01 |  | 45.7157 | 0.6439 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 10 | MSFT | cloud_ai_capex | 395.35 |  | 393.6796 | 0.4243 | 398.39 | 393.52 | 0.0455 | watch_only | none |
| 11 | TT | data_center_power_cooling | 470.17 |  | 469.7221 | 0.0954 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | SOXX | semiconductor_index | 523.33 |  | 518.881 | 0.8574 | 511.83 | 498.665 | 0.1013 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 25.335 |  | 25.1112 | 0.8911 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| 14 | ETN | data_center_power_cooling | 400.1 |  | 399.7449 | 0.0888 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | LRCX | semiconductor_equipment | 312.43 |  | 312.0624 | 0.1178 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | META | cloud_ai_capex | 643.92 |  | 642.6146 | 0.2031 | 649.07 | 638.97 | 3.1836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | CRWV | gpu_cloud_ai_factory | 73.095 |  | 72.3103 | 1.0852 | 71.24 | 68.65 | 0.2599 | buy_precheck_manual_confirm | none |
| 18 | TSM | foundry | 397.9 |  | 397.835 | 0.0163 | 394.11 | 386.02 | 0.9073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1758.5 |  | 1756.8534 | 0.0937 | 1741.99 | 1704.935 | 2.7546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ONTO | semiconductor_test_packaging | 278.35 |  | 277.6761 | 0.2427 | 265.71 | 258.355 | 0.7868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 557.34 |  | 555.2046 | 0.3846 | 550 | 536.9 | 0.0861 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 523.33 |  | 518.881 | 0.8574 | 511.83 | 498.665 | 0.1013 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 213.37 |  | 212.2324 | 0.536 | 210.82 | 204.71 | 0.1922 | buy_precheck_manual_confirm | none |
| 4 | PWR | data_center_power_cooling | 630.65 |  | 630.3101 | 0.0539 | 616.75 | 609.05 | 0.1491 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 696.03 |  | 695.6424 | 0.0557 | 693.36 | 686.78 | 0.0216 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.01 |  | 45.7157 | 0.6439 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 126.3 |  | 126.0518 | 0.1969 | 125.02 | 121.79 | 0.0396 | buy_precheck_manual_confirm | none |
| 8 | SMCI | ai_server_oem | 24.5 |  | 24.3254 | 0.7176 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 9 | CRWV | gpu_cloud_ai_factory | 73.095 |  | 72.3103 | 1.0852 | 71.24 | 68.65 | 0.2599 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.74 |  | 20.6855 | 0.2633 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 67.76 |  | 67.2644 | 0.7368 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| 12 | MU | memory_hbm_storage | 864.15 |  | 864.5927 | -0.0512 | 835.82 | 804.09 | 0.3217 | below_vwap | below_vwap |
| 13 | CIEN | ai_networking_optical | 377.24 |  | 377.6091 | -0.0977 | 375.52 | 359.81 | 1.2671 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 742.97 |  | 744.6218 | -0.2218 | 742.66 | 740.8 | 0.0027 | below_vwap | below_vwap |
| 15 | SNDK | memory_hbm_storage | 1393.99 |  | 1426.5305 | -2.2811 | 1393.96 | 1325.48 | 2.8293 | below_vwap | below_vwap,spread_too_wide |
| 16 | SKHY | memory_hbm_storage | 154.12 |  | 158.6847 | -2.8766 | 151.99 | 145.6 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ANET | ai_networking_optical | 168.125 |  | 166.4216 | 1.0236 | 163.275 | 157.34 | 3.1108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TSM | foundry | 397.9 |  | 397.835 | 0.0163 | 394.11 | 386.02 | 0.9073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AVGO | custom_silicon_networking | 372.005 |  | 370.4591 | 0.4173 | 368.42 | 357.97 | 3.2258 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 495.815 |  | 487.2949 | 1.7485 | 482.43 | 461.04 | 0.5708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 696.03 |  | 695.6424 | 0.0557 | 693.36 | 686.78 | 0.0216 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.76 |  | 67.2644 | 0.7368 | 66.9 | 64.92 | 0.0295 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.82 |  | 203.175 | -0.1747 | 203.41 | 197.98 | 0.0148 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 395.35 |  | 393.6796 | 0.4243 | 398.39 | 393.52 | 0.0455 | watch_only | none |
| AAPL | mega_cap_platform | 332.47 |  | 332.3367 | 0.0401 | 334.98 | 331.295 | 0.015 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.825 |  | 345.7393 | -0.2645 | 348.47 | 341.42 | 0.0667 | below_vwap | below_vwap |
| AMD | ai_accelerator | 495.815 |  | 487.2949 | 1.7485 | 482.43 | 461.04 | 0.5708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 397.9 |  | 397.835 | 0.0163 | 394.11 | 386.02 | 0.9073 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 523.33 |  | 518.881 | 0.8574 | 511.83 | 498.665 | 0.1013 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 557.34 |  | 555.2046 | 0.3846 | 550 | 536.9 | 0.0861 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.005 |  | 370.4591 | 0.4173 | 368.42 | 357.97 | 3.2258 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 864.15 |  | 864.5927 | -0.0512 | 835.82 | 804.09 | 0.3217 | below_vwap | below_vwap |
| MRVL | custom_silicon_networking | 189.18 |  | 187.2962 | 1.0058 | 185.03 | 178.09 | 1.1153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 399.8 |  | 393.7185 | 1.5446 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.01 |  | 45.7157 | 0.6439 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.5 |  | 24.3254 | 0.7176 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.97 |  | 744.6218 | -0.2218 | 742.66 | 740.8 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.45 |  | 294.0824 | -0.215 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.3 |  | 126.0518 | 0.1969 | 125.02 | 121.79 | 0.0396 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.095 |  | 72.3103 | 1.0852 | 71.24 | 68.65 | 0.2599 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 291.03 |  | 287.7499 | 1.1399 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.1 |  | 399.7449 | 0.0888 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 630.65 |  | 630.3101 | 0.0539 | 616.75 | 609.05 | 0.1491 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 1053.96 |  | 1046.4482 | 0.7178 | 1001.82 | 982.21 | 4.6928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.17 |  | 469.7221 | 0.0954 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.695 |  | 140.9081 | -0.1512 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 168.125 |  | 166.4216 | 1.0236 | 163.275 | 157.34 | 3.1108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 279.125 |  | 274.4222 | 1.7137 | 269.59 | 256.24 | 1.5549 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 737.21 |  | 719.8652 | 2.4094 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 377.24 |  | 377.6091 | -0.0977 | 375.52 | 359.81 | 1.2671 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.655 |  | 100.7387 | 1.9022 | 97.585 | 91.92 | 4.0427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 304 |  | 304.6399 | -0.21 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1758.5 |  | 1756.8534 | 0.0937 | 1741.99 | 1704.935 | 2.7546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.155 |  | 533.8214 | -0.4995 | 535.095 | 513.34 | 1.1183 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 312.43 |  | 312.0624 | 0.1178 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.37 |  | 212.2324 | 0.536 | 210.82 | 204.71 | 0.1922 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.03 |  | 320.4501 | 1.1171 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 278.35 |  | 277.6761 | 0.2427 | 265.71 | 258.355 | 0.7868 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.4 |  | 61.6443 | 1.2258 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.04 |  | 50.015 | 2.0495 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.01 |  | 135.2469 | 1.3036 | 129.93 | 126.945 | 5.0361 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.55 |  | 319.3226 | 1.9502 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 513.14 |  | 518.163 | -0.9694 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.48 |  | 298.4469 | -0.9941 | 304.36 | 299.62 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.335 |  | 25.1112 | 0.8911 | 25.45 | 24.1 | 0.0395 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.39 |  | 33.7417 | -1.0424 | 34 | 32.26 | 0.0299 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.74 |  | 20.6855 | 0.2633 | 20.445 | 19.92 | 0.0482 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1393.99 |  | 1426.5305 | -2.2811 | 1393.96 | 1325.48 | 2.8293 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 480.62 |  | 468.0811 | 2.6788 | 453.35 | 431.78 | 0.4369 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 794.33 |  | 766.6247 | 3.6139 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 246.85 |  | 247.945 | -0.4416 | 247.72 | 243.725 | 0.0446 | below_vwap | below_vwap |
| META | cloud_ai_capex | 643.92 |  | 642.6146 | 0.2031 | 649.07 | 638.97 | 3.1836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 267.24 |  | 261.6777 | 2.1256 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 154.12 |  | 158.6847 | -2.8766 | 151.99 | 145.6 |  | below_vwap | below_vwap,spread_unavailable |
