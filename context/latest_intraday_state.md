# Intraday State

- Generated at: `2026-07-16T03:52:08+08:00`
- Market time ET: `2026-07-15T15:52:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 38, 'watch_only': 3, 'below_vwap': 3, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.89 |  | 716.3581 | 0.0742 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| SOXX | semiconductor_index | 555.14 |  | 551.8427 | 0.5975 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.95 |  | 587.6795 | 0.3864 | 606.85 | 597.81 | 0.022 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.875 |  | 753.3466 | 0.0701 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 369.885 |  | 369.1518 | 0.1986 | 364.41 | 357.885 | 0.073 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.56 |  | 254.474 | 0.0338 | 252.89 | 249.98 | 0.0393 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.025 |  | 325.8998 | 0.3453 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.735 |  | 22.0129 | 3.2804 | 22.36 | 21.94 | 0.088 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMZN | cloud_ai_capex | 254.56 |  | 254.474 | 0.0338 | 252.89 | 249.98 | 0.0393 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 369.885 |  | 369.1518 | 0.1986 | 364.41 | 357.885 | 0.073 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.025 |  | 325.8998 | 0.3453 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 211.7 |  | 209.5487 | 1.0266 | 213.775 | 211.225 | 0.1039 | watch_only | none |
| 5 | ASML | semiconductor_equipment | 1807.04 |  | 1775.5009 | 1.7763 | 1829.9 | 1759.045 | 0.0836 | watch_only | none |
| 6 | AVGO | custom_silicon_networking | 394.64 |  | 392.4158 | 0.5668 | 397.94 | 392.62 | 0.8362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | SPY | market_regime | 753.875 |  | 753.3466 | 0.0701 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| 8 | WDC | memory_hbm_storage | 517.6 |  | 516.083 | 0.2939 | 568.16 | 542.4 | 0.0483 | below_opening_15m_low | below_opening_15m_low |
| 9 | CORZ | high_beta_ai_infrastructure | 22.735 |  | 22.0129 | 3.2804 | 22.36 | 21.94 | 0.088 | buy_precheck_manual_confirm | none |
| 10 | QQQ | market_regime | 716.89 |  | 716.3581 | 0.0742 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| 11 | APLD | high_beta_ai_infrastructure | 28.93 |  | 28.3841 | 1.9234 | 29.055 | 28.28 | 0.0691 | watch_only | none |
| 12 | SKHY | memory_hbm_storage | 176.55 |  | 175.7996 | 0.4269 | 183.63 | 176.08 | 0.7703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ORCL | cloud_ai_capex | 132.58 |  | 132.0582 | 0.3951 | 132.925 | 129.92 | 0.8448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMAT | semiconductor_equipment | 579.225 |  | 577.5837 | 0.2842 | 610.62 | 586.86 | 0.2417 | below_opening_15m_low | below_opening_15m_low |
| 15 | TT | data_center_power_cooling | 479.54 |  | 478.5895 | 0.1986 | 485.9 | 482.93 | 0.2106 | below_opening_15m_low | below_opening_15m_low |
| 16 | SOXX | semiconductor_index | 555.14 |  | 551.8427 | 0.5975 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| 17 | TSM | foundry | 420.78 |  | 419.1318 | 0.3932 | 428.59 | 422.945 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| 18 | KLAC | semiconductor_equipment | 223.52 |  | 222.7373 | 0.3514 | 236.49 | 225.11 | 0.0761 | below_opening_15m_low | below_opening_15m_low |
| 19 | SMH | semiconductor_index | 589.95 |  | 587.6795 | 0.3864 | 606.85 | 597.81 | 0.022 | below_opening_15m_low | below_opening_15m_low |
| 20 | SMCI | ai_server_oem | 27.03 |  | 26.9025 | 0.4738 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 369.885 |  | 369.1518 | 0.1986 | 364.41 | 357.885 | 0.073 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 254.56 |  | 254.474 | 0.0338 | 252.89 | 249.98 | 0.0393 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 327.025 |  | 325.8998 | 0.3453 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| 4 | CORZ | high_beta_ai_infrastructure | 22.735 |  | 22.0129 | 3.2804 | 22.36 | 21.94 | 0.088 | buy_precheck_manual_confirm | none |
| 5 | MSFT | cloud_ai_capex | 394.8 |  | 395.3948 | -0.1504 | 391.33 | 387.05 | 0.4078 | below_vwap | below_vwap,spread_too_wide |
| 6 | NVDA | ai_accelerator | 211.7 |  | 209.5487 | 1.0266 | 213.775 | 211.225 | 0.1039 | watch_only | none |
| 7 | META | cloud_ai_capex | 679.185 |  | 675.8073 | 0.4998 | 664.875 | 657.17 | 0.7862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ASML | semiconductor_equipment | 1807.04 |  | 1775.5009 | 1.7763 | 1829.9 | 1759.045 | 0.0836 | watch_only | none |
| 9 | APLD | high_beta_ai_infrastructure | 28.93 |  | 28.3841 | 1.9234 | 29.055 | 28.28 | 0.0691 | watch_only | none |
| 10 | IWM | market_regime | 295.445 |  | 295.6297 | -0.0625 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 394.64 |  | 392.4158 | 0.5668 | 397.94 | 392.62 | 0.8362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | VRT | data_center_power_cooling | 305.29 |  | 299.8682 | 1.8081 | 309.345 | 304.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | GEV | data_center_power_cooling | 1059.78 |  | 1038.3273 | 2.0661 | 1073.34 | 1059.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 176.55 |  | 175.7996 | 0.4269 | 183.63 | 176.08 | 0.7703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ORCL | cloud_ai_capex | 132.58 |  | 132.0582 | 0.3951 | 132.925 | 129.92 | 0.8448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | CIEN | ai_networking_optical | 422.25 |  | 419.8554 | 0.5703 | 438.14 | 427.54 | 0.8384 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | SOXX | semiconductor_index | 555.14 |  | 551.8427 | 0.5975 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| 19 | ANET | ai_networking_optical | 172.335 |  | 171.8329 | 0.2922 | 186.095 | 178.355 | 0.9748 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | STX | memory_hbm_storage | 828.475 |  | 817.969 | 1.2844 | 889.1 | 850.01 | 1.0284 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 716.89 |  | 716.3581 | 0.0742 | 724.31 | 721.08 | 0.0042 | below_opening_15m_low | below_opening_15m_low |
| TQQQ | leveraged_tool | 74.15 |  | 74.1836 | -0.0453 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 211.7 |  | 209.5487 | 1.0266 | 213.775 | 211.225 | 0.1039 | watch_only | none |
| MSFT | cloud_ai_capex | 394.8 |  | 395.3948 | -0.1504 | 391.33 | 387.05 | 0.4078 | below_vwap | below_vwap,spread_too_wide |
| AAPL | mega_cap_platform | 327.025 |  | 325.8998 | 0.3453 | 321.14 | 317.4 | 0.0122 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 369.885 |  | 369.1518 | 0.1986 | 364.41 | 357.885 | 0.073 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 529.215 |  | 527.5265 | 0.3201 | 558.62 | 548.745 | 1.3681 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 420.78 |  | 419.1318 | 0.3932 | 428.59 | 422.945 | 0.0594 | below_opening_15m_low | below_opening_15m_low |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 555.14 |  | 551.8427 | 0.5975 | 575.7 | 565.33 | 0.0721 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 589.95 |  | 587.6795 | 0.3864 | 606.85 | 597.81 | 0.022 | below_opening_15m_low | below_opening_15m_low |
| AVGO | custom_silicon_networking | 394.64 |  | 392.4158 | 0.5668 | 397.94 | 392.62 | 0.8362 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 908.63 |  | 909.4115 | -0.0859 | 977.7 | 953.67 | 0.2828 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.56 |  | 207.9174 | -0.6529 | 223.02 | 214.85 | 0.4212 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 412.9 |  | 407.4327 | 1.3419 | 457.935 | 442.67 | 2.3517 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| HPE | ai_server_oem | 47.74 |  | 47.0742 | 1.4144 | 50.2 | 48.995 | 0.0209 | below_opening_15m_low | below_opening_15m_low |
| SMCI | ai_server_oem | 27.03 |  | 26.9025 | 0.4738 | 28.295 | 27.55 | 0.037 | below_opening_15m_low | below_opening_15m_low |
| SPY | market_regime | 753.875 |  | 753.3466 | 0.0701 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 295.445 |  | 295.6297 | -0.0625 | 296.08 | 294.86 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 132.58 |  | 132.0582 | 0.3951 | 132.925 | 129.92 | 0.8448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.315 |  | 77.4726 | -0.2034 | 80.585 | 78.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 305.29 |  | 299.8682 | 1.8081 | 309.345 | 304.67 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ETN | data_center_power_cooling | 413.505 |  | 408.926 | 1.1198 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 653.46 |  | 646.6114 | 1.0592 | 663.475 | 653.94 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| GEV | data_center_power_cooling | 1059.78 |  | 1038.3273 | 2.0661 | 1073.34 | 1059.27 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 479.54 |  | 478.5895 | 0.1986 | 485.9 | 482.93 | 0.2106 | below_opening_15m_low | below_opening_15m_low |
| JCI | data_center_power_cooling | 143.14 |  | 141.9113 | 0.8658 | 145.99 | 144.625 | 0.0629 | below_opening_15m_low | below_opening_15m_low |
| ANET | ai_networking_optical | 172.335 |  | 171.8329 | 0.2922 | 186.095 | 178.355 | 0.9748 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| COHR | ai_networking_optical | 299.305 |  | 294.386 | 1.6709 | 315.74 | 303.34 | 0.1403 | below_opening_15m_low | below_opening_15m_low |
| LITE | ai_networking_optical | 754.03 |  | 749.4229 | 0.6148 | 820.15 | 780.365 | 2.797 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| CIEN | ai_networking_optical | 422.25 |  | 419.8554 | 0.5703 | 438.14 | 427.54 | 0.8384 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AAOI | ai_networking_optical | 111.45 |  | 111.6052 | -0.139 | 123.995 | 117.25 | 0.4217 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 349.75 |  | 345.2972 | 1.2896 | 369.23 | 356.615 | 3.7513 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ASML | semiconductor_equipment | 1807.04 |  | 1775.5009 | 1.7763 | 1829.9 | 1759.045 | 0.0836 | watch_only | none |
| AMAT | semiconductor_equipment | 579.225 |  | 577.5837 | 0.2842 | 610.62 | 586.86 | 0.2417 | below_opening_15m_low | below_opening_15m_low |
| LRCX | semiconductor_equipment | 334.67 |  | 331.5583 | 0.9385 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| KLAC | semiconductor_equipment | 223.52 |  | 222.7373 | 0.3514 | 236.49 | 225.11 | 0.0761 | below_opening_15m_low | below_opening_15m_low |
| TER | semiconductor_test_packaging | 341.95 |  | 336.8095 | 1.5262 | 356.29 | 343.785 | 4.1088 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ONTO | semiconductor_test_packaging | 305.51 |  | 306.9276 | -0.4619 | 326.25 | 317.3 | 4.3239 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.565 |  | 67.082 | 0.72 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 54.62 |  | 54.3723 | 0.4556 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.39 |  | 137.6436 | 0.5423 | 143.15 | 140.4 | 0.2674 | below_opening_15m_low | below_opening_15m_low |
| MKSI | semiconductor_materials | 354.72 |  | 349.344 | 1.5389 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 514.73 |  | 515.9724 | -0.2408 | 521.075 | 518.3 | 4.6471 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APD | industrial_gases | 293.77 |  | 294.3221 | -0.1876 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.93 |  | 28.3841 | 1.9234 | 29.055 | 28.28 | 0.0691 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 38.64 |  | 39.1759 | -1.368 | 40.01 | 38.815 | 0.0518 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 22.735 |  | 22.0129 | 3.2804 | 22.36 | 21.94 | 0.088 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1639.81 |  | 1587.8521 | 3.2722 | 1726.34 | 1665.91 | 3.898 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 517.6 |  | 516.083 | 0.2939 | 568.16 | 542.4 | 0.0483 | below_opening_15m_low | below_opening_15m_low |
| STX | memory_hbm_storage | 828.475 |  | 817.969 | 1.2844 | 889.1 | 850.01 | 1.0284 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| AMZN | cloud_ai_capex | 254.56 |  | 254.474 | 0.0338 | 252.89 | 249.98 | 0.0393 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 679.185 |  | 675.8073 | 0.4998 | 664.875 | 657.17 | 0.7862 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 276.76 |  | 275.5728 | 0.4308 | 286.73 | 280.14 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| SKHY | memory_hbm_storage | 176.55 |  | 175.7996 | 0.4269 | 183.63 | 176.08 | 0.7703 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
