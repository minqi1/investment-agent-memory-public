# Intraday State

- Generated at: `2026-07-18T03:52:43+08:00`
- Market time ET: `2026-07-17T15:52:43-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 17, 'watch_only': 3, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_vwap': 9, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.43 |  | 695.6806 | 0.2515 | 693.36 | 686.78 | 0.0229 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 524.77 |  | 519.2221 | 1.0685 | 511.83 | 498.665 | 0.0591 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 559.17 |  | 555.3405 | 0.6896 | 550 | 536.9 | 0.0411 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.16 |  | 744.4874 | -0.044 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.715 |  | 203.1731 | 0.2667 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 559.17 |  | 555.3405 | 0.6896 | 550 | 536.9 | 0.0411 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.77 |  | 519.2221 | 1.0685 | 511.83 | 498.665 | 0.0591 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.8 |  | 212.3235 | 0.6954 | 210.82 | 204.71 | 0.0468 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.21 |  | 294.073 | 0.0466 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1059.285 |  | 1047.1827 | 1.1557 | 1001.82 | 982.21 | 0.1029 | buy_precheck_manual_confirm | none |
| 7 | DELL | ai_server_oem | 400.565 |  | 393.9935 | 1.6679 | 384 | 368.28 | 0.2397 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 697.43 |  | 695.6806 | 0.2515 | 693.36 | 686.78 | 0.0229 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.13 |  | 45.7306 | 0.8734 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 10 | LITE | ai_networking_optical | 740.52 |  | 720.7859 | 2.7379 | 694.98 | 653.305 | 0.1215 | buy_precheck_manual_confirm | none |
| 11 | ENTG | semiconductor_materials | 138.4 |  | 135.6947 | 1.9937 | 129.93 | 126.945 | 0.2601 | buy_precheck_manual_confirm | none |
| 12 | TER | semiconductor_test_packaging | 324.94 |  | 320.8755 | 1.2667 | 308.03 | 297.18 | 0.3447 | buy_precheck_manual_confirm | none |
| 13 | MRVL | custom_silicon_networking | 189.56 |  | 187.3421 | 1.1839 | 185.03 | 178.09 | 0.1635 | buy_precheck_manual_confirm | none |
| 14 | ORCL | cloud_ai_capex | 126.53 |  | 126.113 | 0.3306 | 125.02 | 121.79 | 0.0632 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 24.44 |  | 24.3304 | 0.4504 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.83 |  | 20.6901 | 0.6761 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| 17 | TQQQ | leveraged_tool | 68.01 |  | 67.283 | 1.0805 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.715 |  | 203.1731 | 0.2667 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 294.21 |  | 294.073 | 0.0466 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 697.43 |  | 695.6806 | 0.2515 | 693.36 | 686.78 | 0.0229 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 126.53 |  | 126.113 | 0.3306 | 125.02 | 121.79 | 0.0632 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 395.06 |  | 393.756 | 0.3312 | 398.39 | 393.52 | 0.0709 | watch_only | none |
| 6 | SMCI | ai_server_oem | 24.44 |  | 24.3304 | 0.4504 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 7 | KLAC | semiconductor_equipment | 213.8 |  | 212.3235 | 0.6954 | 210.82 | 204.71 | 0.0468 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 345.87 |  | 345.6984 | 0.0496 | 348.47 | 341.42 | 0.2313 | watch_only | none |
| 9 | SMH | semiconductor_index | 559.17 |  | 555.3405 | 0.6896 | 550 | 536.9 | 0.0411 | buy_precheck_manual_confirm | none |
| 10 | AAPL | mega_cap_platform | 333.99 |  | 332.4626 | 0.4594 | 334.98 | 331.295 | 0.012 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.83 |  | 20.6901 | 0.6761 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| 12 | SOXX | semiconductor_index | 524.77 |  | 519.2221 | 1.0685 | 511.83 | 498.665 | 0.0591 | buy_precheck_manual_confirm | none |
| 13 | ALAB | ai_networking_optical | 305.14 |  | 304.627 | 0.1684 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1059.285 |  | 1047.1827 | 1.1557 | 1001.82 | 982.21 | 0.1029 | buy_precheck_manual_confirm | none |
| 15 | HPE | ai_server_oem | 46.13 |  | 45.7306 | 0.8734 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 16 | TT | data_center_power_cooling | 471.13 |  | 469.7956 | 0.284 | 469.08 | 460.78 | 4.0329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TER | semiconductor_test_packaging | 324.94 |  | 320.8755 | 1.2667 | 308.03 | 297.18 | 0.3447 | buy_precheck_manual_confirm | none |
| 18 | MRVL | custom_silicon_networking | 189.56 |  | 187.3421 | 1.1839 | 185.03 | 178.09 | 0.1635 | buy_precheck_manual_confirm | none |
| 19 | PWR | data_center_power_cooling | 632.24 |  | 630.3909 | 0.2933 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | TSM | foundry | 399.065 |  | 397.8596 | 0.303 | 394.11 | 386.02 | 0.4987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 203.715 |  | 203.1731 | 0.2667 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 559.17 |  | 555.3405 | 0.6896 | 550 | 536.9 | 0.0411 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 524.77 |  | 519.2221 | 1.0685 | 511.83 | 498.665 | 0.0591 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.8 |  | 212.3235 | 0.6954 | 210.82 | 204.71 | 0.0468 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 294.21 |  | 294.073 | 0.0466 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1059.285 |  | 1047.1827 | 1.1557 | 1001.82 | 982.21 | 0.1029 | buy_precheck_manual_confirm | none |
| 7 | DELL | ai_server_oem | 400.565 |  | 393.9935 | 1.6679 | 384 | 368.28 | 0.2397 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 697.43 |  | 695.6806 | 0.2515 | 693.36 | 686.78 | 0.0229 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.13 |  | 45.7306 | 0.8734 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 10 | LITE | ai_networking_optical | 740.52 |  | 720.7859 | 2.7379 | 694.98 | 653.305 | 0.1215 | buy_precheck_manual_confirm | none |
| 11 | ENTG | semiconductor_materials | 138.4 |  | 135.6947 | 1.9937 | 129.93 | 126.945 | 0.2601 | buy_precheck_manual_confirm | none |
| 12 | TER | semiconductor_test_packaging | 324.94 |  | 320.8755 | 1.2667 | 308.03 | 297.18 | 0.3447 | buy_precheck_manual_confirm | none |
| 13 | MRVL | custom_silicon_networking | 189.56 |  | 187.3421 | 1.1839 | 185.03 | 178.09 | 0.1635 | buy_precheck_manual_confirm | none |
| 14 | ORCL | cloud_ai_capex | 126.53 |  | 126.113 | 0.3306 | 125.02 | 121.79 | 0.0632 | buy_precheck_manual_confirm | none |
| 15 | SMCI | ai_server_oem | 24.44 |  | 24.3304 | 0.4504 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.83 |  | 20.6901 | 0.6761 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| 17 | TQQQ | leveraged_tool | 68.01 |  | 67.283 | 1.0805 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| 18 | CIEN | ai_networking_optical | 376.595 |  | 377.5495 | -0.2528 | 375.52 | 359.81 | 4.2486 | below_vwap | below_vwap,spread_too_wide |
| 19 | SPY | market_regime | 744.16 |  | 744.4874 | -0.044 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 20 | SKHY | memory_hbm_storage | 154.23 |  | 158.5257 | -2.7098 | 151.99 | 145.6 | 1.6534 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.43 |  | 695.6806 | 0.2515 | 693.36 | 686.78 | 0.0229 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.01 |  | 67.283 | 1.0805 | 66.9 | 64.92 | 0.0294 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.715 |  | 203.1731 | 0.2667 | 203.41 | 197.98 | 0.0098 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 395.06 |  | 393.756 | 0.3312 | 398.39 | 393.52 | 0.0709 | watch_only | none |
| AAPL | mega_cap_platform | 333.99 |  | 332.4626 | 0.4594 | 334.98 | 331.295 | 0.012 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.87 |  | 345.6984 | 0.0496 | 348.47 | 341.42 | 0.2313 | watch_only | none |
| AMD | ai_accelerator | 500 |  | 488.0064 | 2.4577 | 482.43 | 461.04 | 4.774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 399.065 |  | 397.8596 | 0.303 | 394.11 | 386.02 | 0.4987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 524.77 |  | 519.2221 | 1.0685 | 511.83 | 498.665 | 0.0591 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 559.17 |  | 555.3405 | 0.6896 | 550 | 536.9 | 0.0411 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 372.52 |  | 370.5555 | 0.5301 | 368.42 | 357.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 864.66 |  | 864.5171 | 0.0165 | 835.82 | 804.09 | 0.8928 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.56 |  | 187.3421 | 1.1839 | 185.03 | 178.09 | 0.1635 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 400.565 |  | 393.9935 | 1.6679 | 384 | 368.28 | 0.2397 | buy_precheck_manual_confirm | none |
| HPE | ai_server_oem | 46.13 |  | 45.7306 | 0.8734 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.44 |  | 24.3304 | 0.4504 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.16 |  | 744.4874 | -0.044 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 294.21 |  | 294.073 | 0.0466 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.53 |  | 126.113 | 0.3306 | 125.02 | 121.79 | 0.0632 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 73.2 |  | 72.3427 | 1.1851 | 71.24 | 68.65 | 4.2077 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.93 |  | 288.0048 | 1.0157 | 280.565 | 273.17 | 4.3206 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 402.19 |  | 399.8256 | 0.5914 | 389.4 | 382.38 | 0.4774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 632.24 |  | 630.3909 | 0.2933 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1059.285 |  | 1047.1827 | 1.1557 | 1001.82 | 982.21 | 0.1029 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 471.13 |  | 469.7956 | 0.284 | 469.08 | 460.78 | 4.0329 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.735 |  | 140.883 | -0.1051 | 140.765 | 137.165 | 4.7891 | below_vwap | below_vwap,spread_too_wide |
| ANET | ai_networking_optical | 168.875 |  | 166.6096 | 1.3597 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 279.75 |  | 274.7761 | 1.8101 | 269.59 | 256.24 | 1.0438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 740.52 |  | 720.7859 | 2.7379 | 694.98 | 653.305 | 0.1215 | buy_precheck_manual_confirm | none |
| CIEN | ai_networking_optical | 376.595 |  | 377.5495 | -0.2528 | 375.52 | 359.81 | 4.2486 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 102.89 |  | 100.8814 | 1.991 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 305.14 |  | 304.627 | 0.1684 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1758.14 |  | 1756.9371 | 0.0685 | 1741.99 | 1704.935 | 2.5135 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.28 |  | 533.537 | -0.423 | 535.095 | 513.34 | 0.1506 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 313.905 |  | 312.1005 | 0.5782 | 306.51 | 298.89 | 3.208 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 213.8 |  | 212.3235 | 0.6954 | 210.82 | 204.71 | 0.0468 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 324.94 |  | 320.8755 | 1.2667 | 308.03 | 297.18 | 0.3447 | buy_precheck_manual_confirm | none |
| ONTO | semiconductor_test_packaging | 278.63 |  | 277.6845 | 0.3405 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.18 |  | 61.7515 | 2.3133 | 60.51 | 57.99 | 4.7958 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 51.13 |  | 50.0848 | 2.0869 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 138.4 |  | 135.6947 | 1.9937 | 129.93 | 126.945 | 0.2601 | buy_precheck_manual_confirm | none |
| MKSI | semiconductor_materials | 327.22 |  | 320.0346 | 2.2452 | 315.89 | 307.13 | 4.5413 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 512.98 |  | 517.2478 | -0.8251 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 295.385 |  | 298.035 | -0.8892 | 304.36 | 299.62 | 4.3672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.535 |  | 25.1258 | 1.6287 | 25.45 | 24.1 | 0.7049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 33.425 |  | 33.7152 | -0.8607 | 34 | 32.26 | 0.0598 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.83 |  | 20.6901 | 0.6761 | 20.445 | 19.92 | 0.048 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1393.34 |  | 1425.0533 | -2.2254 | 1393.96 | 1325.48 | 2.9203 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 479.17 |  | 468.5938 | 2.257 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 792.745 |  | 769.4708 | 3.0247 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.395 |  | 247.8991 | -0.2033 | 247.72 | 243.725 | 0.0404 | below_vwap | below_vwap |
| META | cloud_ai_capex | 645.88 |  | 642.656 | 0.5017 | 649.07 | 638.97 | 0.8345 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 267.475 |  | 261.849 | 2.1486 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 154.23 |  | 158.5257 | -2.7098 | 151.99 | 145.6 | 1.6534 | below_vwap | below_vwap,spread_too_wide |
