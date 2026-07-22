# Intraday State

- Generated at: `2026-07-23T03:07:22+08:00`
- Market time ET: `2026-07-22T15:07:23-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'spread_too_wide_or_missing': 16, 'below_opening_15m_low': 10, 'price_stale_or_missing': 1, 'below_vwap': 19, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.46 |  | 707.4518 | 0.0012 | 705.86 | 703.63 | 0.0042 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.61 |  | 553.9284 | 0.8452 | 551.02 | 540.105 | 0.034 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.3 |  | 586.5674 | 0.6364 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.285 |  | 748.5044 | -0.0293 | 747.68 | 746.425 | 0.0187 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.86 |  | 421.0334 | 0.4338 | 419.42 | 414.87 | 0.1017 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.61 |  | 553.9284 | 0.8452 | 551.02 | 540.105 | 0.034 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.3 |  | 586.5674 | 0.6364 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 707.46 |  | 707.4518 | 0.0012 | 705.86 | 703.63 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1803.99 |  | 1799.1559 | 0.2687 | 1786.525 | 1767.54 | 0.066 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 216.49 |  | 216.1558 | 0.1546 | 215.465 | 210.975 | 0.0323 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 560.575 |  | 558.8178 | 0.3145 | 559.22 | 544.305 | 0.0945 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 302.54 |  | 299.6739 | 0.9564 | 297.69 | 293.905 | 0.1587 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 70.9 |  | 70.8599 | 0.0566 | 70.43 | 69.81 | 0.0282 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.46 |  | 707.4518 | 0.0012 | 705.86 | 703.63 | 0.0042 | buy_precheck_manual_confirm | none |
| 2 | AMAT | semiconductor_equipment | 560.575 |  | 558.8178 | 0.3145 | 559.22 | 544.305 | 0.0945 | buy_precheck_manual_confirm | none |
| 3 | KLAC | semiconductor_equipment | 216.49 |  | 216.1558 | 0.1546 | 215.465 | 210.975 | 0.0323 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1803.99 |  | 1799.1559 | 0.2687 | 1786.525 | 1767.54 | 0.066 | buy_precheck_manual_confirm | none |
| 5 | TSM | foundry | 422.86 |  | 421.0334 | 0.4338 | 419.42 | 414.87 | 0.1017 | buy_precheck_manual_confirm | none |
| 6 | SMH | semiconductor_index | 590.3 |  | 586.5674 | 0.6364 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 7 | ENTG | semiconductor_materials | 138.95 |  | 138.8605 | 0.0645 | 140.09 | 135.555 | 0.2015 | watch_only | none |
| 8 | SOXX | semiconductor_index | 558.61 |  | 553.9284 | 0.8452 | 551.02 | 540.105 | 0.034 | buy_precheck_manual_confirm | none |
| 9 | LIN | industrial_gases | 509.185 |  | 507.4416 | 0.3436 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 642.555 |  | 641.5782 | 0.1522 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ARM | ai_accelerator | 285.73 |  | 285.5847 | 0.0509 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ANET | ai_networking_optical | 175.53 |  | 174.9531 | 0.3297 | 175.265 | 171.06 | 2.4953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | MU | memory_hbm_storage | 969.345 |  | 968.4703 | 0.0903 | 963.41 | 936.99 | 1.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | VRT | data_center_power_cooling | 302.54 |  | 299.6739 | 0.9564 | 297.69 | 293.905 | 0.1587 | buy_precheck_manual_confirm | none |
| 15 | CRWV | gpu_cloud_ai_factory | 83.38 |  | 83.3453 | 0.0416 | 83.22 | 79.6 | 4.7493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | MKSI | semiconductor_materials | 347.585 |  | 345.4675 | 0.6129 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | ONTO | semiconductor_test_packaging | 296.58 |  | 295.3907 | 0.4026 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ALAB | ai_networking_optical | 330.58 |  | 329.9061 | 0.2043 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | LRCX | semiconductor_equipment | 320.82 |  | 319.555 | 0.3959 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | WDC | memory_hbm_storage | 558.065 |  | 556.2284 | 0.3302 | 548.14 | 526.22 | 0.9479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 422.86 |  | 421.0334 | 0.4338 | 419.42 | 414.87 | 0.1017 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.61 |  | 553.9284 | 0.8452 | 551.02 | 540.105 | 0.034 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.3 |  | 586.5674 | 0.6364 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 707.46 |  | 707.4518 | 0.0012 | 705.86 | 703.63 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1803.99 |  | 1799.1559 | 0.2687 | 1786.525 | 1767.54 | 0.066 | buy_precheck_manual_confirm | none |
| 6 | KLAC | semiconductor_equipment | 216.49 |  | 216.1558 | 0.1546 | 215.465 | 210.975 | 0.0323 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 560.575 |  | 558.8178 | 0.3145 | 559.22 | 544.305 | 0.0945 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 302.54 |  | 299.6739 | 0.9564 | 297.69 | 293.905 | 0.1587 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 70.9 |  | 70.8599 | 0.0566 | 70.43 | 69.81 | 0.0282 | buy_precheck_manual_confirm | none |
| 10 | STX | memory_hbm_storage | 905.025 |  | 909.4712 | -0.4889 | 899.59 | 860.605 | 1.9425 | below_vwap | below_vwap,spread_too_wide |
| 11 | SPY | market_regime | 748.285 |  | 748.5044 | -0.0293 | 747.68 | 746.425 | 0.0187 | below_vwap | below_vwap |
| 12 | TER | semiconductor_test_packaging | 371.4 |  | 371.6687 | -0.0723 | 369.53 | 365 | 0.1589 | below_vwap | below_vwap |
| 13 | DELL | ai_server_oem | 442.32 |  | 442.3527 | -0.0074 | 435.98 | 415.79 | 0.3436 | below_vwap | below_vwap |
| 14 | AMKR | semiconductor_test_packaging | 67.38 |  | 67.4697 | -0.133 | 66.73 | 64.98 | 3.829 | below_vwap | below_vwap,spread_too_wide |
| 15 | SMCI | ai_server_oem | 30.83 |  | 31.1493 | -1.025 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| 16 | NVDA | ai_accelerator | 213.83 |  | 211.6096 | 1.0493 | 207.4 | 205.01 | 0.3507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MU | memory_hbm_storage | 969.345 |  | 968.4703 | 0.0903 | 963.41 | 936.99 | 1.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | AMD | ai_accelerator | 557.29 |  | 552.3682 | 0.891 | 548.755 | 526.6 | 1.4122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | SNDK | memory_hbm_storage | 1610.26 |  | 1582.0586 | 1.7826 | 1558.88 | 1518.99 | 3.7398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | WDC | memory_hbm_storage | 558.065 |  | 556.2284 | 0.3302 | 548.14 | 526.22 | 0.9479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.46 |  | 707.4518 | 0.0012 | 705.86 | 703.63 | 0.0042 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 70.9 |  | 70.8599 | 0.0566 | 70.43 | 69.81 | 0.0282 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.83 |  | 211.6096 | 1.0493 | 207.4 | 205.01 | 0.3507 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MSFT | cloud_ai_capex | 389.41 |  | 389.7358 | -0.0836 | 400.89 | 392.26 | 0.018 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.37 |  | 324.9586 | -0.1811 | 328.865 | 325.74 | 0.3237 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 346.04 |  | 347.689 | -0.4743 | 348.76 | 346.23 | 0.052 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 557.29 |  | 552.3682 | 0.891 | 548.755 | 526.6 | 1.4122 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.86 |  | 421.0334 | 0.4338 | 419.42 | 414.87 | 0.1017 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.61 |  | 553.9284 | 0.8452 | 551.02 | 540.105 | 0.034 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.3 |  | 586.5674 | 0.6364 | 581.9 | 572.01 | 0.0424 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.11 |  | 391.9607 | 1.5689 | 387.635 | 380.205 | 0.5049 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 969.345 |  | 968.4703 | 0.0903 | 963.41 | 936.99 | 1.2379 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.61 |  | 211.5233 | 0.5137 | 207.06 | 202.18 | 1.0065 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 442.32 |  | 442.3527 | -0.0074 | 435.98 | 415.79 | 0.3436 | below_vwap | below_vwap |
| HPE | ai_server_oem | 48.43 |  | 48.9331 | -1.0282 | 48.96 | 47.01 | 0.0619 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.83 |  | 31.1493 | -1.025 | 30.66 | 28.52 | 0.0324 | below_vwap | below_vwap |
| SPY | market_regime | 748.285 |  | 748.5044 | -0.0293 | 747.68 | 746.425 | 0.0187 | below_vwap | below_vwap |
| IWM | market_regime | 293.825 |  | 294.9385 | -0.3775 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.35 |  | 126.4805 | -0.8938 | 128.79 | 125.83 | 1.069 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.38 |  | 83.3453 | 0.0416 | 83.22 | 79.6 | 4.7493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 302.54 |  | 299.6739 | 0.9564 | 297.69 | 293.905 | 0.1587 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.635 |  | 407.7926 | -0.2839 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 642.555 |  | 641.5782 | 0.1522 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 992.22 |  | 1004.4966 | -1.2222 | 1036.605 | 998.94 | 1.2598 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.165 |  | 473.8944 | -0.1539 | 473.865 | 466.83 | 0.1247 | below_vwap | below_vwap |
| JCI | data_center_power_cooling | 142.555 |  | 142.9446 | -0.2726 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.53 |  | 174.9531 | 0.3297 | 175.265 | 171.06 | 2.4953 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.815 |  | 316.0255 | -0.0666 | 317.93 | 306.89 | 0.4908 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 826.61 |  | 838.0763 | -1.3682 | 840.47 | 814.62 | 0.3617 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 401.76 |  | 405.094 | -0.823 | 407.12 | 397.835 | 1.7025 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.1 |  | 114.0235 | -2.564 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.58 |  | 329.9061 | 0.2043 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1803.99 |  | 1799.1559 | 0.2687 | 1786.525 | 1767.54 | 0.066 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.575 |  | 558.8178 | 0.3145 | 559.22 | 544.305 | 0.0945 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 320.82 |  | 319.555 | 0.3959 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.49 |  | 216.1558 | 0.1546 | 215.465 | 210.975 | 0.0323 | buy_precheck_manual_confirm | none |
| TER | semiconductor_test_packaging | 371.4 |  | 371.6687 | -0.0723 | 369.53 | 365 | 0.1589 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.58 |  | 295.3907 | 0.4026 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.38 |  | 67.4697 | -0.133 | 66.73 | 64.98 | 3.829 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.55 |  | 55.6406 | -0.1629 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.95 |  | 138.8605 | 0.0645 | 140.09 | 135.555 | 0.2015 | watch_only | none |
| MKSI | semiconductor_materials | 347.585 |  | 345.4675 | 0.6129 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.185 |  | 507.4416 | 0.3436 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.07 |  | 297.8135 | -0.2496 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.115 |  | 30.6757 | -1.8279 | 30.78 | 29.46 | 0.0996 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.585 |  | 42.465 | -2.0724 | 42.29 | 40.305 | 0.024 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.63 |  | 23.9857 | -1.483 | 24.255 | 23.58 | 0.127 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1610.26 |  | 1582.0586 | 1.7826 | 1558.88 | 1518.99 | 3.7398 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.065 |  | 556.2284 | 0.3302 | 548.14 | 526.22 | 0.9479 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 905.025 |  | 909.4712 | -0.4889 | 899.59 | 860.605 | 1.9425 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 244.34 |  | 244.1705 | 0.0694 | 248.43 | 244.47 | 0.0123 | below_opening_15m_low | below_opening_15m_low |
| META | cloud_ai_capex | 627.54 |  | 630.2858 | -0.4356 | 647.02 | 632.77 | 0.7171 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.73 |  | 285.5847 | 0.0509 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 166.605 |  | 166.7376 | -0.0795 | 166.63 | 162.08 | 1.3265 | below_vwap | below_vwap,spread_too_wide |
