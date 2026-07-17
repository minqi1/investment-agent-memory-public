# Intraday State

- Generated at: `2026-07-18T03:20:29+08:00`
- Market time ET: `2026-07-17T15:20:30-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 24, 'manual_confirm_candidate': 6, 'watch_only': 3, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.46 |  | 695.6438 | -0.0264 | 693.36 | 686.78 | 0.0144 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 520.41 |  | 518.6905 | 0.3315 | 511.83 | 498.665 | 0.0538 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 554.73 |  | 555.2071 | -0.0859 | 550 | 536.9 | 0.0775 | below_vwap | below_vwap |
| SPY | market_regime | 742.89 |  | 744.7997 | -0.2564 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 520.41 |  | 518.6905 | 0.3315 | 511.83 | 498.665 | 0.0538 | buy_precheck_manual_confirm | none |
| 2 | HPE | ai_server_oem | 46.01 |  | 45.7045 | 0.6685 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 3 | MRVL | custom_silicon_networking | 187.86 |  | 187.2631 | 0.3188 | 185.03 | 178.09 | 0.149 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.43 |  | 24.3221 | 0.4438 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.79 |  | 20.679 | 0.5366 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 67.51 |  | 67.2468 | 0.3913 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 520.41 |  | 518.6905 | 0.3315 | 511.83 | 498.665 | 0.0538 | buy_precheck_manual_confirm | none |
| 2 | MRVL | custom_silicon_networking | 187.86 |  | 187.2631 | 0.3188 | 185.03 | 178.09 | 0.149 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 394.73 |  | 393.5766 | 0.2931 | 398.39 | 393.52 | 0.0329 | watch_only | none |
| 4 | SMCI | ai_server_oem | 24.43 |  | 24.3221 | 0.4438 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 333.345 |  | 332.303 | 0.3136 | 334.98 | 331.295 | 0.042 | watch_only | none |
| 6 | HPE | ai_server_oem | 46.01 |  | 45.7045 | 0.6685 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | CORZ | high_beta_ai_infrastructure | 20.79 |  | 20.679 | 0.5366 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 8 | AVGO | custom_silicon_networking | 371.05 |  | 370.3986 | 0.1759 | 368.42 | 357.97 | 2.536 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APLD | high_beta_ai_infrastructure | 25.31 |  | 25.1035 | 0.8228 | 25.45 | 24.1 | 0.079 | watch_only | none |
| 10 | ETN | data_center_power_cooling | 400.055 |  | 399.7349 | 0.0801 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | META | cloud_ai_capex | 642.695 |  | 642.5742 | 0.0188 | 649.07 | 638.97 | 0.3781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | GEV | data_center_power_cooling | 1053.06 |  | 1045.7151 | 0.7024 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | QQQ | market_regime | 695.46 |  | 695.6438 | -0.0264 | 693.36 | 686.78 | 0.0144 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 742.89 |  | 744.7997 | -0.2564 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 15 | TER | semiconductor_test_packaging | 322.01 |  | 320.3156 | 0.529 | 308.03 | 297.18 | 4.3756 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | IWM | market_regime | 293.39 |  | 294.1146 | -0.2464 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| 17 | GOOGL | cloud_ai_capex | 345.2 |  | 345.7737 | -0.1659 | 348.47 | 341.42 | 0.0579 | below_vwap | below_vwap |
| 18 | AMZN | cloud_ai_capex | 247.47 |  | 247.9783 | -0.205 | 247.72 | 243.725 | 0.0929 | below_vwap | below_vwap |
| 19 | TT | data_center_power_cooling | 469.33 |  | 469.7243 | -0.0839 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | SMH | semiconductor_index | 554.73 |  | 555.2071 | -0.0859 | 550 | 536.9 | 0.0775 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SOXX | semiconductor_index | 520.41 |  | 518.6905 | 0.3315 | 511.83 | 498.665 | 0.0538 | buy_precheck_manual_confirm | none |
| 2 | HPE | ai_server_oem | 46.01 |  | 45.7045 | 0.6685 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 3 | MRVL | custom_silicon_networking | 187.86 |  | 187.2631 | 0.3188 | 185.03 | 178.09 | 0.149 | buy_precheck_manual_confirm | none |
| 4 | SMCI | ai_server_oem | 24.43 |  | 24.3221 | 0.4438 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| 5 | CORZ | high_beta_ai_infrastructure | 20.79 |  | 20.679 | 0.5366 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| 6 | TQQQ | leveraged_tool | 67.51 |  | 67.2468 | 0.3913 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 7 | TSM | foundry | 395.475 |  | 397.9118 | -0.6124 | 394.11 | 386.02 | 1.196 | below_vwap | below_vwap,spread_too_wide |
| 8 | SMH | semiconductor_index | 554.73 |  | 555.2071 | -0.0859 | 550 | 536.9 | 0.0775 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1750.4 |  | 1756.8852 | -0.3691 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | TT | data_center_power_cooling | 469.33 |  | 469.7243 | -0.0839 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | KLAC | semiconductor_equipment | 211.65 |  | 212.2086 | -0.2632 | 210.82 | 204.71 | 0.2882 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 862.96 |  | 864.6852 | -0.1995 | 835.82 | 804.09 | 0.6686 | below_vwap | below_vwap,spread_too_wide |
| 13 | CIEN | ai_networking_optical | 375.55 |  | 377.7144 | -0.573 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | PWR | data_center_power_cooling | 630.15 |  | 630.2982 | -0.0235 | 616.75 | 609.05 | 4.7846 | below_vwap | below_vwap,spread_too_wide |
| 15 | QQQ | market_regime | 695.46 |  | 695.6438 | -0.0264 | 693.36 | 686.78 | 0.0144 | below_vwap | below_vwap |
| 16 | LRCX | semiconductor_equipment | 310.31 |  | 312.0907 | -0.5706 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | SPY | market_regime | 742.89 |  | 744.7997 | -0.2564 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| 18 | ONTO | semiconductor_test_packaging | 277.44 |  | 277.7212 | -0.1012 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | SNDK | memory_hbm_storage | 1405.44 |  | 1427.4014 | -1.5386 | 1393.96 | 1325.48 | 3.7661 | below_vwap | below_vwap,spread_too_wide |
| 20 | SKHY | memory_hbm_storage | 155.14 |  | 158.9026 | -2.3679 | 151.99 | 145.6 | 0.4834 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.46 |  | 695.6438 | -0.0264 | 693.36 | 686.78 | 0.0144 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 67.51 |  | 67.2468 | 0.3913 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.23 |  | 203.1942 | -0.4745 | 203.41 | 197.98 | 0.895 | below_vwap | below_vwap,spread_too_wide |
| MSFT | cloud_ai_capex | 394.73 |  | 393.5766 | 0.2931 | 398.39 | 393.52 | 0.0329 | watch_only | none |
| AAPL | mega_cap_platform | 333.345 |  | 332.303 | 0.3136 | 334.98 | 331.295 | 0.042 | watch_only | none |
| GOOGL | cloud_ai_capex | 345.2 |  | 345.7737 | -0.1659 | 348.47 | 341.42 | 0.0579 | below_vwap | below_vwap |
| AMD | ai_accelerator | 493.46 |  | 487.1074 | 1.3041 | 482.43 | 461.04 | 2.8108 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 395.475 |  | 397.9118 | -0.6124 | 394.11 | 386.02 | 1.196 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 520.41 |  | 518.6905 | 0.3315 | 511.83 | 498.665 | 0.0538 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 554.73 |  | 555.2071 | -0.0859 | 550 | 536.9 | 0.0775 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 371.05 |  | 370.3986 | 0.1759 | 368.42 | 357.97 | 2.536 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 862.96 |  | 864.6852 | -0.1995 | 835.82 | 804.09 | 0.6686 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.86 |  | 187.2631 | 0.3188 | 185.03 | 178.09 | 0.149 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 398.38 |  | 393.5143 | 1.2365 | 384 | 368.28 | 1.973 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.01 |  | 45.7045 | 0.6685 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.43 |  | 24.3221 | 0.4438 | 24.3 | 23.46 | 0.0409 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.89 |  | 744.7997 | -0.2564 | 742.66 | 740.8 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 293.39 |  | 294.1146 | -0.2464 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.91 |  | 126.0345 | -0.0988 | 125.02 | 121.79 | 1.7155 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.88 |  | 72.2821 | 0.8272 | 71.24 | 68.65 | 4.528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.85 |  | 287.6212 | 1.1226 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 400.055 |  | 399.7349 | 0.0801 | 389.4 | 382.38 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 630.15 |  | 630.2982 | -0.0235 | 616.75 | 609.05 | 4.7846 | below_vwap | below_vwap,spread_too_wide |
| GEV | data_center_power_cooling | 1053.06 |  | 1045.7151 | 0.7024 | 1001.82 | 982.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 469.33 |  | 469.7243 | -0.0839 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.71 |  | 140.9252 | -0.1527 | 140.765 | 137.165 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.89 |  | 166.3281 | 0.939 | 163.275 | 157.34 | 4.366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 278.035 |  | 274.2378 | 1.3846 | 269.59 | 256.24 | 2.7479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 735.105 |  | 719.1672 | 2.2161 | 694.98 | 653.305 | 2.2963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.55 |  | 377.7144 | -0.573 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.39 |  | 100.6622 | 1.7164 | 97.585 | 91.92 | 4.0824 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 299.71 |  | 304.7169 | -1.6431 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1750.4 |  | 1756.8852 | -0.3691 | 1741.99 | 1704.935 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 528.05 |  | 534.3558 | -1.1801 | 535.095 | 513.34 | 0.5833 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 310.31 |  | 312.0907 | -0.5706 | 306.51 | 298.89 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 211.65 |  | 212.2086 | -0.2632 | 210.82 | 204.71 | 0.2882 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.01 |  | 320.3156 | 0.529 | 308.03 | 297.18 | 4.3756 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 277.44 |  | 277.7212 | -0.1012 | 265.71 | 258.355 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.215 |  | 61.6137 | 0.9759 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.78 |  | 49.9788 | 1.6031 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.32 |  | 135.1443 | 0.87 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 323.71 |  | 319.1772 | 1.4201 | 315.89 | 307.13 | 4.0407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.54 |  | 518.502 | -0.957 | 526.74 | 522.205 | 3.6784 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 295.86 |  | 298.7852 | -0.979 | 304.36 | 299.62 | 4.6407 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.31 |  | 25.1035 | 0.8228 | 25.45 | 24.1 | 0.079 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.435 |  | 33.7644 | -0.9756 | 34 | 32.26 | 0.0299 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.79 |  | 20.679 | 0.5366 | 20.445 | 19.92 | 0.0962 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1405.44 |  | 1427.4014 | -1.5386 | 1393.96 | 1325.48 | 3.7661 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 479.37 |  | 467.8136 | 2.4703 | 453.35 | 431.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 789.655 |  | 764.7922 | 3.2509 | 724.57 | 702.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 247.47 |  | 247.9783 | -0.205 | 247.72 | 243.725 | 0.0929 | below_vwap | below_vwap |
| META | cloud_ai_capex | 642.695 |  | 642.5742 | 0.0188 | 649.07 | 638.97 | 0.3781 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.47 |  | 261.564 | 1.8757 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 155.14 |  | 158.9026 | -2.3679 | 151.99 | 145.6 | 0.4834 | below_vwap | below_vwap,spread_too_wide |
