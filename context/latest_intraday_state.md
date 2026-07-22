# Intraday State

- Generated at: `2026-07-23T03:46:02+08:00`
- Market time ET: `2026-07-22T15:46:03-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 24, 'manual_confirm_candidate': 10, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 12, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.5 |  | 707.399 | -0.1271 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 557.33 |  | 554.6277 | 0.4872 | 551.02 | 540.105 | 0.052 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.49 |  | 586.7594 | 0.2949 | 581.9 | 572.01 | 0.0425 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.785 |  | 748.4225 | -0.0852 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.48 |  | 211.777 | 0.3319 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.14 |  | 421.2053 | 0.2219 | 419.42 | 414.87 | 0.2582 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 911.45 |  | 909.5677 | 0.2069 | 899.59 | 860.605 | 0.1459 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.33 |  | 554.6277 | 0.4872 | 551.02 | 540.105 | 0.052 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 588.49 |  | 586.7594 | 0.2949 | 581.9 | 572.01 | 0.0425 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 398.16 |  | 392.6149 | 1.4124 | 387.635 | 380.205 | 0.0779 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.4 |  | 1799.4633 | 0.3299 | 1786.525 | 1767.54 | 0.0371 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 175.555 |  | 175.0164 | 0.3077 | 175.265 | 171.06 | 0.1538 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 303.015 |  | 300.0096 | 1.0018 | 297.69 | 293.905 | 0.0627 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 645.8 |  | 642.0501 | 0.5841 | 641.19 | 628.17 | 0.1843 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | ANET | ai_networking_optical | 175.555 |  | 175.0164 | 0.3077 | 175.265 | 171.06 | 0.1538 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.14 |  | 421.2053 | 0.2219 | 419.42 | 414.87 | 0.2582 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 911.45 |  | 909.5677 | 0.2069 | 899.59 | 860.605 | 0.1459 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 588.49 |  | 586.7594 | 0.2949 | 581.9 | 572.01 | 0.0425 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1805.4 |  | 1799.4633 | 0.3299 | 1786.525 | 1767.54 | 0.0371 | buy_precheck_manual_confirm | none |
| 6 | NVDA | ai_accelerator | 212.48 |  | 211.777 | 0.3319 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| 7 | AMZN | cloud_ai_capex | 244.81 |  | 244.2529 | 0.2281 | 248.43 | 244.47 | 0.0082 | watch_only | none |
| 8 | SOXX | semiconductor_index | 557.33 |  | 554.6277 | 0.4872 | 551.02 | 540.105 | 0.052 | buy_precheck_manual_confirm | none |
| 9 | PWR | data_center_power_cooling | 645.8 |  | 642.0501 | 0.5841 | 641.19 | 628.17 | 0.1843 | buy_precheck_manual_confirm | none |
| 10 | TT | data_center_power_cooling | 474.47 |  | 473.7873 | 0.1441 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MKSI | semiconductor_materials | 345.825 |  | 345.6145 | 0.0609 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ETN | data_center_power_cooling | 407.92 |  | 407.648 | 0.0667 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | AVGO | custom_silicon_networking | 398.16 |  | 392.6149 | 1.4124 | 387.635 | 380.205 | 0.0779 | buy_precheck_manual_confirm | none |
| 14 | VRT | data_center_power_cooling | 303.015 |  | 300.0096 | 1.0018 | 297.69 | 293.905 | 0.0627 | buy_precheck_manual_confirm | none |
| 15 | SKHY | memory_hbm_storage | 167.165 |  | 166.7138 | 0.2707 | 166.63 | 162.08 | 0.5145 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | LIN | industrial_gases | 508.55 |  | 507.565 | 0.1941 | 507.545 | 505.59 | 4.6898 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | CRWV | gpu_cloud_ai_factory | 83.41 |  | 83.3324 | 0.0931 | 83.22 | 79.6 | 0.4796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MU | memory_hbm_storage | 972.32 |  | 968.9744 | 0.3453 | 963.41 | 936.99 | 1.6455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ONTO | semiconductor_test_packaging | 296.135 |  | 295.4338 | 0.2373 | 298.42 | 288.335 | 4.7647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | AMD | ai_accelerator | 555.39 |  | 553.6634 | 0.3119 | 548.755 | 526.6 | 4.5031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.48 |  | 211.777 | 0.3319 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 422.14 |  | 421.2053 | 0.2219 | 419.42 | 414.87 | 0.2582 | buy_precheck_manual_confirm | none |
| 3 | STX | memory_hbm_storage | 911.45 |  | 909.5677 | 0.2069 | 899.59 | 860.605 | 0.1459 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 557.33 |  | 554.6277 | 0.4872 | 551.02 | 540.105 | 0.052 | buy_precheck_manual_confirm | none |
| 5 | SMH | semiconductor_index | 588.49 |  | 586.7594 | 0.2949 | 581.9 | 572.01 | 0.0425 | buy_precheck_manual_confirm | none |
| 6 | AVGO | custom_silicon_networking | 398.16 |  | 392.6149 | 1.4124 | 387.635 | 380.205 | 0.0779 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1805.4 |  | 1799.4633 | 0.3299 | 1786.525 | 1767.54 | 0.0371 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 175.555 |  | 175.0164 | 0.3077 | 175.265 | 171.06 | 0.1538 | buy_precheck_manual_confirm | none |
| 9 | VRT | data_center_power_cooling | 303.015 |  | 300.0096 | 1.0018 | 297.69 | 293.905 | 0.0627 | buy_precheck_manual_confirm | none |
| 10 | PWR | data_center_power_cooling | 645.8 |  | 642.0501 | 0.5841 | 641.19 | 628.17 | 0.1843 | buy_precheck_manual_confirm | none |
| 11 | MRVL | custom_silicon_networking | 211.585 |  | 211.5892 | -0.002 | 207.06 | 202.18 | 1.6778 | below_vwap | below_vwap,spread_too_wide |
| 12 | QQQ | market_regime | 706.5 |  | 707.399 | -0.1271 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 13 | SPY | market_regime | 747.785 |  | 748.4225 | -0.0852 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 14 | TER | semiconductor_test_packaging | 370.77 |  | 371.6442 | -0.2352 | 369.53 | 365 | 0.2077 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 319.29 |  | 319.6336 | -0.1075 | 317.72 | 311.31 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | ALAB | ai_networking_optical | 328.3 |  | 329.9789 | -0.5088 | 322.67 | 307.545 | 0.2772 | below_vwap | below_vwap |
| 17 | AMKR | semiconductor_test_packaging | 67.105 |  | 67.4399 | -0.4965 | 66.73 | 64.98 | 2.742 | below_vwap | below_vwap,spread_too_wide |
| 18 | MU | memory_hbm_storage | 972.32 |  | 968.9744 | 0.3453 | 963.41 | 936.99 | 1.6455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 555.39 |  | 553.6634 | 0.3119 | 548.755 | 526.6 | 4.5031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TT | data_center_power_cooling | 474.47 |  | 473.7873 | 0.1441 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 706.5 |  | 707.399 | -0.1271 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.65 |  | 70.8496 | -0.2817 | 70.43 | 69.81 | 0.0283 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 212.48 |  | 211.777 | 0.3319 | 207.4 | 205.01 | 0.0141 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.74 |  | 389.6573 | -0.2354 | 400.89 | 392.26 | 0.0129 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.465 |  | 324.8738 | -0.1258 | 328.865 | 325.74 | 0.4161 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| GOOGL | cloud_ai_capex | 345.28 |  | 347.1972 | -0.5522 | 348.76 | 346.23 | 0.1043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 555.39 |  | 553.6634 | 0.3119 | 548.755 | 526.6 | 4.5031 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.14 |  | 421.2053 | 0.2219 | 419.42 | 414.87 | 0.2582 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 557.33 |  | 554.6277 | 0.4872 | 551.02 | 540.105 | 0.052 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 588.49 |  | 586.7594 | 0.2949 | 581.9 | 572.01 | 0.0425 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 398.16 |  | 392.6149 | 1.4124 | 387.635 | 380.205 | 0.0779 | buy_precheck_manual_confirm | none |
| MU | memory_hbm_storage | 972.32 |  | 968.9744 | 0.3453 | 963.41 | 936.99 | 1.6455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 211.585 |  | 211.5892 | -0.002 | 207.06 | 202.18 | 1.6778 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.25 |  | 442.5052 | 0.1683 | 435.98 | 415.79 | 1.586 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.345 |  | 48.8844 | -1.1034 | 48.96 | 47.01 | 0.0207 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.505 |  | 31.1212 | -1.9801 | 30.66 | 28.52 | 0.0328 | below_vwap | below_vwap |
| SPY | market_regime | 747.785 |  | 748.4225 | -0.0852 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.57 |  | 294.7576 | -0.4029 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.04 |  | 126.437 | -0.314 | 128.79 | 125.83 | 0.3253 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.41 |  | 83.3324 | 0.0931 | 83.22 | 79.6 | 0.4796 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 303.015 |  | 300.0096 | 1.0018 | 297.69 | 293.905 | 0.0627 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.92 |  | 407.648 | 0.0667 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 645.8 |  | 642.0501 | 0.5841 | 641.19 | 628.17 | 0.1843 | buy_precheck_manual_confirm | none |
| GEV | data_center_power_cooling | 990.02 |  | 1003.3458 | -1.3281 | 1036.605 | 998.94 | 0.2252 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 474.47 |  | 473.7873 | 0.1441 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.635 |  | 142.836 | -0.1407 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.555 |  | 175.0164 | 0.3077 | 175.265 | 171.06 | 0.1538 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 313.38 |  | 315.8335 | -0.7768 | 317.93 | 306.89 | 3.3761 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 822.595 |  | 836.7372 | -1.6902 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 399.45 |  | 404.3871 | -1.2209 | 407.12 | 397.835 | 1.1516 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.825 |  | 113.7721 | -2.5904 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 328.3 |  | 329.9789 | -0.5088 | 322.67 | 307.545 | 0.2772 | below_vwap | below_vwap |
| ASML | semiconductor_equipment | 1805.4 |  | 1799.4633 | 0.3299 | 1786.525 | 1767.54 | 0.0371 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 558.52 |  | 558.9744 | -0.0813 | 559.22 | 544.305 | 0.0698 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 319.29 |  | 319.6336 | -0.1075 | 317.72 | 311.31 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 215.21 |  | 216.133 | -0.4271 | 215.465 | 210.975 | 2.7136 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 370.77 |  | 371.6442 | -0.2352 | 369.53 | 365 | 0.2077 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.135 |  | 295.4338 | 0.2373 | 298.42 | 288.335 | 4.7647 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMKR | semiconductor_test_packaging | 67.105 |  | 67.4399 | -0.4965 | 66.73 | 64.98 | 2.742 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.04 |  | 55.5338 | -0.8892 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.57 |  | 138.863 | -0.211 | 140.09 | 135.555 | 0.0649 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 345.825 |  | 345.6145 | 0.0609 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.55 |  | 507.565 | 0.1941 | 507.545 | 505.59 | 4.6898 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 296.87 |  | 297.6745 | -0.2703 | 300.24 | 297.585 | 4.6451 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.17 |  | 30.6417 | -1.5394 | 30.78 | 29.46 | 0.0663 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.495 |  | 42.3827 | -2.0946 | 42.29 | 40.305 | 0.0482 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.59 |  | 23.9554 | -1.5255 | 24.255 | 23.58 | 0.0424 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1602.54 |  | 1584.8015 | 1.1193 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.47 |  | 556.4735 | 0.5385 | 548.14 | 526.22 | 4.9726 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 911.45 |  | 909.5677 | 0.2069 | 899.59 | 860.605 | 0.1459 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 244.81 |  | 244.2529 | 0.2281 | 248.43 | 244.47 | 0.0082 | watch_only | none |
| META | cloud_ai_capex | 626.45 |  | 629.8967 | -0.5472 | 647.02 | 632.77 | 0.1963 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.08 |  | 285.5725 | -0.1724 | 286.39 | 280.275 | 0.8454 | below_vwap | below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 167.165 |  | 166.7138 | 0.2707 | 166.63 | 162.08 | 0.5145 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
