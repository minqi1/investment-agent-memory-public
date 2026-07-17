# Intraday State

- Generated at: `2026-07-17T22:23:11+08:00`
- Market time ET: `2026-07-17T10:23:13-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 13, 'below_opening_15m_low': 4, 'below_vwap': 3, 'spread_too_wide_or_missing': 34, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.305 |  | 692.095 | 0.7528 | 693.36 | 686.78 | 0.043 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 522.16 |  | 510.7821 | 2.2276 | 511.83 | 498.665 | 0.1302 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.42 |  | 548.9558 | 1.724 | 550 | 536.9 | 0.1218 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.67 |  | 743.6324 | 0.4085 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.985 |  | 201.4538 | 1.7529 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.42 |  | 548.9558 | 1.724 | 550 | 536.9 | 0.1218 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 522.16 |  | 510.7821 | 2.2276 | 511.83 | 498.665 | 0.1302 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.315 |  | 209.9579 | 1.5989 | 210.82 | 204.71 | 0.2344 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.775 |  | 293.8303 | 0.6619 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 697.305 |  | 692.095 | 0.7528 | 693.36 | 686.78 | 0.043 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.015 |  | 44.8677 | 2.5572 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.67 |  | 743.6324 | 0.4085 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.22 |  | 246.9159 | 0.5281 | 247.72 | 243.725 | 0.0242 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.49 |  | 23.9427 | 2.2857 | 24.3 | 23.46 | 0.1225 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.735 |  | 20.2303 | 2.4945 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.22 |  | 33.3089 | 2.7352 | 34 | 32.26 | 0.0584 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.18 |  | 66.2307 | 2.9431 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 248.22 |  | 246.9159 | 0.5281 | 247.72 | 243.725 | 0.0242 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 295.775 |  | 293.8303 | 0.6619 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | QQQ | market_regime | 697.305 |  | 692.095 | 0.7528 | 693.36 | 686.78 | 0.043 | buy_precheck_manual_confirm | none |
| 4 | SPY | market_regime | 746.67 |  | 743.6324 | 0.4085 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 204.985 |  | 201.4538 | 1.7529 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 6 | TT | data_center_power_cooling | 470.88 |  | 467.6875 | 0.6826 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SMCI | ai_server_oem | 24.49 |  | 23.9427 | 2.2857 | 24.3 | 23.46 | 0.1225 | buy_precheck_manual_confirm | none |
| 8 | IREN | high_beta_ai_infrastructure | 34.22 |  | 33.3089 | 2.7352 | 34 | 32.26 | 0.0584 | buy_precheck_manual_confirm | none |
| 9 | KLAC | semiconductor_equipment | 213.315 |  | 209.9579 | 1.5989 | 210.82 | 204.71 | 0.2344 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 558.42 |  | 548.9558 | 1.724 | 550 | 536.9 | 0.1218 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.735 |  | 20.2303 | 2.4945 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| 12 | SOXX | semiconductor_index | 522.16 |  | 510.7821 | 2.2276 | 511.83 | 498.665 | 0.1302 | buy_precheck_manual_confirm | none |
| 13 | HPE | ai_server_oem | 46.015 |  | 44.8677 | 2.5572 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| 14 | APLD | high_beta_ai_infrastructure | 25.14 |  | 24.7399 | 1.6173 | 25.45 | 24.1 | 0.1193 | watch_only | none |
| 15 | JCI | data_center_power_cooling | 140.955 |  | 139.3673 | 1.1392 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ASML | semiconductor_equipment | 1746.415 |  | 1731.7368 | 0.8476 | 1741.99 | 1704.935 | 0.4237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AVGO | custom_silicon_networking | 371.095 |  | 367.0606 | 1.0991 | 368.42 | 357.97 | 1.951 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMAT | semiconductor_equipment | 536.12 |  | 526.3894 | 1.8486 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 345.275 |  | 345.3286 | -0.0155 | 348.47 | 341.42 | 0.1072 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.985 |  | 201.4538 | 1.7529 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 558.42 |  | 548.9558 | 1.724 | 550 | 536.9 | 0.1218 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 522.16 |  | 510.7821 | 2.2276 | 511.83 | 498.665 | 0.1302 | buy_precheck_manual_confirm | none |
| 4 | KLAC | semiconductor_equipment | 213.315 |  | 209.9579 | 1.5989 | 210.82 | 204.71 | 0.2344 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 295.775 |  | 293.8303 | 0.6619 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 697.305 |  | 692.095 | 0.7528 | 693.36 | 686.78 | 0.043 | buy_precheck_manual_confirm | none |
| 7 | HPE | ai_server_oem | 46.015 |  | 44.8677 | 2.5572 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| 8 | SPY | market_regime | 746.67 |  | 743.6324 | 0.4085 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 9 | AMZN | cloud_ai_capex | 248.22 |  | 246.9159 | 0.5281 | 247.72 | 243.725 | 0.0242 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.49 |  | 23.9427 | 2.2857 | 24.3 | 23.46 | 0.1225 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.735 |  | 20.2303 | 2.4945 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| 12 | IREN | high_beta_ai_infrastructure | 34.22 |  | 33.3089 | 2.7352 | 34 | 32.26 | 0.0584 | buy_precheck_manual_confirm | none |
| 13 | TQQQ | leveraged_tool | 68.18 |  | 66.2307 | 2.9431 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| 14 | ANET | ai_networking_optical | 166.28 |  | 161.8743 | 2.7217 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TSM | foundry | 402.32 |  | 393.0482 | 2.359 | 394.11 | 386.02 | 2.4856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 371.095 |  | 367.0606 | 1.0991 | 368.42 | 357.97 | 1.951 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 536.12 |  | 526.3894 | 1.8486 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AMD | ai_accelerator | 490.71 |  | 474.6669 | 3.3799 | 482.43 | 461.04 | 1.2839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1746.415 |  | 1731.7368 | 0.8476 | 1741.99 | 1704.935 | 0.4237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 470.88 |  | 467.6875 | 0.6826 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 697.305 |  | 692.095 | 0.7528 | 693.36 | 686.78 | 0.043 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.18 |  | 66.2307 | 2.9431 | 66.9 | 64.92 | 0.0293 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.985 |  | 201.4538 | 1.7529 | 203.41 | 197.98 | 0.0146 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 393.17 |  | 394.5909 | -0.3601 | 398.39 | 393.52 | 0.1933 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.585 |  | 331.9643 | -0.4155 | 334.98 | 331.295 | 0.0181 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 345.275 |  | 345.3286 | -0.0155 | 348.47 | 341.42 | 0.1072 | below_vwap | below_vwap |
| AMD | ai_accelerator | 490.71 |  | 474.6669 | 3.3799 | 482.43 | 461.04 | 1.2839 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 402.32 |  | 393.0482 | 2.359 | 394.11 | 386.02 | 2.4856 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 522.16 |  | 510.7821 | 2.2276 | 511.83 | 498.665 | 0.1302 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 558.42 |  | 548.9558 | 1.724 | 550 | 536.9 | 0.1218 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.095 |  | 367.0606 | 1.0991 | 368.42 | 357.97 | 1.951 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 871.5 |  | 839.5183 | 3.8095 | 835.82 | 804.09 | 1.774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.28 |  | 183.7787 | 2.9934 | 185.03 | 178.09 | 0.7766 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 395.47 |  | 382.8971 | 3.2836 | 384 | 368.28 | 4.5591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.015 |  | 44.8677 | 2.5572 | 44.92 | 43.715 | 0.0435 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.49 |  | 23.9427 | 2.2857 | 24.3 | 23.46 | 0.1225 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 746.67 |  | 743.6324 | 0.4085 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 295.775 |  | 293.8303 | 0.6619 | 294.205 | 291.675 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 125.71 |  | 124.2762 | 1.1537 | 125.02 | 121.79 | 3.5399 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 72.815 |  | 70.4878 | 3.3016 | 71.24 | 68.65 | 3.7904 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 287.815 |  | 280.8691 | 2.473 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 399.33 |  | 394.6787 | 1.1785 | 389.4 | 382.38 | 3.8815 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 630.21 |  | 619.7244 | 1.692 | 616.75 | 609.05 | 4.9285 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1051.2 |  | 1020.5938 | 2.9989 | 1001.82 | 982.21 | 1.4269 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.88 |  | 467.6875 | 0.6826 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.955 |  | 139.3673 | 1.1392 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.28 |  | 161.8743 | 2.7217 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.42 |  | 266.9866 | 3.5333 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 728.43 |  | 690.8511 | 5.4395 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 380.53 |  | 371.566 | 2.4125 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 101.4 |  | 96.1873 | 5.4193 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 308.23 |  | 299.7108 | 2.8425 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1746.415 |  | 1731.7368 | 0.8476 | 1741.99 | 1704.935 | 0.4237 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 536.12 |  | 526.3894 | 1.8486 | 535.095 | 513.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 312.76 |  | 305.0468 | 2.5285 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 213.315 |  | 209.9579 | 1.5989 | 210.82 | 204.71 | 0.2344 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 315.88 |  | 307.6703 | 2.6683 | 308.03 | 297.18 | 4.5302 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 269.61 |  | 265.2508 | 1.6434 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 61.32 |  | 59.7009 | 2.7119 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.85 |  | 48.3247 | 3.1564 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.43 |  | 131.8945 | 3.4387 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 319.21 |  | 313.6449 | 1.7743 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 521.05 |  | 522.2395 | -0.2278 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 301.96 |  | 302.0301 | -0.0232 | 304.36 | 299.62 | 4.5701 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.14 |  | 24.7399 | 1.6173 | 25.45 | 24.1 | 0.1193 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.22 |  | 33.3089 | 2.7352 | 34 | 32.26 | 0.0584 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 20.735 |  | 20.2303 | 2.4945 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1446.61 |  | 1392.9106 | 3.8552 | 1393.96 | 1325.48 | 4.1276 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 459.375 |  | 448.3758 | 2.4531 | 453.35 | 431.78 | 4.8239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 742.41 |  | 728.1406 | 1.9597 | 724.57 | 702.24 | 4.5271 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.22 |  | 246.9159 | 0.5281 | 247.72 | 243.725 | 0.0242 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 633.18 |  | 639.838 | -1.0406 | 649.07 | 638.97 | 0.278 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 265.36 |  | 252.1825 | 5.2254 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 158.27 |  | 154.0967 | 2.7083 | 151.99 | 145.6 | 2.2746 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
