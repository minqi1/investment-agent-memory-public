# Intraday State

- Generated at: `2026-07-29T02:23:15+08:00`
- Market time ET: `2026-07-28T14:23:16-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 16, 'manual_confirm_candidate': 6, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 1, 'below_vwap': 10, 'below_opening_15m_low': 6}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.08 |  | 674.0654 | 0.2989 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| SOXX | semiconductor_index | 490.4 |  | 489.9597 | 0.0899 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| SMH | semiconductor_index | 528.87 |  | 527.3281 | 0.2924 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| SPY | market_regime | 740.81 |  | 739.4967 | 0.1776 | 739.42 | 736.57 | 0.0243 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.14 |  | 196.0227 | 0.57 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.205 |  | 387.6205 | 0.9247 | 390.46 | 382.495 | 0.0307 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.81 |  | 739.4967 | 0.1776 | 739.42 | 736.57 | 0.0243 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.175 |  | 330.5711 | 1.3927 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 139.91 |  | 138.4811 | 1.0318 | 139.755 | 137.31 | 0.1072 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.51 |  | 118.3684 | 1.8092 | 117.17 | 115.25 | 0.166 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.81 |  | 739.4967 | 0.1776 | 739.42 | 736.57 | 0.0243 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 816.49 |  | 815.3178 | 0.1438 | 846.4 | 813.91 | 0.0625 | watch_only | none |
| 3 | SMH | semiconductor_index | 528.87 |  | 527.3281 | 0.2924 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| 4 | SOXX | semiconductor_index | 490.4 |  | 489.9597 | 0.0899 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| 5 | QQQ | market_regime | 676.08 |  | 674.0654 | 0.2989 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| 6 | IWM | market_regime | 292.62 |  | 292.3387 | 0.0962 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 7 | META | cloud_ai_capex | 594.86 |  | 593.838 | 0.1721 | 600.765 | 594.21 | 0.0975 | watch_only | none |
| 8 | NVDA | ai_accelerator | 197.14 |  | 196.0227 | 0.57 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 9 | MSFT | cloud_ai_capex | 397.65 |  | 396.3356 | 0.3316 | 400.09 | 392.355 | 0.0151 | watch_only | none |
| 10 | AMZN | cloud_ai_capex | 231.19 |  | 230.4685 | 0.3131 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 11 | AAPL | mega_cap_platform | 339.83 |  | 338.9397 | 0.2627 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 12 | TSM | foundry | 391.205 |  | 387.6205 | 0.9247 | 390.46 | 382.495 | 0.0307 | buy_precheck_manual_confirm | none |
| 13 | JCI | data_center_power_cooling | 139.91 |  | 138.4811 | 1.0318 | 139.755 | 137.31 | 0.1072 | buy_precheck_manual_confirm | none |
| 14 | SMCI | ai_server_oem | 28.19 |  | 27.9934 | 0.7024 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| 15 | PWR | data_center_power_cooling | 585.59 |  | 582.1831 | 0.5852 | 603.25 | 584.69 | 0.1725 | watch_only | none |
| 16 | MRVL | custom_silicon_networking | 174.915 |  | 174.1719 | 0.4266 | 181.24 | 172.395 | 0.1601 | watch_only | none |
| 17 | ASML | semiconductor_equipment | 1579.8 |  | 1577.2076 | 0.1644 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | GOOGL | cloud_ai_capex | 335.175 |  | 330.5711 | 1.3927 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 19 | AVGO | custom_silicon_networking | 379.47 |  | 378.5625 | 0.2397 | 378.64 | 371.57 | 2.153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 467.33 |  | 465.1309 | 0.4728 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.14 |  | 196.0227 | 0.57 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 391.205 |  | 387.6205 | 0.9247 | 390.46 | 382.495 | 0.0307 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 740.81 |  | 739.4967 | 0.1776 | 739.42 | 736.57 | 0.0243 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 335.175 |  | 330.5711 | 1.3927 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| 5 | JCI | data_center_power_cooling | 139.91 |  | 138.4811 | 1.0318 | 139.755 | 137.31 | 0.1072 | buy_precheck_manual_confirm | none |
| 6 | ORCL | cloud_ai_capex | 120.51 |  | 118.3684 | 1.8092 | 117.17 | 115.25 | 0.166 | buy_precheck_manual_confirm | none |
| 7 | AVGO | custom_silicon_networking | 379.47 |  | 378.5625 | 0.2397 | 378.64 | 371.57 | 2.153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ANET | ai_networking_optical | 168.375 |  | 164.6367 | 2.2706 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | ETN | data_center_power_cooling | 384.79 |  | 381.103 | 0.9675 | 384.565 | 377.43 | 2.6066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | MU | memory_hbm_storage | 816.49 |  | 815.3178 | 0.1438 | 846.4 | 813.91 | 0.0625 | watch_only | none |
| 11 | SMH | semiconductor_index | 528.87 |  | 527.3281 | 0.2924 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| 12 | SOXX | semiconductor_index | 490.4 |  | 489.9597 | 0.0899 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| 13 | QQQ | market_regime | 676.08 |  | 674.0654 | 0.2989 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| 14 | PWR | data_center_power_cooling | 585.59 |  | 582.1831 | 0.5852 | 603.25 | 584.69 | 0.1725 | watch_only | none |
| 15 | WDC | memory_hbm_storage | 455.18 |  | 439.254 | 3.6257 | 465.04 | 435.22 | 0.1933 | watch_only | none |
| 16 | IWM | market_regime | 292.62 |  | 292.3387 | 0.0962 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| 17 | LITE | ai_networking_optical | 641.85 |  | 631.7926 | 1.5919 | 673.65 | 624.91 | 0.3241 | watch_only | none |
| 18 | META | cloud_ai_capex | 594.86 |  | 593.838 | 0.1721 | 600.765 | 594.21 | 0.0975 | watch_only | none |
| 19 | MSFT | cloud_ai_capex | 397.65 |  | 396.3356 | 0.3316 | 400.09 | 392.355 | 0.0151 | watch_only | none |
| 20 | AMZN | cloud_ai_capex | 231.19 |  | 230.4685 | 0.3131 | 233.05 | 229.7 | 0.013 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.08 |  | 674.0654 | 0.2989 | 677.3 | 670.84 | 0.0163 | watch_only | none |
| TQQQ | leveraged_tool | 61.68 |  | 61.0985 | 0.9517 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.14 |  | 196.0227 | 0.57 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.65 |  | 396.3356 | 0.3316 | 400.09 | 392.355 | 0.0151 | watch_only | none |
| AAPL | mega_cap_platform | 339.83 |  | 338.9397 | 0.2627 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.175 |  | 330.5711 | 1.3927 | 330.21 | 324.97 | 0.0119 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.89 |  | 455.5275 | 0.0796 | 472.485 | 453.76 | 2.4852 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.205 |  | 387.6205 | 0.9247 | 390.46 | 382.495 | 0.0307 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.4 |  | 489.9597 | 0.0899 | 497.64 | 485.42 | 0.0693 | watch_only | none |
| SMH | semiconductor_index | 528.87 |  | 527.3281 | 0.2924 | 533.01 | 523.325 | 0.0548 | watch_only | none |
| AVGO | custom_silicon_networking | 379.47 |  | 378.5625 | 0.2397 | 378.64 | 371.57 | 2.153 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 816.49 |  | 815.3178 | 0.1438 | 846.4 | 813.91 | 0.0625 | watch_only | none |
| MRVL | custom_silicon_networking | 174.915 |  | 174.1719 | 0.4266 | 181.24 | 172.395 | 0.1601 | watch_only | none |
| DELL | ai_server_oem | 383.05 |  | 374.9528 | 2.1595 | 402 | 374.02 | 1.0129 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.4 |  | 44.4401 | -0.0901 | 46.19 | 44.33 | 0.045 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.19 |  | 27.9934 | 0.7024 | 28.86 | 27.59 | 0.0355 | watch_only | none |
| SPY | market_regime | 740.81 |  | 739.4967 | 0.1776 | 739.42 | 736.57 | 0.0243 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.62 |  | 292.3387 | 0.0962 | 293.26 | 291.55 | 0.0068 | watch_only | none |
| ORCL | cloud_ai_capex | 120.51 |  | 118.3684 | 1.8092 | 117.17 | 115.25 | 0.166 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.37 |  | 66.2543 | 0.1746 | 68.995 | 65.635 | 2.0491 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.24 |  | 266.1843 | -0.3548 | 273.86 | 266.04 | 2.2621 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 384.79 |  | 381.103 | 0.9675 | 384.565 | 377.43 | 2.6066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 585.59 |  | 582.1831 | 0.5852 | 603.25 | 584.69 | 0.1725 | watch_only | none |
| GEV | data_center_power_cooling | 939.31 |  | 937.5528 | 0.1874 | 955.825 | 935.665 | 0.5472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 467.33 |  | 465.1309 | 0.4728 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.91 |  | 138.4811 | 1.0318 | 139.755 | 137.31 | 0.1072 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 168.375 |  | 164.6367 | 2.2706 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240.1 |  | 237.2814 | 1.1879 | 256.145 | 236.73 | 4.3107 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 641.85 |  | 631.7926 | 1.5919 | 673.65 | 624.91 | 0.3241 | watch_only | none |
| CIEN | ai_networking_optical | 338.86 |  | 337.3711 | 0.4413 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 86.62 |  | 85.7769 | 0.9829 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.69 |  | 259.0503 | 0.633 | 268.265 | 253.05 | 4.0776 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1579.8 |  | 1577.2076 | 0.1644 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 473.87 |  | 476.4192 | -0.5351 | 494.87 | 477.03 | 0.8125 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 269.955 |  | 266.5593 | 1.2739 | 276.85 | 267.14 | 4.4452 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.775 |  | 190.7622 | 0.0067 | 194.96 | 189.48 | 0.4298 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 308.07 |  | 308.3996 | -0.1069 | 315.21 | 304.11 | 4.9112 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 238.35 |  | 236.7165 | 0.6901 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.62 |  | 46.7278 | -2.3708 | 51.64 | 47.435 | 1.4248 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.965 |  | 42.4646 | -1.1766 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.37 |  | 119.2735 | -0.7575 | 121 | 117.72 | 0.169 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 281.49 |  | 282.3811 | -0.3156 | 296.8 | 283.22 | 4.4904 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.08 |  | 518.3117 | -0.8164 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.63 |  | 295.7846 | -0.3903 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.33 |  | 26.5196 | -0.715 | 27 | 25.42 | 0.1139 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.575 |  | 33.7157 | -0.4172 | 35.08 | 33.52 | 0.0298 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.505 |  | 20.0521 | 2.2586 | 20.97 | 19.755 | 0.0975 | watch_only | none |
| SNDK | memory_hbm_storage | 1075.7 |  | 1100.4537 | -2.2494 | 1185.19 | 1114.57 | 0.3523 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 455.18 |  | 439.254 | 3.6257 | 465.04 | 435.22 | 0.1933 | watch_only | none |
| STX | memory_hbm_storage | 750.62 |  | 730.6884 | 2.7278 | 774.805 | 719.02 | 0.5009 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.19 |  | 230.4685 | 0.3131 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594.86 |  | 593.838 | 0.1721 | 600.765 | 594.21 | 0.0975 | watch_only | none |
| ARM | ai_accelerator | 243.95 |  | 245.2745 | -0.54 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 130.735 |  | 131.6216 | -0.6736 | 136.45 | 131.735 | 0.8873 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
