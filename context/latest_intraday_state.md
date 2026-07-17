# Intraday State

- Generated at: `2026-07-17T23:09:35+08:00`
- Market time ET: `2026-07-17T11:09:37-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'spread_too_wide_or_missing': 32, 'below_opening_15m_low': 2, 'watch_only': 3, 'price_stale_or_missing': 1, 'below_vwap': 9}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.395 |  | 693.1505 | 0.1795 | 693.36 | 686.78 | 0.0475 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 514.225 |  | 512.3435 | 0.3672 | 511.83 | 498.665 | 0.1342 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 551.63 |  | 549.7342 | 0.3449 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.85 |  | 744.3857 | 0.0624 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 396.17 |  | 394.7771 | 0.3528 | 394.11 | 386.02 | 0.1262 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 551.63 |  | 549.7342 | 0.3449 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 514.225 |  | 512.3435 | 0.3672 | 511.83 | 498.665 | 0.1342 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 852.94 |  | 848.2209 | 0.5564 | 835.82 | 804.09 | 0.1712 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.42 |  | 294.0941 | 0.1108 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 694.395 |  | 693.1505 | 0.1795 | 693.36 | 686.78 | 0.0475 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 744.85 |  | 744.3857 | 0.0624 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.67 |  | 247.6534 | 0.4105 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.14 |  | 66.6273 | 0.7695 | 66.9 | 64.92 | 0.0298 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 551.63 |  | 549.7342 | 0.3449 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.42 |  | 294.0941 | 0.1108 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 694.395 |  | 693.1505 | 0.1795 | 693.36 | 686.78 | 0.0475 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 744.85 |  | 744.3857 | 0.0624 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 396.17 |  | 394.7771 | 0.3528 | 394.11 | 386.02 | 0.1262 | buy_precheck_manual_confirm | none |
| 6 | SOXX | semiconductor_index | 514.225 |  | 512.3435 | 0.3672 | 511.83 | 498.665 | 0.1342 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 248.67 |  | 247.6534 | 0.4105 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 346.38 |  | 345.5615 | 0.2369 | 348.47 | 341.42 | 0.0318 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 333.335 |  | 332.1214 | 0.3654 | 334.98 | 331.295 | 0.015 | watch_only | none |
| 10 | MU | memory_hbm_storage | 852.94 |  | 848.2209 | 0.5564 | 835.82 | 804.09 | 0.1712 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.4 |  | 20.3188 | 0.3996 | 20.445 | 19.92 | 0.098 | watch_only | none |
| 12 | TT | data_center_power_cooling | 470.26 |  | 468.6757 | 0.338 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TER | semiconductor_test_packaging | 309.98 |  | 309.4011 | 0.1871 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 368.72 |  | 367.9035 | 0.2219 | 368.42 | 357.97 | 3.0511 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 141.03 |  | 140.3421 | 0.4901 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1405.24 |  | 1400.8554 | 0.313 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ASML | semiconductor_equipment | 1740.15 |  | 1735.949 | 0.242 | 1741.99 | 1704.935 | 0.6884 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | CIEN | ai_networking_optical | 375.455 |  | 373.1449 | 0.6191 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | ORCL | cloud_ai_capex | 125.4 |  | 124.856 | 0.4357 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | LIN | industrial_gases | 522.65 |  | 521.8495 | 0.1534 | 526.74 | 522.205 | 4.9957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 396.17 |  | 394.7771 | 0.3528 | 394.11 | 386.02 | 0.1262 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 551.63 |  | 549.7342 | 0.3449 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 514.225 |  | 512.3435 | 0.3672 | 511.83 | 498.665 | 0.1342 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 852.94 |  | 848.2209 | 0.5564 | 835.82 | 804.09 | 0.1712 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.42 |  | 294.0941 | 0.1108 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 694.395 |  | 693.1505 | 0.1795 | 693.36 | 686.78 | 0.0475 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 744.85 |  | 744.3857 | 0.0624 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 248.67 |  | 247.6534 | 0.4105 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 67.14 |  | 66.6273 | 0.7695 | 66.9 | 64.92 | 0.0298 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 45.26 |  | 45.2875 | -0.0608 | 44.92 | 43.715 | 0.0663 | below_vwap | below_vwap |
| 11 | SKHY | memory_hbm_storage | 154.51 |  | 154.9965 | -0.3139 | 151.99 | 145.6 | 4.5952 | below_vwap | below_vwap,spread_too_wide |
| 12 | ANET | ai_networking_optical | 164.18 |  | 162.86 | 0.8105 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 368.72 |  | 367.9035 | 0.2219 | 368.42 | 357.97 | 3.0511 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 485.3 |  | 478.0966 | 1.5067 | 482.43 | 461.04 | 1.053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 470.26 |  | 468.6757 | 0.338 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | VRT | data_center_power_cooling | 285.58 |  | 282.3581 | 1.1411 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | JCI | data_center_power_cooling | 141.03 |  | 140.3421 | 0.4901 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 396.73 |  | 395.9338 | 0.2011 | 389.4 | 382.38 | 5.0412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | GEV | data_center_power_cooling | 1038.645 |  | 1026.0818 | 1.2244 | 1001.82 | 982.21 | 0.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | DELL | ai_server_oem | 392.5 |  | 386.5055 | 1.551 | 384 | 368.28 | 1.9643 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.395 |  | 693.1505 | 0.1795 | 693.36 | 686.78 | 0.0475 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.14 |  | 66.6273 | 0.7695 | 66.9 | 64.92 | 0.0298 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.1 |  | 202.0631 | 0.5132 | 203.41 | 197.98 | 1.2309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 391.63 |  | 393.67 | -0.5182 | 398.39 | 393.52 | 0.2732 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.335 |  | 332.1214 | 0.3654 | 334.98 | 331.295 | 0.015 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.38 |  | 345.5615 | 0.2369 | 348.47 | 341.42 | 0.0318 | watch_only | none |
| AMD | ai_accelerator | 485.3 |  | 478.0966 | 1.5067 | 482.43 | 461.04 | 1.053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 396.17 |  | 394.7771 | 0.3528 | 394.11 | 386.02 | 0.1262 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 514.225 |  | 512.3435 | 0.3672 | 511.83 | 498.665 | 0.1342 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 551.63 |  | 549.7342 | 0.3449 | 550 | 536.9 | 0.0852 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 368.72 |  | 367.9035 | 0.2219 | 368.42 | 357.97 | 3.0511 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 852.94 |  | 848.2209 | 0.5564 | 835.82 | 804.09 | 0.1712 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 184.59 |  | 184.4933 | 0.0524 | 185.03 | 178.09 | 0.7909 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 392.5 |  | 386.5055 | 1.551 | 384 | 368.28 | 1.9643 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.26 |  | 45.2875 | -0.0608 | 44.92 | 43.715 | 0.0663 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 23.93 |  | 24.0164 | -0.3599 | 24.3 | 23.46 | 0.0418 | below_vwap | below_vwap |
| SPY | market_regime | 744.85 |  | 744.3857 | 0.0624 | 742.66 | 740.8 | 0.0067 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.42 |  | 294.0941 | 0.1108 | 294.205 | 291.675 | 0.0136 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.4 |  | 124.856 | 0.4357 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 72.955 |  | 71.2459 | 2.3989 | 71.24 | 68.65 | 1.6586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 285.58 |  | 282.3581 | 1.1411 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 396.73 |  | 395.9338 | 0.2011 | 389.4 | 382.38 | 5.0412 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 626.125 |  | 623.3501 | 0.4452 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1038.645 |  | 1026.0818 | 1.2244 | 1001.82 | 982.21 | 0.5719 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.26 |  | 468.6757 | 0.338 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.03 |  | 140.3421 | 0.4901 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.18 |  | 162.86 | 0.8105 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 272.645 |  | 268.336 | 1.6058 | 269.59 | 256.24 | 4.8451 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 716.23 |  | 697.948 | 2.6194 | 694.98 | 653.305 | 3.9778 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.455 |  | 373.1449 | 0.6191 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 99.64 |  | 98.0326 | 1.6396 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 295.82 |  | 300.2781 | -1.4847 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1740.15 |  | 1735.949 | 0.242 | 1741.99 | 1704.935 | 0.6884 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.54 |  | 528.6064 | 0.555 | 535.095 | 513.34 | 0.7375 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 310.59 |  | 307.0436 | 1.155 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 209.53 |  | 210.339 | -0.3846 | 210.82 | 204.71 | 0.2864 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 309.98 |  | 309.4011 | 0.1871 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 268.15 |  | 266.779 | 0.5139 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 60.83 |  | 60.1901 | 1.0632 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.11 |  | 48.5581 | 1.1367 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 134.395 |  | 132.6772 | 1.2948 | 129.93 | 126.945 | 4.8737 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 318.58 |  | 314.7568 | 1.2146 | 315.89 | 307.13 | 1.2022 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 522.65 |  | 521.8495 | 0.1534 | 526.74 | 522.205 | 4.9957 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 301.365 |  | 301.5615 | -0.0652 | 304.36 | 299.62 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 24.81 |  | 24.8162 | -0.0248 | 25.45 | 24.1 | 0.0403 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.4 |  | 33.4239 | -0.0715 | 34 | 32.26 | 0.0599 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.4 |  | 20.3188 | 0.3996 | 20.445 | 19.92 | 0.098 | watch_only | none |
| SNDK | memory_hbm_storage | 1405.24 |  | 1400.8554 | 0.313 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 456 |  | 451.8854 | 0.9105 | 453.35 | 431.78 | 4.8224 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 747.84 |  | 734.969 | 1.7512 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 248.67 |  | 247.6534 | 0.4105 | 247.72 | 243.725 | 0.0362 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 628.52 |  | 637.0023 | -1.3316 | 649.07 | 638.97 | 0.6237 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.65 |  | 254.7485 | 1.5315 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 154.51 |  | 154.9965 | -0.3139 | 151.99 | 145.6 | 4.5952 | below_vwap | below_vwap,spread_too_wide |
