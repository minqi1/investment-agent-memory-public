# Intraday State

- Generated at: `2026-07-24T00:16:35+08:00`
- Market time ET: `2026-07-23T12:16:36-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 11, 'watch_only': 5, 'below_vwap': 25, 'price_stale_or_missing': 3, 'spread_too_wide_or_missing': 11, 'manual_confirm_candidate': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.8 |  | 693.0679 | -0.0387 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 549.72 |  | 550.9459 | -0.2225 | 557.38 | 545.965 | 0.0746 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.69 |  | 581.2403 | -0.2667 | 585.98 | 576.635 | 0.0725 | below_vwap | below_vwap |
| SPY | market_regime | 738.725 |  | 738.8095 | -0.0114 | 742.515 | 738.54 | 0.0257 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.67 |  | 31.4383 | 0.7369 | 31.52 | 30.23 | 0.0316 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | HPE | ai_server_oem | 48.37 |  | 48.3307 | 0.0813 | 48.88 | 47.635 | 0.1034 | watch_only | none |
| 2 | SMCI | ai_server_oem | 31.67 |  | 31.4383 | 0.7369 | 31.52 | 30.23 | 0.0316 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 321.45 |  | 321.218 | 0.0722 | 323.25 | 320.82 | 0.0124 | watch_only | none |
| 4 | NVDA | ai_accelerator | 209.09 |  | 208.2334 | 0.4114 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 5 | MU | memory_hbm_storage | 992.865 |  | 988.8365 | 0.4074 | 999.04 | 964.86 | 0.138 | watch_only | none |
| 6 | GOOGL | cloud_ai_capex | 320.755 |  | 319.4883 | 0.3965 | 324.42 | 320.24 | 0.0624 | watch_only | none |
| 7 | TT | data_center_power_cooling | 477.99 |  | 476.707 | 0.2691 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | JCI | data_center_power_cooling | 144.23 |  | 143.9484 | 0.1956 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 414.27 |  | 413.2644 | 0.2433 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ARM | ai_accelerator | 279.01 |  | 278.9419 | 0.0244 | 283 | 276.24 | 0.6666 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | CIEN | ai_networking_optical | 407.96 |  | 407.9598 | 0 | 408.58 | 397.9 | 4.5838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | TER | semiconductor_test_packaging | 372.33 |  | 371.598 | 0.197 | 376.78 | 363.37 | 4.8962 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | DELL | ai_server_oem | 444.24 |  | 443.9524 | 0.0648 | 450.07 | 438.55 | 1.6905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | GEV | data_center_power_cooling | 1015.02 |  | 1011.2847 | 0.3694 | 1023.33 | 979.08 | 2.5211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | WDC | memory_hbm_storage | 566.565 |  | 563.1187 | 0.612 | 576.24 | 556.3 | 0.7925 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SMH | semiconductor_index | 579.69 |  | 581.2403 | -0.2667 | 585.98 | 576.635 | 0.0725 | below_vwap | below_vwap |
| 17 | SOXX | semiconductor_index | 549.72 |  | 550.9459 | -0.2225 | 557.38 | 545.965 | 0.0746 | below_vwap | below_vwap |
| 18 | ASML | semiconductor_equipment | 1803.39 |  | 1803.8628 | -0.0262 | 1806.11 | 1780.9 | 0.0843 | below_vwap | below_vwap |
| 19 | STX | memory_hbm_storage | 928.43 |  | 923.7323 | 0.5086 | 933.5 | 908.955 | 0.4987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | IWM | market_regime | 291.59 |  | 291.6991 | -0.0374 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMCI | ai_server_oem | 31.67 |  | 31.4383 | 0.7369 | 31.52 | 30.23 | 0.0316 | buy_precheck_manual_confirm | none |
| 2 | SNDK | memory_hbm_storage | 1671.89 |  | 1629.0755 | 2.6281 | 1651.355 | 1560 | 3.3968 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 3 | NVDA | ai_accelerator | 209.09 |  | 208.2334 | 0.4114 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| 4 | MU | memory_hbm_storage | 992.865 |  | 988.8365 | 0.4074 | 999.04 | 964.86 | 0.138 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 320.755 |  | 319.4883 | 0.3965 | 324.42 | 320.24 | 0.0624 | watch_only | none |
| 6 | HPE | ai_server_oem | 48.37 |  | 48.3307 | 0.0813 | 48.88 | 47.635 | 0.1034 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 321.45 |  | 321.218 | 0.0722 | 323.25 | 320.82 | 0.0124 | watch_only | none |
| 8 | TSM | foundry | 416.26 |  | 416.5179 | -0.0619 | 420.72 | 412.69 | 4.084 | below_vwap | below_vwap,spread_too_wide |
| 9 | SMH | semiconductor_index | 579.69 |  | 581.2403 | -0.2667 | 585.98 | 576.635 | 0.0725 | below_vwap | below_vwap |
| 10 | SOXX | semiconductor_index | 549.72 |  | 550.9459 | -0.2225 | 557.38 | 545.965 | 0.0746 | below_vwap | below_vwap |
| 11 | ASML | semiconductor_equipment | 1803.39 |  | 1803.8628 | -0.0262 | 1806.11 | 1780.9 | 0.0843 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 565.11 |  | 566.2894 | -0.2083 | 566.18 | 548.47 | 0.2973 | below_vwap | below_vwap |
| 13 | ANET | ai_networking_optical | 176.61 |  | 176.626 | -0.0091 | 177.84 | 173.19 | 1.9931 | below_vwap | below_vwap,spread_too_wide |
| 14 | PWR | data_center_power_cooling | 648.58 |  | 652.6426 | -0.6225 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | KLAC | semiconductor_equipment | 215.155 |  | 215.6795 | -0.2432 | 217.88 | 212.99 | 2.8863 | below_vwap | below_vwap,spread_too_wide |
| 16 | VRT | data_center_power_cooling | 304.305 |  | 306.5004 | -0.7163 | 311.13 | 303.96 | 1.9553 | below_vwap | below_vwap,spread_too_wide |
| 17 | IWM | market_regime | 291.59 |  | 291.6991 | -0.0374 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| 18 | LRCX | semiconductor_equipment | 319.67 |  | 321.3572 | -0.525 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | SPY | market_regime | 738.725 |  | 738.8095 | -0.0114 | 742.515 | 738.54 | 0.0257 | below_vwap | below_vwap |
| 20 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 692.8 |  | 693.0679 | -0.0387 | 698.65 | 693.24 | 0.0101 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 66.52 |  | 66.5505 | -0.0458 | 68.245 | 66.7 | 0.0301 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.09 |  | 208.2334 | 0.4114 | 210.85 | 208.49 | 0.0096 | watch_only | none |
| MSFT | cloud_ai_capex | 380.2 |  | 383.0727 | -0.7499 | 391.71 | 387.245 | 0.5918 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 321.45 |  | 321.218 | 0.0722 | 323.25 | 320.82 | 0.0124 | watch_only | none |
| GOOGL | cloud_ai_capex | 320.755 |  | 319.4883 | 0.3965 | 324.42 | 320.24 | 0.0624 | watch_only | none |
| AMD | ai_accelerator | 542.25 |  | 546.5062 | -0.7788 | 556.12 | 542.33 | 1.5602 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 416.26 |  | 416.5179 | -0.0619 | 420.72 | 412.69 | 4.084 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1907000 |  | 1862907.8116 | 2.3668 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 549.72 |  | 550.9459 | -0.2225 | 557.38 | 545.965 | 0.0746 | below_vwap | below_vwap |
| SMH | semiconductor_index | 579.69 |  | 581.2403 | -0.2667 | 585.98 | 576.635 | 0.0725 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.34 |  | 392.7996 | -0.6262 | 397.34 | 390.54 | 1.4577 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 992.865 |  | 988.8365 | 0.4074 | 999.04 | 964.86 | 0.138 | watch_only | none |
| MRVL | custom_silicon_networking | 208.39 |  | 210.021 | -0.7766 | 213.785 | 207.665 | 0.643 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 444.24 |  | 443.9524 | 0.0648 | 450.07 | 438.55 | 1.6905 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.37 |  | 48.3307 | 0.0813 | 48.88 | 47.635 | 0.1034 | watch_only | none |
| SMCI | ai_server_oem | 31.67 |  | 31.4383 | 0.7369 | 31.52 | 30.23 | 0.0316 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 738.725 |  | 738.8095 | -0.0114 | 742.515 | 738.54 | 0.0257 | below_vwap | below_vwap |
| IWM | market_regime | 291.59 |  | 291.6991 | -0.0374 | 293.01 | 290.365 | 0.0069 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 120.65 |  | 122.2761 | -1.3299 | 124.22 | 122.07 | 0.2155 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 82.275 |  | 82.9466 | -0.8097 | 84.415 | 80.64 | 4.6916 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 304.305 |  | 306.5004 | -0.7163 | 311.13 | 303.96 | 1.9553 | below_vwap | below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 414.27 |  | 413.2644 | 0.2433 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 648.58 |  | 652.6426 | -0.6225 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1015.02 |  | 1011.2847 | 0.3694 | 1023.33 | 979.08 | 2.5211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 477.99 |  | 476.707 | 0.2691 | 480 | 472.33 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 144.23 |  | 143.9484 | 0.1956 | 145.035 | 141.815 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 176.61 |  | 176.626 | -0.0091 | 177.84 | 173.19 | 1.9931 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 316.22 |  | 318.3854 | -0.6801 | 320.13 | 307.04 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 844.53 |  | 859.4331 | -1.7341 | 880.26 | 833 | 4.573 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 407.96 |  | 407.9598 | 0 | 408.58 | 397.9 | 4.5838 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 113.99 |  | 114.8055 | -0.7103 | 118.01 | 108.505 |  | below_vwap | below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 326.08 |  | 327.6153 | -0.4686 | 341.68 | 327.43 | 4.41 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1803.39 |  | 1803.8628 | -0.0262 | 1806.11 | 1780.9 | 0.0843 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 565.11 |  | 566.2894 | -0.2083 | 566.18 | 548.47 | 0.2973 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.67 |  | 321.3572 | -0.525 | 322.4 | 317.27 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.155 |  | 215.6795 | -0.2432 | 217.88 | 212.99 | 2.8863 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.33 |  | 371.598 | 0.197 | 376.78 | 363.37 | 4.8962 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 294.235 |  | 295.6721 | -0.486 | 301.305 | 293.685 | 3.9322 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.485 |  | 65.3246 | -1.2853 | 67.455 | 65.81 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.44 |  | 54.6028 | -0.2981 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.79 |  | 135.3788 | -0.4349 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 341.2 |  | 342.8499 | -0.4812 | 347.92 | 341.755 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| LIN | industrial_gases | 506.85 |  | 507.7039 | -0.1682 | 510.71 | 502.72 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.49 |  | 296.3861 | -0.3023 | 299.26 | 295.795 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.88 |  | 30.0697 | -0.6309 | 31.13 | 29.12 | 0.0335 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.41 |  | 41.873 | -1.1056 | 43.21 | 40.51 | 0.0483 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.9 |  | 24.0467 | -0.6101 | 24.46 | 23.265 | 0.1255 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1671.89 |  | 1629.0755 | 2.6281 | 1651.355 | 1560 | 3.3968 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 566.565 |  | 563.1187 | 0.612 | 576.24 | 556.3 | 0.7925 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 928.43 |  | 923.7323 | 0.5086 | 933.5 | 908.955 | 0.4987 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 234.135 |  | 234.3154 | -0.077 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 602.72 |  | 603.8476 | -0.1867 | 614.15 | 605.39 | 0.0697 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 279.01 |  | 278.9419 | 0.0244 | 283 | 276.24 | 0.6666 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 173.42 |  | 173.5512 | -0.0756 | 177.88 | 168.18 | 0.369 | below_vwap | below_vwap,spread_too_wide |
