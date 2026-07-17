# Intraday State

- Generated at: `2026-07-17T22:38:31+08:00`
- Market time ET: `2026-07-17T10:38:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'spread_too_wide_or_missing': 33, 'below_opening_15m_low': 3, 'watch_only': 4, 'price_stale_or_missing': 1, 'below_vwap': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.585 |  | 692.7117 | 0.7035 | 693.36 | 686.78 | 0.0129 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 521.34 |  | 511.9201 | 1.8401 | 511.83 | 498.665 | 0.1515 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.99 |  | 549.337 | 1.3931 | 550 | 536.9 | 0.1203 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.46 |  | 744.0966 | 0.3176 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.99 |  | 549.337 | 1.3931 | 550 | 536.9 | 0.1203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 372.155 |  | 367.4936 | 1.2684 | 368.42 | 357.97 | 0.2633 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 490.45 |  | 476.7587 | 2.8717 | 482.43 | 461.04 | 0.2019 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 521.34 |  | 511.9201 | 1.8401 | 511.83 | 498.665 | 0.1515 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.49 |  | 293.9436 | 0.5261 | 294.205 | 291.675 | 0.0135 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 697.585 |  | 692.7117 | 0.7035 | 693.36 | 686.78 | 0.0129 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.71 |  | 45.1385 | 1.2662 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.46 |  | 744.0966 | 0.3176 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 463.485 |  | 449.3965 | 3.135 | 453.35 | 431.78 | 0.1446 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.32 |  | 247.1258 | 0.4833 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 11 | MRVL | custom_silicon_networking | 187.24 |  | 184.2907 | 1.6004 | 185.03 | 178.09 | 0.2403 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.59 |  | 20.2806 | 1.5258 | 20.445 | 19.92 | 0.1457 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.17 |  | 66.4531 | 2.5837 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.46 |  | 744.0966 | 0.3176 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.32 |  | 247.1258 | 0.4833 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 295.49 |  | 293.9436 | 0.5261 | 294.205 | 291.675 | 0.0135 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 697.585 |  | 692.7117 | 0.7035 | 693.36 | 686.78 | 0.0129 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 332.4 |  | 331.9742 | 0.1283 | 334.98 | 331.295 | 0.0542 | watch_only | none |
| 6 | SMH | semiconductor_index | 556.99 |  | 549.337 | 1.3931 | 550 | 536.9 | 0.1203 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 372.155 |  | 367.4936 | 1.2684 | 368.42 | 357.97 | 0.2633 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.71 |  | 45.1385 | 1.2662 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 469.14 |  | 468.0689 | 0.2288 | 469.08 | 460.78 | 4.5914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | SMCI | ai_server_oem | 24.295 |  | 24.0052 | 1.2071 | 24.3 | 23.46 | 0.0412 | watch_only | none |
| 11 | IREN | high_beta_ai_infrastructure | 33.8 |  | 33.3942 | 1.2151 | 34 | 32.26 | 0.0888 | watch_only | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.59 |  | 20.2806 | 1.5258 | 20.445 | 19.92 | 0.1457 | buy_precheck_manual_confirm | none |
| 13 | GOOGL | cloud_ai_capex | 345.39 |  | 345.3685 | 0.0062 | 348.47 | 341.42 | 0.4864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ORCL | cloud_ai_capex | 125.525 |  | 124.6715 | 0.6846 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | MRVL | custom_silicon_networking | 187.24 |  | 184.2907 | 1.6004 | 185.03 | 178.09 | 0.2403 | buy_precheck_manual_confirm | none |
| 16 | WDC | memory_hbm_storage | 463.485 |  | 449.3965 | 3.135 | 453.35 | 431.78 | 0.1446 | buy_precheck_manual_confirm | none |
| 17 | AMD | ai_accelerator | 490.45 |  | 476.7587 | 2.8717 | 482.43 | 461.04 | 0.2019 | buy_precheck_manual_confirm | none |
| 18 | SOXX | semiconductor_index | 521.34 |  | 511.9201 | 1.8401 | 511.83 | 498.665 | 0.1515 | buy_precheck_manual_confirm | none |
| 19 | ETN | data_center_power_cooling | 398.56 |  | 395.5823 | 0.7527 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | APLD | high_beta_ai_infrastructure | 25.19 |  | 24.7936 | 1.5988 | 25.45 | 24.1 | 0.0397 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 556.99 |  | 549.337 | 1.3931 | 550 | 536.9 | 0.1203 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 372.155 |  | 367.4936 | 1.2684 | 368.42 | 357.97 | 0.2633 | buy_precheck_manual_confirm | none |
| 3 | AMD | ai_accelerator | 490.45 |  | 476.7587 | 2.8717 | 482.43 | 461.04 | 0.2019 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 521.34 |  | 511.9201 | 1.8401 | 511.83 | 498.665 | 0.1515 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.49 |  | 293.9436 | 0.5261 | 294.205 | 291.675 | 0.0135 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 697.585 |  | 692.7117 | 0.7035 | 693.36 | 686.78 | 0.0129 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.71 |  | 45.1385 | 1.2662 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.46 |  | 744.0966 | 0.3176 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | WDC | memory_hbm_storage | 463.485 |  | 449.3965 | 3.135 | 453.35 | 431.78 | 0.1446 | buy_precheck_manual_confirm | none |
| 10 | AMZN | cloud_ai_capex | 248.32 |  | 247.1258 | 0.4833 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 11 | MRVL | custom_silicon_networking | 187.24 |  | 184.2907 | 1.6004 | 185.03 | 178.09 | 0.2403 | buy_precheck_manual_confirm | none |
| 12 | CORZ | high_beta_ai_infrastructure | 20.59 |  | 20.2806 | 1.5258 | 20.445 | 19.92 | 0.1457 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.17 |  | 66.4531 | 2.5837 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 166.2 |  | 162.4142 | 2.3309 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | NVDA | ai_accelerator | 204.3 |  | 201.8014 | 1.2382 | 203.41 | 197.98 | 2.7655 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TSM | foundry | 401.17 |  | 393.9128 | 1.8423 | 394.11 | 386.02 | 0.85 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 535.93 |  | 527.3591 | 1.6252 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ASML | semiconductor_equipment | 1748.62 |  | 1733.1343 | 0.8935 | 1741.99 | 1704.935 | 0.672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TT | data_center_power_cooling | 469.14 |  | 468.0689 | 0.2288 | 469.08 | 460.78 | 4.5914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | KLAC | semiconductor_equipment | 212.28 |  | 210.2345 | 0.973 | 210.82 | 204.71 | 1.7053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.585 |  | 692.7117 | 0.7035 | 693.36 | 686.78 | 0.0129 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.17 |  | 66.4531 | 2.5837 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.3 |  | 201.8014 | 1.2382 | 203.41 | 197.98 | 2.7655 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 391.965 |  | 394.3099 | -0.5947 | 398.39 | 393.52 | 0.1327 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 332.4 |  | 331.9742 | 0.1283 | 334.98 | 331.295 | 0.0542 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.39 |  | 345.3685 | 0.0062 | 348.47 | 341.42 | 0.4864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMD | ai_accelerator | 490.45 |  | 476.7587 | 2.8717 | 482.43 | 461.04 | 0.2019 | buy_precheck_manual_confirm | none |
| TSM | foundry | 401.17 |  | 393.9128 | 1.8423 | 394.11 | 386.02 | 0.85 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 521.34 |  | 511.9201 | 1.8401 | 511.83 | 498.665 | 0.1515 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 556.99 |  | 549.337 | 1.3931 | 550 | 536.9 | 0.1203 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.155 |  | 367.4936 | 1.2684 | 368.42 | 357.97 | 0.2633 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 877.11 |  | 844.8624 | 3.8169 | 835.82 | 804.09 | 0.4332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 187.24 |  | 184.2907 | 1.6004 | 185.03 | 178.09 | 0.2403 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 396.12 |  | 384.76 | 2.9525 | 384 | 368.28 | 0.5705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.71 |  | 45.1385 | 1.2662 | 44.92 | 43.715 | 0.0219 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.295 |  | 24.0052 | 1.2071 | 24.3 | 23.46 | 0.0412 | watch_only | none |
| SPY | market_regime | 746.46 |  | 744.0966 | 0.3176 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.49 |  | 293.9436 | 0.5261 | 294.205 | 291.675 | 0.0135 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.525 |  | 124.6715 | 0.6846 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 73.98 |  | 70.8972 | 4.3483 | 71.24 | 68.65 | 1.6085 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 286.295 |  | 281.5116 | 1.6992 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 398.56 |  | 395.5823 | 0.7527 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 627.855 |  | 621.9916 | 0.9427 | 616.75 | 609.05 | 0.5718 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1050.03 |  | 1023.479 | 2.5942 | 1001.82 | 982.21 | 0.8209 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.14 |  | 468.0689 | 0.2288 | 469.08 | 460.78 | 4.5914 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.72 |  | 139.5875 | 0.8113 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.2 |  | 162.4142 | 2.3309 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.25 |  | 267.6511 | 3.96 | 269.59 | 256.24 | 4.1725 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 725.1 |  | 694.4991 | 4.4062 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 381.15 |  | 372.1434 | 2.4202 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.13 |  | 96.9071 | 4.3577 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.85 |  | 300.2978 | 1.5159 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1748.62 |  | 1733.1343 | 0.8935 | 1741.99 | 1704.935 | 0.672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 535.93 |  | 527.3591 | 1.6252 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 312.04 |  | 305.7086 | 2.0711 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 212.28 |  | 210.2345 | 0.973 | 210.82 | 204.71 | 1.7053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 315.41 |  | 308.4421 | 2.2591 | 308.03 | 297.18 | 4.835 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 270.94 |  | 266.0894 | 1.8229 | 265.71 | 258.355 | 4.1448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 61.31 |  | 59.9586 | 2.2538 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.89 |  | 48.4059 | 3.0659 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 135.72 |  | 132.1919 | 2.6689 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 318.88 |  | 314.3049 | 1.4556 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 521.085 |  | 521.8332 | -0.1434 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.04 |  | 301.6977 | -0.218 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 25.19 |  | 24.7936 | 1.5988 | 25.45 | 24.1 | 0.0397 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.8 |  | 33.3942 | 1.2151 | 34 | 32.26 | 0.0888 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.59 |  | 20.2806 | 1.5258 | 20.445 | 19.92 | 0.1457 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1445.7 |  | 1398.3865 | 3.3834 | 1393.96 | 1325.48 | 4.4885 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 463.485 |  | 449.3965 | 3.135 | 453.35 | 431.78 | 0.1446 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 750.755 |  | 729.8051 | 2.8706 | 724.57 | 702.24 | 5.0083 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.32 |  | 247.1258 | 0.4833 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 634.13 |  | 638.9914 | -0.7608 | 649.07 | 638.97 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ARM | ai_accelerator | 261.26 |  | 253.3794 | 3.1102 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 157.905 |  | 154.7109 | 2.0645 | 151.99 | 145.6 | 4.3064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
