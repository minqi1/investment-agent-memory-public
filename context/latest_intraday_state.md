# Intraday State

- Generated at: `2026-07-29T01:25:43+08:00`
- Market time ET: `2026-07-28T13:25:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 5, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 1, 'below_vwap': 6, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.27 |  | 673.8574 | 0.5064 | 677.3 | 670.84 | 0.0546 | watch_only | none |
| SOXX | semiconductor_index | 493.45 |  | 489.8557 | 0.7337 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| SMH | semiconductor_index | 531.04 |  | 527.231 | 0.7224 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| SPY | market_regime | 741.45 |  | 739.2998 | 0.2908 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.71 |  | 195.9033 | 0.9223 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.68 |  | 378.4216 | 0.5968 | 378.64 | 371.57 | 0.1313 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.45 |  | 739.2998 | 0.2908 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.835 |  | 329.8775 | 1.5028 | 330.21 | 324.97 | 0.1195 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.33 |  | 292.2462 | 0.3708 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.45 |  | 739.2998 | 0.2908 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 293.33 |  | 292.2462 | 0.3708 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | AVGO | custom_silicon_networking | 380.68 |  | 378.4216 | 0.5968 | 378.64 | 371.57 | 0.1313 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 339.24 |  | 338.8724 | 0.1085 | 342.87 | 337.78 | 0.0206 | watch_only | none |
| 5 | SMH | semiconductor_index | 531.04 |  | 527.231 | 0.7224 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| 6 | SOXX | semiconductor_index | 493.45 |  | 489.8557 | 0.7337 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| 7 | QQQ | market_regime | 677.27 |  | 673.8574 | 0.5064 | 677.3 | 670.84 | 0.0546 | watch_only | none |
| 8 | MSFT | cloud_ai_capex | 398.09 |  | 396.1438 | 0.4913 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 9 | AMZN | cloud_ai_capex | 232.1 |  | 230.3204 | 0.7727 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| 10 | PWR | data_center_power_cooling | 585.42 |  | 581.8213 | 0.6185 | 603.25 | 584.69 | 0.2716 | watch_only | none |
| 11 | NVDA | ai_accelerator | 197.71 |  | 195.9033 | 0.9223 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 12 | ENTG | semiconductor_materials | 119.48 |  | 119.435 | 0.0377 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SMCI | ai_server_oem | 28.35 |  | 27.958 | 1.4021 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 14 | IREN | high_beta_ai_infrastructure | 34 |  | 33.7117 | 0.8552 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| 15 | ASML | semiconductor_equipment | 1584.04 |  | 1576.9694 | 0.4484 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | TT | data_center_power_cooling | 466.69 |  | 464.9946 | 0.3646 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | GEV | data_center_power_cooling | 943.155 |  | 937.4122 | 0.6126 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TER | semiconductor_test_packaging | 311.91 |  | 308.131 | 1.2264 | 315.21 | 304.11 | 0.2148 | watch_only | none |
| 19 | JCI | data_center_power_cooling | 139.155 |  | 138.3488 | 0.5828 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | GOOGL | cloud_ai_capex | 334.835 |  | 329.8775 | 1.5028 | 330.21 | 324.97 | 0.1195 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.71 |  | 195.9033 | 0.9223 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | AVGO | custom_silicon_networking | 380.68 |  | 378.4216 | 0.5968 | 378.64 | 371.57 | 0.1313 | buy_precheck_manual_confirm | none |
| 3 | SPY | market_regime | 741.45 |  | 739.2998 | 0.2908 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 4 | GOOGL | cloud_ai_capex | 334.835 |  | 329.8775 | 1.5028 | 330.21 | 324.97 | 0.1195 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 293.33 |  | 292.2462 | 0.3708 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 6 | TSM | foundry | 391.81 |  | 387.2959 | 1.1655 | 390.46 | 382.495 | 2.6543 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 167.6 |  | 164.0575 | 2.1593 | 165.975 | 160.51 | 4.7792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ORCL | cloud_ai_capex | 120.72 |  | 117.9963 | 2.3083 | 117.17 | 115.25 | 1.3254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 531.04 |  | 527.231 | 0.7224 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| 10 | SOXX | semiconductor_index | 493.45 |  | 489.8557 | 0.7337 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| 11 | QQQ | market_regime | 677.27 |  | 673.8574 | 0.5064 | 677.3 | 670.84 | 0.0546 | watch_only | none |
| 12 | STX | memory_hbm_storage | 751.31 |  | 727.797 | 3.2307 | 774.805 | 719.02 | 0.1863 | watch_only | none |
| 13 | PWR | data_center_power_cooling | 585.42 |  | 581.8213 | 0.6185 | 603.25 | 584.69 | 0.2716 | watch_only | none |
| 14 | LITE | ai_networking_optical | 646.22 |  | 630.6904 | 2.4623 | 673.65 | 624.91 | 0.1594 | watch_only | none |
| 15 | TER | semiconductor_test_packaging | 311.91 |  | 308.131 | 1.2264 | 315.21 | 304.11 | 0.2148 | watch_only | none |
| 16 | MSFT | cloud_ai_capex | 398.09 |  | 396.1438 | 0.4913 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| 17 | AMZN | cloud_ai_capex | 232.1 |  | 230.3204 | 0.7727 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| 18 | SMCI | ai_server_oem | 28.35 |  | 27.958 | 1.4021 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 19 | IREN | high_beta_ai_infrastructure | 34 |  | 33.7117 | 0.8552 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| 20 | AAPL | mega_cap_platform | 339.24 |  | 338.8724 | 0.1085 | 342.87 | 337.78 | 0.0206 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.27 |  | 673.8574 | 0.5064 | 677.3 | 670.84 | 0.0546 | watch_only | none |
| TQQQ | leveraged_tool | 62 |  | 61.0312 | 1.5874 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.71 |  | 195.9033 | 0.9223 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.09 |  | 396.1438 | 0.4913 | 400.09 | 392.355 | 0.0301 | watch_only | none |
| AAPL | mega_cap_platform | 339.24 |  | 338.8724 | 0.1085 | 342.87 | 337.78 | 0.0206 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.835 |  | 329.8775 | 1.5028 | 330.21 | 324.97 | 0.1195 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.77 |  | 455.317 | 0.7584 | 472.485 | 453.76 | 4.6559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.81 |  | 387.2959 | 1.1655 | 390.46 | 382.495 | 2.6543 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.45 |  | 489.8557 | 0.7337 | 497.64 | 485.42 | 0.0669 | watch_only | none |
| SMH | semiconductor_index | 531.04 |  | 527.231 | 0.7224 | 533.01 | 523.325 | 0.0452 | watch_only | none |
| AVGO | custom_silicon_networking | 380.68 |  | 378.4216 | 0.5968 | 378.64 | 371.57 | 0.1313 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.67 |  | 815.0854 | 0.5625 | 846.4 | 813.91 | 0.5478 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.435 |  | 173.9852 | 1.408 | 181.24 | 172.395 | 0.3627 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 384.23 |  | 374.4609 | 2.6088 | 402 | 374.02 | 0.7365 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.41 |  | 44.4515 | -0.0933 | 46.19 | 44.33 | 0.045 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.35 |  | 27.958 | 1.4021 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.45 |  | 739.2998 | 0.2908 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.33 |  | 292.2462 | 0.3708 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.72 |  | 117.9963 | 2.3083 | 117.17 | 115.25 | 1.3254 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 67.44 |  | 66.221 | 1.8408 | 68.995 | 65.635 | 0.519 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.35 |  | 266.2898 | 0.3981 | 273.86 | 266.04 | 0.576 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 384 |  | 380.4069 | 0.9445 | 384.565 | 377.43 | 3.4141 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 585.42 |  | 581.8213 | 0.6185 | 603.25 | 584.69 | 0.2716 | watch_only | none |
| GEV | data_center_power_cooling | 943.155 |  | 937.4122 | 0.6126 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 466.69 |  | 464.9946 | 0.3646 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.155 |  | 138.3488 | 0.5828 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.6 |  | 164.0575 | 2.1593 | 165.975 | 160.51 | 4.7792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 241.4 |  | 236.7334 | 1.9713 | 256.145 | 236.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 646.22 |  | 630.6904 | 2.4623 | 673.65 | 624.91 | 0.1594 | watch_only | none |
| CIEN | ai_networking_optical | 343.41 |  | 337.0746 | 1.8795 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.93 |  | 85.6501 | 2.6618 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 261.81 |  | 258.7259 | 1.192 | 268.265 | 253.05 | 1.0886 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1584.04 |  | 1576.9694 | 0.4484 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 474.52 |  | 476.9005 | -0.4992 | 494.87 | 477.03 | 0.2613 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 268.78 |  | 266.237 | 0.9552 | 276.85 | 267.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 191.49 |  | 190.6779 | 0.4259 | 194.96 | 189.48 | 2.7991 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 311.91 |  | 308.131 | 1.2264 | 315.21 | 304.11 | 0.2148 | watch_only | none |
| ONTO | semiconductor_test_packaging | 237.85 |  | 236.542 | 0.5529 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 46.01 |  | 46.8038 | -1.6959 | 51.64 | 47.435 | 0.1521 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.21 |  | 42.5 | -0.6824 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.48 |  | 119.435 | 0.0377 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 283.42 |  | 282.407 | 0.3587 | 296.8 | 283.22 | 0.4234 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 517.99 |  | 518.5576 | -0.1095 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.49 |  | 295.8683 | -0.1279 | 297.25 | 293.555 | 0.1184 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.34 |  | 26.536 | -0.7386 | 27 | 25.42 | 2.6955 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 34 |  | 33.7117 | 0.8552 | 35.08 | 33.52 | 0.0294 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.385 |  | 20.0169 | 1.8391 | 20.97 | 19.755 | 0.0491 | watch_only | none |
| SNDK | memory_hbm_storage | 1090.01 |  | 1102.2687 | -1.1121 | 1185.19 | 1114.57 | 1.8853 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 457.45 |  | 437.933 | 4.4566 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 751.31 |  | 727.797 | 3.2307 | 774.805 | 719.02 | 0.1863 | watch_only | none |
| AMZN | cloud_ai_capex | 232.1 |  | 230.3204 | 0.7727 | 233.05 | 229.7 | 0.0172 | watch_only | none |
| META | cloud_ai_capex | 593.615 |  | 593.836 | -0.0372 | 600.765 | 594.21 | 1.5128 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 247.19 |  | 245.3342 | 0.7565 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.09 |  | 131.6381 | 0.3433 | 136.45 | 131.735 | 0.9463 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
