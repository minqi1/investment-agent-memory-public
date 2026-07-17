# Intraday State

- Generated at: `2026-07-18T00:22:54+08:00`
- Market time ET: `2026-07-17T12:22:55-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 14, 'below_opening_15m_low': 4, 'watch_only': 3, 'spread_too_wide_or_missing': 32, 'price_stale_or_missing': 2, 'below_vwap': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.715 |  | 693.9151 | 0.6917 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 526.72 |  | 515.1974 | 2.2365 | 511.83 | 498.665 | 0.1044 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.12 |  | 551.6513 | 1.7164 | 550 | 536.9 | 0.0392 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.82 |  | 744.6866 | 0.1522 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.645 |  | 202.587 | 1.0158 | 203.41 | 197.98 | 0.3421 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 401.56 |  | 396.4567 | 1.2872 | 394.11 | 386.02 | 0.1693 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 561.12 |  | 551.6513 | 1.7164 | 550 | 536.9 | 0.0392 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 526.72 |  | 515.1974 | 2.2365 | 511.83 | 498.665 | 0.1044 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 214.29 |  | 211.1492 | 1.4875 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 294.34 |  | 294.0389 | 0.1024 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ETN | data_center_power_cooling | 401.85 |  | 398.734 | 0.7815 | 389.4 | 382.38 | 0.1194 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 698.715 |  | 693.9151 | 0.6917 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 45.92 |  | 45.3828 | 1.1837 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| 10 | SPY | market_regime | 745.82 |  | 744.6866 | 0.1522 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.18 |  | 247.8866 | 0.1184 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.495 |  | 24.0831 | 1.7105 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.72 |  | 20.5117 | 1.0156 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.45 |  | 66.8685 | 2.3652 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 294.34 |  | 294.0389 | 0.1024 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 248.18 |  | 247.8866 | 0.1184 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 745.82 |  | 744.6866 | 0.1522 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 698.715 |  | 693.9151 | 0.6917 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 346.945 |  | 346.1026 | 0.2434 | 348.47 | 341.42 | 0.245 | watch_only | none |
| 6 | ETN | data_center_power_cooling | 401.85 |  | 398.734 | 0.7815 | 389.4 | 382.38 | 0.1194 | buy_precheck_manual_confirm | none |
| 7 | IREN | high_beta_ai_infrastructure | 33.675 |  | 33.5152 | 0.4767 | 34 | 32.26 | 0.0594 | watch_only | none |
| 8 | NVDA | ai_accelerator | 204.645 |  | 202.587 | 1.0158 | 203.41 | 197.98 | 0.3421 | buy_precheck_manual_confirm | none |
| 9 | CORZ | high_beta_ai_infrastructure | 20.72 |  | 20.5117 | 1.0156 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| 10 | HPE | ai_server_oem | 45.92 |  | 45.3828 | 1.1837 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| 11 | TSM | foundry | 401.56 |  | 396.4567 | 1.2872 | 394.11 | 386.02 | 0.1693 | buy_precheck_manual_confirm | none |
| 12 | KLAC | semiconductor_equipment | 214.29 |  | 211.1492 | 1.4875 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| 13 | APLD | high_beta_ai_infrastructure | 25.19 |  | 24.8872 | 1.2169 | 25.45 | 24.1 | 0.0794 | watch_only | none |
| 14 | SMCI | ai_server_oem | 24.495 |  | 24.0831 | 1.7105 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 15 | SMH | semiconductor_index | 561.12 |  | 551.6513 | 1.7164 | 550 | 536.9 | 0.0392 | buy_precheck_manual_confirm | none |
| 16 | SOXX | semiconductor_index | 526.72 |  | 515.1974 | 2.2365 | 511.83 | 498.665 | 0.1044 | buy_precheck_manual_confirm | none |
| 17 | ALAB | ai_networking_optical | 304.72 |  | 301.7843 | 0.9728 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 635.74 |  | 627.1912 | 1.363 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | META | cloud_ai_capex | 643.435 |  | 636.9372 | 1.0202 | 649.07 | 638.97 | 2.698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 204.645 |  | 202.587 | 1.0158 | 203.41 | 197.98 | 0.3421 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 401.56 |  | 396.4567 | 1.2872 | 394.11 | 386.02 | 0.1693 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 561.12 |  | 551.6513 | 1.7164 | 550 | 536.9 | 0.0392 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 526.72 |  | 515.1974 | 2.2365 | 511.83 | 498.665 | 0.1044 | buy_precheck_manual_confirm | none |
| 5 | KLAC | semiconductor_equipment | 214.29 |  | 211.1492 | 1.4875 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| 6 | IWM | market_regime | 294.34 |  | 294.0389 | 0.1024 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| 7 | ETN | data_center_power_cooling | 401.85 |  | 398.734 | 0.7815 | 389.4 | 382.38 | 0.1194 | buy_precheck_manual_confirm | none |
| 8 | QQQ | market_regime | 698.715 |  | 693.9151 | 0.6917 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 45.92 |  | 45.3828 | 1.1837 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| 10 | SPY | market_regime | 745.82 |  | 744.6866 | 0.1522 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| 11 | AMZN | cloud_ai_capex | 248.18 |  | 247.8866 | 0.1184 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| 12 | SMCI | ai_server_oem | 24.495 |  | 24.0831 | 1.7105 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 13 | CORZ | high_beta_ai_infrastructure | 20.72 |  | 20.5117 | 1.0156 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| 14 | TQQQ | leveraged_tool | 68.45 |  | 66.8685 | 2.3652 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| 15 | ANET | ai_networking_optical | 167.825 |  | 163.7791 | 2.4703 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | AVGO | custom_silicon_networking | 371.995 |  | 368.3619 | 0.9863 | 368.42 | 357.97 | 1.207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | AMAT | semiconductor_equipment | 545.23 |  | 531.0644 | 2.6674 | 535.095 | 513.34 | 0.8859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 501.32 |  | 483.0789 | 3.776 | 482.43 | 461.04 | 0.8418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1780.88 |  | 1744.9856 | 2.057 | 1741.99 | 1704.935 | 0.8771 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 473.34 |  | 469.3047 | 0.8598 | 469.08 | 460.78 | 3.619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 698.715 |  | 693.9151 | 0.6917 | 693.36 | 686.78 | 0.0315 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 68.45 |  | 66.8685 | 2.3652 | 66.9 | 64.92 | 0.0292 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 204.645 |  | 202.587 | 1.0158 | 203.41 | 197.98 | 0.3421 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 392.41 |  | 392.9558 | -0.1389 | 398.39 | 393.52 | 0.0714 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 330.785 |  | 332.3207 | -0.4621 | 334.98 | 331.295 | 0.2237 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.945 |  | 346.1026 | 0.2434 | 348.47 | 341.42 | 0.245 | watch_only | none |
| AMD | ai_accelerator | 501.32 |  | 483.0789 | 3.776 | 482.43 | 461.04 | 0.8418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 401.56 |  | 396.4567 | 1.2872 | 394.11 | 386.02 | 0.1693 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.72 |  | 515.1974 | 2.2365 | 511.83 | 498.665 | 0.1044 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 561.12 |  | 551.6513 | 1.7164 | 550 | 536.9 | 0.0392 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 371.995 |  | 368.3619 | 0.9863 | 368.42 | 357.97 | 1.207 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 880.98 |  | 854.5767 | 3.0896 | 835.82 | 804.09 | 2.1499 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 189.66 |  | 185.1937 | 2.4117 | 185.03 | 178.09 | 0.9438 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 395.01 |  | 388.3511 | 1.7146 | 384 | 368.28 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.92 |  | 45.3828 | 1.1837 | 44.92 | 43.715 | 0.0436 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.495 |  | 24.0831 | 1.7105 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 745.82 |  | 744.6866 | 0.1522 | 742.66 | 740.8 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.34 |  | 294.0389 | 0.1024 | 294.205 | 291.675 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 127.24 |  | 125.2848 | 1.5606 | 125.02 | 121.79 | 0.723 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 72.695 |  | 71.7806 | 1.2738 | 71.24 | 68.65 | 1.9121 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 294.02 |  | 283.8451 | 3.5847 | 280.565 | 273.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 401.85 |  | 398.734 | 0.7815 | 389.4 | 382.38 | 0.1194 | buy_precheck_manual_confirm | none |
| PWR | data_center_power_cooling | 635.74 |  | 627.1912 | 1.363 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1057.05 |  | 1039.4512 | 1.6931 | 1001.82 | 982.21 | 2.8646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 473.34 |  | 469.3047 | 0.8598 | 469.08 | 460.78 | 3.619 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 142.29 |  | 140.7127 | 1.121 | 140.765 | 137.165 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ANET | ai_networking_optical | 167.825 |  | 163.7791 | 2.4703 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 280.925 |  | 271.5176 | 3.4648 | 269.59 | 256.24 | 4.9586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 728.91 |  | 705.2001 | 3.3622 | 694.98 | 653.305 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 381.585 |  | 374.6903 | 1.8401 | 375.52 | 359.81 | 4.8141 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 102.01 |  | 98.9049 | 3.1395 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 304.72 |  | 301.7843 | 0.9728 | 305.21 | 289.97 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1780.88 |  | 1744.9856 | 2.057 | 1741.99 | 1704.935 | 0.8771 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 545.23 |  | 531.0644 | 2.6674 | 535.095 | 513.34 | 0.8859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 319.45 |  | 310.199 | 2.9823 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 214.29 |  | 211.1492 | 1.4875 | 210.82 | 204.71 | 0.1727 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 322.86 |  | 311.3867 | 3.6846 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 280.75 |  | 270.7492 | 3.6937 | 265.71 | 258.355 | 0.5129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 62.575 |  | 60.8462 | 2.8412 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.685 |  | 49.4428 | 2.5125 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 137.84 |  | 133.4181 | 3.3143 | 129.93 | 126.945 | 4.2368 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 325.34 |  | 316.4118 | 2.8217 | 315.89 | 307.13 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 516.77 |  | 521.3026 | -0.8695 | 526.74 | 522.205 | 4.2959 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 298.3 |  | 301.0459 | -0.9121 | 304.36 | 299.62 | 3.2853 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.19 |  | 24.8872 | 1.2169 | 25.45 | 24.1 | 0.0794 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.675 |  | 33.5152 | 0.4767 | 34 | 32.26 | 0.0594 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.72 |  | 20.5117 | 1.0156 | 20.445 | 19.92 | 0.0965 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1473.39 |  | 1416.6953 | 4.0019 | 1393.96 | 1325.48 | 3.3935 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 478.11 |  | 455.8779 | 4.8768 | 453.35 | 431.78 | 1.6377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 778.74 |  | 744.4166 | 4.6108 | 724.57 | 702.24 | 0.4045 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.18 |  | 247.8866 | 0.1184 | 247.72 | 243.725 | 0.0282 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 643.435 |  | 636.9372 | 1.0202 | 649.07 | 638.97 | 2.698 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 266.4 |  | 256.9534 | 3.6764 | 252.95 | 243.21 | 4.6997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 163.695 |  | 156.8487 | 4.3649 | 151.99 | 145.6 | 0.9163 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
