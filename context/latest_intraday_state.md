# Intraday State

- Generated at: `2026-07-29T02:00:11+08:00`
- Market time ET: `2026-07-28T14:00:12-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 16, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 2, 'below_vwap': 8, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.82 |  | 673.9854 | 0.4206 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| SOXX | semiconductor_index | 491.14 |  | 489.9099 | 0.2511 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| SMH | semiconductor_index | 529.03 |  | 527.2994 | 0.3282 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| SPY | market_regime | 741.19 |  | 739.4419 | 0.2364 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.1 |  | 195.9856 | 0.5686 | 195.4 | 193.65 | 0.0254 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.39 |  | 378.5364 | 0.2255 | 378.64 | 371.57 | 0.0791 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.19 |  | 739.4419 | 0.2364 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.865 |  | 330.3465 | 1.6705 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.68 |  | 118.1936 | 2.1037 | 117.17 | 115.25 | 0.1409 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.39 |  | 378.5364 | 0.2255 | 378.64 | 371.57 | 0.0791 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.19 |  | 739.4419 | 0.2364 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 529.03 |  | 527.2994 | 0.3282 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| 4 | SOXX | semiconductor_index | 491.14 |  | 489.9099 | 0.2511 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| 5 | IWM | market_regime | 293.05 |  | 292.3181 | 0.2504 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 6 | NVDA | ai_accelerator | 197.1 |  | 195.9856 | 0.5686 | 195.4 | 193.65 | 0.0254 | buy_precheck_manual_confirm | none |
| 7 | MU | memory_hbm_storage | 817.9 |  | 815.2374 | 0.3266 | 846.4 | 813.91 | 0.1504 | watch_only | none |
| 8 | IREN | high_beta_ai_infrastructure | 33.72 |  | 33.7182 | 0.0052 | 35.08 | 33.52 | 0.0297 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 339.77 |  | 338.9146 | 0.2524 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 10 | TSM | foundry | 389.825 |  | 387.5211 | 0.5945 | 390.46 | 382.495 | 0.0385 | watch_only | none |
| 11 | QQQ | market_regime | 676.82 |  | 673.9854 | 0.4206 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 139.095 |  | 138.3888 | 0.5103 | 139.755 | 137.31 | 0.115 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 399.2 |  | 396.2841 | 0.7358 | 400.09 | 392.355 | 0.0225 | watch_only | none |
| 14 | AMZN | cloud_ai_capex | 231.58 |  | 230.4429 | 0.4934 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 191.43 |  | 190.7434 | 0.36 | 194.96 | 189.48 | 0.2037 | watch_only | none |
| 16 | TT | data_center_power_cooling | 465.8 |  | 465.0082 | 0.1703 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ONTO | semiconductor_test_packaging | 237.19 |  | 236.5921 | 0.2527 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | SMCI | ai_server_oem | 28.33 |  | 27.9814 | 1.2458 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 19 | ETN | data_center_power_cooling | 384.02 |  | 380.9252 | 0.8124 | 384.565 | 377.43 | 0.2187 | watch_only | none |
| 20 | ALAB | ai_networking_optical | 260.94 |  | 258.9335 | 0.7749 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.1 |  | 195.9856 | 0.5686 | 195.4 | 193.65 | 0.0254 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 379.39 |  | 378.5364 | 0.2255 | 378.64 | 371.57 | 0.0791 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.19 |  | 739.4419 | 0.2364 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.865 |  | 330.3465 | 1.6705 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| 5 | ORCL | cloud_ai_capex | 120.68 |  | 118.1936 | 2.1037 | 117.17 | 115.25 | 0.1409 | buy_precheck_manual_confirm | none |
| 6 | ANET | ai_networking_optical | 167.05 |  | 164.303 | 1.6719 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | TSM | foundry | 389.825 |  | 387.5211 | 0.5945 | 390.46 | 382.495 | 0.0385 | watch_only | none |
| 8 | MU | memory_hbm_storage | 817.9 |  | 815.2374 | 0.3266 | 846.4 | 813.91 | 0.1504 | watch_only | none |
| 9 | SMH | semiconductor_index | 529.03 |  | 527.2994 | 0.3282 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| 10 | SOXX | semiconductor_index | 491.14 |  | 489.9099 | 0.2511 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| 11 | QQQ | market_regime | 676.82 |  | 673.9854 | 0.4206 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| 12 | JCI | data_center_power_cooling | 139.095 |  | 138.3888 | 0.5103 | 139.755 | 137.31 | 0.115 | watch_only | none |
| 13 | ETN | data_center_power_cooling | 384.02 |  | 380.9252 | 0.8124 | 384.565 | 377.43 | 0.2187 | watch_only | none |
| 14 | IWM | market_regime | 293.05 |  | 292.3181 | 0.2504 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 191.43 |  | 190.7434 | 0.36 | 194.96 | 189.48 | 0.2037 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 399.2 |  | 396.2841 | 0.7358 | 400.09 | 392.355 | 0.0225 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 231.58 |  | 230.4429 | 0.4934 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.33 |  | 27.9814 | 1.2458 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 33.72 |  | 33.7182 | 0.0052 | 35.08 | 33.52 | 0.0297 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.77 |  | 338.9146 | 0.2524 | 342.87 | 337.78 | 0.0118 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.82 |  | 673.9854 | 0.4206 | 677.3 | 670.84 | 0.0059 | watch_only | none |
| TQQQ | leveraged_tool | 61.88 |  | 61.0772 | 1.3143 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.1 |  | 195.9856 | 0.5686 | 195.4 | 193.65 | 0.0254 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 399.2 |  | 396.2841 | 0.7358 | 400.09 | 392.355 | 0.0225 | watch_only | none |
| AAPL | mega_cap_platform | 339.77 |  | 338.9146 | 0.2524 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.865 |  | 330.3465 | 1.6705 | 330.21 | 324.97 | 0.0149 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.19 |  | 455.4915 | 0.5924 | 472.485 | 453.76 | 1.8442 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 389.825 |  | 387.5211 | 0.5945 | 390.46 | 382.495 | 0.0385 | watch_only | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.14 |  | 489.9099 | 0.2511 | 497.64 | 485.42 | 0.0509 | watch_only | none |
| SMH | semiconductor_index | 529.03 |  | 527.2994 | 0.3282 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| AVGO | custom_silicon_networking | 379.39 |  | 378.5364 | 0.2255 | 378.64 | 371.57 | 0.0791 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 817.9 |  | 815.2374 | 0.3266 | 846.4 | 813.91 | 0.1504 | watch_only | none |
| MRVL | custom_silicon_networking | 175.22 |  | 174.1327 | 0.6244 | 181.24 | 172.395 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| DELL | ai_server_oem | 383.255 |  | 374.7937 | 2.2576 | 402 | 374.02 | 1.135 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.26 |  | 44.4425 | -0.4108 | 46.19 | 44.33 | 0.0452 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 28.33 |  | 27.9814 | 1.2458 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.19 |  | 739.4419 | 0.2364 | 739.42 | 736.57 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.05 |  | 292.3181 | 0.2504 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.68 |  | 118.1936 | 2.1037 | 117.17 | 115.25 | 0.1409 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.44 |  | 66.2533 | 0.2818 | 68.995 | 65.635 | 2.0018 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 264.475 |  | 266.2454 | -0.6649 | 273.86 | 266.04 | 0.1701 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 384.02 |  | 380.9252 | 0.8124 | 384.565 | 377.43 | 0.2187 | watch_only | none |
| PWR | data_center_power_cooling | 584.065 |  | 582.0563 | 0.3451 | 603.25 | 584.69 | 0.1198 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 936.17 |  | 937.5426 | -0.1464 | 955.825 | 935.665 | 0.0545 | below_vwap | below_vwap |
| TT | data_center_power_cooling | 465.8 |  | 465.0082 | 0.1703 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.095 |  | 138.3888 | 0.5103 | 139.755 | 137.31 | 0.115 | watch_only | none |
| ANET | ai_networking_optical | 167.05 |  | 164.303 | 1.6719 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 242.69 |  | 237.1122 | 2.3524 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 642.49 |  | 631.4919 | 1.7416 | 673.65 | 624.91 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 340.47 |  | 337.2541 | 0.9535 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.27 |  | 85.7466 | 1.7766 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.94 |  | 258.9335 | 0.7749 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1576.7 |  | 1577.1402 | -0.0279 | 1586.01 | 1565.95 | 0.1313 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 473.05 |  | 476.5962 | -0.7441 | 494.87 | 477.03 | 0.6807 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 269.33 |  | 266.4052 | 1.0979 | 276.85 | 267.14 | 4.4555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.43 |  | 190.7434 | 0.36 | 194.96 | 189.48 | 0.2037 | watch_only | none |
| TER | semiconductor_test_packaging | 308.64 |  | 308.3964 | 0.079 | 315.21 | 304.11 | 0.6707 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 237.19 |  | 236.5921 | 0.2527 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.14 |  | 46.7696 | -1.3462 | 51.64 | 47.435 | 1.8422 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.935 |  | 42.4893 | -1.3047 | 44.155 | 41.78 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 117.97 |  | 119.3809 | -1.1818 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.77 |  | 282.4218 | -0.2308 | 296.8 | 283.22 | 0.763 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.795 |  | 518.4594 | -0.7068 | 518.6 | 511.495 | 0.0874 | below_vwap | below_vwap |
| APD | industrial_gases | 294.71 |  | 295.8413 | -0.3824 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.13 |  | 26.5244 | -1.4869 | 27 | 25.42 | 3.4443 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.72 |  | 33.7182 | 0.0052 | 35.08 | 33.52 | 0.0297 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.46 |  | 20.0388 | 2.102 | 20.97 | 19.755 | 0.0978 | watch_only | none |
| SNDK | memory_hbm_storage | 1081.255 |  | 1101.073 | -1.7999 | 1185.19 | 1114.57 | 3.0335 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 451.745 |  | 438.7552 | 2.9606 | 465.04 | 435.22 | 4.7881 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 750.48 |  | 729.159 | 2.9241 | 774.805 | 719.02 | 4.753 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.58 |  | 230.4429 | 0.4934 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 594.47 |  | 593.8332 | 0.1072 | 600.765 | 594.21 | 1.99 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 244.05 |  | 245.3172 | -0.5166 | 253.38 | 243.72 | 0.1967 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 131.51 |  | 131.6396 | -0.0985 | 136.45 | 131.735 | 0.9125 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
