# Intraday State

- Generated at: `2026-07-29T00:01:01+08:00`
- Market time ET: `2026-07-28T12:01:02-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 10, 'watch_only': 16, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 1, 'below_vwap': 3, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.58 |  | 673.1005 | 0.8141 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 496.1 |  | 489.2549 | 1.3991 | 497.64 | 485.42 | 0.0605 | watch_only | none |
| SMH | semiconductor_index | 533.81 |  | 526.6949 | 1.3509 | 533.01 | 523.325 | 0.0581 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 742.17 |  | 738.6534 | 0.4761 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.3 |  | 195.3794 | 1.4948 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 392.59 |  | 386.3824 | 1.6066 | 390.46 | 382.495 | 0.028 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 533.81 |  | 526.6949 | 1.3509 | 533.01 | 523.325 | 0.0581 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 383.37 |  | 377.531 | 1.5466 | 378.64 | 371.57 | 0.0783 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 742.17 |  | 738.6534 | 0.4761 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 678.58 |  | 673.1005 | 0.8141 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.47 |  | 328.7994 | 1.4205 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 293.36 |  | 292.0071 | 0.4633 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 120.07 |  | 117.176 | 2.4698 | 117.17 | 115.25 | 0.0666 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 62.38 |  | 60.7585 | 2.6688 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | IWM | market_regime | 293.36 |  | 292.0071 | 0.4633 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 742.17 |  | 738.6534 | 0.4761 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| 3 | META | cloud_ai_capex | 594.98 |  | 593.2529 | 0.2911 | 600.765 | 594.21 | 0.0891 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.645 |  | 338.6324 | 0.299 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 5 | SMH | semiconductor_index | 533.81 |  | 526.6949 | 1.3509 | 533.01 | 523.325 | 0.0581 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 678.58 |  | 673.1005 | 0.8141 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 7 | MSFT | cloud_ai_capex | 397.855 |  | 395.748 | 0.5324 | 400.09 | 392.355 | 0.0302 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 231.235 |  | 229.9807 | 0.5454 | 233.05 | 229.7 | 0.013 | watch_only | none |
| 9 | TT | data_center_power_cooling | 468.085 |  | 464.4752 | 0.7772 | 477.73 | 460.77 | 0.2542 | watch_only | none |
| 10 | AMAT | semiconductor_equipment | 480.52 |  | 477.0722 | 0.7227 | 494.87 | 477.03 | 0.3496 | watch_only | none |
| 11 | NVDA | ai_accelerator | 198.3 |  | 195.3794 | 1.4948 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 12 | GOOGL | cloud_ai_capex | 333.47 |  | 328.7994 | 1.4205 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 13 | SOXX | semiconductor_index | 496.1 |  | 489.2549 | 1.3991 | 497.64 | 485.42 | 0.0605 | watch_only | none |
| 14 | TSM | foundry | 392.59 |  | 386.3824 | 1.6066 | 390.46 | 382.495 | 0.028 | buy_precheck_manual_confirm | none |
| 15 | KLAC | semiconductor_equipment | 193.04 |  | 190.2972 | 1.4413 | 194.96 | 189.48 | 0.057 | watch_only | none |
| 16 | COHU | semiconductor_test_packaging | 42.64 |  | 42.5503 | 0.2109 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | HPE | ai_server_oem | 45.02 |  | 44.3575 | 1.4935 | 46.19 | 44.33 | 0.0888 | watch_only | none |
| 18 | SKHY | memory_hbm_storage | 133.12 |  | 131.439 | 1.2789 | 136.45 | 131.735 | 0.308 | watch_only | none |
| 19 | AVGO | custom_silicon_networking | 383.37 |  | 377.531 | 1.5466 | 378.64 | 371.57 | 0.0783 | buy_precheck_manual_confirm | none |
| 20 | LRCX | semiconductor_equipment | 268.955 |  | 265.7348 | 1.2118 | 276.85 | 267.14 | 0.1933 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 198.3 |  | 195.3794 | 1.4948 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 392.59 |  | 386.3824 | 1.6066 | 390.46 | 382.495 | 0.028 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 533.81 |  | 526.6949 | 1.3509 | 533.01 | 523.325 | 0.0581 | buy_precheck_manual_confirm | none |
| 4 | AVGO | custom_silicon_networking | 383.37 |  | 377.531 | 1.5466 | 378.64 | 371.57 | 0.0783 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 742.17 |  | 738.6534 | 0.4761 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| 6 | QQQ | market_regime | 678.58 |  | 673.1005 | 0.8141 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| 7 | GOOGL | cloud_ai_capex | 333.47 |  | 328.7994 | 1.4205 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| 8 | IWM | market_regime | 293.36 |  | 292.0071 | 0.4633 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| 9 | ORCL | cloud_ai_capex | 120.07 |  | 117.176 | 2.4698 | 117.17 | 115.25 | 0.0666 | buy_precheck_manual_confirm | none |
| 10 | TQQQ | leveraged_tool | 62.38 |  | 60.7585 | 2.6688 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| 11 | ASML | semiconductor_equipment | 1591.1 |  | 1574.768 | 1.0371 | 1586.01 | 1565.95 | 2.0671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ANET | ai_networking_optical | 167.37 |  | 163.3921 | 2.4346 | 165.975 | 160.51 | 4.3496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ETN | data_center_power_cooling | 386.48 |  | 379.3951 | 1.8674 | 384.565 | 377.43 | 0.4632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | SOXX | semiconductor_index | 496.1 |  | 489.2549 | 1.3991 | 497.64 | 485.42 | 0.0605 | watch_only | none |
| 15 | TT | data_center_power_cooling | 468.085 |  | 464.4752 | 0.7772 | 477.73 | 460.77 | 0.2542 | watch_only | none |
| 16 | PWR | data_center_power_cooling | 588.85 |  | 580.0688 | 1.5138 | 603.25 | 584.69 | 0.1766 | watch_only | none |
| 17 | AMAT | semiconductor_equipment | 480.52 |  | 477.0722 | 0.7227 | 494.87 | 477.03 | 0.3496 | watch_only | none |
| 18 | SKHY | memory_hbm_storage | 133.12 |  | 131.439 | 1.2789 | 136.45 | 131.735 | 0.308 | watch_only | none |
| 19 | KLAC | semiconductor_equipment | 193.04 |  | 190.2972 | 1.4413 | 194.96 | 189.48 | 0.057 | watch_only | none |
| 20 | APLD | high_beta_ai_infrastructure | 27.14 |  | 26.4896 | 2.4555 | 27 | 25.42 | 3.1319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 678.58 |  | 673.1005 | 0.8141 | 677.3 | 670.84 | 0.0074 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 62.38 |  | 60.7585 | 2.6688 | 62.01 | 60.23 | 0.016 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 198.3 |  | 195.3794 | 1.4948 | 195.4 | 193.65 | 0.0151 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.855 |  | 395.748 | 0.5324 | 400.09 | 392.355 | 0.0302 | watch_only | none |
| AAPL | mega_cap_platform | 339.645 |  | 338.6324 | 0.299 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.47 |  | 328.7994 | 1.4205 | 330.21 | 324.97 | 0.015 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 463.43 |  | 454.0946 | 2.0558 | 472.485 | 453.76 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TSM | foundry | 392.59 |  | 386.3824 | 1.6066 | 390.46 | 382.495 | 0.028 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 496.1 |  | 489.2549 | 1.3991 | 497.64 | 485.42 | 0.0605 | watch_only | none |
| SMH | semiconductor_index | 533.81 |  | 526.6949 | 1.3509 | 533.01 | 523.325 | 0.0581 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 383.37 |  | 377.531 | 1.5466 | 378.64 | 371.57 | 0.0783 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 828.01 |  | 813.261 | 1.8136 | 846.4 | 813.91 | 0.9517 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 178.41 |  | 173.3203 | 2.9366 | 181.24 | 172.395 | 3.8507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 386.57 |  | 373.0767 | 3.6168 | 402 | 374.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 45.02 |  | 44.3575 | 1.4935 | 46.19 | 44.33 | 0.0888 | watch_only | none |
| SMCI | ai_server_oem | 28.52 |  | 27.8416 | 2.4366 | 28.86 | 27.59 | 0.0351 | watch_only | none |
| SPY | market_regime | 742.17 |  | 738.6534 | 0.4761 | 739.42 | 736.57 | 0.031 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.36 |  | 292.0071 | 0.4633 | 293.26 | 291.55 | 0.0102 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 120.07 |  | 117.176 | 2.4698 | 117.17 | 115.25 | 0.0666 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.27 |  | 65.989 | 1.9412 | 68.995 | 65.635 | 4.6826 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 269.3 |  | 265.9354 | 1.2652 | 273.86 | 266.04 | 5.013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 386.48 |  | 379.3951 | 1.8674 | 384.565 | 377.43 | 0.4632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 588.85 |  | 580.0688 | 1.5138 | 603.25 | 584.69 | 0.1766 | watch_only | none |
| GEV | data_center_power_cooling | 951.08 |  | 934.8343 | 1.7378 | 955.825 | 935.665 | 0.3638 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 468.085 |  | 464.4752 | 0.7772 | 477.73 | 460.77 | 0.2542 | watch_only | none |
| JCI | data_center_power_cooling | 139.305 |  | 138.0215 | 0.9299 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.37 |  | 163.3921 | 2.4346 | 165.975 | 160.51 | 4.3496 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 240.96 |  | 236.0284 | 2.0894 | 256.145 | 236.73 | 4.6481 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 645.855 |  | 626.368 | 3.1111 | 673.65 | 624.91 | 4.2672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 344.1 |  | 336.1497 | 2.3651 | 354.09 | 338.14 | 4.6498 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 88.01 |  | 85.2556 | 3.2307 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 266.1 |  | 257.6249 | 3.2897 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1591.1 |  | 1574.768 | 1.0371 | 1586.01 | 1565.95 | 2.0671 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 480.52 |  | 477.0722 | 0.7227 | 494.87 | 477.03 | 0.3496 | watch_only | none |
| LRCX | semiconductor_equipment | 268.955 |  | 265.7348 | 1.2118 | 276.85 | 267.14 | 0.1933 | watch_only | none |
| KLAC | semiconductor_equipment | 193.04 |  | 190.2972 | 1.4413 | 194.96 | 189.48 | 0.057 | watch_only | none |
| TER | semiconductor_test_packaging | 313.45 |  | 306.5927 | 2.2366 | 315.21 | 304.11 | 0.2297 | watch_only | none |
| ONTO | semiconductor_test_packaging | 237.16 |  | 236.4315 | 0.3081 | 248.8 | 236.42 | 0.4174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.55 |  | 47.0509 | -1.0646 | 51.64 | 47.435 | 0.1504 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.64 |  | 42.5503 | 0.2109 | 44.155 | 41.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 120.09 |  | 119.4267 | 0.5554 | 121 | 117.72 | 3.9137 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 285.07 |  | 281.6636 | 1.2094 | 296.8 | 283.22 | 0.5999 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 517.69 |  | 518.534 | -0.1628 | 518.6 | 511.495 | 0.2221 | below_vwap | below_vwap |
| APD | industrial_gases | 294.41 |  | 296.0111 | -0.5409 | 297.25 | 293.555 | 4.6398 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 27.14 |  | 26.4896 | 2.4555 | 27 | 25.42 | 3.1319 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| IREN | high_beta_ai_infrastructure | 34.705 |  | 33.5605 | 3.4104 | 35.08 | 33.52 | 0.0288 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.45 |  | 19.963 | 2.4393 | 20.97 | 19.755 | 0.0489 | watch_only | none |
| SNDK | memory_hbm_storage | 1111.93 |  | 1102.262 | 0.8771 | 1185.19 | 1114.57 | 0.4227 | below_opening_15m_low | below_opening_15m_low,spread_too_wide |
| WDC | memory_hbm_storage | 451.76 |  | 435.1506 | 3.8169 | 465.04 | 435.22 | 1.5229 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 746.01 |  | 723.8933 | 3.0552 | 774.805 | 719.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 231.235 |  | 229.9807 | 0.5454 | 233.05 | 229.7 | 0.013 | watch_only | none |
| META | cloud_ai_capex | 594.98 |  | 593.2529 | 0.2911 | 600.765 | 594.21 | 0.0891 | watch_only | none |
| ARM | ai_accelerator | 247 |  | 244.995 | 0.8184 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 133.12 |  | 131.439 | 1.2789 | 136.45 | 131.735 | 0.308 | watch_only | none |
