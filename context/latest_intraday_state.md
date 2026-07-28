# Intraday State

- Generated at: `2026-07-29T00:35:52+08:00`
- Market time ET: `2026-07-28T12:35:53-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 17, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 23, 'price_stale_or_missing': 1, 'below_vwap': 5, 'below_opening_15m_low': 5}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.835 |  | 673.5346 | 0.49 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.94 |  | 489.5632 | 0.4855 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| SMH | semiconductor_index | 529.88 |  | 526.8966 | 0.5662 | 533.01 | 523.325 | 0.0547 | watch_only | none |
| SPY | market_regime | 741.24 |  | 738.9762 | 0.3063 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.84 |  | 195.6551 | 0.6056 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.59 |  | 377.9992 | 0.6854 | 378.64 | 371.57 | 0.092 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.24 |  | 738.9762 | 0.3063 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 333.165 |  | 329.2419 | 1.1915 | 330.21 | 324.97 | 0.09 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.36 |  | 117.6594 | 2.2953 | 117.17 | 115.25 | 0.1579 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.24 |  | 738.9762 | 0.3063 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 196.84 |  | 195.6551 | 0.6056 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 380.59 |  | 377.9992 | 0.6854 | 378.64 | 371.57 | 0.092 | buy_precheck_manual_confirm | none |
| 4 | IWM | market_regime | 292.865 |  | 292.0788 | 0.2692 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 5 | MU | memory_hbm_storage | 819.67 |  | 814.0587 | 0.6893 | 846.4 | 813.91 | 0.1074 | watch_only | none |
| 6 | SMH | semiconductor_index | 529.88 |  | 526.8966 | 0.5662 | 533.01 | 523.325 | 0.0547 | watch_only | none |
| 7 | SOXX | semiconductor_index | 491.94 |  | 489.5632 | 0.4855 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| 8 | QQQ | market_regime | 676.835 |  | 673.5346 | 0.49 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 231.32 |  | 230.1322 | 0.5162 | 233.05 | 229.7 | 0.0821 | watch_only | none |
| 10 | AAPL | mega_cap_platform | 340.37 |  | 338.7742 | 0.4711 | 342.87 | 337.78 | 0.0382 | watch_only | none |
| 11 | PWR | data_center_power_cooling | 584.84 |  | 581.1854 | 0.6288 | 603.25 | 584.69 | 0.2941 | watch_only | none |
| 12 | GEV | data_center_power_cooling | 943.36 |  | 936.6409 | 0.7174 | 955.825 | 935.665 | 0.2258 | watch_only | none |
| 13 | APLD | high_beta_ai_infrastructure | 26.72 |  | 26.5328 | 0.7057 | 27 | 25.42 | 0.1123 | watch_only | none |
| 14 | TER | semiconductor_test_packaging | 309.99 |  | 307.5373 | 0.7975 | 315.21 | 304.11 | 0.2258 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 398.1 |  | 395.9506 | 0.5429 | 400.09 | 392.355 | 0.2487 | watch_only | none |
| 16 | MKSI | semiconductor_materials | 283.445 |  | 281.9908 | 0.5157 | 296.8 | 283.22 | 0.3493 | watch_only | none |
| 17 | GOOGL | cloud_ai_capex | 333.165 |  | 329.2419 | 1.1915 | 330.21 | 324.97 | 0.09 | buy_precheck_manual_confirm | none |
| 18 | ARM | ai_accelerator | 245.48 |  | 245.1206 | 0.1466 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | APD | industrial_gases | 295.92 |  | 295.9067 | 0.0045 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SMCI | ai_server_oem | 28.3 |  | 27.8906 | 1.4678 | 28.86 | 27.59 | 0.0353 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.84 |  | 195.6551 | 0.6056 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.59 |  | 377.9992 | 0.6854 | 378.64 | 371.57 | 0.092 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.24 |  | 738.9762 | 0.3063 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 333.165 |  | 329.2419 | 1.1915 | 330.21 | 324.97 | 0.09 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.36 |  | 117.6594 | 2.2953 | 117.17 | 115.25 | 0.1579 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 390.52 |  | 386.9183 | 0.9309 | 390.46 | 382.495 | 1.3316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 166.66 |  | 163.7344 | 1.7868 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ETN | data_center_power_cooling | 385.23 |  | 379.9413 | 1.392 | 384.565 | 377.43 | 3.9379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | LIN | industrial_gases | 519.07 |  | 518.5289 | 0.1044 | 518.6 | 511.495 | 4.6448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | MU | memory_hbm_storage | 819.67 |  | 814.0587 | 0.6893 | 846.4 | 813.91 | 0.1074 | watch_only | none |
| 11 | SMH | semiconductor_index | 529.88 |  | 526.8966 | 0.5662 | 533.01 | 523.325 | 0.0547 | watch_only | none |
| 12 | SOXX | semiconductor_index | 491.94 |  | 489.5632 | 0.4855 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| 13 | QQQ | market_regime | 676.835 |  | 673.5346 | 0.49 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 14 | PWR | data_center_power_cooling | 584.84 |  | 581.1854 | 0.6288 | 603.25 | 584.69 | 0.2941 | watch_only | none |
| 15 | GEV | data_center_power_cooling | 943.36 |  | 936.6409 | 0.7174 | 955.825 | 935.665 | 0.2258 | watch_only | none |
| 16 | IWM | market_regime | 292.865 |  | 292.0788 | 0.2692 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 17 | TER | semiconductor_test_packaging | 309.99 |  | 307.5373 | 0.7975 | 315.21 | 304.11 | 0.2258 | watch_only | none |
| 18 | MSFT | cloud_ai_capex | 398.1 |  | 395.9506 | 0.5429 | 400.09 | 392.355 | 0.2487 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 231.32 |  | 230.1322 | 0.5162 | 233.05 | 229.7 | 0.0821 | watch_only | none |
| 20 | MKSI | semiconductor_materials | 283.445 |  | 281.9908 | 0.5157 | 296.8 | 283.22 | 0.3493 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.835 |  | 673.5346 | 0.49 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.98 |  | 60.8826 | 1.8026 | 62.01 | 60.23 | 0.0323 | watch_only | none |
| NVDA | ai_accelerator | 196.84 |  | 195.6551 | 0.6056 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.1 |  | 395.9506 | 0.5429 | 400.09 | 392.355 | 0.2487 | watch_only | none |
| AAPL | mega_cap_platform | 340.37 |  | 338.7742 | 0.4711 | 342.87 | 337.78 | 0.0382 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.165 |  | 329.2419 | 1.1915 | 330.21 | 324.97 | 0.09 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 459.72 |  | 454.8376 | 1.0734 | 472.485 | 453.76 | 3.3651 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 390.52 |  | 386.9183 | 0.9309 | 390.46 | 382.495 | 1.3316 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.94 |  | 489.5632 | 0.4855 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| SMH | semiconductor_index | 529.88 |  | 526.8966 | 0.5662 | 533.01 | 523.325 | 0.0547 | watch_only | none |
| AVGO | custom_silicon_networking | 380.59 |  | 377.9992 | 0.6854 | 378.64 | 371.57 | 0.092 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.67 |  | 814.0587 | 0.6893 | 846.4 | 813.91 | 0.1074 | watch_only | none |
| MRVL | custom_silicon_networking | 176.5 |  | 173.7302 | 1.5943 | 181.24 | 172.395 | 0.6516 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 383.64 |  | 374.0156 | 2.5733 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 44.8 |  | 44.4197 | 0.8562 | 46.19 | 44.33 | 1.6295 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SMCI | ai_server_oem | 28.3 |  | 27.8906 | 1.4678 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.24 |  | 738.9762 | 0.3063 | 739.42 | 736.57 | 0.0148 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.865 |  | 292.0788 | 0.2692 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.36 |  | 117.6594 | 2.2953 | 117.17 | 115.25 | 0.1579 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.6 |  | 66.0754 | 0.7939 | 68.995 | 65.635 | 4.5045 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.36 |  | 266.1348 | 0.0846 | 273.86 | 266.04 | 0.871 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.23 |  | 379.9413 | 1.392 | 384.565 | 377.43 | 3.9379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 584.84 |  | 581.1854 | 0.6288 | 603.25 | 584.69 | 0.2941 | watch_only | none |
| GEV | data_center_power_cooling | 943.36 |  | 936.6409 | 0.7174 | 955.825 | 935.665 | 0.2258 | watch_only | none |
| TT | data_center_power_cooling | 467.6 |  | 464.6704 | 0.6305 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.21 |  | 138.1689 | 0.7535 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.66 |  | 163.7344 | 1.7868 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 239.125 |  | 236.1637 | 1.2539 | 256.145 | 236.73 | 3.6926 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 644.07 |  | 628.3478 | 2.5021 | 673.65 | 624.91 | 0.5729 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 339.89 |  | 336.6232 | 0.9705 | 354.09 | 338.14 | 4.3514 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.58 |  | 85.4385 | 2.5064 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 264.25 |  | 258.47 | 2.2362 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1575.12 |  | 1576.1104 | -0.0628 | 1586.01 | 1565.95 |  | below_vwap | below_vwap,spread_unavailable |
| AMAT | semiconductor_equipment | 473.91 |  | 477.0236 | -0.6527 | 494.87 | 477.03 | 4.5916 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 266.92 |  | 265.9153 | 0.3778 | 276.85 | 267.14 | 2.2216 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| KLAC | semiconductor_equipment | 190.455 |  | 190.52 | -0.0341 | 194.96 | 189.48 | 0.3413 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 309.99 |  | 307.5373 | 0.7975 | 315.21 | 304.11 | 0.2258 | watch_only | none |
| ONTO | semiconductor_test_packaging | 235.9 |  | 236.4443 | -0.2302 | 248.8 | 236.42 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.66 |  | 46.8491 | -2.5382 | 51.64 | 47.435 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 41.99 |  | 42.5269 | -1.2625 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.92 |  | 119.4446 | -0.4392 | 121 | 117.72 | 0.3111 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 283.445 |  | 281.9908 | 0.5157 | 296.8 | 283.22 | 0.3493 | watch_only | none |
| LIN | industrial_gases | 519.07 |  | 518.5289 | 0.1044 | 518.6 | 511.495 | 4.6448 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 295.92 |  | 295.9067 | 0.0045 | 297.25 | 293.555 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.72 |  | 26.5328 | 0.7057 | 27 | 25.42 | 0.1123 | watch_only | none |
| IREN | high_beta_ai_infrastructure | 34.065 |  | 33.6672 | 1.1816 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.28 |  | 19.9957 | 1.4218 | 20.97 | 19.755 | 0.0493 | watch_only | none |
| SNDK | memory_hbm_storage | 1098.57 |  | 1102.6761 | -0.3724 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| WDC | memory_hbm_storage | 455.1 |  | 436.4533 | 4.2723 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 743.755 |  | 724.9965 | 2.5874 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.32 |  | 230.1322 | 0.5162 | 233.05 | 229.7 | 0.0821 | watch_only | none |
| META | cloud_ai_capex | 595.19 |  | 593.7666 | 0.2397 | 600.765 | 594.21 | 0.3948 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 245.48 |  | 245.1206 | 0.1466 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.38 |  | 131.5664 | 0.6184 | 136.45 | 131.735 | 1.6166 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
