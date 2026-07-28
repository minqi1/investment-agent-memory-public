# Intraday State

- Generated at: `2026-07-29T02:04:03+08:00`
- Market time ET: `2026-07-28T14:04:04-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 18, 'spread_too_wide_or_missing': 18, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 1, 'below_vwap': 7, 'below_opening_15m_low': 8}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.815 |  | 673.9989 | 0.4178 | 677.3 | 670.84 | 0.0103 | watch_only | none |
| SOXX | semiconductor_index | 491.73 |  | 489.9276 | 0.3679 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| SMH | semiconductor_index | 529.45 |  | 527.316 | 0.4047 | 533.01 | 523.325 | 0.068 | watch_only | none |
| SPY | market_regime | 741.07 |  | 739.4538 | 0.2186 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.45 |  | 378.5406 | 0.2402 | 378.64 | 371.57 | 0.0422 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.07 |  | 739.4538 | 0.2186 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 335.16 |  | 330.3672 | 1.4508 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.655 |  | 118.214 | 2.0649 | 117.17 | 115.25 | 0.0912 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.45 |  | 378.5406 | 0.2402 | 378.64 | 371.57 | 0.0422 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.07 |  | 739.4538 | 0.2186 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | GEV | data_center_power_cooling | 937.96 |  | 937.5407 | 0.0447 | 955.825 | 935.665 | 0.1301 | watch_only | none |
| 4 | IWM | market_regime | 293.11 |  | 292.3204 | 0.2701 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 5 | AMZN | cloud_ai_capex | 231.21 |  | 230.4498 | 0.3299 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| 6 | IREN | high_beta_ai_infrastructure | 33.735 |  | 33.7186 | 0.0485 | 35.08 | 33.52 | 0.0593 | watch_only | none |
| 7 | AAPL | mega_cap_platform | 339.54 |  | 338.921 | 0.1826 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 8 | TER | semiconductor_test_packaging | 309.37 |  | 308.4117 | 0.3107 | 315.21 | 304.11 | 0.1875 | watch_only | none |
| 9 | MU | memory_hbm_storage | 819.48 |  | 815.2529 | 0.5185 | 846.4 | 813.91 | 0.0976 | watch_only | none |
| 10 | SMH | semiconductor_index | 529.45 |  | 527.316 | 0.4047 | 533.01 | 523.325 | 0.068 | watch_only | none |
| 11 | SOXX | semiconductor_index | 491.73 |  | 489.9276 | 0.3679 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| 12 | QQQ | market_regime | 676.815 |  | 673.9989 | 0.4178 | 677.3 | 670.84 | 0.0103 | watch_only | none |
| 13 | TT | data_center_power_cooling | 467.145 |  | 465.0307 | 0.4547 | 477.73 | 460.77 | 0.2034 | watch_only | none |
| 14 | AMD | ai_accelerator | 457.88 |  | 455.503 | 0.5218 | 472.485 | 453.76 | 0.2249 | watch_only | none |
| 15 | MRVL | custom_silicon_networking | 175.38 |  | 174.1403 | 0.7119 | 181.24 | 172.395 | 0.2566 | watch_only | none |
| 16 | GOOGL | cloud_ai_capex | 335.16 |  | 330.3672 | 1.4508 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| 17 | ASML | semiconductor_equipment | 1577.53 |  | 1577.1445 | 0.0244 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | JCI | data_center_power_cooling | 139.685 |  | 138.3999 | 0.9286 | 139.755 | 137.31 | 0.0931 | watch_only | none |
| 19 | SMCI | ai_server_oem | 28.36 |  | 27.9837 | 1.3449 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| 20 | ONTO | semiconductor_test_packaging | 236.87 |  | 236.6057 | 0.1117 | 248.8 | 236.42 | 0.5066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AVGO | custom_silicon_networking | 379.45 |  | 378.5406 | 0.2402 | 378.64 | 371.57 | 0.0422 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 741.07 |  | 739.4538 | 0.2186 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 335.16 |  | 330.3672 | 1.4508 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| 4 | ORCL | cloud_ai_capex | 120.655 |  | 118.214 | 2.0649 | 117.17 | 115.25 | 0.0912 | buy_precheck_manual_confirm | none |
| 5 | NVDA | ai_accelerator | 197.06 |  | 195.9937 | 0.5441 | 195.4 | 193.65 | 0.5328 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.04 |  | 164.3305 | 1.6488 | 165.975 | 160.51 | 1.2991 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ETN | data_center_power_cooling | 385.275 |  | 380.9866 | 1.1256 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | MU | memory_hbm_storage | 819.48 |  | 815.2529 | 0.5185 | 846.4 | 813.91 | 0.0976 | watch_only | none |
| 9 | SMH | semiconductor_index | 529.45 |  | 527.316 | 0.4047 | 533.01 | 523.325 | 0.068 | watch_only | none |
| 10 | SOXX | semiconductor_index | 491.73 |  | 489.9276 | 0.3679 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| 11 | QQQ | market_regime | 676.815 |  | 673.9989 | 0.4178 | 677.3 | 670.84 | 0.0103 | watch_only | none |
| 12 | TT | data_center_power_cooling | 467.145 |  | 465.0307 | 0.4547 | 477.73 | 460.77 | 0.2034 | watch_only | none |
| 13 | GEV | data_center_power_cooling | 937.96 |  | 937.5407 | 0.0447 | 955.825 | 935.665 | 0.1301 | watch_only | none |
| 14 | JCI | data_center_power_cooling | 139.685 |  | 138.3999 | 0.9286 | 139.755 | 137.31 | 0.0931 | watch_only | none |
| 15 | WDC | memory_hbm_storage | 453.38 |  | 438.8316 | 3.3153 | 465.04 | 435.22 | 0.2382 | watch_only | none |
| 16 | IWM | market_regime | 293.11 |  | 292.3204 | 0.2701 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| 17 | AMD | ai_accelerator | 457.88 |  | 455.503 | 0.5218 | 472.485 | 453.76 | 0.2249 | watch_only | none |
| 18 | TER | semiconductor_test_packaging | 309.37 |  | 308.4117 | 0.3107 | 315.21 | 304.11 | 0.1875 | watch_only | none |
| 19 | AMZN | cloud_ai_capex | 231.21 |  | 230.4498 | 0.3299 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| 20 | MRVL | custom_silicon_networking | 175.38 |  | 174.1403 | 0.7119 | 181.24 | 172.395 | 0.2566 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 676.815 |  | 673.9989 | 0.4178 | 677.3 | 670.84 | 0.0103 | watch_only | none |
| TQQQ | leveraged_tool | 61.79 |  | 61.0871 | 1.1507 | 62.01 | 60.23 | 0.0162 | watch_only | none |
| NVDA | ai_accelerator | 197.06 |  | 195.9937 | 0.5441 | 195.4 | 193.65 | 0.5328 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 398.475 |  | 396.2962 | 0.5498 | 400.09 | 392.355 | 0.8332 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAPL | mega_cap_platform | 339.54 |  | 338.921 | 0.1826 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 335.16 |  | 330.3672 | 1.4508 | 330.21 | 324.97 | 0.0269 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 457.88 |  | 455.503 | 0.5218 | 472.485 | 453.76 | 0.2249 | watch_only | none |
| TSM | foundry | 390.25 |  | 387.5368 | 0.7001 | 390.46 | 382.495 | 1.3632 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1758999.4257 | -11.8817 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 491.73 |  | 489.9276 | 0.3679 | 497.64 | 485.42 | 0.0447 | watch_only | none |
| SMH | semiconductor_index | 529.45 |  | 527.316 | 0.4047 | 533.01 | 523.325 | 0.068 | watch_only | none |
| AVGO | custom_silicon_networking | 379.45 |  | 378.5406 | 0.2402 | 378.64 | 371.57 | 0.0422 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 819.48 |  | 815.2529 | 0.5185 | 846.4 | 813.91 | 0.0976 | watch_only | none |
| MRVL | custom_silicon_networking | 175.38 |  | 174.1403 | 0.7119 | 181.24 | 172.395 | 0.2566 | watch_only | none |
| DELL | ai_server_oem | 383.12 |  | 374.8358 | 2.2101 | 402 | 374.02 | 4.6669 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.315 |  | 44.4421 | -0.286 | 46.19 | 44.33 | 0.0677 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 28.36 |  | 27.9837 | 1.3449 | 28.86 | 27.59 | 0.0353 | watch_only | none |
| SPY | market_regime | 741.07 |  | 739.4538 | 0.2186 | 739.42 | 736.57 | 0.0256 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 293.11 |  | 292.3204 | 0.2701 | 293.26 | 291.55 | 0.0102 | watch_only | none |
| ORCL | cloud_ai_capex | 120.655 |  | 118.214 | 2.0649 | 117.17 | 115.25 | 0.0912 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 66.48 |  | 66.2545 | 0.3404 | 68.995 | 65.635 | 2.1661 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 265.57 |  | 266.2324 | -0.2488 | 273.86 | 266.04 | 0.2636 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 385.275 |  | 380.9866 | 1.1256 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.3 |  | 582.0721 | 0.5546 | 603.25 | 584.69 | 2.5628 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 937.96 |  | 937.5407 | 0.0447 | 955.825 | 935.665 | 0.1301 | watch_only | none |
| TT | data_center_power_cooling | 467.145 |  | 465.0307 | 0.4547 | 477.73 | 460.77 | 0.2034 | watch_only | none |
| JCI | data_center_power_cooling | 139.685 |  | 138.3999 | 0.9286 | 139.755 | 137.31 | 0.0931 | watch_only | none |
| ANET | ai_networking_optical | 167.04 |  | 164.3305 | 1.6488 | 165.975 | 160.51 | 1.2991 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 243 |  | 237.1608 | 2.4621 | 256.145 | 236.73 | 0.7654 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 643.32 |  | 631.5606 | 1.862 | 673.65 | 624.91 | 4.2389 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 341.37 |  | 337.2678 | 1.2163 | 354.09 | 338.14 | 4.7485 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 87.27 |  | 85.7466 | 1.7766 | 92.95 | 84.63 | 3.9762 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 262.06 |  | 258.956 | 1.1987 | 268.265 | 253.05 | 4.6936 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1577.53 |  | 1577.1445 | 0.0244 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 474.11 |  | 476.5506 | -0.5121 | 494.87 | 477.03 | 0.2151 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 269.625 |  | 266.4063 | 1.2082 | 276.85 | 267.14 | 3.7682 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 191.44 |  | 190.7497 | 0.3619 | 194.96 | 189.48 | 0.935 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 309.37 |  | 308.4117 | 0.3107 | 315.21 | 304.11 | 0.1875 | watch_only | none |
| ONTO | semiconductor_test_packaging | 236.87 |  | 236.6057 | 0.1117 | 248.8 | 236.42 | 0.5066 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 46.03 |  | 46.7664 | -1.5746 | 51.64 | 47.435 | 0.0869 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| COHU | semiconductor_test_packaging | 42.12 |  | 42.4865 | -0.8626 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.18 |  | 119.3698 | -0.9968 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.86 |  | 282.4188 | -0.1979 | 296.8 | 283.22 | 0.5393 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.72 |  | 518.4525 | -0.7199 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.61 |  | 295.8234 | -0.4102 | 297.25 | 293.555 |  | below_vwap | below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.34 |  | 26.524 | -0.6935 | 27 | 25.42 | 1.4047 | below_vwap | below_vwap,spread_too_wide |
| IREN | high_beta_ai_infrastructure | 33.735 |  | 33.7186 | 0.0485 | 35.08 | 33.52 | 0.0593 | watch_only | none |
| CORZ | high_beta_ai_infrastructure | 20.45 |  | 20.0392 | 2.05 | 20.97 | 19.755 | 0.0489 | watch_only | none |
| SNDK | memory_hbm_storage | 1081.575 |  | 1100.9794 | -1.7625 | 1185.19 | 1114.57 | 3.0326 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 453.38 |  | 438.8316 | 3.3153 | 465.04 | 435.22 | 0.2382 | watch_only | none |
| STX | memory_hbm_storage | 753.5 |  | 729.5047 | 3.2893 | 774.805 | 719.02 | 0.5003 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.21 |  | 230.4498 | 0.3299 | 233.05 | 229.7 | 0.0087 | watch_only | none |
| META | cloud_ai_capex | 593.45 |  | 593.8362 | -0.065 | 600.765 | 594.21 | 2.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 244.18 |  | 245.3129 | -0.4618 | 253.38 | 243.72 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 131.455 |  | 131.6394 | -0.1401 | 136.45 | 131.735 | 0.7455 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
