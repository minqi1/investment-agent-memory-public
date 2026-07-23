# Intraday State

- Generated at: `2026-07-24T00:38:53+08:00`
- Market time ET: `2026-07-23T12:38:54-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 11, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 3, 'below_vwap': 10, 'manual_confirm_candidate': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.51 |  | 693.1254 | 0.1998 | 698.65 | 693.24 | 0.0115 | watch_only | none |
| SOXX | semiconductor_index | 553.67 |  | 550.9096 | 0.5011 | 557.38 | 545.965 | 0.0596 | watch_only | none |
| SMH | semiconductor_index | 583.55 |  | 581.2182 | 0.4012 | 585.98 | 576.635 | 0.0754 | watch_only | none |
| SPY | market_regime | 739.285 |  | 738.8359 | 0.0608 | 742.515 | 738.54 | 0.0027 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.8 |  | 1803.9268 | 0.2701 | 1806.11 | 1780.9 | 0.0697 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 569.74 |  | 566.3447 | 0.5995 | 566.18 | 548.47 | 0.1527 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.49 |  | 31.5196 | 3.0787 | 31.52 | 30.23 | 0.0308 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.8 |  | 1803.9268 | 0.2701 | 1806.11 | 1780.9 | 0.0697 | buy_precheck_manual_confirm | none |
| 2 | JCI | data_center_power_cooling | 144.07 |  | 143.9549 | 0.08 | 145.035 | 141.815 | 0.0486 | watch_only | none |
| 3 | IWM | market_regime | 291.71 |  | 291.6995 | 0.0036 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 4 | QQQ | market_regime | 694.51 |  | 693.1254 | 0.1998 | 698.65 | 693.24 | 0.0115 | watch_only | none |
| 5 | SPY | market_regime | 739.285 |  | 738.8359 | 0.0608 | 742.515 | 738.54 | 0.0027 | watch_only | none |
| 6 | AMAT | semiconductor_equipment | 569.74 |  | 566.3447 | 0.5995 | 566.18 | 548.47 | 0.1527 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 583.55 |  | 581.2182 | 0.4012 | 585.98 | 576.635 | 0.0754 | watch_only | none |
| 8 | SOXX | semiconductor_index | 553.67 |  | 550.9096 | 0.5011 | 557.38 | 545.965 | 0.0596 | watch_only | none |
| 9 | NVDA | ai_accelerator | 209.96 |  | 208.3234 | 0.7856 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 10 | TT | data_center_power_cooling | 477.89 |  | 476.7432 | 0.2406 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | LRCX | semiconductor_equipment | 321.83 |  | 321.3596 | 0.1464 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | HPE | ai_server_oem | 48.735 |  | 48.3438 | 0.8092 | 48.88 | 47.635 | 0.0821 | watch_only | none |
| 13 | ARM | ai_accelerator | 282.19 |  | 279.0582 | 1.1223 | 283 | 276.24 | 0.2977 | watch_only | none |
| 14 | AVGO | custom_silicon_networking | 392.8 |  | 392.6817 | 0.0301 | 397.34 | 390.54 | 1.9476 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | AMD | ai_accelerator | 547.25 |  | 546.318 | 0.1706 | 556.12 | 542.33 | 2.6514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ETN | data_center_power_cooling | 415.02 |  | 413.3114 | 0.4134 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 135.88 |  | 135.4015 | 0.3534 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | COHR | ai_networking_optical | 319.205 |  | 318.348 | 0.2692 | 320.13 | 307.04 | 0.7801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 210.17 |  | 209.9753 | 0.0927 | 213.785 | 207.665 | 2.793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ALAB | ai_networking_optical | 330.08 |  | 327.6479 | 0.7423 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ASML | semiconductor_equipment | 1808.8 |  | 1803.9268 | 0.2701 | 1806.11 | 1780.9 | 0.0697 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 569.74 |  | 566.3447 | 0.5995 | 566.18 | 548.47 | 0.1527 | buy_precheck_manual_confirm | none |
| 3 | SMCI | ai_server_oem | 32.49 |  | 31.5196 | 3.0787 | 31.52 | 30.23 | 0.0308 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 1009.34 |  | 989.9633 | 1.9573 | 999.04 | 964.86 | 0.3557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | ANET | ai_networking_optical | 177.93 |  | 176.6663 | 0.7153 | 177.84 | 173.19 | 1.2533 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | CIEN | ai_networking_optical | 410.16 |  | 407.9797 | 0.5344 | 408.58 | 397.9 | 3.4621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SNDK | memory_hbm_storage | 1691.19 |  | 1635.3166 | 3.4167 | 1651.355 | 1560 | 0.3506 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | STX | memory_hbm_storage | 934.02 |  | 924.5913 | 1.0198 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 583.55 |  | 581.2182 | 0.4012 | 585.98 | 576.635 | 0.0754 | watch_only | none |
| 10 | SOXX | semiconductor_index | 553.67 |  | 550.9096 | 0.5011 | 557.38 | 545.965 | 0.0596 | watch_only | none |
| 11 | NVDA | ai_accelerator | 209.96 |  | 208.3234 | 0.7856 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 144.07 |  | 143.9549 | 0.08 | 145.035 | 141.815 | 0.0486 | watch_only | none |
| 13 | IWM | market_regime | 291.71 |  | 291.6995 | 0.0036 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| 14 | QQQ | market_regime | 694.51 |  | 693.1254 | 0.1998 | 698.65 | 693.24 | 0.0115 | watch_only | none |
| 15 | ARM | ai_accelerator | 282.19 |  | 279.0582 | 1.1223 | 283 | 276.24 | 0.2977 | watch_only | none |
| 16 | SPY | market_regime | 739.285 |  | 738.8359 | 0.0608 | 742.515 | 738.54 | 0.0027 | watch_only | none |
| 17 | HPE | ai_server_oem | 48.735 |  | 48.3438 | 0.8092 | 48.88 | 47.635 | 0.0821 | watch_only | none |
| 18 | CORZ | high_beta_ai_infrastructure | 24.17 |  | 24.0427 | 0.5296 | 24.46 | 23.265 | 0.1241 | watch_only | none |
| 19 | TQQQ | leveraged_tool | 66.965 |  | 66.5752 | 0.5856 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| 20 | PWR | data_center_power_cooling | 651.22 |  | 652.3899 | -0.1793 | 656.38 | 642.37 | 0.2503 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 694.51 |  | 693.1254 | 0.1998 | 698.65 | 693.24 | 0.0115 | watch_only | none |
| TQQQ | leveraged_tool | 66.965 |  | 66.5752 | 0.5856 | 68.245 | 66.7 | 0.0149 | watch_only | none |
| NVDA | ai_accelerator | 209.96 |  | 208.3234 | 0.7856 | 210.85 | 208.49 | 0.0143 | watch_only | none |
| MSFT | cloud_ai_capex | 380.26 |  | 382.9538 | -0.7034 | 391.71 | 387.245 | 0.5917 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 320.25 |  | 321.184 | -0.2908 | 323.25 | 320.82 | 0.0156 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 319.9 |  | 319.5474 | 0.1103 | 324.42 | 320.24 | 0.6252 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMD | ai_accelerator | 547.25 |  | 546.318 | 0.1706 | 556.12 | 542.33 | 2.6514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 418.56 |  | 416.5822 | 0.4748 | 420.72 | 412.69 | 3.3161 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 553.67 |  | 550.9096 | 0.5011 | 557.38 | 545.965 | 0.0596 | watch_only | none |
| SMH | semiconductor_index | 583.55 |  | 581.2182 | 0.4012 | 585.98 | 576.635 | 0.0754 | watch_only | none |
| AVGO | custom_silicon_networking | 392.8 |  | 392.6817 | 0.0301 | 397.34 | 390.54 | 1.9476 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 1009.34 |  | 989.9633 | 1.9573 | 999.04 | 964.86 | 0.3557 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 210.17 |  | 209.9753 | 0.0927 | 213.785 | 207.665 | 2.793 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 446.54 |  | 444.0619 | 0.5581 | 450.07 | 438.55 | 1.0817 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.735 |  | 48.3438 | 0.8092 | 48.88 | 47.635 | 0.0821 | watch_only | none |
| SMCI | ai_server_oem | 32.49 |  | 31.5196 | 3.0787 | 31.52 | 30.23 | 0.0308 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 739.285 |  | 738.8359 | 0.0608 | 742.515 | 738.54 | 0.0027 | watch_only | none |
| IWM | market_regime | 291.71 |  | 291.6995 | 0.0036 | 293.01 | 290.365 | 0.0069 | watch_only | none |
| ORCL | cloud_ai_capex | 121.01 |  | 122.1986 | -0.9727 | 124.22 | 122.07 | 0.1074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.855 |  | 82.9393 | -0.1016 | 84.415 | 80.64 | 0.0845 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 304.8 |  | 306.4303 | -0.532 | 311.13 | 303.96 | 0.6234 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 415.02 |  | 413.3114 | 0.4134 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 651.22 |  | 652.3899 | -0.1793 | 656.38 | 642.37 | 0.2503 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1021.4 |  | 1011.6427 | 0.9645 | 1023.33 | 979.08 | 2.6983 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.89 |  | 476.7432 | 0.2406 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.07 |  | 143.9549 | 0.08 | 145.035 | 141.815 | 0.0486 | watch_only | none |
| ANET | ai_networking_optical | 177.93 |  | 176.6663 | 0.7153 | 177.84 | 173.19 | 1.2533 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 319.205 |  | 318.348 | 0.2692 | 320.13 | 307.04 | 0.7801 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 853 |  | 858.9142 | -0.6886 | 880.26 | 833 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 410.16 |  | 407.9797 | 0.5344 | 408.58 | 397.9 | 3.4621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 114.47 |  | 114.7761 | -0.2667 | 118.01 | 108.505 | 0.4979 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 330.08 |  | 327.6479 | 0.7423 | 341.68 | 327.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1808.8 |  | 1803.9268 | 0.2701 | 1806.11 | 1780.9 | 0.0697 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 569.74 |  | 566.3447 | 0.5995 | 566.18 | 548.47 | 0.1527 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.83 |  | 321.3596 | 0.1464 | 322.4 | 317.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.75 |  | 215.6844 | 0.4941 | 217.88 | 212.99 | 2.0623 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 376.72 |  | 371.818 | 1.3184 | 376.78 | 363.37 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 293.955 |  | 295.4802 | -0.5162 | 301.305 | 293.685 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 65.39 |  | 65.3205 | 0.1063 | 67.455 | 65.81 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 135.88 |  | 135.4015 | 0.3534 | 137.81 | 135.66 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 344.3 |  | 342.8588 | 0.4203 | 347.92 | 341.755 | 0.9875 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| LIN | industrial_gases | 506.62 |  | 507.6549 | -0.2039 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.59 |  | 296.2862 | -0.235 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.95 |  | 30.0654 | -0.3839 | 31.13 | 29.12 | 0.0668 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.22 |  | 41.8446 | -1.4927 | 43.21 | 40.51 | 0.0485 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 24.17 |  | 24.0427 | 0.5296 | 24.46 | 23.265 | 0.1241 | watch_only | none |
| SNDK | memory_hbm_storage | 1691.19 |  | 1635.3166 | 3.4167 | 1651.355 | 1560 | 0.3506 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 573.48 |  | 563.7279 | 1.7299 | 576.24 | 556.3 | 0.4708 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 934.02 |  | 924.5913 | 1.0198 | 933.5 | 908.955 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 234.24 |  | 234.3489 | -0.0465 | 238.285 | 235.71 | 0.0256 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 602.07 |  | 603.8258 | -0.2908 | 614.15 | 605.39 | 0.2342 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 282.19 |  | 279.0582 | 1.1223 | 283 | 276.24 | 0.2977 | watch_only | none |
| SKHY | memory_hbm_storage | 175 |  | 173.6041 | 0.8041 | 177.88 | 168.18 | 0.7257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
