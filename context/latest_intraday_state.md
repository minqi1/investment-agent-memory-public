# Intraday State

- Generated at: `2026-07-23T03:53:49+08:00`
- Market time ET: `2026-07-22T15:53:50-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 25, 'manual_confirm_candidate': 6, 'below_opening_15m_low': 7, 'watch_only': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 14}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.57 |  | 707.3476 | -0.1099 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.06 |  | 554.7818 | 0.4107 | 551.02 | 540.105 | 0.0521 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.395 |  | 586.8208 | 0.2683 | 581.9 | 572.01 | 0.0238 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.9 |  | 748.3853 | -0.0648 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.55 |  | 211.7973 | 0.3554 | 207.4 | 205.01 | 0.0282 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 971.835 |  | 969.0584 | 0.2865 | 963.41 | 936.99 | 0.0453 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 422.97 |  | 421.2669 | 0.4043 | 419.42 | 414.87 | 0.0922 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.06 |  | 554.7818 | 0.4107 | 551.02 | 540.105 | 0.0521 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 588.395 |  | 586.8208 | 0.2683 | 581.9 | 572.01 | 0.0238 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1807.64 |  | 1799.7723 | 0.4371 | 1786.525 | 1767.54 | 0.0254 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MU | memory_hbm_storage | 971.835 |  | 969.0584 | 0.2865 | 963.41 | 936.99 | 0.0453 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 588.395 |  | 586.8208 | 0.2683 | 581.9 | 572.01 | 0.0238 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 325.94 |  | 324.9062 | 0.3182 | 328.865 | 325.74 | 0.0123 | watch_only | none |
| 4 | ETN | data_center_power_cooling | 408.06 |  | 407.661 | 0.0979 | 409.095 | 398.16 | 0.0368 | watch_only | none |
| 5 | TSM | foundry | 422.97 |  | 421.2669 | 0.4043 | 419.42 | 414.87 | 0.0922 | buy_precheck_manual_confirm | none |
| 6 | SOXX | semiconductor_index | 557.06 |  | 554.7818 | 0.4107 | 551.02 | 540.105 | 0.0521 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1807.64 |  | 1799.7723 | 0.4371 | 1786.525 | 1767.54 | 0.0254 | buy_precheck_manual_confirm | none |
| 8 | AMZN | cloud_ai_capex | 244.85 |  | 244.2804 | 0.2332 | 248.43 | 244.47 | 0.1879 | watch_only | none |
| 9 | NVDA | ai_accelerator | 212.55 |  | 211.7973 | 0.3554 | 207.4 | 205.01 | 0.0282 | buy_precheck_manual_confirm | none |
| 10 | TT | data_center_power_cooling | 474.43 |  | 473.8821 | 0.1156 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | LIN | industrial_gases | 508.685 |  | 507.6578 | 0.2023 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | PWR | data_center_power_cooling | 644.25 |  | 642.3262 | 0.2995 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ONTO | semiconductor_test_packaging | 296.02 |  | 295.4392 | 0.1966 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | STX | memory_hbm_storage | 911.53 |  | 909.63 | 0.2089 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SKHY | memory_hbm_storage | 166.875 |  | 166.7215 | 0.0921 | 166.63 | 162.08 | 1.4322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ANET | ai_networking_optical | 175.18 |  | 175.0412 | 0.0793 | 175.265 | 171.06 | 2.6373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LRCX | semiconductor_equipment | 319.85 |  | 319.6429 | 0.0648 | 317.72 | 311.31 | 5.0211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ALAB | ai_networking_optical | 330.19 |  | 329.9901 | 0.0606 | 322.67 | 307.545 | 4.5731 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | QQQ | market_regime | 706.57 |  | 707.3476 | -0.1099 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 20 | TER | semiconductor_test_packaging | 370.35 |  | 371.5781 | -0.3305 | 369.53 | 365 | 0.1323 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.55 |  | 211.7973 | 0.3554 | 207.4 | 205.01 | 0.0282 | buy_precheck_manual_confirm | none |
| 2 | MU | memory_hbm_storage | 971.835 |  | 969.0584 | 0.2865 | 963.41 | 936.99 | 0.0453 | buy_precheck_manual_confirm | none |
| 3 | TSM | foundry | 422.97 |  | 421.2669 | 0.4043 | 419.42 | 414.87 | 0.0922 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.06 |  | 554.7818 | 0.4107 | 551.02 | 540.105 | 0.0521 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 588.395 |  | 586.8208 | 0.2683 | 581.9 | 572.01 | 0.0238 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1807.64 |  | 1799.7723 | 0.4371 | 1786.525 | 1767.54 | 0.0254 | buy_precheck_manual_confirm | none |
| 7 | AMD | ai_accelerator | 552.62 |  | 553.6624 | -0.1883 | 548.755 | 526.6 | 0.9554 | below_vwap | below_vwap,spread_too_wide |
| 8 | MRVL | custom_silicon_networking | 211.585 |  | 211.5913 | -0.003 | 207.06 | 202.18 | 1.4982 | below_vwap | below_vwap,spread_too_wide |
| 9 | QQQ | market_regime | 706.57 |  | 707.3476 | -0.1099 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 747.9 |  | 748.3853 | -0.0648 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 11 | TER | semiconductor_test_packaging | 370.35 |  | 371.5781 | -0.3305 | 369.53 | 365 | 0.1323 | below_vwap | below_vwap |
| 12 | AMKR | semiconductor_test_packaging | 67.185 |  | 67.4214 | -0.3506 | 66.73 | 64.98 | 2.5452 | below_vwap | below_vwap,spread_too_wide |
| 13 | SMCI | ai_server_oem | 30.74 |  | 31.1141 | -1.2023 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| 14 | TT | data_center_power_cooling | 474.43 |  | 473.8821 | 0.1156 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SNDK | memory_hbm_storage | 1603 |  | 1585.301 | 1.1164 | 1558.88 | 1518.99 | 2.6282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | WDC | memory_hbm_storage | 559.87 |  | 556.6614 | 0.5764 | 548.14 | 526.22 | 1.2878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | STX | memory_hbm_storage | 911.53 |  | 909.63 | 0.2089 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 397.3 |  | 392.9394 | 1.1097 | 387.635 | 380.205 | 0.589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | TQQQ | leveraged_tool | 70.635 |  | 70.8425 | -0.2929 | 70.43 | 69.81 | 0.0142 | below_vwap | below_vwap |
| 20 | SKHY | memory_hbm_storage | 166.875 |  | 166.7215 | 0.0921 | 166.63 | 162.08 | 1.4322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.57 |  | 707.3476 | -0.1099 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.635 |  | 70.8425 | -0.2929 | 70.43 | 69.81 | 0.0142 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 212.55 |  | 211.7973 | 0.3554 | 207.4 | 205.01 | 0.0282 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.605 |  | 389.6391 | -0.0088 | 400.89 | 392.26 | 0.0154 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 325.94 |  | 324.9062 | 0.3182 | 328.865 | 325.74 | 0.0123 | watch_only | none |
| GOOGL | cloud_ai_capex | 344.15 |  | 346.9672 | -0.812 | 348.76 | 346.23 | 0.0378 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 552.62 |  | 553.6624 | -0.1883 | 548.755 | 526.6 | 0.9554 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 422.97 |  | 421.2669 | 0.4043 | 419.42 | 414.87 | 0.0922 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.06 |  | 554.7818 | 0.4107 | 551.02 | 540.105 | 0.0521 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.395 |  | 586.8208 | 0.2683 | 581.9 | 572.01 | 0.0238 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.3 |  | 392.9394 | 1.1097 | 387.635 | 380.205 | 0.589 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 971.835 |  | 969.0584 | 0.2865 | 963.41 | 936.99 | 0.0453 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 211.585 |  | 211.5913 | -0.003 | 207.06 | 202.18 | 1.4982 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 445.58 |  | 442.5709 | 0.6799 | 435.98 | 415.79 | 0.8416 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.535 |  | 48.8708 | -0.6871 | 48.96 | 47.01 | 0.0412 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.74 |  | 31.1141 | -1.2023 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| SPY | market_regime | 747.9 |  | 748.3853 | -0.0648 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.65 |  | 294.719 | -0.3627 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.84 |  | 126.4243 | -0.4621 | 128.79 | 125.83 | 0.5324 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.03 |  | 83.3222 | -0.3507 | 83.22 | 79.6 | 4.4442 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.86 |  | 300.1569 | 0.9006 | 297.69 | 293.905 | 3.6023 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 408.06 |  | 407.661 | 0.0979 | 409.095 | 398.16 | 0.0368 | watch_only | none |
| PWR | data_center_power_cooling | 644.25 |  | 642.3262 | 0.2995 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 994.11 |  | 1002.8338 | -0.8699 | 1036.605 | 998.94 | 1.7101 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.43 |  | 473.8821 | 0.1156 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.66 |  | 142.8229 | -0.1141 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.18 |  | 175.0412 | 0.0793 | 175.265 | 171.06 | 2.6373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 313.74 |  | 315.7002 | -0.6209 | 317.93 | 306.89 | 3.0599 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 818.75 |  | 835.2578 | -1.9764 | 840.47 | 814.62 | 1.4327 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 398.31 |  | 404.0945 | -1.4315 | 407.12 | 397.835 | 0.1029 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 110.585 |  | 113.6836 | -2.7257 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.19 |  | 329.9901 | 0.0606 | 322.67 | 307.545 | 4.5731 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1807.64 |  | 1799.7723 | 0.4371 | 1786.525 | 1767.54 | 0.0254 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 557.51 |  | 558.9157 | -0.2515 | 559.22 | 544.305 | 3.5156 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.85 |  | 319.6429 | 0.0648 | 317.72 | 311.31 | 5.0211 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 215.07 |  | 216.081 | -0.4679 | 215.465 | 210.975 | 0.0372 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 370.35 |  | 371.5781 | -0.3305 | 369.53 | 365 | 0.1323 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.02 |  | 295.4392 | 0.1966 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.185 |  | 67.4214 | -0.3506 | 66.73 | 64.98 | 2.5452 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.16 |  | 55.477 | -0.5714 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.39 |  | 138.8048 | -0.2988 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 344.71 |  | 345.5993 | -0.2573 | 345.675 | 331.945 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 508.685 |  | 507.6578 | 0.2023 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.24 |  | 297.5985 | -0.4565 | 300.24 | 297.585 | 0.0371 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| APLD | high_beta_ai_infrastructure | 30.28 |  | 30.6317 | -1.1482 | 30.78 | 29.46 | 0.0991 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.38 |  | 42.3468 | -2.2831 | 42.29 | 40.305 | 0.0242 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.59 |  | 23.9418 | -1.4695 | 24.255 | 23.58 | 0.0848 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1603 |  | 1585.301 | 1.1164 | 1558.88 | 1518.99 | 2.6282 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 559.87 |  | 556.6614 | 0.5764 | 548.14 | 526.22 | 1.2878 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 911.53 |  | 909.63 | 0.2089 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 244.85 |  | 244.2804 | 0.2332 | 248.43 | 244.47 | 0.1879 | watch_only | none |
| META | cloud_ai_capex | 625.44 |  | 629.6377 | -0.6667 | 647.02 | 632.77 | 1.471 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.39 |  | 285.5573 | -0.0586 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 166.875 |  | 166.7215 | 0.0921 | 166.63 | 162.08 | 1.4322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
