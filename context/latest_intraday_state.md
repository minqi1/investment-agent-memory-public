# Intraday State

- Generated at: `2026-07-18T03:12:26+08:00`
- Market time ET: `2026-07-17T15:12:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 12, 'below_vwap': 22, 'watch_only': 2, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 1, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.96 |  | 695.6564 | 0.0436 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 520.57 |  | 518.6728 | 0.3658 | 511.83 | 498.665 | 0.0672 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.09 |  | 555.227 | -0.0247 | 550 | 536.9 | 0.0432 | below_vwap | below_vwap |
| SPY | market_regime | 743.16 |  | 744.8525 | -0.2272 | 742.66 | 740.8 | 0.0067 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 168.15 |  | 166.2872 | 1.1202 | 163.275 | 157.34 | 0.1963 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 520.57 |  | 518.6728 | 0.3658 | 511.83 | 498.665 | 0.0672 | buy_precheck_manual_confirm | none |
| 3 | MU | memory_hbm_storage | 864.81 |  | 864.7164 | 0.0108 | 835.82 | 804.09 | 0.1156 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1051.98 |  | 1045.547 | 0.6153 | 1001.82 | 982.21 | 0.307 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 695.96 |  | 695.6564 | 0.0436 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.08 |  | 45.7001 | 0.8312 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | STX | memory_hbm_storage | 787.455 |  | 763.6162 | 3.1218 | 724.57 | 702.24 | 0.1283 | buy_precheck_manual_confirm | none |
| 8 | WDC | memory_hbm_storage | 479.81 |  | 467.6225 | 2.6063 | 453.35 | 431.78 | 0.2918 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 188.1 |  | 187.259 | 0.4491 | 185.03 | 178.09 | 0.101 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.53 |  | 24.3208 | 0.86 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6759 | 1.1807 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.65 |  | 67.2443 | 0.6033 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 695.96 |  | 695.6564 | 0.0436 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 864.81 |  | 864.7164 | 0.0108 | 835.82 | 804.09 | 0.1156 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 394.755 |  | 393.532 | 0.3108 | 398.39 | 393.52 | 0.0532 | watch_only | none |
| 4 | SOXX | semiconductor_index | 520.57 |  | 518.6728 | 0.3658 | 511.83 | 498.665 | 0.0672 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 188.1 |  | 187.259 | 0.4491 | 185.03 | 178.09 | 0.101 | buy_precheck_manual_confirm | none |
| 6 | GEV | data_center_power_cooling | 1051.98 |  | 1045.547 | 0.6153 | 1001.82 | 982.21 | 0.307 | buy_precheck_manual_confirm | none |
| 7 | APLD | high_beta_ai_infrastructure | 25.275 |  | 25.0995 | 0.6991 | 25.45 | 24.1 | 0.0791 | watch_only | none |
| 8 | SMCI | ai_server_oem | 24.53 |  | 24.3208 | 0.86 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 9 | HPE | ai_server_oem | 46.08 |  | 45.7001 | 0.8312 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 10 | ANET | ai_networking_optical | 168.15 |  | 166.2872 | 1.1202 | 163.275 | 157.34 | 0.1963 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6759 | 1.1807 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| 12 | PWR | data_center_power_cooling | 631.42 |  | 630.3071 | 0.1766 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ONTO | semiconductor_test_packaging | 277.82 |  | 277.7683 | 0.0186 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | STX | memory_hbm_storage | 787.455 |  | 763.6162 | 3.1218 | 724.57 | 702.24 | 0.1283 | buy_precheck_manual_confirm | none |
| 15 | AVGO | custom_silicon_networking | 371.755 |  | 370.3887 | 0.3689 | 368.42 | 357.97 | 2.5528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AAPL | mega_cap_platform | 334.225 |  | 332.2584 | 0.5919 | 334.98 | 331.295 | 0.8647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | TER | semiconductor_test_packaging | 322.26 |  | 320.2987 | 0.6123 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 479.81 |  | 467.6225 | 2.6063 | 453.35 | 431.78 | 0.2918 | buy_precheck_manual_confirm | none |
| 19 | TSM | foundry | 395.22 |  | 397.9749 | -0.6922 | 394.11 | 386.02 | 0.0734 | below_vwap | below_vwap |
| 20 | SPY | market_regime | 743.16 |  | 744.8525 | -0.2272 | 742.66 | 740.8 | 0.0067 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 168.15 |  | 166.2872 | 1.1202 | 163.275 | 157.34 | 0.1963 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 520.57 |  | 518.6728 | 0.3658 | 511.83 | 498.665 | 0.0672 | buy_precheck_manual_confirm | none |
| 3 | MU | memory_hbm_storage | 864.81 |  | 864.7164 | 0.0108 | 835.82 | 804.09 | 0.1156 | buy_precheck_manual_confirm | none |
| 4 | GEV | data_center_power_cooling | 1051.98 |  | 1045.547 | 0.6153 | 1001.82 | 982.21 | 0.307 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 695.96 |  | 695.6564 | 0.0436 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| 6 | HPE | ai_server_oem | 46.08 |  | 45.7001 | 0.8312 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| 7 | STX | memory_hbm_storage | 787.455 |  | 763.6162 | 3.1218 | 724.57 | 702.24 | 0.1283 | buy_precheck_manual_confirm | none |
| 8 | WDC | memory_hbm_storage | 479.81 |  | 467.6225 | 2.6063 | 453.35 | 431.78 | 0.2918 | buy_precheck_manual_confirm | none |
| 9 | MRVL | custom_silicon_networking | 188.1 |  | 187.259 | 0.4491 | 185.03 | 178.09 | 0.101 | buy_precheck_manual_confirm | none |
| 10 | SMCI | ai_server_oem | 24.53 |  | 24.3208 | 0.86 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6759 | 1.1807 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| 12 | TQQQ | leveraged_tool | 67.65 |  | 67.2443 | 0.6033 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| 13 | TSM | foundry | 395.22 |  | 397.9749 | -0.6922 | 394.11 | 386.02 | 0.0734 | below_vwap | below_vwap |
| 14 | SMH | semiconductor_index | 555.09 |  | 555.227 | -0.0247 | 550 | 536.9 | 0.0432 | below_vwap | below_vwap |
| 15 | ASML | semiconductor_equipment | 1753.43 |  | 1757.1273 | -0.2104 | 1741.99 | 1704.935 | 0.5737 | below_vwap | below_vwap,spread_too_wide |
| 16 | KLAC | semiconductor_equipment | 212.01 |  | 212.2413 | -0.109 | 210.82 | 204.71 | 0.1415 | below_vwap | below_vwap |
| 17 | CIEN | ai_networking_optical | 375.72 |  | 377.7651 | -0.5414 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 398.77 |  | 399.7355 | -0.2415 | 389.4 | 382.38 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 310.91 |  | 312.1273 | -0.39 | 306.51 | 298.89 | 3.9047 | below_vwap | below_vwap,spread_too_wide |
| 20 | SPY | market_regime | 743.16 |  | 744.8525 | -0.2272 | 742.66 | 740.8 | 0.0067 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 695.96 |  | 695.6564 | 0.0436 | 693.36 | 686.78 | 0.0029 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67.65 |  | 67.2443 | 0.6033 | 66.9 | 64.92 | 0.0148 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 202.5 |  | 203.232 | -0.3602 | 203.41 | 197.98 | 0.0099 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 394.755 |  | 393.532 | 0.3108 | 398.39 | 393.52 | 0.0532 | watch_only | none |
| AAPL | mega_cap_platform | 334.225 |  | 332.2584 | 0.5919 | 334.98 | 331.295 | 0.8647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 345.24 |  | 345.7824 | -0.1569 | 348.47 | 341.42 | 0.0406 | below_vwap | below_vwap |
| AMD | ai_accelerator | 494.17 |  | 487.0174 | 1.4686 | 482.43 | 461.04 | 2.7319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 395.22 |  | 397.9749 | -0.6922 | 394.11 | 386.02 | 0.0734 | below_vwap | below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 520.57 |  | 518.6728 | 0.3658 | 511.83 | 498.665 | 0.0672 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 555.09 |  | 555.227 | -0.0247 | 550 | 536.9 | 0.0432 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 371.755 |  | 370.3887 | 0.3689 | 368.42 | 357.97 | 2.5528 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 864.81 |  | 864.7164 | 0.0108 | 835.82 | 804.09 | 0.1156 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 188.1 |  | 187.259 | 0.4491 | 185.03 | 178.09 | 0.101 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 399.875 |  | 393.4079 | 1.6439 | 384 | 368.28 | 0.5377 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 46.08 |  | 45.7001 | 0.8312 | 44.92 | 43.715 | 0.0217 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 24.53 |  | 24.3208 | 0.86 | 24.3 | 23.46 | 0.0408 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 743.16 |  | 744.8525 | -0.2272 | 742.66 | 740.8 | 0.0067 | below_vwap | below_vwap |
| IWM | market_regime | 293.32 |  | 294.1396 | -0.2786 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.865 |  | 126.0382 | -0.1374 | 125.02 | 121.79 | 1.6446 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.115 |  | 72.2742 | 1.1633 | 71.24 | 68.65 | 2.5029 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 290.455 |  | 287.5812 | 0.9993 | 280.565 | 273.17 | 4.0591 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 398.77 |  | 399.7355 | -0.2415 | 389.4 | 382.38 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 631.42 |  | 630.3071 | 0.1766 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1051.98 |  | 1045.547 | 0.6153 | 1001.82 | 982.21 | 0.307 | buy_precheck_manual_confirm | none |
| TT | data_center_power_cooling | 468.3 |  | 469.7264 | -0.3037 | 469.08 | 460.78 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 140.705 |  | 140.9273 | -0.1578 | 140.765 | 137.165 | 0.0497 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 168.15 |  | 166.2872 | 1.1202 | 163.275 | 157.34 | 0.1963 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 277.02 |  | 274.1789 | 1.0362 | 269.59 | 256.24 | 4.8552 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 735.86 |  | 718.9021 | 2.3589 | 694.98 | 653.305 | 1.4242 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.72 |  | 377.7651 | -0.5414 | 375.52 | 359.81 |  | below_vwap | below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 102.01 |  | 100.6259 | 1.3755 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 299.91 |  | 304.8261 | -1.6128 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1753.43 |  | 1757.1273 | -0.2104 | 1741.99 | 1704.935 | 0.5737 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 529.04 |  | 534.8652 | -1.0891 | 535.095 | 513.34 | 2.2512 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 310.91 |  | 312.1273 | -0.39 | 306.51 | 298.89 | 3.9047 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 212.01 |  | 212.2413 | -0.109 | 210.82 | 204.71 | 0.1415 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.26 |  | 320.2987 | 0.6123 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 277.82 |  | 277.7683 | 0.0186 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.2 |  | 61.5998 | 0.9744 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.84 |  | 49.9621 | 1.7571 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.41 |  | 134.9975 | 1.0463 | 129.93 | 126.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 323.78 |  | 319.0954 | 1.4681 | 315.89 | 307.13 | 4.3054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 513.57 |  | 518.647 | -0.9789 | 526.74 | 522.205 | 3.6976 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 295.81 |  | 298.8442 | -1.0153 | 304.36 | 299.62 | 4.6719 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 25.275 |  | 25.0995 | 0.6991 | 25.45 | 24.1 | 0.0791 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 33.405 |  | 33.7787 | -1.1063 | 34 | 32.26 | 0.0299 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.92 |  | 20.6759 | 1.1807 | 20.445 | 19.92 | 0.0956 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1415.02 |  | 1427.7043 | -0.8884 | 1393.96 | 1325.48 | 3.3371 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 479.81 |  | 467.6225 | 2.6063 | 453.35 | 431.78 | 0.2918 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 787.455 |  | 763.6162 | 3.1218 | 724.57 | 702.24 | 0.1283 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 247.46 |  | 247.9864 | -0.2123 | 247.72 | 243.725 | 0.0202 | below_vwap | below_vwap |
| META | cloud_ai_capex | 642.225 |  | 642.5803 | -0.0553 | 649.07 | 638.97 | 0.4531 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 266.26 |  | 261.4635 | 1.8345 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 155.615 |  | 158.96 | -2.1043 | 151.99 | 145.6 | 3.4315 | below_vwap | below_vwap,spread_too_wide |
