# Intraday State

- Generated at: `2026-07-28T23:49:30+08:00`
- Market time ET: `2026-07-28T11:49:31-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'watch_only': 11, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_vwap': 4, 'below_opening_15m_low': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.74 |  | 672.7155 | 0.8955 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 498.01 |  | 489.1158 | 1.8184 | 497.64 | 485.42 | 0.0542 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 535.65 |  | 526.4629 | 1.7451 | 533.01 | 523.325 | 0.0373 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.34 |  | 738.5198 | 0.5173 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.53 |  | 195.2365 | 1.6869 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.51 |  | 385.9277 | 1.9647 | 390.46 | 382.495 | 0.0839 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 535.65 |  | 526.4629 | 1.7451 | 533.01 | 523.325 | 0.0373 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 498.01 |  | 489.1158 | 1.8184 | 497.64 | 485.42 | 0.0542 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 385.05 |  | 377.2258 | 2.0741 | 378.64 | 371.57 | 0.0597 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 742.34 |  | 738.5198 | 0.5173 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 678.74 |  | 672.7155 | 0.8955 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 333.16 |  | 328.6037 | 1.3866 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 293.625 |  | 291.9644 | 0.5688 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 120.27 |  | 116.9949 | 2.7993 | 117.17 | 115.25 | 0.0582 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 62.46 |  | 60.6933 | 2.9108 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 293.625 |  | 291.9644 | 0.5688 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 742.34 |  | 738.5198 | 0.5173 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 230.34 |  | 229.9313 | 0.1777 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.36 |  | 338.6055 | 0.2228 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 5 | QQQ | market_regime | 678.74 |  | 672.7155 | 0.8955 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 6 | MSFT | cloud_ai_capex | 397.48 |  | 395.6878 | 0.4529 | 400.09 | 392.355 | 0.0226 | watch_only | none |
| 7 | GOOGL | cloud_ai_capex | 333.16 |  | 328.6037 | 1.3866 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 8 | SOXX | semiconductor_index | 498.01 |  | 489.1158 | 1.8184 | 497.64 | 485.42 | 0.0542 | buy_precheck_manual_confirm | none |
| 9 | TSM | foundry | 393.51 |  | 385.9277 | 1.9647 | 390.46 | 382.495 | 0.0839 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 535.65 |  | 526.4629 | 1.7451 | 533.01 | 523.325 | 0.0373 | buy_precheck_manual_confirm | none |
| 11 | PWR | data_center_power_cooling | 587.66 |  | 579.5549 | 1.3985 | 603.25 | 584.69 | 0.2791 | watch_only | none |
| 12 | NVDA | ai_accelerator | 198.53 |  | 195.2365 | 1.6869 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 13 | AVGO | custom_silicon_networking | 385.05 |  | 377.2258 | 2.0741 | 378.64 | 371.57 | 0.0597 | buy_precheck_manual_confirm | none |
| 14 | ORCL | cloud_ai_capex | 120.27 |  | 116.9949 | 2.7993 | 117.17 | 115.25 | 0.0582 | buy_precheck_manual_confirm | none |
| 15 | HPE | ai_server_oem | 45.31 |  | 44.3101 | 2.2567 | 46.19 | 44.33 | 0.0883 | watch_only | none |
| 16 | SMCI | ai_server_oem | 28.59 |  | 27.8173 | 2.7778 | 28.86 | 27.59 | 0.035 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 34.77 |  | 33.5291 | 3.701 | 35.08 | 33.52 | 0.0288 | watch_only | none |
| 18 | CORZ | high_beta_ai_infrastructure | 20.45 |  | 19.9544 | 2.4839 | 20.97 | 19.755 | 0.0978 | watch_only | none |
| 19 | KLAC | semiconductor_equipment | 193.54 |  | 190.1612 | 1.7768 | 194.96 | 189.48 | 0.1963 | watch_only | none |
| 20 | LITE | ai_networking_optical | 643.11 |  | 625.5701 | 2.8038 | 673.65 | 624.91 | 0.2379 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.53 |  | 195.2365 | 1.6869 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 393.51 |  | 385.9277 | 1.9647 | 390.46 | 382.495 | 0.0839 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 535.65 |  | 526.4629 | 1.7451 | 533.01 | 523.325 | 0.0373 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 498.01 |  | 489.1158 | 1.8184 | 497.64 | 485.42 | 0.0542 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 385.05 |  | 377.2258 | 2.0741 | 378.64 | 371.57 | 0.0597 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 742.34 |  | 738.5198 | 0.5173 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | QQQ | market_regime | 678.74 |  | 672.7155 | 0.8955 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 8 | GOOGL | cloud_ai_capex | 333.16 |  | 328.6037 | 1.3866 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| 9 | IWM | market_regime | 293.625 |  | 291.9644 | 0.5688 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 10 | ORCL | cloud_ai_capex | 120.27 |  | 116.9949 | 2.7993 | 117.17 | 115.25 | 0.0582 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 62.46 |  | 60.6933 | 2.9108 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| 12 | ASML | semiconductor_equipment | 1594.98 |  | 1573.2289 | 1.3826 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ANET | ai_networking_optical | 166.77 |  | 163.3369 | 2.1019 | 165.975 | 160.51 | 1.4811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | ETN | data_center_power_cooling | 387.165 |  | 379.2668 | 2.0825 | 384.565 | 377.43 | 3.9182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 587.66 |  | 579.5549 | 1.3985 | 603.25 | 584.69 | 0.2791 | watch_only | none |
| 16 | KLAC | semiconductor_equipment | 193.54 |  | 190.1612 | 1.7768 | 194.96 | 189.48 | 0.1963 | watch_only | none |
| 17 | LITE | ai_networking_optical | 643.11 |  | 625.5701 | 2.8038 | 673.65 | 624.91 | 0.2379 | watch_only | none |
| 18 | APLD | high_beta_ai_infrastructure | 27 |  | 26.4532 | 2.0669 | 27 | 25.42 | 3.7407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MSFT | cloud_ai_capex | 397.48 |  | 395.6878 | 0.4529 | 400.09 | 392.355 | 0.0226 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 230.34 |  | 229.9313 | 0.1777 | 233.05 | 229.7 | 0.013 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.74 |  | 672.7155 | 0.8955 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.46 |  | 60.6933 | 2.9108 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 198.53 |  | 195.2365 | 1.6869 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.48 |  | 395.6878 | 0.4529 | 400.09 | 392.355 | 0.0226 | watch_only | none |
| AAPL | mega_cap_platform | 339.36 |  | 338.6055 | 0.2228 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.16 |  | 328.6037 | 1.3866 | 330.21 | 324.97 | 0.018 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 464 |  | 453.6009 | 2.2926 | 472.485 | 453.76 | 4.7845 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 393.51 |  | 385.9277 | 1.9647 | 390.46 | 382.495 | 0.0839 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 498.01 |  | 489.1158 | 1.8184 | 497.64 | 485.42 | 0.0542 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 535.65 |  | 526.4629 | 1.7451 | 533.01 | 523.325 | 0.0373 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 385.05 |  | 377.2258 | 2.0741 | 378.64 | 371.57 | 0.0597 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 830 |  | 812.8286 | 2.1125 | 846.4 | 813.91 | 1.394 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 179.21 |  | 173.1826 | 3.4804 | 181.24 | 172.395 | 2.1874 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 386.095 |  | 372.8325 | 3.5572 | 402 | 374.02 | 3.6675 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.31 |  | 44.3101 | 2.2567 | 46.19 | 44.33 | 0.0883 | watch_only | none |
| SMCI | ai_server_oem | 28.59 |  | 27.8173 | 2.7778 | 28.86 | 27.59 | 0.035 | watch_only | none |
| SPY | market_regime | 742.34 |  | 738.5198 | 0.5173 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.625 |  | 291.9644 | 0.5688 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.27 |  | 116.9949 | 2.7993 | 117.17 | 115.25 | 0.0582 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.19 |  | 65.9598 | 1.8651 | 68.995 | 65.635 | 1.4883 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.68 |  | 265.8193 | 1.4524 | 273.86 | 266.04 | 1.6241 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 387.165 |  | 379.2668 | 2.0825 | 384.565 | 377.43 | 3.9182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 587.66 |  | 579.5549 | 1.3985 | 603.25 | 584.69 | 0.2791 | watch_only | none |
| GEV | data_center_power_cooling | 952.46 |  | 934.4373 | 1.9287 | 955.825 | 935.665 | 0.7339 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 469.28 |  | 464.4406 | 1.042 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.4 |  | 138.0014 | 1.0135 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 166.77 |  | 163.3369 | 2.1019 | 165.975 | 160.51 | 1.4811 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 241.16 |  | 235.9273 | 2.2179 | 256.145 | 236.73 | 0.2115 | watch_only | none |
| LITE | ai_networking_optical | 643.11 |  | 625.5701 | 2.8038 | 673.65 | 624.91 | 0.2379 | watch_only | none |
| CIEN | ai_networking_optical | 344.3 |  | 336.0504 | 2.4549 | 354.09 | 338.14 | 0.3776 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.65 |  | 85.2056 | 4.0425 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 265.71 |  | 256.6495 | 3.5303 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1594.98 |  | 1573.2289 | 1.3826 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 481.455 |  | 476.8882 | 0.9576 | 494.87 | 477.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LRCX | semiconductor_equipment | 269.545 |  | 265.6341 | 1.4723 | 276.85 | 267.14 | 3.1535 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 193.54 |  | 190.1612 | 1.7768 | 194.96 | 189.48 | 0.1963 | watch_only | none |
| TER | semiconductor_test_packaging | 314.58 |  | 306.3364 | 2.691 | 315.21 | 304.11 | 4.5457 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 237.84 |  | 236.4042 | 0.6073 | 248.8 | 236.42 | 4.2297 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.905 |  | 47.0625 | -0.3346 | 51.64 | 47.435 | 4.3919 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.53 |  | 42.5512 | -0.0498 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 120.41 |  | 119.3973 | 0.8482 | 121 | 117.72 | 3.8535 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 285 |  | 281.5647 | 1.2201 | 296.8 | 283.22 | 3.7965 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 517.72 |  | 518.5573 | -0.1615 | 518.6 | 511.495 | 4.4561 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 294.195 |  | 296.0903 | -0.6401 | 297.25 | 293.555 | 0.3263 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 27 |  | 26.4532 | 2.0669 | 27 | 25.42 | 3.7407 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.77 |  | 33.5291 | 3.701 | 35.08 | 33.52 | 0.0288 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.45 |  | 19.9544 | 2.4839 | 20.97 | 19.755 | 0.0978 | watch_only | none |
| SNDK | memory_hbm_storage | 1112.81 |  | 1101.9473 | 0.9858 | 1185.19 | 1114.57 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| WDC | memory_hbm_storage | 450.83 |  | 434.7902 | 3.6891 | 465.04 | 435.22 | 2.0717 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 742.21 |  | 723.3947 | 2.601 | 774.805 | 719.02 | 3.6634 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 230.34 |  | 229.9313 | 0.1777 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594.01 |  | 593.204 | 0.1359 | 600.765 | 594.21 | 0.8956 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| ARM | ai_accelerator | 248 |  | 244.8871 | 1.2711 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.81 |  | 131.3859 | 1.8451 | 136.45 | 131.735 | 1.0089 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
