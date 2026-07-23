# Intraday State

- Generated at: `2026-07-24T01:30:57+08:00`
- Market time ET: `2026-07-23T13:30:58-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 10, 'below_opening_15m_low': 8, 'below_vwap': 19, 'spread_too_wide_or_missing': 14, 'price_stale_or_missing': 3, 'manual_confirm_candidate': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.275 |  | 693.1237 | 0.0218 | 698.65 | 693.24 | 0.0087 | watch_only | none |
| SOXX | semiconductor_index | 550.59 |  | 550.9811 | -0.071 | 557.38 | 545.965 | 0.0745 | below_vwap | below_vwap |
| SMH | semiconductor_index | 581.19 |  | 581.1586 | 0.0054 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| SPY | market_regime | 738.765 |  | 738.7987 | -0.0046 | 742.515 | 738.54 | 0.0501 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 1000.23 |  | 991.4102 | 0.8896 | 999.04 | 964.86 | 0.139 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.37 |  | 31.6719 | 2.204 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 581.19 |  | 581.1586 | 0.0054 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| 2 | ASML | semiconductor_equipment | 1804.21 |  | 1804.0581 | 0.0084 | 1806.11 | 1780.9 | 0.1031 | watch_only | none |
| 3 | QQQ | market_regime | 693.275 |  | 693.1237 | 0.0218 | 698.65 | 693.24 | 0.0087 | watch_only | none |
| 4 | GOOGL | cloud_ai_capex | 320.4 |  | 319.5485 | 0.2665 | 324.42 | 320.24 | 0.103 | watch_only | none |
| 5 | HPE | ai_server_oem | 48.4 |  | 48.3545 | 0.0941 | 48.88 | 47.635 | 0.0826 | watch_only | none |
| 6 | NVDA | ai_accelerator | 210.13 |  | 208.5424 | 0.7613 | 210.85 | 208.49 | 0.1237 | watch_only | none |
| 7 | MU | memory_hbm_storage | 1000.23 |  | 991.4102 | 0.8896 | 999.04 | 964.86 | 0.139 | buy_precheck_manual_confirm | none |
| 8 | WDC | memory_hbm_storage | 567.15 |  | 564.2676 | 0.5108 | 576.24 | 556.3 | 0.171 | watch_only | none |
| 9 | CIEN | ai_networking_optical | 409.53 |  | 408.2107 | 0.3232 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | TT | data_center_power_cooling | 477.58 |  | 476.8113 | 0.1612 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 144.065 |  | 143.9683 | 0.0672 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 414.29 |  | 413.4013 | 0.215 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | MKSI | semiconductor_materials | 343.45 |  | 342.8978 | 0.161 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ALAB | ai_networking_optical | 328.695 |  | 327.7889 | 0.2764 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | APLD | high_beta_ai_infrastructure | 30.245 |  | 30.0557 | 0.6298 | 31.13 | 29.12 | 0.0992 | watch_only | none |
| 16 | TSM | foundry | 418.03 |  | 416.7033 | 0.3184 | 420.72 | 412.69 | 0.5717 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | ARM | ai_accelerator | 282.44 |  | 279.5681 | 1.0273 | 283 | 276.24 | 0.2939 | watch_only | none |
| 18 | ANET | ai_networking_optical | 177.27 |  | 176.7251 | 0.3083 | 177.84 | 173.19 | 2.2564 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | META | cloud_ai_capex | 605.995 |  | 604.0234 | 0.3264 | 614.15 | 605.39 | 1.8102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 374.69 |  | 372.2659 | 0.6512 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 1000.23 |  | 991.4102 | 0.8896 | 999.04 | 964.86 | 0.139 | buy_precheck_manual_confirm | none |
| 2 | SMCI | ai_server_oem | 32.37 |  | 31.6719 | 2.204 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 1031.545 |  | 1012.9868 | 1.832 | 1023.33 | 979.08 | 4.3624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | CIEN | ai_networking_optical | 409.53 |  | 408.2107 | 0.3232 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | SNDK | memory_hbm_storage | 1676.835 |  | 1640.3709 | 2.2229 | 1651.355 | 1560 | 3.6128 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | SMH | semiconductor_index | 581.19 |  | 581.1586 | 0.0054 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| 7 | NVDA | ai_accelerator | 210.13 |  | 208.5424 | 0.7613 | 210.85 | 208.49 | 0.1237 | watch_only | none |
| 8 | ASML | semiconductor_equipment | 1804.21 |  | 1804.0581 | 0.0084 | 1806.11 | 1780.9 | 0.1031 | watch_only | none |
| 9 | QQQ | market_regime | 693.275 |  | 693.1237 | 0.0218 | 698.65 | 693.24 | 0.0087 | watch_only | none |
| 10 | ARM | ai_accelerator | 282.44 |  | 279.5681 | 1.0273 | 283 | 276.24 | 0.2939 | watch_only | none |
| 11 | WDC | memory_hbm_storage | 567.15 |  | 564.2676 | 0.5108 | 576.24 | 556.3 | 0.171 | watch_only | none |
| 12 | GOOGL | cloud_ai_capex | 320.4 |  | 319.5485 | 0.2665 | 324.42 | 320.24 | 0.103 | watch_only | none |
| 13 | HPE | ai_server_oem | 48.4 |  | 48.3545 | 0.0941 | 48.88 | 47.635 | 0.0826 | watch_only | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.24 |  | 24.0609 | 0.7442 | 24.46 | 23.265 | 0.0825 | watch_only | none |
| 15 | APLD | high_beta_ai_infrastructure | 30.245 |  | 30.0557 | 0.6298 | 31.13 | 29.12 | 0.0992 | watch_only | none |
| 16 | SOXX | semiconductor_index | 550.59 |  | 550.9811 | -0.071 | 557.38 | 545.965 | 0.0745 | below_vwap | below_vwap |
| 17 | AVGO | custom_silicon_networking | 392.49 |  | 392.5743 | -0.0215 | 397.34 | 390.54 | 1.0242 | below_vwap | below_vwap,spread_too_wide |
| 18 | AMAT | semiconductor_equipment | 563.56 |  | 566.1134 | -0.451 | 566.18 | 548.47 | 3.996 | below_vwap | below_vwap,spread_too_wide |
| 19 | PWR | data_center_power_cooling | 650.76 |  | 652.0955 | -0.2048 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | KLAC | semiconductor_equipment | 215.6 |  | 215.7322 | -0.0613 | 217.88 | 212.99 | 0.0974 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.275 |  | 693.1237 | 0.0218 | 698.65 | 693.24 | 0.0087 | watch_only | none |
| TQQQ | leveraged_tool | 66.59 |  | 66.5741 | 0.0238 | 68.245 | 66.7 | 0.03 | below_opening_15m_low | below_opening_15m_low |
| NVDA | ai_accelerator | 210.13 |  | 208.5424 | 0.7613 | 210.85 | 208.49 | 0.1237 | watch_only | none |
| MSFT | cloud_ai_capex | 381.465 |  | 382.7287 | -0.3302 | 391.71 | 387.245 | 0.3513 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.86 |  | 321.1147 | -0.0793 | 323.25 | 320.82 | 0.0093 | below_vwap | below_vwap |
| GOOGL | cloud_ai_capex | 320.4 |  | 319.5485 | 0.2665 | 324.42 | 320.24 | 0.103 | watch_only | none |
| AMD | ai_accelerator | 535.695 |  | 541.25 | -1.0263 | 556.12 | 542.33 | 2.5089 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 418.03 |  | 416.7033 | 0.3184 | 420.72 | 412.69 | 0.5717 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.59 |  | 550.9811 | -0.071 | 557.38 | 545.965 | 0.0745 | below_vwap | below_vwap |
| SMH | semiconductor_index | 581.19 |  | 581.1586 | 0.0054 | 585.98 | 576.635 | 0.0705 | watch_only | none |
| AVGO | custom_silicon_networking | 392.49 |  | 392.5743 | -0.0215 | 397.34 | 390.54 | 1.0242 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 1000.23 |  | 991.4102 | 0.8896 | 999.04 | 964.86 | 0.139 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 208.4 |  | 209.8201 | -0.6768 | 213.785 | 207.665 | 0.5134 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.54 |  | 444.0567 | -0.1164 | 450.07 | 438.55 | 1.1386 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 48.4 |  | 48.3545 | 0.0941 | 48.88 | 47.635 | 0.0826 | watch_only | none |
| SMCI | ai_server_oem | 32.37 |  | 31.6719 | 2.204 | 31.52 | 30.23 | 0.0309 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.765 |  | 738.7987 | -0.0046 | 742.515 | 738.54 | 0.0501 | below_vwap | below_vwap |
| IWM | market_regime | 291.45 |  | 291.6855 | -0.0807 | 293.01 | 290.365 | 0.0103 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.75 |  | 122.0558 | -1.0699 | 124.22 | 122.07 | 0.2484 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.745 |  | 82.8583 | -0.1368 | 84.415 | 80.64 | 5.0758 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.805 |  | 306.3195 | -0.4944 | 311.13 | 303.96 | 1.227 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.29 |  | 413.4013 | 0.215 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 650.76 |  | 652.0955 | -0.2048 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1031.545 |  | 1012.9868 | 1.832 | 1023.33 | 979.08 | 4.3624 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.58 |  | 476.8113 | 0.1612 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.065 |  | 143.9683 | 0.0672 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 177.27 |  | 176.7251 | 0.3083 | 177.84 | 173.19 | 2.2564 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 316.12 |  | 318.2158 | -0.6586 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 847.65 |  | 858.2168 | -1.2312 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 409.53 |  | 408.2107 | 0.3232 | 408.58 | 397.9 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 114.16 |  | 114.6743 | -0.4485 | 118.01 | 108.505 | 4.8353 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 328.695 |  | 327.7889 | 0.2764 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1804.21 |  | 1804.0581 | 0.0084 | 1806.11 | 1780.9 | 0.1031 | watch_only | none |
| AMAT | semiconductor_equipment | 563.56 |  | 566.1134 | -0.451 | 566.18 | 548.47 | 3.996 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.91 |  | 321.3045 | -0.1228 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.6 |  | 215.7322 | -0.0613 | 217.88 | 212.99 | 0.0974 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 374.69 |  | 372.2659 | 0.6512 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.96 |  | 294.8528 | -0.9811 | 301.305 | 293.685 | 0.3939 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 65.21 |  | 65.306 | -0.147 | 67.455 | 65.81 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.51 |  | 54.6048 | -0.1735 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 134.99 |  | 135.3632 | -0.2757 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 343.45 |  | 342.8978 | 0.161 | 347.92 | 341.755 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 505.92 |  | 507.5573 | -0.3226 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.43 |  | 296.0012 | -0.5308 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.245 |  | 30.0557 | 0.6298 | 31.13 | 29.12 | 0.0992 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 41.21 |  | 41.7345 | -1.2567 | 43.21 | 40.51 | 0.0485 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.24 |  | 24.0609 | 0.7442 | 24.46 | 23.265 | 0.0825 | watch_only | none |
| SNDK | memory_hbm_storage | 1676.835 |  | 1640.3709 | 2.2229 | 1651.355 | 1560 | 3.6128 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 567.15 |  | 564.2676 | 0.5108 | 576.24 | 556.3 | 0.171 | watch_only | none |
| STX | memory_hbm_storage | 926.865 |  | 924.6779 | 0.2365 | 933.5 | 908.955 | 4.8767 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.52 |  | 234.3567 | 0.0697 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 605.995 |  | 604.0234 | 0.3264 | 614.15 | 605.39 | 1.8102 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 282.44 |  | 279.5681 | 1.0273 | 283 | 276.24 | 0.2939 | watch_only | none |
| SKHY | memory_hbm_storage | 173.94 |  | 173.6188 | 0.185 | 177.88 | 168.18 | 1.6098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
