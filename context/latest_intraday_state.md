# Intraday State

- Generated at: `2026-07-28T22:52:31+08:00`
- Market time ET: `2026-07-28T10:52:32-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 13, 'manual_confirm_candidate': 3, 'spread_too_wide_or_missing': 25, 'below_vwap': 4, 'price_stale_or_missing': 1, 'below_opening_15m_low': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 674.67 |  | 671.409 | 0.4857 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.8 |  | 488.0755 | 0.7631 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| SMH | semiconductor_index | 530.005 |  | 525.1715 | 0.9204 | 533.01 | 523.325 | 0.0943 | watch_only | none |
| SPY | market_regime | 739.7 |  | 737.724 | 0.2678 | 739.42 | 736.57 | 0.0095 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.4 |  | 194.3911 | 1.5478 | 195.4 | 193.65 | 0.0355 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.21 |  | 375.5797 | 1.2328 | 378.64 | 371.57 | 0.0815 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 739.7 |  | 737.724 | 0.2678 | 739.42 | 736.57 | 0.0095 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 739.7 |  | 737.724 | 0.2678 | 739.42 | 736.57 | 0.0095 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 292.005 |  | 291.6185 | 0.1325 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| 3 | SOXX | semiconductor_index | 491.8 |  | 488.0755 | 0.7631 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| 4 | QQQ | market_regime | 674.67 |  | 671.409 | 0.4857 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 328.51 |  | 327.2703 | 0.3788 | 330.21 | 324.97 | 0.0365 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 380.21 |  | 375.5797 | 1.2328 | 378.64 | 371.57 | 0.0815 | buy_precheck_manual_confirm | none |
| 7 | ETN | data_center_power_cooling | 380.29 |  | 378.5148 | 0.469 | 384.565 | 377.43 | 0.2919 | watch_only | none |
| 8 | SMH | semiconductor_index | 530.005 |  | 525.1715 | 0.9204 | 533.01 | 523.325 | 0.0943 | watch_only | none |
| 9 | COHU | semiconductor_test_packaging | 42.79 |  | 42.6504 | 0.3274 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | SMCI | ai_server_oem | 28.04 |  | 27.6588 | 1.3783 | 28.86 | 27.59 | 0.0357 | watch_only | none |
| 11 | CORZ | high_beta_ai_infrastructure | 20.11 |  | 19.9392 | 0.8567 | 20.97 | 19.755 | 0.0995 | watch_only | none |
| 12 | NVDA | ai_accelerator | 197.4 |  | 194.3911 | 1.5478 | 195.4 | 193.65 | 0.0355 | buy_precheck_manual_confirm | none |
| 13 | TT | data_center_power_cooling | 466.25 |  | 464.0429 | 0.4756 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 138.51 |  | 137.7866 | 0.525 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | HPE | ai_server_oem | 44.56 |  | 44.1106 | 1.0187 | 46.19 | 44.33 | 0.1795 | watch_only | none |
| 16 | AMD | ai_accelerator | 454.28 |  | 452.9065 | 0.3033 | 472.485 | 453.76 | 0.8761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ALAB | ai_networking_optical | 256.95 |  | 255.2836 | 0.6528 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ARM | ai_accelerator | 245.815 |  | 244.5821 | 0.5041 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | APLD | high_beta_ai_infrastructure | 26.515 |  | 26.3039 | 0.8025 | 27 | 25.42 | 0.1509 | watch_only | none |
| 20 | TSM | foundry | 387.47 |  | 384.6537 | 0.7322 | 390.46 | 382.495 | 1.8711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.4 |  | 194.3911 | 1.5478 | 195.4 | 193.65 | 0.0355 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.21 |  | 375.5797 | 1.2328 | 378.64 | 371.57 | 0.0815 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 739.7 |  | 737.724 | 0.2678 | 739.42 | 736.57 | 0.0095 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 117.68 |  | 115.8077 | 1.6167 | 117.17 | 115.25 | 1.8525 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | SMH | semiconductor_index | 530.005 |  | 525.1715 | 0.9204 | 533.01 | 523.325 | 0.0943 | watch_only | none |
| 6 | SOXX | semiconductor_index | 491.8 |  | 488.0755 | 0.7631 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| 7 | ENTG | semiconductor_materials | 121.32 |  | 119.0998 | 1.8641 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | QQQ | market_regime | 674.67 |  | 671.409 | 0.4857 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 9 | GOOGL | cloud_ai_capex | 328.51 |  | 327.2703 | 0.3788 | 330.21 | 324.97 | 0.0365 | watch_only | none |
| 10 | ETN | data_center_power_cooling | 380.29 |  | 378.5148 | 0.469 | 384.565 | 377.43 | 0.2919 | watch_only | none |
| 11 | IWM | market_regime | 292.005 |  | 291.6185 | 0.1325 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| 12 | HPE | ai_server_oem | 44.56 |  | 44.1106 | 1.0187 | 46.19 | 44.33 | 0.1795 | watch_only | none |
| 13 | MRVL | custom_silicon_networking | 174.835 |  | 171.7194 | 1.8143 | 181.24 | 172.395 | 0.2974 | watch_only | none |
| 14 | SMCI | ai_server_oem | 28.04 |  | 27.6588 | 1.3783 | 28.86 | 27.59 | 0.0357 | watch_only | none |
| 15 | IREN | high_beta_ai_infrastructure | 34.135 |  | 33.2925 | 2.5308 | 35.08 | 33.52 | 0.0586 | watch_only | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.11 |  | 19.9392 | 0.8567 | 20.97 | 19.755 | 0.0995 | watch_only | none |
| 17 | APLD | high_beta_ai_infrastructure | 26.515 |  | 26.3039 | 0.8025 | 27 | 25.42 | 0.1509 | watch_only | none |
| 18 | TQQQ | leveraged_tool | 61.29 |  | 60.4069 | 1.4619 | 62.01 | 60.23 | 0.0163 | watch_only | none |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | LIN | industrial_gases | 518.16 |  | 518.6865 | -0.1015 | 518.6 | 511.495 | 4.3963 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 674.67 |  | 671.409 | 0.4857 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.29 |  | 60.4069 | 1.4619 | 62.01 | 60.23 | 0.0163 | watch_only | none |
| NVDA | ai_accelerator | 197.4 |  | 194.3911 | 1.5478 | 195.4 | 193.65 | 0.0355 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 396.86 |  | 394.8478 | 0.5096 | 400.09 | 392.355 | 0.6123 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 338.155 |  | 338.5929 | -0.1293 | 342.87 | 337.78 | 0.0148 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 328.51 |  | 327.2703 | 0.3788 | 330.21 | 324.97 | 0.0365 | watch_only | none |
| AMD | ai_accelerator | 454.28 |  | 452.9065 | 0.3033 | 472.485 | 453.76 | 0.8761 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 387.47 |  | 384.6537 | 0.7322 | 390.46 | 382.495 | 1.8711 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.8 |  | 488.0755 | 0.7631 | 497.64 | 485.42 | 0.0732 | watch_only | none |
| SMH | semiconductor_index | 530.005 |  | 525.1715 | 0.9204 | 533.01 | 523.325 | 0.0943 | watch_only | none |
| AVGO | custom_silicon_networking | 380.21 |  | 375.5797 | 1.2328 | 378.64 | 371.57 | 0.0815 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 823.44 |  | 811.3386 | 1.4915 | 846.4 | 813.91 | 0.5489 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 174.835 |  | 171.7194 | 1.8143 | 181.24 | 172.395 | 0.2974 | watch_only | none |
| DELL | ai_server_oem | 374.89 |  | 370.655 | 1.1426 | 402 | 374.02 | 4.3693 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.56 |  | 44.1106 | 1.0187 | 46.19 | 44.33 | 0.1795 | watch_only | none |
| SMCI | ai_server_oem | 28.04 |  | 27.6588 | 1.3783 | 28.86 | 27.59 | 0.0357 | watch_only | none |
| SPY | market_regime | 739.7 |  | 737.724 | 0.2678 | 739.42 | 736.57 | 0.0095 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.005 |  | 291.6185 | 0.1325 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| ORCL | cloud_ai_capex | 117.68 |  | 115.8077 | 1.6167 | 117.17 | 115.25 | 1.8525 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.34 |  | 65.8646 | 0.7218 | 68.995 | 65.635 | 4.8538 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.56 |  | 265.5967 | -0.0138 | 273.86 | 266.04 | 1.3745 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 380.29 |  | 378.5148 | 0.469 | 384.565 | 377.43 | 0.2919 | watch_only | none |
| PWR | data_center_power_cooling | 579.1 |  | 578.7873 | 0.054 | 603.25 | 584.69 | 0.5491 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| GEV | data_center_power_cooling | 935.485 |  | 933.0398 | 0.2621 | 955.825 | 935.665 | 1.8076 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 466.25 |  | 464.0429 | 0.4756 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 138.51 |  | 137.7866 | 0.525 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 163.14 |  | 161.8145 | 0.8191 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 238.15 |  | 235.6164 | 1.0753 | 256.145 | 236.73 | 4.1864 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 634.87 |  | 623.4991 | 1.8237 | 673.65 | 624.91 | 4.3158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 337.91 |  | 335.4168 | 0.7433 | 354.09 | 338.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| AAOI | ai_networking_optical | 87.08 |  | 84.7569 | 2.7409 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 256.95 |  | 255.2836 | 0.6528 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1580.38 |  | 1570.9738 | 0.5988 | 1586.01 | 1565.95 | 0.3569 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 476.535 |  | 477.3084 | -0.162 | 494.87 | 477.03 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LRCX | semiconductor_equipment | 266.64 |  | 265.7022 | 0.3529 | 276.85 | 267.14 | 1.9502 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 191.21 |  | 189.9415 | 0.6679 | 194.96 | 189.48 | 0.774 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 309.84 |  | 305.277 | 1.4947 | 315.21 | 304.11 | 0.9941 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 235.05 |  | 237.7626 | -1.1409 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 47.525 |  | 47.2287 | 0.6274 | 51.64 | 47.435 | 2.8617 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 42.79 |  | 42.6504 | 0.3274 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 121.32 |  | 119.0998 | 1.8641 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 282.28 |  | 281.9533 | 0.1159 | 296.8 | 283.22 | 4.949 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| LIN | industrial_gases | 518.16 |  | 518.6865 | -0.1015 | 518.6 | 511.495 | 4.3963 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 296 |  | 296.4348 | -0.1467 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.515 |  | 26.3039 | 0.8025 | 27 | 25.42 | 0.1509 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.135 |  | 33.2925 | 2.5308 | 35.08 | 33.52 | 0.0586 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.11 |  | 19.9392 | 0.8567 | 20.97 | 19.755 | 0.0995 | watch_only | none |
| SNDK | memory_hbm_storage | 1119.745 |  | 1103.4481 | 1.4769 | 1185.19 | 1114.57 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 438.09 |  | 433.3359 | 1.0971 | 465.04 | 435.22 | 1.5705 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 728.84 |  | 721.7772 | 0.9785 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 228.92 |  | 230.0134 | -0.4754 | 233.05 | 229.7 | 0.1092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 592.265 |  | 594.5619 | -0.3863 | 600.765 | 594.21 | 0.1756 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 245.815 |  | 244.5821 | 0.5041 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.76 |  | 131.3816 | 1.8103 | 136.45 | 131.735 | 1.2709 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
