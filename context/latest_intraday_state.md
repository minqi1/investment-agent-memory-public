# Intraday State

- Generated at: `2026-07-29T02:15:34+08:00`
- Market time ET: `2026-07-28T14:15:35-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 12, 'manual_confirm_candidate': 4, 'below_vwap': 12, 'spread_too_wide_or_missing': 17, 'price_stale_or_missing': 1, 'below_opening_15m_low': 10}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.59 |  | 674.0175 | 0.2333 | 677.3 | 670.84 | 0.034 | watch_only | none |
| SOXX | semiconductor_index | 490.15 |  | 489.9559 | 0.0396 | 497.64 | 485.42 | 0.0836 | watch_only | none |
| SMH | semiconductor_index | 528.06 |  | 527.3214 | 0.1401 | 533.01 | 523.325 | 0.0568 | watch_only | none |
| SPY | market_regime | 740.42 |  | 739.484 | 0.1266 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.92 |  | 196.0103 | 0.4641 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.42 |  | 739.484 | 0.1266 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.495 |  | 330.4833 | 1.2139 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 139.84 |  | 138.4393 | 1.0118 | 139.755 | 137.31 | 0.1144 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 740.42 |  | 739.484 | 0.1266 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | NVDA | ai_accelerator | 196.92 |  | 196.0103 | 0.4641 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 528.06 |  | 527.3214 | 0.1401 | 533.01 | 523.325 | 0.0568 | watch_only | none |
| 4 | SOXX | semiconductor_index | 490.15 |  | 489.9559 | 0.0396 | 497.64 | 485.42 | 0.0836 | watch_only | none |
| 5 | QQQ | market_regime | 675.59 |  | 674.0175 | 0.2333 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 6 | IWM | market_regime | 292.73 |  | 292.3285 | 0.1373 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 397.4 |  | 396.3197 | 0.2726 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 231.05 |  | 230.4603 | 0.2559 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 9 | AAPL | mega_cap_platform | 339.565 |  | 338.933 | 0.1865 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 10 | JCI | data_center_power_cooling | 139.84 |  | 138.4393 | 1.0118 | 139.755 | 137.31 | 0.1144 | buy_precheck_manual_confirm | none |
| 11 | TT | data_center_power_cooling | 466.865 |  | 465.0889 | 0.3819 | 477.73 | 460.77 | 0.1756 | watch_only | none |
| 12 | PWR | data_center_power_cooling | 585.65 |  | 582.1025 | 0.6094 | 603.25 | 584.69 | 0.1929 | watch_only | none |
| 13 | GOOGL | cloud_ai_capex | 334.495 |  | 330.4833 | 1.2139 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 14 | ASML | semiconductor_equipment | 1578.645 |  | 1577.1829 | 0.0927 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | AVGO | custom_silicon_networking | 379.17 |  | 378.5531 | 0.163 | 378.64 | 371.57 | 2.0149 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | SMCI | ai_server_oem | 28.24 |  | 27.9903 | 0.8921 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 17 | ALAB | ai_networking_optical | 260.24 |  | 259.0323 | 0.4662 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MRVL | custom_silicon_networking | 174.7 |  | 174.1655 | 0.3069 | 181.24 | 172.395 | 3.32 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TSM | foundry | 390.28 |  | 387.581 | 0.6964 | 390.46 | 382.495 | 1.3759 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | CORZ | high_beta_ai_infrastructure | 20.57 |  | 20.045 | 2.6191 | 20.97 | 19.755 | 0.0972 | watch_only | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 196.92 |  | 196.0103 | 0.4641 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 740.42 |  | 739.484 | 0.1266 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| 3 | GOOGL | cloud_ai_capex | 334.495 |  | 330.4833 | 1.2139 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| 4 | JCI | data_center_power_cooling | 139.84 |  | 138.4393 | 1.0118 | 139.755 | 137.31 | 0.1144 | buy_precheck_manual_confirm | none |
| 5 | AVGO | custom_silicon_networking | 379.17 |  | 378.5531 | 0.163 | 378.64 | 371.57 | 2.0149 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | ANET | ai_networking_optical | 167.74 |  | 164.5403 | 1.9446 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ETN | data_center_power_cooling | 384.67 |  | 381.0439 | 0.9516 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ORCL | cloud_ai_capex | 120.36 |  | 118.3162 | 1.7274 | 117.17 | 115.25 | 4.5198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | SMH | semiconductor_index | 528.06 |  | 527.3214 | 0.1401 | 533.01 | 523.325 | 0.0568 | watch_only | none |
| 10 | SOXX | semiconductor_index | 490.15 |  | 489.9559 | 0.0396 | 497.64 | 485.42 | 0.0836 | watch_only | none |
| 11 | QQQ | market_regime | 675.59 |  | 674.0175 | 0.2333 | 677.3 | 670.84 | 0.034 | watch_only | none |
| 12 | TT | data_center_power_cooling | 466.865 |  | 465.0889 | 0.3819 | 477.73 | 460.77 | 0.1756 | watch_only | none |
| 13 | PWR | data_center_power_cooling | 585.65 |  | 582.1025 | 0.6094 | 603.25 | 584.69 | 0.1929 | watch_only | none |
| 14 | IWM | market_regime | 292.73 |  | 292.3285 | 0.1373 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| 15 | MSFT | cloud_ai_capex | 397.4 |  | 396.3197 | 0.2726 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| 16 | AMZN | cloud_ai_capex | 231.05 |  | 230.4603 | 0.2559 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| 17 | SMCI | ai_server_oem | 28.24 |  | 27.9903 | 0.8921 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| 18 | AAPL | mega_cap_platform | 339.565 |  | 338.933 | 0.1865 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| 19 | CORZ | high_beta_ai_infrastructure | 20.57 |  | 20.045 | 2.6191 | 20.97 | 19.755 | 0.0972 | watch_only | none |
| 20 | TQQQ | leveraged_tool | 61.5 |  | 61.0949 | 0.663 | 62.01 | 60.23 | 0.0163 | watch_only | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 675.59 |  | 674.0175 | 0.2333 | 677.3 | 670.84 | 0.034 | watch_only | none |
| TQQQ | leveraged_tool | 61.5 |  | 61.0949 | 0.663 | 62.01 | 60.23 | 0.0163 | watch_only | none |
| NVDA | ai_accelerator | 196.92 |  | 196.0103 | 0.4641 | 195.4 | 193.65 | 0.0102 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 397.4 |  | 396.3197 | 0.2726 | 400.09 | 392.355 | 0.0201 | watch_only | none |
| AAPL | mega_cap_platform | 339.565 |  | 338.933 | 0.1865 | 342.87 | 337.78 | 0.0088 | watch_only | none |
| GOOGL | cloud_ai_capex | 334.495 |  | 330.4833 | 1.2139 | 330.21 | 324.97 | 0.0239 | buy_precheck_manual_confirm | none |
| AMD | ai_accelerator | 455.34 |  | 455.5289 | -0.0415 | 472.485 | 453.76 | 4.691 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 390.28 |  | 387.581 | 0.6964 | 390.46 | 382.495 | 1.3759 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1550000 |  | 1782638.6117 | -13.0502 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 490.15 |  | 489.9559 | 0.0396 | 497.64 | 485.42 | 0.0836 | watch_only | none |
| SMH | semiconductor_index | 528.06 |  | 527.3214 | 0.1401 | 533.01 | 523.325 | 0.0568 | watch_only | none |
| AVGO | custom_silicon_networking | 379.17 |  | 378.5531 | 0.163 | 378.64 | 371.57 | 2.0149 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 813.76 |  | 815.3327 | -0.1929 | 846.4 | 813.91 | 1.4722 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 174.7 |  | 174.1655 | 0.3069 | 181.24 | 172.395 | 3.32 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 383.615 |  | 374.9237 | 2.3181 | 402 | 374.02 | 4.9164 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 44.34 |  | 44.4406 | -0.2265 | 46.19 | 44.33 | 0.0677 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 28.24 |  | 27.9903 | 0.8921 | 28.86 | 27.59 | 0.0354 | watch_only | none |
| SPY | market_regime | 740.42 |  | 739.484 | 0.1266 | 739.42 | 736.57 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 292.73 |  | 292.3285 | 0.1373 | 293.26 | 291.55 | 0.0137 | watch_only | none |
| ORCL | cloud_ai_capex | 120.36 |  | 118.3162 | 1.7274 | 117.17 | 115.25 | 4.5198 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CRWV | gpu_cloud_ai_factory | 66.125 |  | 66.2551 | -0.1963 | 68.995 | 65.635 | 2.5255 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 264.88 |  | 266.1983 | -0.4952 | 273.86 | 266.04 | 0.6003 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 384.67 |  | 381.0439 | 0.9516 | 384.565 | 377.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 585.65 |  | 582.1025 | 0.6094 | 603.25 | 584.69 | 0.1929 | watch_only | none |
| GEV | data_center_power_cooling | 937.28 |  | 937.5355 | -0.0273 | 955.825 | 935.665 |  | below_vwap | below_vwap,spread_unavailable |
| TT | data_center_power_cooling | 466.865 |  | 465.0889 | 0.3819 | 477.73 | 460.77 | 0.1756 | watch_only | none |
| JCI | data_center_power_cooling | 139.84 |  | 138.4393 | 1.0118 | 139.755 | 137.31 | 0.1144 | buy_precheck_manual_confirm | none |
| ANET | ai_networking_optical | 167.74 |  | 164.5403 | 1.9446 | 165.975 | 160.51 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 240 |  | 237.24 | 1.1634 | 256.145 | 236.73 | 0.4792 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 640 |  | 631.696 | 1.3146 | 673.65 | 624.91 | 1.4656 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 338.935 |  | 337.354 | 0.4686 | 354.09 | 338.14 | 3.9919 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AAOI | ai_networking_optical | 86.51 |  | 85.77 | 0.8628 | 92.95 | 84.63 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 260.24 |  | 259.0323 | 0.4662 | 268.265 | 253.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1578.645 |  | 1577.1829 | 0.0927 | 1586.01 | 1565.95 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMAT | semiconductor_equipment | 473.63 |  | 476.4835 | -0.5989 | 494.87 | 477.03 | 0.2513 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| LRCX | semiconductor_equipment | 269.835 |  | 266.5121 | 1.2468 | 276.85 | 267.14 | 4.4472 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 190.68 |  | 190.7612 | -0.0426 | 194.96 | 189.48 | 0.0472 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 307.59 |  | 308.4164 | -0.2679 | 315.21 | 304.11 | 0.1788 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 237.775 |  | 236.6871 | 0.4596 | 248.8 | 236.42 | 0.9042 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 45.86 |  | 46.7568 | -1.918 | 51.64 | 47.435 | 1.6572 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 41.95 |  | 42.4771 | -1.241 | 44.155 | 41.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 118.245 |  | 119.3329 | -0.9117 | 121 | 117.72 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 281.47 |  | 282.3972 | -0.3283 | 296.8 | 283.22 | 0.405 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.32 |  | 518.3433 | -0.7762 | 518.6 | 511.495 |  | below_vwap | below_vwap,spread_unavailable |
| APD | industrial_gases | 294.74 |  | 295.8061 | -0.3604 | 297.25 | 293.555 | 0.0984 | below_vwap | below_vwap |
| APLD | high_beta_ai_infrastructure | 26.24 |  | 26.5216 | -1.0617 | 27 | 25.42 | 0.0381 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.515 |  | 33.7174 | -0.6001 | 35.08 | 33.52 | 0.0597 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.57 |  | 20.045 | 2.6191 | 20.97 | 19.755 | 0.0972 | watch_only | none |
| SNDK | memory_hbm_storage | 1073.08 |  | 1100.7188 | -2.511 | 1185.19 | 1114.57 | 1.286 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 454.24 |  | 438.9909 | 3.4737 | 465.04 | 435.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 750.29 |  | 730.3619 | 2.7285 | 774.805 | 719.02 | 0.5238 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 231.05 |  | 230.4603 | 0.2559 | 233.05 | 229.7 | 0.0173 | watch_only | none |
| META | cloud_ai_capex | 593.72 |  | 593.831 | -0.0187 | 600.765 | 594.21 | 0.059 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 243.3 |  | 245.2921 | -0.8121 | 253.38 | 243.72 | 0.3 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SKHY | memory_hbm_storage | 130.55 |  | 131.6318 | -0.8218 | 136.45 | 131.735 | 0.0996 | below_opening_15m_low | below_opening_15m_low,below_vwap |
