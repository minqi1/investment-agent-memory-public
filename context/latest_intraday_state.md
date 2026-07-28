# Intraday State

- Generated at: `2026-07-29T01:44:52+08:00`
- Market time ET: `2026-07-28T13:44:52-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 14, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 19, 'price_stale_or_missing': 1, 'below_vwap': 11, 'below_opening_15m_low': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.48 |  | 673.9364 | 0.3774 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| SOXX | semiconductor_index | 491.49 |  | 489.886 | 0.3274 | 497.64 | 485.42 | 0.0773 | watch_only | none |
| SMH | semiconductor_index | 529.58 |  | 527.2738 | 0.4374 | 533.01 | 523.325 | 0.0359 | watch_only | none |
| SPY | market_regime | 740.84 |  | 739.3845 | 0.1969 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.4 |  | 195.9568 | 0.7365 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.84 |  | 739.3845 | 0.1969 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 335.17 |  | 330.1673 | 1.5152 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.445 |  | 118.1017 | 1.9841 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.84 |  | 739.3845 | 0.1969 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 491.49 |  | 489.886 | 0.3274 | 497.64 | 485.42 | 0.0773 | watch_only | none |
| 3 | IWM | market_regime | 292.955 |  | 292.2735 | 0.2332 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 4 | KLAC | semiconductor_equipment | 191.19 |  | 190.7284 | 0.242 | 194.96 | 189.48 | 0.0523 | watch_only | none |
| 5 | NVDA | ai_accelerator | 197.4 |  | 195.9568 | 0.7365 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 231.19 |  | 230.4147 | 0.3365 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| 7 | IREN | high_beta_ai_infrastructure | 33.75 |  | 33.7185 | 0.0933 | 35.08 | 33.52 | 0.0296 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 339.56 |  | 338.8856 | 0.199 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 9 | SMH | semiconductor_index | 529.58 |  | 527.2738 | 0.4374 | 533.01 | 523.325 | 0.0359 | watch_only | none |
| 10 | QQQ | market_regime | 676.48 |  | 673.9364 | 0.3774 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 11 | TER | semiconductor_test_packaging | 309.77 |  | 308.3313 | 0.4666 | 315.21 | 304.11 | 0.1324 | watch_only | none |
| 12 | MSFT | cloud_ai_capex | 398.77 |  | 396.2125 | 0.6455 | 400.09 | 392.355 | 0.0401 | watch_only | none |
| 13 | ASML | semiconductor_equipment | 1581.18 |  | 1577.1544 | 0.2552 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 138.515 |  | 138.3748 | 0.1013 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SMCI | ai_server_oem | 28.255 |  | 27.9724 | 1.0103 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 16 | CORZ | high_beta_ai_infrastructure | 20.32 |  | 20.0232 | 1.4823 | 20.97 | 19.755 | 0.0984 | watch_only | none |
| 17 | GEV | data_center_power_cooling | 938.99 |  | 937.5872 | 0.1496 | 955.825 | 935.665 | 2.2013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | GOOGL | cloud_ai_capex | 335.17 |  | 330.1673 | 1.5152 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| 19 | TSM | foundry | 390.34 |  | 387.4475 | 0.7466 | 390.46 | 382.495 | 1.2835 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ORCL | cloud_ai_capex | 120.445 |  | 118.1017 | 1.9841 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.4 |  | 195.9568 | 0.7365 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.84 |  | 739.3845 | 0.1969 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 335.17 |  | 330.1673 | 1.5152 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.445 |  | 118.1017 | 1.9841 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 379.98 |  | 378.4999 | 0.391 | 378.64 | 371.57 | 2.3054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.41 |  | 164.1548 | 1.983 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SMH | semiconductor_index | 529.58 |  | 527.2738 | 0.4374 | 533.01 | 523.325 | 0.0359 | watch_only | none |
| 8 | SOXX | semiconductor_index | 491.49 |  | 489.886 | 0.3274 | 497.64 | 485.42 | 0.0773 | watch_only | none |
| 9 | QQQ | market_regime | 676.48 |  | 673.9364 | 0.3774 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| 10 | IWM | market_regime | 292.955 |  | 292.2735 | 0.2332 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 11 | KLAC | semiconductor_equipment | 191.19 |  | 190.7284 | 0.242 | 194.96 | 189.48 | 0.0523 | watch_only | none |
| 12 | TER | semiconductor_test_packaging | 309.77 |  | 308.3313 | 0.4666 | 315.21 | 304.11 | 0.1324 | watch_only | none |
| 13 | MSFT | cloud_ai_capex | 398.77 |  | 396.2125 | 0.6455 | 400.09 | 392.355 | 0.0401 | watch_only | none |
| 14 | AMZN | cloud_ai_capex | 231.19 |  | 230.4147 | 0.3365 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| 15 | COHR | ai_networking_optical | 242.46 |  | 236.9204 | 2.3381 | 256.145 | 236.73 | 0.1526 | watch_only | none |
| 16 | SMCI | ai_server_oem | 28.255 |  | 27.9724 | 1.0103 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 17 | IREN | high_beta_ai_infrastructure | 33.75 |  | 33.7185 | 0.0933 | 35.08 | 33.52 | 0.0296 | watch_only | none |
| 18 | AAPL | mega_cap_platform | 339.56 |  | 338.8856 | 0.199 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| 19 | CORZ | high_beta_ai_infrastructure | 20.32 |  | 20.0232 | 1.4823 | 20.97 | 19.755 | 0.0984 | watch_only | none |
| 20 | TQQQ | leveraged_tool | 61.8 |  | 61.0618 | 1.209 | 62.01 | 60.23 | 0.0324 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.48 |  | 673.9364 | 0.3774 | 677.3 | 670.84 | 0.0089 | watch_only | none |
| TQQQ | leveraged_tool | 61.8 |  | 61.0618 | 1.209 | 62.01 | 60.23 | 0.0324 | watch_only | none |
| NVDA | ai_accelerator | 197.4 |  | 195.9568 | 0.7365 | 195.4 | 193.65 | 0.0101 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.77 |  | 396.2125 | 0.6455 | 400.09 | 392.355 | 0.0401 | watch_only | none |
| AAPL | mega_cap_platform | 339.56 |  | 338.8856 | 0.199 | 342.87 | 337.78 | 0.0118 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.17 |  | 330.1673 | 1.5152 | 330.21 | 324.97 | 0.0328 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458 |  | 455.4314 | 0.564 | 472.485 | 453.76 | 3.0022 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 390.34 |  | 387.4475 | 0.7466 | 390.46 | 382.495 | 1.2835 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.49 |  | 489.886 | 0.3274 | 497.64 | 485.42 | 0.0773 | watch_only | none |
| SMH | semiconductor_index | 529.58 |  | 527.2738 | 0.4374 | 533.01 | 523.325 | 0.0359 | watch_only | none |
| AVGO | custom_silicon_networking | 379.98 |  | 378.4999 | 0.391 | 378.64 | 371.57 | 2.3054 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 814.8 |  | 815.3089 | -0.0624 | 846.4 | 813.91 | 0.8419 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 175.47 |  | 174.0657 | 0.8067 | 181.24 | 172.395 | 0.7523 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 383.7 |  | 374.6495 | 2.4157 | 402 | 374.02 | 1.9286 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.34 |  | 44.4475 | -0.2418 | 46.19 | 44.33 | 0.0451 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.255 |  | 27.9724 | 1.0103 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 740.84 |  | 739.3845 | 0.1969 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.955 |  | 292.2735 | 0.2332 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.445 |  | 118.1017 | 1.9841 | 117.17 | 115.25 | 0.0498 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.555 |  | 66.2484 | 0.4628 | 68.995 | 65.635 | 1.818 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 266.12 |  | 266.3285 | -0.0783 | 273.86 | 266.04 | 0.2555 | below_vwap | below_vwap |
| ETN | data_center_power_cooling | 384.35 |  | 380.7271 | 0.9516 | 384.565 | 377.43 | 3.5072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 584.42 |  | 581.9811 | 0.4191 | 603.25 | 584.69 | 0.3439 | below_opening_15m_low | below_opening_15m_low |
| GEV | data_center_power_cooling | 938.99 |  | 937.5872 | 0.1496 | 955.825 | 935.665 | 2.2013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 464.19 |  | 465.0134 | -0.1771 | 477.73 | 460.77 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 138.515 |  | 138.3748 | 0.1013 | 139.755 | 137.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.41 |  | 164.1548 | 1.983 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 242.46 |  | 236.9204 | 2.3381 | 256.145 | 236.73 | 0.1526 | watch_only | none |
| LITE | ai_networking_optical | 644.46 |  | 631.2437 | 2.0937 | 673.65 | 624.91 | 0.7231 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 341.485 |  | 337.185 | 1.2753 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.73 |  | 85.7074 | 2.3599 | 92.95 | 84.63 | 4.2175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 261.44 |  | 258.841 | 1.0041 | 268.265 | 253.05 | 4.196 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1581.18 |  | 1577.1544 | 0.2552 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 473.82 |  | 476.7897 | -0.6229 | 494.87 | 477.03 | 0.2891 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 268.56 |  | 266.3331 | 0.8361 | 276.85 | 267.14 | 2.681 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.19 |  | 190.7284 | 0.242 | 194.96 | 189.48 | 0.0523 | watch_only | none |
| TER | semiconductor_test_packaging | 309.77 |  | 308.3313 | 0.4666 | 315.21 | 304.11 | 0.1324 | watch_only | none |
| ONTO | semiconductor_test_packaging | 238.495 |  | 236.5608 | 0.8176 | 248.8 | 236.42 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 45.875 |  | 46.7891 | -1.9537 | 51.64 | 47.435 | 1.8747 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.2 |  | 42.4975 | -0.7 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.55 |  | 119.412 | -0.7218 | 121 | 117.72 | 4.5719 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 282.23 |  | 282.4535 | -0.0791 | 296.8 | 283.22 | 0.3508 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.78 |  | 518.526 | -0.3367 | 518.6 | 511.495 | 0.0793 | below_vwap | below_vwap |
| APD | industrial_gases | 295.43 |  | 295.861 | -0.1457 | 297.25 | 293.555 | 4.3225 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.195 |  | 26.531 | -1.2665 | 27 | 25.42 | 0.0382 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.75 |  | 33.7185 | 0.0933 | 35.08 | 33.52 | 0.0296 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.32 |  | 20.0232 | 1.4823 | 20.97 | 19.755 | 0.0984 | watch_only | none |
| SNDK | memory_hbm_storage | 1076.495 |  | 1101.8892 | -2.3046 | 1185.19 | 1114.57 | 3.0655 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.08 |  | 438.4565 | 3.5633 | 465.04 | 435.22 | 0.3546 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 746.82 |  | 728.7207 | 2.4837 | 774.805 | 719.02 | 3.2484 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.19 |  | 230.4147 | 0.3365 | 233.05 | 229.7 | 0.0216 | watch_only | none |
| META | cloud_ai_capex | 593.77 |  | 593.8475 | -0.0131 | 600.765 | 594.21 | 1.0004 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.495 |  | 245.3753 | -0.3588 | 253.38 | 243.72 | 0.2904 | below_vwap | below_vwap |
| SKHY | memory_hbm_storage | 131.36 |  | 131.6463 | -0.2174 | 136.45 | 131.735 | 0.7613 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
