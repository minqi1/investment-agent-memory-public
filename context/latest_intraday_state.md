# Intraday State

- Generated at: `2026-07-16T01:43:40+08:00`
- Market time ET: `2026-07-15T13:43:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 41, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 3, 'below_vwap': 2, 'watch_only': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.73 |  | 716.1748 | -0.0621 | 724.31 | 721.08 | 0.0014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 550.69 |  | 551.0906 | -0.0727 | 575.7 | 565.33 | 0.0763 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.59 |  | 587.2329 | -0.2798 | 606.85 | 597.81 | 0.0649 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.23 |  | 753.126 | 0.0138 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.41 |  | 395.1063 | 0.33 | 391.33 | 387.05 | 0.0605 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.61 |  | 368.5844 | 0.5496 | 364.41 | 357.885 | 0.143 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.13 |  | 254.4379 | 0.272 | 252.89 | 249.98 | 0.1764 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.35 |  | 325.4242 | 0.5918 | 321.14 | 317.4 | 0.165 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.41 |  | 395.1063 | 0.33 | 391.33 | 387.05 | 0.0605 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.02 |  | 295.5913 | 0.145 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 3 | AMZN | cloud_ai_capex | 255.13 |  | 254.4379 | 0.272 | 252.89 | 249.98 | 0.1764 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1784.915 |  | 1770.8232 | 0.7958 | 1829.9 | 1759.045 | 0.088 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 370.61 |  | 368.5844 | 0.5496 | 364.41 | 357.885 | 0.143 | buy_precheck_manual_confirm | none |
| 6 | AAPL | mega_cap_platform | 327.35 |  | 325.4242 | 0.5918 | 321.14 | 317.4 | 0.165 | buy_precheck_manual_confirm | none |
| 7 | ORCL | cloud_ai_capex | 132.87 |  | 131.6323 | 0.9403 | 132.925 | 129.92 | 0.0452 | watch_only | none |
| 8 | IREN | high_beta_ai_infrastructure | 39.505 |  | 39.083 | 1.0797 | 40.01 | 38.815 | 0.0253 | watch_only | none |
| 9 | SPY | market_regime | 753.23 |  | 753.126 | 0.0138 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| 10 | CORZ | high_beta_ai_infrastructure | 22.23 |  | 21.6961 | 2.461 | 22.36 | 21.94 | 0.135 | watch_only | none |
| 11 | APLD | high_beta_ai_infrastructure | 28.76 |  | 28.1008 | 2.3457 | 29.055 | 28.28 | 0.2782 | watch_only | none |
| 12 | TT | data_center_power_cooling | 479.545 |  | 478.7159 | 0.1732 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 13 | VRT | data_center_power_cooling | 299.61 |  | 298.9896 | 0.2075 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 14 | ETN | data_center_power_cooling | 409.655 |  | 408.3581 | 0.3176 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 335.93 |  | 335.3931 | 0.1601 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 16 | PWR | data_center_power_cooling | 647.67 |  | 644.2418 | 0.5321 | 663.475 | 653.94 | 0.122 | below_opening_15m_low | below_opening_15m_low |
| 17 | AVGO | custom_silicon_networking | 392.07 |  | 391.685 | 0.0983 | 397.94 | 392.62 | 1.4691 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 19 | AMD | ai_accelerator | 527.32 |  | 527.0912 | 0.0434 | 558.62 | 548.745 | 0.4893 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | ALAB | ai_networking_optical | 346.16 |  | 344.6136 | 0.4487 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.41 |  | 395.1063 | 0.33 | 391.33 | 387.05 | 0.0605 | buy_precheck_manual_confirm | none |
| 2 | GOOGL | cloud_ai_capex | 370.61 |  | 368.5844 | 0.5496 | 364.41 | 357.885 | 0.143 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.13 |  | 254.4379 | 0.272 | 252.89 | 249.98 | 0.1764 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 327.35 |  | 325.4242 | 0.5918 | 321.14 | 317.4 | 0.165 | buy_precheck_manual_confirm | none |
| 5 | META | cloud_ai_capex | 674.81 |  | 675.4604 | -0.0963 | 664.875 | 657.17 | 1.6983 | below_vwap | below_vwap,spread_too_wide |
| 6 | ASML | semiconductor_equipment | 1784.915 |  | 1770.8232 | 0.7958 | 1829.9 | 1759.045 | 0.088 | watch_only | none |
| 7 | IWM | market_regime | 296.02 |  | 295.5913 | 0.145 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| 8 | ORCL | cloud_ai_capex | 132.87 |  | 131.6323 | 0.9403 | 132.925 | 129.92 | 0.0452 | watch_only | none |
| 9 | CORZ | high_beta_ai_infrastructure | 22.23 |  | 21.6961 | 2.461 | 22.36 | 21.94 | 0.135 | watch_only | none |
| 10 | IREN | high_beta_ai_infrastructure | 39.505 |  | 39.083 | 1.0797 | 40.01 | 38.815 | 0.0253 | watch_only | none |
| 11 | APLD | high_beta_ai_infrastructure | 28.76 |  | 28.1008 | 2.3457 | 29.055 | 28.28 | 0.2782 | watch_only | none |
| 12 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 392.07 |  | 391.685 | 0.0983 | 397.94 | 392.62 | 1.4691 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 14 | SPY | market_regime | 753.23 |  | 753.126 | 0.0138 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| 15 | AMD | ai_accelerator | 527.32 |  | 527.0912 | 0.0434 | 558.62 | 548.745 | 0.4893 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | TT | data_center_power_cooling | 479.545 |  | 478.7159 | 0.1732 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 17 | VRT | data_center_power_cooling | 299.61 |  | 298.9896 | 0.2075 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | SNDK | memory_hbm_storage | 1590.09 |  | 1562.6641 | 1.7551 | 1726.34 | 1665.91 | 2.9973 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | PWR | data_center_power_cooling | 647.67 |  | 644.2418 | 0.5321 | 663.475 | 653.94 | 0.122 | below_opening_15m_low | below_opening_15m_low |
| 20 | GEV | data_center_power_cooling | 1043.13 |  | 1031.4868 | 1.1288 | 1073.34 | 1059.27 | 0.1821 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.73 |  | 716.1748 | -0.0621 | 724.31 | 721.08 | 0.0014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.79 |  | 74.1949 | -0.5457 | 76.46 | 75.39 | 0.0136 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 208.88 |  | 209.1526 | -0.1303 | 213.775 | 211.225 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 396.41 |  | 395.1063 | 0.33 | 391.33 | 387.05 | 0.0605 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.35 |  | 325.4242 | 0.5918 | 321.14 | 317.4 | 0.165 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.61 |  | 368.5844 | 0.5496 | 364.41 | 357.885 | 0.143 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 527.32 |  | 527.0912 | 0.0434 | 558.62 | 548.745 | 0.4893 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 418.205 |  | 418.8566 | -0.1556 | 428.59 | 422.945 | 0.1172 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 550.69 |  | 551.0906 | -0.0727 | 575.7 | 565.33 | 0.0763 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 585.59 |  | 587.2329 | -0.2798 | 606.85 | 597.81 | 0.0649 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 392.07 |  | 391.685 | 0.0983 | 397.94 | 392.62 | 1.4691 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MU | memory_hbm_storage | 905 |  | 910.1565 | -0.5665 | 977.7 | 953.67 | 0.1989 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 207.05 |  | 208.5437 | -0.7162 | 223.02 | 214.85 | 0.1159 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 399.625 |  | 407.5203 | -1.9374 | 457.935 | 442.67 | 0.3078 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| HPE | ai_server_oem | 46.58 |  | 46.9274 | -0.7404 | 50.2 | 48.995 | 0.0429 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.725 |  | 26.8683 | -0.5333 | 28.295 | 27.55 | 0.0374 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.23 |  | 753.126 | 0.0138 | 755.54 | 754.215 | 0.0027 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 296.02 |  | 295.5913 | 0.145 | 296.08 | 294.86 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 132.87 |  | 131.6323 | 0.9403 | 132.925 | 129.92 | 0.0452 | watch_only | none |
| CRWV | gpu_cloud_ai_factory | 77.08 |  | 77.3889 | -0.3991 | 80.585 | 78.73 | 0.1427 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| VRT | data_center_power_cooling | 299.61 |  | 298.9896 | 0.2075 | 309.345 | 304.67 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ETN | data_center_power_cooling | 409.655 |  | 408.3581 | 0.3176 | 417.84 | 413.82 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| PWR | data_center_power_cooling | 647.67 |  | 644.2418 | 0.5321 | 663.475 | 653.94 | 0.122 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1043.13 |  | 1031.4868 | 1.1288 | 1073.34 | 1059.27 | 0.1821 | below_opening_15m_low | below_opening_15m_low |
| TT | data_center_power_cooling | 479.545 |  | 478.7159 | 0.1732 | 485.9 | 482.93 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| JCI | data_center_power_cooling | 141.53 |  | 141.6816 | -0.107 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.9 |  | 171.9411 | -1.1871 | 186.095 | 178.355 | 4.7087 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 292.125 |  | 293.8615 | -0.5909 | 315.74 | 303.34 | 3.4232 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 746.13 |  | 748.1243 | -0.2666 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 417.755 |  | 418.8793 | -0.2684 | 438.14 | 427.54 | 4.0239 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.96 |  | 112.3544 | -1.2411 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 346.16 |  | 344.6136 | 0.4487 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1784.915 |  | 1770.8232 | 0.7958 | 1829.9 | 1759.045 | 0.088 | watch_only | none |
| AMAT | semiconductor_equipment | 573.24 |  | 577.7407 | -0.779 | 610.62 | 586.86 | 0.1989 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 328.96 |  | 331.4383 | -0.7477 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 221.31 |  | 222.6048 | -0.5816 | 236.49 | 225.11 | 3.8588 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 335.93 |  | 335.3931 | 0.1601 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 303.61 |  | 307.5016 | -1.2655 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.76 |  | 66.7846 | -0.0369 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.675 |  | 54.3334 | -1.2118 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 136.65 |  | 137.6698 | -0.7408 | 143.15 | 140.4 | 3.0223 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| MKSI | semiconductor_materials | 349.77 |  | 348.4131 | 0.3895 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.06 |  | 516.1073 | -0.0092 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.85 |  | 295.11 | -0.4269 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.76 |  | 28.1008 | 2.3457 | 29.055 | 28.28 | 0.2782 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.505 |  | 39.083 | 1.0797 | 40.01 | 38.815 | 0.0253 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.23 |  | 21.6961 | 2.461 | 22.36 | 21.94 | 0.135 | watch_only | none |
| SNDK | memory_hbm_storage | 1590.09 |  | 1562.6641 | 1.7551 | 1726.34 | 1665.91 | 2.9973 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 506.505 |  | 516.9825 | -2.0267 | 568.16 | 542.4 | 1.3188 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 810.01 |  | 817.2912 | -0.8909 | 889.1 | 850.01 | 4.7814 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.13 |  | 254.4379 | 0.272 | 252.89 | 249.98 | 0.1764 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 674.81 |  | 675.4604 | -0.0963 | 664.875 | 657.17 | 1.6983 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 272.355 |  | 276.0259 | -1.3299 | 286.73 | 280.14 | 3.5982 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 174.79 |  | 175.6106 | -0.4673 | 183.63 | 176.08 | 4.0563 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
