# Intraday State

- Generated at: `2026-07-23T03:34:27+08:00`
- Market time ET: `2026-07-22T15:34:27-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 25, 'manual_confirm_candidate': 8, 'below_opening_15m_low': 8, 'spread_too_wide_or_missing': 13, 'price_stale_or_missing': 1, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.03 |  | 707.4352 | -0.0573 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 558.2 |  | 554.4985 | 0.6675 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.58 |  | 586.7101 | 0.4892 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 747.76 |  | 748.4668 | -0.0944 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.75 |  | 211.7396 | 0.4772 | 207.4 | 205.01 | 0.0611 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 911.86 |  | 909.499 | 0.2596 | 899.59 | 860.605 | 0.2149 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.2 |  | 554.4985 | 0.6675 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.58 |  | 586.7101 | 0.4892 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.18 |  | 211.5848 | 0.2813 | 207.06 | 202.18 | 0.2074 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.69 |  | 1799.3477 | 0.2413 | 1786.525 | 1767.54 | 0.0577 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 559.65 |  | 558.9702 | 0.1216 | 559.22 | 544.305 | 0.2234 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 175.39 |  | 174.989 | 0.2291 | 175.265 | 171.06 | 0.1539 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AMAT | semiconductor_equipment | 559.65 |  | 558.9702 | 0.1216 | 559.22 | 544.305 | 0.2234 | buy_precheck_manual_confirm | none |
| 2 | ANET | ai_networking_optical | 175.39 |  | 174.989 | 0.2291 | 175.265 | 171.06 | 0.1539 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1803.69 |  | 1799.3477 | 0.2413 | 1786.525 | 1767.54 | 0.0577 | buy_precheck_manual_confirm | none |
| 4 | STX | memory_hbm_storage | 911.86 |  | 909.499 | 0.2596 | 899.59 | 860.605 | 0.2149 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 244.48 |  | 244.2359 | 0.0999 | 248.43 | 244.47 | 0.0123 | watch_only | none |
| 6 | SOXX | semiconductor_index | 558.2 |  | 554.4985 | 0.6675 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 589.58 |  | 586.7101 | 0.4892 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 8 | MRVL | custom_silicon_networking | 212.18 |  | 211.5848 | 0.2813 | 207.06 | 202.18 | 0.2074 | buy_precheck_manual_confirm | none |
| 9 | NVDA | ai_accelerator | 212.75 |  | 211.7396 | 0.4772 | 207.4 | 205.01 | 0.0611 | buy_precheck_manual_confirm | none |
| 10 | LIN | industrial_gases | 508.8 |  | 507.5128 | 0.2536 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | MKSI | semiconductor_materials | 346.26 |  | 345.604 | 0.1898 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ARM | ai_accelerator | 285.82 |  | 285.5817 | 0.0834 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | ONTO | semiconductor_test_packaging | 296.05 |  | 295.4137 | 0.2154 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | TSM | foundry | 421.99 |  | 421.1804 | 0.1922 | 419.42 | 414.87 | 0.5308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 645.59 |  | 641.8429 | 0.5838 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | DELL | ai_server_oem | 443.85 |  | 442.4184 | 0.3236 | 435.98 | 415.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | MU | memory_hbm_storage | 973.875 |  | 968.6108 | 0.5435 | 963.41 | 936.99 | 1.2322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | QQQ | market_regime | 707.03 |  | 707.4352 | -0.0573 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 19 | SPY | market_regime | 747.76 |  | 748.4668 | -0.0944 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 20 | WDC | memory_hbm_storage | 558.85 |  | 556.3579 | 0.4479 | 548.14 | 526.22 | 0.7158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 212.75 |  | 211.7396 | 0.4772 | 207.4 | 205.01 | 0.0611 | buy_precheck_manual_confirm | none |
| 2 | STX | memory_hbm_storage | 911.86 |  | 909.499 | 0.2596 | 899.59 | 860.605 | 0.2149 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 558.2 |  | 554.4985 | 0.6675 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| 4 | SMH | semiconductor_index | 589.58 |  | 586.7101 | 0.4892 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| 5 | MRVL | custom_silicon_networking | 212.18 |  | 211.5848 | 0.2813 | 207.06 | 202.18 | 0.2074 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1803.69 |  | 1799.3477 | 0.2413 | 1786.525 | 1767.54 | 0.0577 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 559.65 |  | 558.9702 | 0.1216 | 559.22 | 544.305 | 0.2234 | buy_precheck_manual_confirm | none |
| 8 | ANET | ai_networking_optical | 175.39 |  | 174.989 | 0.2291 | 175.265 | 171.06 | 0.1539 | buy_precheck_manual_confirm | none |
| 9 | QQQ | market_regime | 707.03 |  | 707.4352 | -0.0573 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| 10 | SPY | market_regime | 747.76 |  | 748.4668 | -0.0944 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| 11 | TER | semiconductor_test_packaging | 371.31 |  | 371.6631 | -0.095 | 369.53 | 365 | 0.1939 | below_vwap | below_vwap |
| 12 | KLAC | semiconductor_equipment | 215.76 |  | 216.1709 | -0.1901 | 215.465 | 210.975 | 0.0371 | below_vwap | below_vwap |
| 13 | LRCX | semiconductor_equipment | 319.485 |  | 319.6351 | -0.047 | 317.72 | 311.31 | 0.338 | below_vwap | below_vwap |
| 14 | ALAB | ai_networking_optical | 329.9 |  | 330.0391 | -0.0422 | 322.67 | 307.545 | 4.4953 | below_vwap | below_vwap,spread_too_wide |
| 15 | AMKR | semiconductor_test_packaging | 67.17 |  | 67.4587 | -0.428 | 66.73 | 64.98 | 2.4267 | below_vwap | below_vwap,spread_too_wide |
| 16 | SMCI | ai_server_oem | 30.78 |  | 31.1381 | -1.1501 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| 17 | MU | memory_hbm_storage | 973.875 |  | 968.6108 | 0.5435 | 963.41 | 936.99 | 1.2322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TSM | foundry | 421.99 |  | 421.1804 | 0.1922 | 419.42 | 414.87 | 0.5308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | AMD | ai_accelerator | 561.1 |  | 553.4856 | 1.3757 | 548.755 | 526.6 | 4.8138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | SNDK | memory_hbm_storage | 1617.64 |  | 1583.9975 | 2.1239 | 1558.88 | 1518.99 | 0.502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.03 |  | 707.4352 | -0.0573 | 705.86 | 703.63 | 0.0057 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.8 |  | 70.8559 | -0.0788 | 70.43 | 69.81 | 0.0141 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 212.75 |  | 211.7396 | 0.4772 | 207.4 | 205.01 | 0.0611 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.05 |  | 389.7097 | -0.1693 | 400.89 | 392.26 | 0.0617 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.48 |  | 324.9322 | -0.1392 | 328.865 | 325.74 | 0.074 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 345.01 |  | 347.4129 | -0.6917 | 348.76 | 346.23 | 0.0203 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 561.1 |  | 553.4856 | 1.3757 | 548.755 | 526.6 | 4.8138 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 421.99 |  | 421.1804 | 0.1922 | 419.42 | 414.87 | 0.5308 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.2 |  | 554.4985 | 0.6675 | 551.02 | 540.105 | 0.0609 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.58 |  | 586.7101 | 0.4892 | 581.9 | 572.01 | 0.0492 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.82 |  | 392.3048 | 1.4059 | 387.635 | 380.205 | 0.5053 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 973.875 |  | 968.6108 | 0.5435 | 963.41 | 936.99 | 1.2322 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.18 |  | 211.5848 | 0.2813 | 207.06 | 202.18 | 0.2074 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 443.85 |  | 442.4184 | 0.3236 | 435.98 | 415.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 48.435 |  | 48.8982 | -0.9473 | 48.96 | 47.01 | 0.0206 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.78 |  | 31.1381 | -1.1501 | 30.66 | 28.52 | 0.0325 | below_vwap | below_vwap |
| SPY | market_regime | 747.76 |  | 748.4668 | -0.0944 | 747.68 | 746.425 | 0.0027 | below_vwap | below_vwap |
| IWM | market_regime | 293.7 |  | 294.8333 | -0.3844 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.13 |  | 126.4542 | -0.2564 | 128.79 | 125.83 | 0.1744 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.19 |  | 83.3386 | -0.1784 | 83.22 | 79.6 | 0.5049 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 303.32 |  | 299.895 | 1.1421 | 297.69 | 293.905 | 3.4353 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 407.42 |  | 407.642 | -0.0545 | 409.095 | 398.16 | 0.2209 | below_vwap | below_vwap |
| PWR | data_center_power_cooling | 645.59 |  | 641.8429 | 0.5838 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 994.42 |  | 1003.751 | -0.9296 | 1036.605 | 998.94 | 0.6969 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.3 |  | 473.7812 | -0.1016 | 473.865 | 466.83 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 142.48 |  | 142.8602 | -0.2662 | 143.27 | 141.04 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.39 |  | 174.989 | 0.2291 | 175.265 | 171.06 | 0.1539 | buy_precheck_manual_confirm | none |
| COHR | ai_networking_optical | 314.83 |  | 315.98 | -0.364 | 317.93 | 306.89 | 2.7983 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 833.625 |  | 837.7355 | -0.4907 | 840.47 | 814.62 | 3.324 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 400.28 |  | 404.5844 | -1.0639 | 407.12 | 397.835 | 0.1074 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 111.02 |  | 113.8564 | -2.4912 | 117.185 | 113.68 | 4.828 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 329.9 |  | 330.0391 | -0.0422 | 322.67 | 307.545 | 4.4953 | below_vwap | below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1803.69 |  | 1799.3477 | 0.2413 | 1786.525 | 1767.54 | 0.0577 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 559.65 |  | 558.9702 | 0.1216 | 559.22 | 544.305 | 0.2234 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 319.485 |  | 319.6351 | -0.047 | 317.72 | 311.31 | 0.338 | below_vwap | below_vwap |
| KLAC | semiconductor_equipment | 215.76 |  | 216.1709 | -0.1901 | 215.465 | 210.975 | 0.0371 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 371.31 |  | 371.6631 | -0.095 | 369.53 | 365 | 0.1939 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 296.05 |  | 295.4137 | 0.2154 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.17 |  | 67.4587 | -0.428 | 66.73 | 64.98 | 2.4267 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.36 |  | 55.5749 | -0.3868 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 138.61 |  | 138.9077 | -0.2143 | 140.09 | 135.555 | 0.0866 | below_vwap | below_vwap |
| MKSI | semiconductor_materials | 346.26 |  | 345.604 | 0.1898 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 508.8 |  | 507.5128 | 0.2536 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.89 |  | 297.7083 | -0.2749 | 300.24 | 297.585 | 4.6785 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 30.065 |  | 30.6505 | -1.9102 | 30.78 | 29.46 | 0.0333 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.4 |  | 42.405 | -2.3701 | 42.29 | 40.305 | 0.0242 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.625 |  | 23.969 | -1.4351 | 24.255 | 23.58 | 0.0847 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1617.64 |  | 1583.9975 | 2.1239 | 1558.88 | 1518.99 | 0.502 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 558.85 |  | 556.3579 | 0.4479 | 548.14 | 526.22 | 0.7158 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 911.86 |  | 909.499 | 0.2596 | 899.59 | 860.605 | 0.2149 | buy_precheck_manual_confirm | none |
| AMZN | cloud_ai_capex | 244.48 |  | 244.2359 | 0.0999 | 248.43 | 244.47 | 0.0123 | watch_only | none |
| META | cloud_ai_capex | 626.74 |  | 630.0321 | -0.5225 | 647.02 | 632.77 | 0.1069 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.82 |  | 285.5817 | 0.0834 | 286.39 | 280.275 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 166.34 |  | 166.7208 | -0.2284 | 166.63 | 162.08 | 0.7936 | below_vwap | below_vwap,spread_too_wide |
