# Intraday State

- Generated at: `2026-07-16T01:45:03+08:00`
- Market time ET: `2026-07-15T13:45:04-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 42, 'manual_confirm_candidate': 5, 'price_stale_or_missing': 2, 'below_vwap': 2, 'spread_too_wide_or_missing': 1, 'watch_only': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.97 |  | 716.1743 | -0.0285 | 724.31 | 721.08 | 0.0028 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 551.22 |  | 551.0906 | 0.0235 | 575.7 | 565.33 | 0.0671 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 585.75 |  | 587.2317 | -0.2523 | 606.85 | 597.81 | 0.058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.38 |  | 753.1265 | 0.0337 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.33 |  | 395.1078 | 0.3093 | 391.33 | 387.05 | 0.0328 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.08 |  | 295.5931 | 0.1647 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.68 |  | 368.5899 | 0.5671 | 364.41 | 357.885 | 0.0459 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.19 |  | 254.44 | 0.2948 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.33 |  | 325.427 | 0.5848 | 321.14 | 317.4 | 0.2383 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 296.08 |  | 295.5931 | 0.1647 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 2 | MSFT | cloud_ai_capex | 396.33 |  | 395.1078 | 0.3093 | 391.33 | 387.05 | 0.0328 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 255.19 |  | 254.44 | 0.2948 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 370.68 |  | 368.5899 | 0.5671 | 364.41 | 357.885 | 0.0459 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.33 |  | 325.427 | 0.5848 | 321.14 | 317.4 | 0.2383 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1785.79 |  | 1770.8587 | 0.8432 | 1829.9 | 1759.045 | 0.0672 | watch_only | none |
| 7 | IREN | high_beta_ai_infrastructure | 39.5 |  | 39.0843 | 1.0635 | 40.01 | 38.815 | 0.0253 | watch_only | none |
| 8 | NVDA | ai_accelerator | 209.22 |  | 209.1525 | 0.0323 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 9 | SOXX | semiconductor_index | 551.22 |  | 551.0906 | 0.0235 | 575.7 | 565.33 | 0.0671 | below_opening_15m_low | below_opening_15m_low |
| 10 | SPY | market_regime | 753.38 |  | 753.1265 | 0.0337 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 11 | TT | data_center_power_cooling | 479.545 |  | 478.7159 | 0.1732 | 485.9 | 482.93 | 0.1335 | below_opening_15m_low | below_opening_15m_low |
| 12 | CORZ | high_beta_ai_infrastructure | 22.26 |  | 21.6979 | 2.5907 | 22.36 | 21.94 | 0.0898 | watch_only | none |
| 13 | APLD | high_beta_ai_infrastructure | 28.81 |  | 28.1216 | 2.4479 | 29.055 | 28.28 | 0.1041 | watch_only | none |
| 14 | TER | semiconductor_test_packaging | 335.93 |  | 335.3931 | 0.1601 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 647.67 |  | 644.2418 | 0.5321 | 663.475 | 653.94 | 0.1204 | below_opening_15m_low | below_opening_15m_low |
| 16 | ETN | data_center_power_cooling | 409.995 |  | 408.3649 | 0.3992 | 417.84 | 413.82 | 0.1244 | below_opening_15m_low | below_opening_15m_low |
| 17 | AMKR | semiconductor_test_packaging | 66.99 |  | 66.7856 | 0.3061 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 392.3 |  | 391.6858 | 0.1568 | 397.94 | 392.62 | 1.509 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 19 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 20 | AMD | ai_accelerator | 528.34 |  | 527.0931 | 0.2366 | 558.62 | 548.745 | 0.9142 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 396.33 |  | 395.1078 | 0.3093 | 391.33 | 387.05 | 0.0328 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.08 |  | 295.5931 | 0.1647 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 370.68 |  | 368.5899 | 0.5671 | 364.41 | 357.885 | 0.0459 | buy_precheck_manual_confirm | none |
| 4 | AMZN | cloud_ai_capex | 255.19 |  | 254.44 | 0.2948 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| 5 | AAPL | mega_cap_platform | 327.33 |  | 325.427 | 0.5848 | 321.14 | 317.4 | 0.2383 | buy_precheck_manual_confirm | none |
| 6 | META | cloud_ai_capex | 675.375 |  | 675.4595 | -0.0125 | 664.875 | 657.17 | 1.5251 | below_vwap | below_vwap,spread_too_wide |
| 7 | ASML | semiconductor_equipment | 1785.79 |  | 1770.8587 | 0.8432 | 1829.9 | 1759.045 | 0.0672 | watch_only | none |
| 8 | CORZ | high_beta_ai_infrastructure | 22.26 |  | 21.6979 | 2.5907 | 22.36 | 21.94 | 0.0898 | watch_only | none |
| 9 | IREN | high_beta_ai_infrastructure | 39.5 |  | 39.0843 | 1.0635 | 40.01 | 38.815 | 0.0253 | watch_only | none |
| 10 | APLD | high_beta_ai_infrastructure | 28.81 |  | 28.1216 | 2.4479 | 29.055 | 28.28 | 0.1041 | watch_only | none |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | ORCL | cloud_ai_capex | 132.895 |  | 131.6345 | 0.9576 | 132.925 | 129.92 | 0.6321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | NVDA | ai_accelerator | 209.22 |  | 209.1525 | 0.0323 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| 14 | SOXX | semiconductor_index | 551.22 |  | 551.0906 | 0.0235 | 575.7 | 565.33 | 0.0671 | below_opening_15m_low | below_opening_15m_low |
| 15 | AVGO | custom_silicon_networking | 392.3 |  | 391.6858 | 0.1568 | 397.94 | 392.62 | 1.509 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 16 | SPY | market_regime | 753.38 |  | 753.1265 | 0.0337 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| 17 | AMD | ai_accelerator | 528.34 |  | 527.0931 | 0.2366 | 558.62 | 548.745 | 0.9142 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 18 | TT | data_center_power_cooling | 479.545 |  | 478.7159 | 0.1732 | 485.9 | 482.93 | 0.1335 | below_opening_15m_low | below_opening_15m_low |
| 19 | VRT | data_center_power_cooling | 299.875 |  | 298.9908 | 0.2957 | 309.345 | 304.67 | 3.8083 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| 20 | SNDK | memory_hbm_storage | 1594.44 |  | 1562.7595 | 2.0272 | 1726.34 | 1665.91 | 0.1223 | below_opening_15m_low | below_opening_15m_low |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 715.97 |  | 716.1743 | -0.0285 | 724.31 | 721.08 | 0.0028 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 73.86 |  | 74.1946 | -0.4509 | 76.46 | 75.39 | 0.0135 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 209.22 |  | 209.1525 | 0.0323 | 213.775 | 211.225 | 0.0143 | below_opening_15m_low | below_opening_15m_low |
| MSFT | cloud_ai_capex | 396.33 |  | 395.1078 | 0.3093 | 391.33 | 387.05 | 0.0328 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 327.33 |  | 325.427 | 0.5848 | 321.14 | 317.4 | 0.2383 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 370.68 |  | 368.5899 | 0.5671 | 364.41 | 357.885 | 0.0459 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 528.34 |  | 527.0931 | 0.2366 | 558.62 | 548.745 | 0.9142 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TSM | foundry | 418.31 |  | 418.8546 | -0.13 | 428.59 | 422.945 | 0.5809 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 2082000 |  | 2013801.8151 | 3.3865 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 551.22 |  | 551.0906 | 0.0235 | 575.7 | 565.33 | 0.0671 | below_opening_15m_low | below_opening_15m_low |
| SMH | semiconductor_index | 585.75 |  | 587.2317 | -0.2523 | 606.85 | 597.81 | 0.058 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 392.3 |  | 391.6858 | 0.1568 | 397.94 | 392.62 | 1.509 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| MU | memory_hbm_storage | 905.56 |  | 910.1387 | -0.5031 | 977.7 | 953.67 | 0.275 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 206.905 |  | 208.542 | -0.785 | 223.02 | 214.85 | 3.3832 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.39 |  | 407.5096 | -1.9925 | 457.935 | 442.67 | 4.0988 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 46.6 |  | 46.9267 | -0.6961 | 50.2 | 48.995 | 0.0215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 26.74 |  | 26.8677 | -0.4753 | 28.295 | 27.55 | 0.0374 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.38 |  | 753.1265 | 0.0337 | 755.54 | 754.215 | 0.004 | below_opening_15m_low | below_opening_15m_low |
| IWM | market_regime | 296.08 |  | 295.5931 | 0.1647 | 296.08 | 294.86 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 132.895 |  | 131.6345 | 0.9576 | 132.925 | 129.92 | 0.6321 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 77.09 |  | 77.3882 | -0.3853 | 80.585 | 78.73 | 2.7889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 299.875 |  | 298.9908 | 0.2957 | 309.345 | 304.67 | 3.8083 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ETN | data_center_power_cooling | 409.995 |  | 408.3649 | 0.3992 | 417.84 | 413.82 | 0.1244 | below_opening_15m_low | below_opening_15m_low |
| PWR | data_center_power_cooling | 647.67 |  | 644.2418 | 0.5321 | 663.475 | 653.94 | 0.1204 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 1044.56 |  | 1031.5353 | 1.2626 | 1073.34 | 1059.27 | 3.2789 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| TT | data_center_power_cooling | 479.545 |  | 478.7159 | 0.1732 | 485.9 | 482.93 | 0.1335 | below_opening_15m_low | below_opening_15m_low |
| JCI | data_center_power_cooling | 141.53 |  | 141.6816 | -0.107 | 145.99 | 144.625 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 169.9 |  | 171.9411 | -1.1871 | 186.095 | 178.355 | 4.7087 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 292.355 |  | 293.8575 | -0.5113 | 315.74 | 303.34 | 3.4205 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 746.52 |  | 748.1175 | -0.2135 | 820.15 | 780.365 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 417.61 |  | 418.8771 | -0.3025 | 438.14 | 427.54 | 4.1187 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.95 |  | 112.3535 | -1.2492 | 123.995 | 117.25 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 346.16 |  | 344.6136 | 0.4487 | 369.23 | 356.615 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ASML | semiconductor_equipment | 1785.79 |  | 1770.8587 | 0.8432 | 1829.9 | 1759.045 | 0.0672 | watch_only | none |
| AMAT | semiconductor_equipment | 573.24 |  | 577.7407 | -0.779 | 610.62 | 586.86 | 0.0872 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 328.93 |  | 331.4356 | -0.756 | 355.245 | 340.745 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 221.525 |  | 222.604 | -0.4847 | 236.49 | 225.11 | 3.8325 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 335.93 |  | 335.3931 | 0.1601 | 356.29 | 343.785 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| ONTO | semiconductor_test_packaging | 303.61 |  | 307.5016 | -1.2655 | 326.25 | 317.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.99 |  | 66.7856 | 0.3061 | 70.42 | 68.43 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.675 |  | 54.3334 | -1.2118 | 57.92 | 55.2 |  | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 137.18 |  | 137.6681 | -0.3545 | 143.15 | 140.4 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 350.1 |  | 348.4173 | 0.483 | 368.67 | 358.39 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| LIN | industrial_gases | 516.05 |  | 516.1072 | -0.0111 | 521.075 | 518.3 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APD | industrial_gases | 293.85 |  | 295.11 | -0.4269 | 297.8 | 295.655 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 28.81 |  | 28.1216 | 2.4479 | 29.055 | 28.28 | 0.1041 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 39.5 |  | 39.0843 | 1.0635 | 40.01 | 38.815 | 0.0253 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 22.26 |  | 21.6979 | 2.5907 | 22.36 | 21.94 | 0.0898 | watch_only | none |
| SNDK | memory_hbm_storage | 1594.44 |  | 1562.7595 | 2.0272 | 1726.34 | 1665.91 | 0.1223 | below_opening_15m_low | below_opening_15m_low |
| WDC | memory_hbm_storage | 508.285 |  | 516.9034 | -1.6673 | 568.16 | 542.4 | 0.9384 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 810.77 |  | 817.2801 | -0.7966 | 889.1 | 850.01 | 2.8356 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.19 |  | 254.44 | 0.2948 | 252.89 | 249.98 | 0.0196 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 675.375 |  | 675.4595 | -0.0125 | 664.875 | 657.17 | 1.5251 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 272.355 |  | 276.0259 | -1.3299 | 286.73 | 280.14 | 3.5982 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 175.275 |  | 175.6096 | -0.1905 | 183.63 | 176.08 | 3.8967 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
