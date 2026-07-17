# Intraday State

- Generated at: `2026-07-18T00:43:08+08:00`
- Market time ET: `2026-07-17T12:43:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 3, 'below_vwap': 2, 'watch_only': 3, 'spread_too_wide_or_missing': 33, 'price_stale_or_missing': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.21 |  | 694.088 | 0.738 | 693.36 | 686.78 | 0.0372 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 526.52 |  | 515.7629 | 2.0857 | 511.83 | 498.665 | 0.0874 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.32 |  | 552.2884 | 1.6353 | 550 | 536.9 | 0.0267 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.8 |  | 744.744 | 0.1418 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.975 |  | 202.6951 | 1.1248 | 203.41 | 197.98 | 0.2293 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 561.32 |  | 552.2884 | 1.6353 | 550 | 536.9 | 0.0267 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 373.22 |  | 368.6126 | 1.2499 | 368.42 | 357.97 | 0.1929 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 526.52 |  | 515.7629 | 2.0857 | 511.83 | 498.665 | 0.0874 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 884.425 |  | 855.8139 | 3.3431 | 835.82 | 804.09 | 0.104 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 699.21 |  | 694.088 | 0.738 | 693.36 | 686.78 | 0.0372 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.855 |  | 45.4123 | 0.9748 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.8 |  | 744.744 | 0.1418 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189.79 |  | 185.3717 | 2.3835 | 185.03 | 178.09 | 0.2634 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 127.085 |  | 125.3857 | 1.3553 | 125.02 | 121.79 | 0.0472 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.54 |  | 24.1137 | 1.768 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 72.52 |  | 71.7804 | 1.0304 | 71.24 | 68.65 | 0.3034 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.5273 | 1.231 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.64 |  | 66.911 | 2.5841 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 745.8 |  | 744.744 | 0.1418 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.08 |  | 294.0444 | 0.0121 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| 3 | QQQ | market_regime | 699.21 |  | 694.088 | 0.738 | 693.36 | 686.78 | 0.0372 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 347.07 |  | 346.1282 | 0.2721 | 348.47 | 341.42 | 0.1729 | watch_only | none |
| 5 | NVDA | ai_accelerator | 204.975 |  | 202.6951 | 1.1248 | 203.41 | 197.98 | 0.2293 | buy_precheck_manual_confirm | none |
| 6 | JCI | data_center_power_cooling | 141.1 |  | 140.724 | 0.2672 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | AVGO | custom_silicon_networking | 373.22 |  | 368.6126 | 1.2499 | 368.42 | 357.97 | 0.1929 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.855 |  | 45.4123 | 0.9748 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 127.085 |  | 125.3857 | 1.3553 | 125.02 | 121.79 | 0.0472 | buy_precheck_manual_confirm | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.5273 | 1.231 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 11 | IREN | high_beta_ai_infrastructure | 33.89 |  | 33.5507 | 1.0113 | 34 | 32.26 | 0.0885 | watch_only | none |
| 12 | TT | data_center_power_cooling | 472.82 |  | 469.4164 | 0.7251 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AMZN | cloud_ai_capex | 248.61 |  | 247.9123 | 0.2814 | 247.72 | 243.725 | 0.3942 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | CRWV | gpu_cloud_ai_factory | 72.52 |  | 71.7804 | 1.0304 | 71.24 | 68.65 | 0.3034 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 24.54 |  | 24.1137 | 1.768 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 16 | SMH | semiconductor_index | 561.32 |  | 552.2884 | 1.6353 | 550 | 536.9 | 0.0267 | buy_precheck_manual_confirm | none |
| 17 | SOXX | semiconductor_index | 526.52 |  | 515.7629 | 2.0857 | 511.83 | 498.665 | 0.0874 | buy_precheck_manual_confirm | none |
| 18 | MU | memory_hbm_storage | 884.425 |  | 855.8139 | 3.3431 | 835.82 | 804.09 | 0.104 | buy_precheck_manual_confirm | none |
| 19 | MSFT | cloud_ai_capex | 393.32 |  | 392.9433 | 0.0959 | 398.39 | 393.52 | 0.0305 | below_opening_15m_low | below_opening_15m_low |
| 20 | MRVL | custom_silicon_networking | 189.79 |  | 185.3717 | 2.3835 | 185.03 | 178.09 | 0.2634 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.975 |  | 202.6951 | 1.1248 | 203.41 | 197.98 | 0.2293 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 561.32 |  | 552.2884 | 1.6353 | 550 | 536.9 | 0.0267 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 373.22 |  | 368.6126 | 1.2499 | 368.42 | 357.97 | 0.1929 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 526.52 |  | 515.7629 | 2.0857 | 511.83 | 498.665 | 0.0874 | buy_precheck_manual_confirm | none |
| 5 | MU | memory_hbm_storage | 884.425 |  | 855.8139 | 3.3431 | 835.82 | 804.09 | 0.104 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 699.21 |  | 694.088 | 0.738 | 693.36 | 686.78 | 0.0372 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 45.855 |  | 45.4123 | 0.9748 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 745.8 |  | 744.744 | 0.1418 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 189.79 |  | 185.3717 | 2.3835 | 185.03 | 178.09 | 0.2634 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 127.085 |  | 125.3857 | 1.3553 | 125.02 | 121.79 | 0.0472 | buy_precheck_manual_confirm | none |
| 11 | SMCI | ai_server_oem | 24.54 |  | 24.1137 | 1.768 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| 12 | CRWV | gpu_cloud_ai_factory | 72.52 |  | 71.7804 | 1.0304 | 71.24 | 68.65 | 0.3034 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.5273 | 1.231 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.64 |  | 66.911 | 2.5841 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 167.975 |  | 164.1947 | 2.3023 | 163.275 | 157.34 | 3.191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | TSM | foundry | 400.53 |  | 396.7941 | 0.9415 | 394.11 | 386.02 | 1.4556 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 545.65 |  | 532.2262 | 2.5222 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 498.79 |  | 483.4561 | 3.1717 | 482.43 | 461.04 | 3.8393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1771.92 |  | 1746.875 | 1.4337 | 1741.99 | 1704.935 | 1.6366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 472.82 |  | 469.4164 | 0.7251 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 699.21 |  | 694.088 | 0.738 | 693.36 | 686.78 | 0.0372 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.64 |  | 66.911 | 2.5841 | 66.9 | 64.92 | 0.0146 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.975 |  | 202.6951 | 1.1248 | 203.41 | 197.98 | 0.2293 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.32 |  | 392.9433 | 0.0959 | 398.39 | 393.52 | 0.0305 | below_opening_15m_low | below_opening_15m_low |
| AAPL | mega_cap_platform | 332.075 |  | 332.2712 | -0.059 | 334.98 | 331.295 | 0.1024 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 347.07 |  | 346.1282 | 0.2721 | 348.47 | 341.42 | 0.1729 | watch_only | none |
| AMD | ai_accelerator | 498.79 |  | 483.4561 | 3.1717 | 482.43 | 461.04 | 3.8393 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 400.53 |  | 396.7941 | 0.9415 | 394.11 | 386.02 | 1.4556 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.52 |  | 515.7629 | 2.0857 | 511.83 | 498.665 | 0.0874 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.32 |  | 552.2884 | 1.6353 | 550 | 536.9 | 0.0267 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 373.22 |  | 368.6126 | 1.2499 | 368.42 | 357.97 | 0.1929 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 884.425 |  | 855.8139 | 3.3431 | 835.82 | 804.09 | 0.104 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 189.79 |  | 185.3717 | 2.3835 | 185.03 | 178.09 | 0.2634 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 394.46 |  | 388.7072 | 1.48 | 384 | 368.28 | 2.4134 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.855 |  | 45.4123 | 0.9748 | 44.92 | 43.715 | 0.0218 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.54 |  | 24.1137 | 1.768 | 24.3 | 23.46 | 0.0407 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.8 |  | 744.744 | 0.1418 | 742.66 | 740.8 | 0.0054 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.08 |  | 294.0444 | 0.0121 | 294.205 | 291.675 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 127.085 |  | 125.3857 | 1.3553 | 125.02 | 121.79 | 0.0472 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 72.52 |  | 71.7804 | 1.0304 | 71.24 | 68.65 | 0.3034 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 293.54 |  | 284.4021 | 3.213 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 402.63 |  | 399.0423 | 0.8991 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 632.995 |  | 627.6056 | 0.8587 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1051.8 |  | 1040.0068 | 1.1339 | 1001.82 | 982.21 | 1.3672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 472.82 |  | 469.4164 | 0.7251 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.1 |  | 140.724 | 0.2672 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.975 |  | 164.1947 | 2.3023 | 163.275 | 157.34 | 3.191 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 279.89 |  | 272.3855 | 2.7551 | 269.59 | 256.24 | 1.3934 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 725.83 |  | 706.223 | 2.7763 | 694.98 | 653.305 | 4.0078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 378.755 |  | 375.0305 | 0.9931 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.5 |  | 99.0014 | 2.5238 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 308.53 |  | 302.1038 | 2.1272 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1771.92 |  | 1746.875 | 1.4337 | 1741.99 | 1704.935 | 1.6366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 545.65 |  | 532.2262 | 2.5222 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 317.1 |  | 310.5882 | 2.0966 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.18 |  | 211.3414 | 1.3431 | 210.82 | 204.71 | 4.5803 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 322.6 |  | 312.4543 | 3.2471 | 308.03 | 297.18 | 4.8171 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 281.14 |  | 272.3445 | 3.2295 | 265.71 | 258.355 | 4.8268 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.51 |  | 60.9777 | 2.5129 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.85 |  | 49.4868 | 2.7546 | 49.35 | 46.44 | 1.1406 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ENTG | semiconductor_materials | 137.96 |  | 133.5855 | 3.2747 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 325.39 |  | 316.7715 | 2.7207 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 516.28 |  | 521.1241 | -0.9295 | 526.74 | 522.205 | 0.1259 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APD | industrial_gases | 296.98 |  | 300.2288 | -1.0821 | 304.36 | 299.62 | 3.7612 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.16 |  | 24.901 | 1.0403 | 25.45 | 24.1 | 0.3975 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.89 |  | 33.5507 | 1.0113 | 34 | 32.26 | 0.0885 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.78 |  | 20.5273 | 1.231 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1463.32 |  | 1418.2856 | 3.1753 | 1393.96 | 1325.48 | 3.4169 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 477.75 |  | 457.6713 | 4.3871 | 453.35 | 431.78 | 1.3836 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 781.53 |  | 747.7053 | 4.5238 | 724.57 | 702.24 | 0.4018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.61 |  | 247.9123 | 0.2814 | 247.72 | 243.725 | 0.3942 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| META | cloud_ai_capex | 644.38 |  | 638.2389 | 0.9622 | 649.07 | 638.97 | 2.9796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 267.1 |  | 257.7498 | 3.6276 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 162.725 |  | 157.2007 | 3.5142 | 151.99 | 145.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
