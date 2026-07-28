# Intraday State

- Generated at: `2026-07-29T01:10:23+08:00`
- Market time ET: `2026-07-28T13:10:24-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 17, 'manual_confirm_candidate': 4, 'spread_too_wide_or_missing': 25, 'price_stale_or_missing': 1, 'below_vwap': 5, 'below_opening_15m_low': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.08 |  | 673.7796 | 0.4898 | 677.3 | 670.84 | 0.0606 | watch_only | none |
| SOXX | semiconductor_index | 493.11 |  | 489.8008 | 0.6756 | 497.64 | 485.42 | 0.0913 | watch_only | none |
| SMH | semiconductor_index | 530.83 |  | 527.1479 | 0.6985 | 533.01 | 523.325 | 0.0603 | watch_only | none |
| SPY | market_regime | 741.485 |  | 739.2324 | 0.3047 | 739.42 | 736.57 | 0.027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.31 |  | 195.8202 | 0.7608 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.485 |  | 739.2324 | 0.3047 | 739.42 | 736.57 | 0.027 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 333.92 |  | 329.7043 | 1.2786 | 330.21 | 324.97 | 0.3444 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.68 |  | 117.9324 | 2.3298 | 117.17 | 115.25 | 0.0746 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 741.485 |  | 739.2324 | 0.3047 | 739.42 | 736.57 | 0.027 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 197.31 |  | 195.8202 | 0.7608 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 44.5 |  | 44.4495 | 0.1137 | 46.19 | 44.33 | 0.0674 | watch_only | none |
| 4 | AAPL | mega_cap_platform | 339.39 |  | 338.8634 | 0.1554 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 5 | SMH | semiconductor_index | 530.83 |  | 527.1479 | 0.6985 | 533.01 | 523.325 | 0.0603 | watch_only | none |
| 6 | SOXX | semiconductor_index | 493.11 |  | 489.8008 | 0.6756 | 497.64 | 485.42 | 0.0913 | watch_only | none |
| 7 | QQQ | market_regime | 677.08 |  | 673.7796 | 0.4898 | 677.3 | 670.84 | 0.0606 | watch_only | none |
| 8 | ASML | semiconductor_equipment | 1582.42 |  | 1576.8322 | 0.3544 | 1586.01 | 1565.95 | 0.0543 | watch_only | none |
| 9 | IWM | market_regime | 293.22 |  | 292.1829 | 0.355 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 10 | MSFT | cloud_ai_capex | 398.145 |  | 396.1047 | 0.5151 | 400.09 | 392.355 | 0.0427 | watch_only | none |
| 11 | AMZN | cloud_ai_capex | 231.75 |  | 230.2532 | 0.6501 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 12 | KLAC | semiconductor_equipment | 191.585 |  | 190.629 | 0.5015 | 194.96 | 189.48 | 0.1722 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 333.92 |  | 329.7043 | 1.2786 | 330.21 | 324.97 | 0.3444 | buy_precheck_manual_confirm | none |
| 14 | ENTG | semiconductor_materials | 119.71 |  | 119.4427 | 0.2238 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | TER | semiconductor_test_packaging | 311.45 |  | 308 | 1.1201 | 315.21 | 304.11 | 0.1284 | watch_only | none |
| 16 | IREN | high_beta_ai_infrastructure | 34.06 |  | 33.7045 | 1.0547 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| 17 | TT | data_center_power_cooling | 468.34 |  | 464.9301 | 0.7334 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MRVL | custom_silicon_networking | 176.32 |  | 173.9382 | 1.3693 | 181.24 | 172.395 | 0.1645 | watch_only | none |
| 19 | ARM | ai_accelerator | 246.34 |  | 245.303 | 0.4227 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 819.72 |  | 814.8963 | 0.5919 | 846.4 | 813.91 | 0.466 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 197.31 |  | 195.8202 | 0.7608 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.485 |  | 739.2324 | 0.3047 | 739.42 | 736.57 | 0.027 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 333.92 |  | 329.7043 | 1.2786 | 330.21 | 324.97 | 0.3444 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.68 |  | 117.9324 | 2.3298 | 117.17 | 115.25 | 0.0746 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 391.64 |  | 387.199 | 1.147 | 390.46 | 382.495 | 1.6112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | AVGO | custom_silicon_networking | 381.5 |  | 378.3273 | 0.8386 | 378.64 | 371.57 | 2.6789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ANET | ai_networking_optical | 167.52 |  | 163.9826 | 2.1572 | 165.975 | 160.51 | 4.7397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | ETN | data_center_power_cooling | 385.16 |  | 380.3506 | 1.2645 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | SMH | semiconductor_index | 530.83 |  | 527.1479 | 0.6985 | 533.01 | 523.325 | 0.0603 | watch_only | none |
| 10 | SOXX | semiconductor_index | 493.11 |  | 489.8008 | 0.6756 | 497.64 | 485.42 | 0.0913 | watch_only | none |
| 11 | QQQ | market_regime | 677.08 |  | 673.7796 | 0.4898 | 677.3 | 670.84 | 0.0606 | watch_only | none |
| 12 | ASML | semiconductor_equipment | 1582.42 |  | 1576.8322 | 0.3544 | 1586.01 | 1565.95 | 0.0543 | watch_only | none |
| 13 | WDC | memory_hbm_storage | 457.725 |  | 437.6041 | 4.598 | 465.04 | 435.22 | 0.1639 | watch_only | none |
| 14 | IWM | market_regime | 293.22 |  | 292.1829 | 0.355 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 15 | KLAC | semiconductor_equipment | 191.585 |  | 190.629 | 0.5015 | 194.96 | 189.48 | 0.1722 | watch_only | none |
| 16 | TER | semiconductor_test_packaging | 311.45 |  | 308 | 1.1201 | 315.21 | 304.11 | 0.1284 | watch_only | none |
| 17 | MSFT | cloud_ai_capex | 398.145 |  | 396.1047 | 0.5151 | 400.09 | 392.355 | 0.0427 | watch_only | none |
| 18 | AMZN | cloud_ai_capex | 231.75 |  | 230.2532 | 0.6501 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 19 | HPE | ai_server_oem | 44.5 |  | 44.4495 | 0.1137 | 46.19 | 44.33 | 0.0674 | watch_only | none |
| 20 | MRVL | custom_silicon_networking | 176.32 |  | 173.9382 | 1.3693 | 181.24 | 172.395 | 0.1645 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 677.08 |  | 673.7796 | 0.4898 | 677.3 | 670.84 | 0.0606 | watch_only | none |
| TQQQ | leveraged_tool | 61.97 |  | 61.001 | 1.5885 | 62.01 | 60.23 | 0.0161 | watch_only | none |
| NVDA | ai_accelerator | 197.31 |  | 195.8202 | 0.7608 | 195.4 | 193.65 | 0.0152 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 398.145 |  | 396.1047 | 0.5151 | 400.09 | 392.355 | 0.0427 | watch_only | none |
| AAPL | mega_cap_platform | 339.39 |  | 338.8634 | 0.1554 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 333.92 |  | 329.7043 | 1.2786 | 330.21 | 324.97 | 0.3444 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 458.02 |  | 455.2338 | 0.612 | 472.485 | 453.76 | 2.8296 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 391.64 |  | 387.199 | 1.147 | 390.46 | 382.495 | 1.6112 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1765485.4624 | -12.2055 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 493.11 |  | 489.8008 | 0.6756 | 497.64 | 485.42 | 0.0913 | watch_only | none |
| SMH | semiconductor_index | 530.83 |  | 527.1479 | 0.6985 | 533.01 | 523.325 | 0.0603 | watch_only | none |
| AVGO | custom_silicon_networking | 381.5 |  | 378.3273 | 0.8386 | 378.64 | 371.57 | 2.6789 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 819.72 |  | 814.8963 | 0.5919 | 846.4 | 813.91 | 0.466 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 176.32 |  | 173.9382 | 1.3693 | 181.24 | 172.395 | 0.1645 | watch_only | none |
| DELL | ai_server_oem | 383.22 |  | 374.3703 | 2.3639 | 402 | 374.02 | 0.8115 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.5 |  | 44.4495 | 0.1137 | 46.19 | 44.33 | 0.0674 | watch_only | none |
| SMCI | ai_server_oem | 28.43 |  | 27.9337 | 1.7766 | 28.86 | 27.59 | 0.0352 | watch_only | none |
| SPY | market_regime | 741.485 |  | 739.2324 | 0.3047 | 739.42 | 736.57 | 0.027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.22 |  | 292.1829 | 0.355 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.68 |  | 117.9324 | 2.3298 | 117.17 | 115.25 | 0.0746 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 67.81 |  | 66.1932 | 2.4425 | 68.995 | 65.635 | 1.2388 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 267.5 |  | 266.2536 | 0.4681 | 273.86 | 266.04 | 0.3963 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 385.16 |  | 380.3506 | 1.2645 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.935 |  | 581.6961 | 0.7287 | 603.25 | 584.69 | 1.8927 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 945.775 |  | 937.1836 | 0.9167 | 955.825 | 935.665 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 468.34 |  | 464.9301 | 0.7334 | 477.73 | 460.77 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 139.47 |  | 138.2989 | 0.8468 | 139.755 | 137.31 | 3.8216 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ANET | ai_networking_optical | 167.52 |  | 163.9826 | 2.1572 | 165.975 | 160.51 | 4.7397 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 240.93 |  | 236.6279 | 1.8181 | 256.145 | 236.73 | 0.8218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 646.7 |  | 630.1641 | 2.6241 | 673.65 | 624.91 | 0.3696 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 343.75 |  | 336.9847 | 2.0076 | 354.09 | 338.14 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 87.96 |  | 85.6022 | 2.7544 | 92.95 | 84.63 | 4.3656 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 263.735 |  | 258.6991 | 1.9466 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1582.42 |  | 1576.8322 | 0.3544 | 1586.01 | 1565.95 | 0.0543 | watch_only | none |
| AMAT | semiconductor_equipment | 475.34 |  | 477.0052 | -0.3491 | 494.87 | 477.03 | 2.1816 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 269.265 |  | 266.1826 | 1.158 | 276.85 | 267.14 | 2.997 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.585 |  | 190.629 | 0.5015 | 194.96 | 189.48 | 0.1722 | watch_only | none |
| TER | semiconductor_test_packaging | 311.45 |  | 308 | 1.1201 | 315.21 | 304.11 | 0.1284 | watch_only | none |
| ONTO | semiconductor_test_packaging | 237.58 |  | 236.5307 | 0.4436 | 248.8 | 236.42 | 4.6174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.005 |  | 46.8196 | -1.7398 | 51.64 | 47.435 | 1.9128 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 42.31 |  | 42.5098 | -0.4699 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 119.71 |  | 119.4427 | 0.2238 | 121 | 117.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 284.15 |  | 282.3147 | 0.6501 | 296.8 | 283.22 | 0.454 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 518.39 |  | 518.5625 | -0.0333 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 295.63 |  | 295.875 | -0.0828 | 297.25 | 293.555 | 4.1099 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 26.305 |  | 26.5411 | -0.8895 | 27 | 25.42 | 0.076 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 34.06 |  | 33.7045 | 1.0547 | 35.08 | 33.52 | 0.0587 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.34 |  | 20.0125 | 1.6365 | 20.97 | 19.755 | 0.0492 | watch_only | none |
| SNDK | memory_hbm_storage | 1089.52 |  | 1102.6074 | -1.1869 | 1185.19 | 1114.57 | 2.5103 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 457.725 |  | 437.6041 | 4.598 | 465.04 | 435.22 | 0.1639 | watch_only | none |
| STX | memory_hbm_storage | 755.31 |  | 726.6731 | 3.9408 | 774.805 | 719.02 | 3.9547 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.75 |  | 230.2532 | 0.6501 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.13 |  | 593.8594 | -0.1228 | 600.765 | 594.21 | 0.8329 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 246.34 |  | 245.303 | 0.4227 | 253.38 | 243.72 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 132.405 |  | 131.6293 | 0.5893 | 136.45 | 131.735 | 0.6193 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
