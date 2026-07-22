# Intraday State

- Generated at: `2026-07-23T03:38:19+08:00`
- Market time ET: `2026-07-22T15:38:20-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'manual_confirm_candidate': 9, 'below_opening_15m_low': 9, 'spread_too_wide_or_missing': 13, 'price_stale_or_missing': 1, 'watch_only': 3}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.72 |  | 707.4292 | -0.1002 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.78 |  | 554.5563 | 0.5813 | 551.02 | 540.105 | 0.0376 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.05 |  | 586.7265 | 0.396 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.59 |  | 748.4499 | -0.1149 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.61 |  | 211.7569 | 0.4029 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.68 |  | 421.1907 | 0.1162 | 419.42 | 414.87 | 0.0379 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.12 |  | 473.775 | 0.0728 | 473.865 | 466.83 | 0.0612 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.78 |  | 554.5563 | 0.5813 | 551.02 | 540.105 | 0.0376 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.05 |  | 586.7265 | 0.396 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 211.7 |  | 211.5902 | 0.0519 | 207.06 | 202.18 | 0.2645 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1803.11 |  | 1799.3805 | 0.2073 | 1786.525 | 1767.54 | 0.0804 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 559.37 |  | 558.9842 | 0.069 | 559.22 | 544.305 | 0.3468 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 303.09 |  | 299.9483 | 1.0474 | 297.69 | 293.905 | 0.0957 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TT | data_center_power_cooling | 474.12 |  | 473.775 | 0.0728 | 473.865 | 466.83 | 0.0612 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.68 |  | 421.1907 | 0.1162 | 419.42 | 414.87 | 0.0379 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 559.37 |  | 558.9842 | 0.069 | 559.22 | 544.305 | 0.3468 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1803.11 |  | 1799.3805 | 0.2073 | 1786.525 | 1767.54 | 0.0804 | buy_precheck_manual_confirm | none |
| 5 | ANET | ai_networking_optical | 175.2 |  | 174.9947 | 0.1173 | 175.265 | 171.06 | 0.0856 | watch_only | none |
| 6 | ETN | data_center_power_cooling | 407.7 |  | 407.643 | 0.014 | 409.095 | 398.16 | 0.0809 | watch_only | none |
| 7 | AMZN | cloud_ai_capex | 244.47 |  | 244.2393 | 0.0944 | 248.43 | 244.47 | 0.0123 | watch_only | none |
| 8 | SOXX | semiconductor_index | 557.78 |  | 554.5563 | 0.5813 | 551.02 | 540.105 | 0.0376 | buy_precheck_manual_confirm | none |
| 9 | SMH | semiconductor_index | 589.05 |  | 586.7265 | 0.396 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| 10 | MRVL | custom_silicon_networking | 211.7 |  | 211.5902 | 0.0519 | 207.06 | 202.18 | 0.2645 | buy_precheck_manual_confirm | none |
| 11 | NVDA | ai_accelerator | 212.61 |  | 211.7569 | 0.4029 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| 12 | ARM | ai_accelerator | 285.63 |  | 285.5813 | 0.0171 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | LRCX | semiconductor_equipment | 319.98 |  | 319.6391 | 0.1066 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 296.02 |  | 295.4285 | 0.2002 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | STX | memory_hbm_storage | 910.91 |  | 909.5369 | 0.151 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | VRT | data_center_power_cooling | 303.09 |  | 299.9483 | 1.0474 | 297.69 | 293.905 | 0.0957 | buy_precheck_manual_confirm | none |
| 17 | LIN | industrial_gases | 509.19 |  | 507.5326 | 0.3266 | 507.545 | 505.59 | 4.5366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MKSI | semiconductor_materials | 345.95 |  | 345.6051 | 0.0998 | 345.675 | 331.945 | 0.4712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 644.73 |  | 641.9202 | 0.4377 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | MU | memory_hbm_storage | 976.05 |  | 968.8521 | 0.7429 | 963.41 | 936.99 | 0.4682 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.61 |  | 211.7569 | 0.4029 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.68 |  | 421.1907 | 0.1162 | 419.42 | 414.87 | 0.0379 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.12 |  | 473.775 | 0.0728 | 473.865 | 466.83 | 0.0612 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.78 |  | 554.5563 | 0.5813 | 551.02 | 540.105 | 0.0376 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 589.05 |  | 586.7265 | 0.396 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| 6 | MRVL | custom_silicon_networking | 211.7 |  | 211.5902 | 0.0519 | 207.06 | 202.18 | 0.2645 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1803.11 |  | 1799.3805 | 0.2073 | 1786.525 | 1767.54 | 0.0804 | buy_precheck_manual_confirm | none |
| 8 | AMAT | semiconductor_equipment | 559.37 |  | 558.9842 | 0.069 | 559.22 | 544.305 | 0.3468 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 303.09 |  | 299.9483 | 1.0474 | 297.69 | 293.905 | 0.0957 | buy_precheck_manual_confirm | none |
| 10 | QQQ | market_regime | 706.72 |  | 707.4292 | -0.1002 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| 11 | TER | semiconductor_test_packaging | 371.43 |  | 371.6614 | -0.0622 | 369.53 | 365 | 0.2423 | below_vwap | below_vwap |
| 12 | KLAC | semiconductor_equipment | 215.64 |  | 216.1574 | -0.2394 | 215.465 | 210.975 | 0.0603 | below_vwap | below_vwap |
| 13 | ALAB | ai_networking_optical | 329.955 |  | 330.0391 | -0.0255 | 322.67 | 307.545 | 4.2763 | below_vwap | below_vwap,spread_too_wide |
| 14 | AMKR | semiconductor_test_packaging | 67.23 |  | 67.4549 | -0.3335 | 66.73 | 64.98 | 2.7517 | below_vwap | below_vwap,spread_too_wide |
| 15 | MU | memory_hbm_storage | 976.05 |  | 968.8521 | 0.7429 | 963.41 | 936.99 | 0.4682 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AMD | ai_accelerator | 556.03 |  | 553.6191 | 0.4355 | 548.755 | 526.6 | 4.0555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | SNDK | memory_hbm_storage | 1610.29 |  | 1584.348 | 1.6374 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | WDC | memory_hbm_storage | 559.12 |  | 556.4083 | 0.4874 | 548.14 | 526.22 | 1.1303 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | STX | memory_hbm_storage | 910.91 |  | 909.5369 | 0.151 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 398.19 |  | 392.4477 | 1.4632 | 387.635 | 380.205 | 0.4646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.72 |  | 707.4292 | -0.1002 | 705.86 | 703.63 | 0.0071 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.66 |  | 70.8538 | -0.2735 | 70.43 | 69.81 | 0.0142 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 212.61 |  | 211.7569 | 0.4029 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.835 |  | 389.69 | -0.2194 | 400.89 | 392.26 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.26 |  | 324.9265 | -0.2051 | 328.865 | 325.74 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 344.93 |  | 347.3583 | -0.6991 | 348.76 | 346.23 | 0.0348 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 556.03 |  | 553.6191 | 0.4355 | 548.755 | 526.6 | 4.0555 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.68 |  | 421.1907 | 0.1162 | 419.42 | 414.87 | 0.0379 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.78 |  | 554.5563 | 0.5813 | 551.02 | 540.105 | 0.0376 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.05 |  | 586.7265 | 0.396 | 581.9 | 572.01 | 0.039 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.19 |  | 392.4477 | 1.4632 | 387.635 | 380.205 | 0.4646 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 976.05 |  | 968.8521 | 0.7429 | 963.41 | 936.99 | 0.4682 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 211.7 |  | 211.5902 | 0.0519 | 207.06 | 202.18 | 0.2645 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 443.985 |  | 442.4928 | 0.3372 | 435.98 | 415.79 | 1.4145 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.485 |  | 48.8931 | -0.8347 | 48.96 | 47.01 | 0.0412 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.47 |  | 31.1322 | -2.1272 | 30.66 | 28.52 | 0.0328 | below_vwap | below_vwap |
| SPY | market_regime | 747.59 |  | 748.4499 | -0.1149 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.57 |  | 294.8116 | -0.4211 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.77 |  | 126.4475 | -0.5358 | 128.79 | 125.83 | 2.3615 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.03 |  | 83.3332 | -0.3638 | 83.22 | 79.6 | 0.6504 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.09 |  | 299.9483 | 1.0474 | 297.69 | 293.905 | 0.0957 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.7 |  | 407.643 | 0.014 | 409.095 | 398.16 | 0.0809 | watch_only | none |
| PWR | data_center_power_cooling | 644.73 |  | 641.9202 | 0.4377 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 992.34 |  | 1003.6855 | -1.1304 | 1036.605 | 998.94 | 1.2596 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.12 |  | 473.775 | 0.0728 | 473.865 | 466.83 | 0.0612 | buy_precheck_manual_confirm | none |
| JCI | data_center_power_cooling | 142.73 |  | 142.8454 | -0.0808 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.2 |  | 174.9947 | 0.1173 | 175.265 | 171.06 | 0.0856 | watch_only | none |
| COHR | ai_networking_optical | 314.1 |  | 315.9669 | -0.5909 | 317.93 | 306.89 | 0.086 | below_vwap | below_vwap |
| LITE | ai_networking_optical | 831.09 |  | 837.6817 | -0.7869 | 840.47 | 814.62 | 0.1492 | below_vwap | below_vwap |
| CIEN | ai_networking_optical | 400.42 |  | 404.5144 | -1.0122 | 407.12 | 397.835 | 0.2822 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.37 |  | 113.8298 | -2.161 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 329.955 |  | 330.0391 | -0.0255 | 322.67 | 307.545 | 4.2763 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1803.11 |  | 1799.3805 | 0.2073 | 1786.525 | 1767.54 | 0.0804 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.37 |  | 558.9842 | 0.069 | 559.22 | 544.305 | 0.3468 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 319.98 |  | 319.6391 | 0.1066 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.64 |  | 216.1574 | -0.2394 | 215.465 | 210.975 | 0.0603 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 371.43 |  | 371.6614 | -0.0622 | 369.53 | 365 | 0.2423 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.02 |  | 295.4285 | 0.2002 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.23 |  | 67.4549 | -0.3335 | 66.73 | 64.98 | 2.7517 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.035 |  | 55.5498 | -0.9268 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.38 |  | 138.8888 | -0.3664 | 140.09 | 135.555 | 0.1807 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 345.95 |  | 345.6051 | 0.0998 | 345.675 | 331.945 | 0.4712 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 509.19 |  | 507.5326 | 0.3266 | 507.545 | 505.59 | 4.5366 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.065 |  | 297.6978 | -0.2126 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.13 |  | 30.6473 | -1.6878 | 30.78 | 29.46 | 0.0664 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.5 |  | 42.3976 | -2.1171 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.625 |  | 23.9649 | -1.4182 | 24.255 | 23.58 | 0.0423 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1610.29 |  | 1584.348 | 1.6374 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.12 |  | 556.4083 | 0.4874 | 548.14 | 526.22 | 1.1303 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 910.91 |  | 909.5369 | 0.151 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 244.47 |  | 244.2393 | 0.0944 | 248.43 | 244.47 | 0.0123 | watch_only | none |
| META | cloud_ai_capex | 625.505 |  | 629.9839 | -0.711 | 647.02 | 632.77 | 0.1215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.63 |  | 285.5813 | 0.0171 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 166.345 |  | 166.7196 | -0.2247 | 166.63 | 162.08 | 1.4368 | below_vwap | below_vwap,spread_too_wide |
