# Intraday State

- Generated at: `2026-07-18T01:13:18+08:00`
- Market time ET: `2026-07-17T13:13:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'spread_too_wide_or_missing': 35, 'watch_only': 2, 'below_opening_15m_low': 3, 'price_stale_or_missing': 1, 'below_vwap': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701.78 |  | 694.626 | 1.0299 | 693.36 | 686.78 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 532.15 |  | 516.7907 | 2.9721 | 511.83 | 498.665 | 0.1015 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 566.39 |  | 553.7325 | 2.2859 | 550 | 536.9 | 0.0847 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.98 |  | 744.8798 | 0.2819 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 566.39 |  | 553.7325 | 2.2859 | 550 | 536.9 | 0.0847 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 532.15 |  | 516.7907 | 2.9721 | 511.83 | 498.665 | 0.1015 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 141.74 |  | 140.8089 | 0.6613 | 140.765 | 137.165 | 0.1482 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 295.24 |  | 294.0911 | 0.3907 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 701.78 |  | 694.626 | 1.0299 | 693.36 | 686.78 | 0.0085 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.465 |  | 45.4898 | 2.1438 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 746.98 |  | 744.8798 | 0.2819 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 249.03 |  | 248.0238 | 0.4057 | 247.72 | 243.725 | 0.012 | buy_precheck_manual_confirm | none |
| 9 | SKHY | memory_hbm_storage | 165.04 |  | 157.9805 | 4.4686 | 151.99 | 145.6 | 0.1515 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.08 |  | 24.1939 | 3.6625 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.32 |  | 20.5726 | 3.6329 | 20.445 | 19.92 | 0.1407 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.825 |  | 24.9413 | 3.5431 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.51 |  | 33.6374 | 2.5941 | 34 | 32.26 | 0.029 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 69.47 |  | 67.0608 | 3.5925 | 66.9 | 64.92 | 0.0288 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 746.98 |  | 744.8798 | 0.2819 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 141.74 |  | 140.8089 | 0.6613 | 140.765 | 137.165 | 0.1482 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 295.24 |  | 294.0911 | 0.3907 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 249.03 |  | 248.0238 | 0.4057 | 247.72 | 243.725 | 0.012 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 394.24 |  | 393.051 | 0.3025 | 398.39 | 393.52 | 0.0355 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 346.435 |  | 346.1816 | 0.0732 | 348.47 | 341.42 | 0.3493 | watch_only | none |
| 7 | QQQ | market_regime | 701.78 |  | 694.626 | 1.0299 | 693.36 | 686.78 | 0.0085 | buy_precheck_manual_confirm | none |
| 8 | TT | data_center_power_cooling | 473.26 |  | 469.5639 | 0.7871 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 566.39 |  | 553.7325 | 2.2859 | 550 | 536.9 | 0.0847 | buy_precheck_manual_confirm | none |
| 10 | SOXX | semiconductor_index | 532.15 |  | 516.7907 | 2.9721 | 511.83 | 498.665 | 0.1015 | buy_precheck_manual_confirm | none |
| 11 | APLD | high_beta_ai_infrastructure | 25.825 |  | 24.9413 | 3.5431 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.51 |  | 33.6374 | 2.5941 | 34 | 32.26 | 0.029 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 46.465 |  | 45.4898 | 2.1438 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 25.08 |  | 24.1939 | 3.6625 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| 15 | CORZ | high_beta_ai_infrastructure | 21.32 |  | 20.5726 | 3.6329 | 20.445 | 19.92 | 0.1407 | buy_precheck_manual_confirm | none |
| 16 | SKHY | memory_hbm_storage | 165.04 |  | 157.9805 | 4.4686 | 151.99 | 145.6 | 0.1515 | buy_precheck_manual_confirm | none |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 404 |  | 399.2506 | 1.1896 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 634.055 |  | 628.4662 | 0.8893 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TSM | foundry | 403.25 |  | 397.473 | 1.4534 | 394.11 | 386.02 | 0.3596 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 566.39 |  | 553.7325 | 2.2859 | 550 | 536.9 | 0.0847 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 532.15 |  | 516.7907 | 2.9721 | 511.83 | 498.665 | 0.1015 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 141.74 |  | 140.8089 | 0.6613 | 140.765 | 137.165 | 0.1482 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 295.24 |  | 294.0911 | 0.3907 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 701.78 |  | 694.626 | 1.0299 | 693.36 | 686.78 | 0.0085 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.465 |  | 45.4898 | 2.1438 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| 7 | SPY | market_regime | 746.98 |  | 744.8798 | 0.2819 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 249.03 |  | 248.0238 | 0.4057 | 247.72 | 243.725 | 0.012 | buy_precheck_manual_confirm | none |
| 9 | SKHY | memory_hbm_storage | 165.04 |  | 157.9805 | 4.4686 | 151.99 | 145.6 | 0.1515 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 25.08 |  | 24.1939 | 3.6625 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 21.32 |  | 20.5726 | 3.6329 | 20.445 | 19.92 | 0.1407 | buy_precheck_manual_confirm | none |
| 12 | APLD | high_beta_ai_infrastructure | 25.825 |  | 24.9413 | 3.5431 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| 13 | IREN | high_beta_ai_infrastructure | 34.51 |  | 33.6374 | 2.5941 | 34 | 32.26 | 0.029 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 69.47 |  | 67.0608 | 3.5925 | 66.9 | 64.92 | 0.0288 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 170.33 |  | 164.8392 | 3.331 | 163.275 | 157.34 | 1.82 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | NVDA | ai_accelerator | 206.4 |  | 202.9196 | 1.7151 | 203.41 | 197.98 | 0.4893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TSM | foundry | 403.25 |  | 397.473 | 1.4534 | 394.11 | 386.02 | 0.3596 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AVGO | custom_silicon_networking | 376.86 |  | 369.5089 | 1.9894 | 368.42 | 357.97 | 2.5182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMAT | semiconductor_equipment | 546.025 |  | 534.3653 | 2.182 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AMD | ai_accelerator | 500.61 |  | 484.8818 | 3.2437 | 482.43 | 461.04 | 4.129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 701.78 |  | 694.626 | 1.0299 | 693.36 | 686.78 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 69.47 |  | 67.0608 | 3.5925 | 66.9 | 64.92 | 0.0288 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.4 |  | 202.9196 | 1.7151 | 203.41 | 197.98 | 0.4893 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 394.24 |  | 393.051 | 0.3025 | 398.39 | 393.52 | 0.0355 | watch_only | none |
| AAPL | mega_cap_platform | 329.98 |  | 332.1811 | -0.6626 | 334.98 | 331.295 | 0.4546 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 346.435 |  | 346.1816 | 0.0732 | 348.47 | 341.42 | 0.3493 | watch_only | none |
| AMD | ai_accelerator | 500.61 |  | 484.8818 | 3.2437 | 482.43 | 461.04 | 4.129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 403.25 |  | 397.473 | 1.4534 | 394.11 | 386.02 | 0.3596 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 532.15 |  | 516.7907 | 2.9721 | 511.83 | 498.665 | 0.1015 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 566.39 |  | 553.7325 | 2.2859 | 550 | 536.9 | 0.0847 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 376.86 |  | 369.5089 | 1.9894 | 368.42 | 357.97 | 2.5182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 898.35 |  | 859.6733 | 4.499 | 835.82 | 804.09 | 0.8326 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 193.43 |  | 186.2202 | 3.8716 | 185.03 | 178.09 | 0.3619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403.87 |  | 389.9063 | 3.5813 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 46.465 |  | 45.4898 | 2.1438 | 44.92 | 43.715 | 0.0215 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.08 |  | 24.1939 | 3.6625 | 24.3 | 23.46 | 0.0399 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.98 |  | 744.8798 | 0.2819 | 742.66 | 740.8 | 0.0174 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.24 |  | 294.0911 | 0.3907 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 128.29 |  | 125.6576 | 2.0949 | 125.02 | 121.79 | 2.7282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 73.84 |  | 71.8716 | 2.7387 | 71.24 | 68.65 | 4.3879 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 295.95 |  | 285.4438 | 3.6807 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 404 |  | 399.2506 | 1.1896 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 634.055 |  | 628.4662 | 0.8893 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1065.35 |  | 1041.4659 | 2.2933 | 1001.82 | 982.21 | 1.0072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 473.26 |  | 469.5639 | 0.7871 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.74 |  | 140.8089 | 0.6613 | 140.765 | 137.165 | 0.1482 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 170.33 |  | 164.8392 | 3.331 | 163.275 | 157.34 | 1.82 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 284.065 |  | 273.0822 | 4.0218 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 740.87 |  | 711.6249 | 4.1096 | 694.98 | 653.305 | 4.569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 382.09 |  | 375.8138 | 1.67 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 104.55 |  | 99.333 | 5.252 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 313.61 |  | 303.6757 | 3.2713 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1787.915 |  | 1749.8379 | 2.176 | 1741.99 | 1704.935 | 2.2014 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 546.025 |  | 534.3653 | 2.182 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 317.82 |  | 311.4267 | 2.0529 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216 |  | 211.7437 | 2.0101 | 210.82 | 204.71 | 0.5139 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 329.725 |  | 316.8651 | 4.0585 | 308.03 | 297.18 | 4.6766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 284.21 |  | 274.9794 | 3.3568 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.39 |  | 61.1673 | 3.6338 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.47 |  | 49.6669 | 3.6305 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 139.83 |  | 133.8189 | 4.4919 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 329.01 |  | 317.2265 | 3.7145 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 515.94 |  | 520.6508 | -0.9048 | 526.74 | 522.205 | 0.4652 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 297.33 |  | 300.0065 | -0.8922 | 304.36 | 299.62 | 4.0494 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.825 |  | 24.9413 | 3.5431 | 25.45 | 24.1 | 0.0387 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 34.51 |  | 33.6374 | 2.5941 | 34 | 32.26 | 0.029 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 21.32 |  | 20.5726 | 3.6329 | 20.445 | 19.92 | 0.1407 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1487.66 |  | 1423.991 | 4.4712 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 484.87 |  | 461.0995 | 5.1552 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 796.585 |  | 751.4057 | 6.0126 | 724.57 | 702.24 | 2.6865 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 249.03 |  | 248.0238 | 0.4057 | 247.72 | 243.725 | 0.012 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 650.19 |  | 640.3433 | 1.5377 | 649.07 | 638.97 | 2.3516 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 271.7 |  | 259.1226 | 4.8538 | 252.95 | 243.21 | 2.3187 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 165.04 |  | 157.9805 | 4.4686 | 151.99 | 145.6 | 0.1515 | buy_precheck_manual_confirm | none |
