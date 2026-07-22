# Intraday State

- Generated at: `2026-07-23T03:57:43+08:00`
- Market time ET: `2026-07-22T15:57:44-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 31, 'manual_confirm_candidate': 5, 'below_opening_15m_low': 9, 'watch_only': 3, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 7}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.6 |  | 707.2993 | -0.2403 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 555.205 |  | 554.8982 | 0.0553 | 551.02 | 540.105 | 0.036 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 586.57 |  | 586.8492 | -0.0476 | 581.9 | 572.01 | 0.0239 | below_vwap | below_vwap |
| SPY | market_regime | 747.76 |  | 748.3664 | -0.081 | 747.68 | 746.425 | 0.0254 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 211.91 |  | 211.8035 | 0.0503 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.66 |  | 421.2973 | 0.0861 | 419.42 | 414.87 | 0.0356 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 555.205 |  | 554.8982 | 0.0553 | 551.02 | 540.105 | 0.036 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1801.75 |  | 1800.0406 | 0.095 | 1786.525 | 1767.54 | 0.0244 | buy_precheck_manual_confirm | none |
| 5 | VRT | data_center_power_cooling | 301.89 |  | 300.2015 | 0.5624 | 297.69 | 293.905 | 0.0861 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 421.66 |  | 421.2973 | 0.0861 | 419.42 | 414.87 | 0.0356 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 555.205 |  | 554.8982 | 0.0553 | 551.02 | 540.105 | 0.036 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1801.75 |  | 1800.0406 | 0.095 | 1786.525 | 1767.54 | 0.0244 | buy_precheck_manual_confirm | none |
| 4 | NVDA | ai_accelerator | 211.91 |  | 211.8035 | 0.0503 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 5 | AMZN | cloud_ai_capex | 244.96 |  | 244.3009 | 0.2698 | 248.43 | 244.47 | 0.0122 | watch_only | none |
| 6 | VRT | data_center_power_cooling | 301.89 |  | 300.2015 | 0.5624 | 297.69 | 293.905 | 0.0861 | buy_precheck_manual_confirm | none |
| 7 | ANET | ai_networking_optical | 175.1 |  | 175.0443 | 0.0318 | 175.265 | 171.06 | 0.2684 | watch_only | none |
| 8 | AAPL | mega_cap_platform | 326.14 |  | 324.9966 | 0.3518 | 328.865 | 325.74 | 0.0123 | watch_only | none |
| 9 | TT | data_center_power_cooling | 474.425 |  | 473.9141 | 0.1078 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | PWR | data_center_power_cooling | 642.87 |  | 642.375 | 0.0771 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | LIN | industrial_gases | 509.28 |  | 507.7398 | 0.3033 | 507.545 | 505.59 | 4.5339 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | SNDK | memory_hbm_storage | 1590.55 |  | 1585.7123 | 0.3051 | 1558.88 | 1518.99 | 4.7072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | ALAB | ai_networking_optical | 330.36 |  | 330.0469 | 0.0949 | 322.67 | 307.545 | 4.7373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | DELL | ai_server_oem | 443.82 |  | 442.6487 | 0.2646 | 435.98 | 415.79 | 3.9813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | MSFT | cloud_ai_capex | 389.91 |  | 389.6377 | 0.0699 | 400.89 | 392.26 | 0.2488 | below_opening_15m_low | below_opening_15m_low |
| 16 | SPY | market_regime | 747.76 |  | 748.3664 | -0.081 | 747.68 | 746.425 | 0.0254 | below_vwap | below_vwap |
| 17 | QQQ | market_regime | 705.6 |  | 707.2993 | -0.2403 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| 18 | KLAC | semiconductor_equipment | 214.185 |  | 215.9765 | -0.8295 | 215.465 | 210.975 | 0.0374 | below_vwap | below_vwap |
| 19 | AMAT | semiconductor_equipment | 553.21 |  | 558.5826 | -0.9618 | 559.22 | 544.305 | 0.1301 | below_vwap | below_vwap |
| 20 | JCI | data_center_power_cooling | 142.67 |  | 142.7941 | -0.0869 | 143.27 | 141.04 | 0.028 | below_vwap | below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 211.91 |  | 211.8035 | 0.0503 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | TSM | foundry | 421.66 |  | 421.2973 | 0.0861 | 419.42 | 414.87 | 0.0356 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 555.205 |  | 554.8982 | 0.0553 | 551.02 | 540.105 | 0.036 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1801.75 |  | 1800.0406 | 0.095 | 1786.525 | 1767.54 | 0.0244 | buy_precheck_manual_confirm | none |
| 5 | VRT | data_center_power_cooling | 301.89 |  | 300.2015 | 0.5624 | 297.69 | 293.905 | 0.0861 | buy_precheck_manual_confirm | none |
| 6 | AMD | ai_accelerator | 551.7 |  | 553.5575 | -0.3356 | 548.755 | 526.6 | 0.377 | below_vwap | below_vwap,spread_too_wide |
| 7 | WDC | memory_hbm_storage | 556.16 |  | 556.6841 | -0.0941 | 548.14 | 526.22 |  | below_vwap | below_vwap,spread_unavailable |
| 8 | STX | memory_hbm_storage | 907.77 |  | 909.6887 | -0.2109 | 899.59 | 860.605 | 0.8945 | below_vwap | below_vwap,spread_too_wide |
| 9 | SMH | semiconductor_index | 586.57 |  | 586.8492 | -0.0476 | 581.9 | 572.01 | 0.0239 | below_vwap | below_vwap |
| 10 | MRVL | custom_silicon_networking | 210.81 |  | 211.58 | -0.3639 | 207.06 | 202.18 | 1.7267 | below_vwap | below_vwap,spread_too_wide |
| 11 | SPY | market_regime | 747.76 |  | 748.3664 | -0.081 | 747.68 | 746.425 | 0.0254 | below_vwap | below_vwap |
| 12 | LRCX | semiconductor_equipment | 318.99 |  | 319.631 | -0.2005 | 317.72 | 311.31 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AMKR | semiconductor_test_packaging | 66.825 |  | 67.4058 | -0.8616 | 66.73 | 64.98 | 2.9181 | below_vwap | below_vwap,spread_too_wide |
| 14 | TT | data_center_power_cooling | 474.425 |  | 473.9141 | 0.1078 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | SNDK | memory_hbm_storage | 1590.55 |  | 1585.7123 | 0.3051 | 1558.88 | 1518.99 | 4.7072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | AVGO | custom_silicon_networking | 396.9 |  | 393.2189 | 0.9361 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | LIN | industrial_gases | 509.28 |  | 507.7398 | 0.3033 | 507.545 | 505.59 | 4.5339 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | ALAB | ai_networking_optical | 330.36 |  | 330.0469 | 0.0949 | 322.67 | 307.545 | 4.7373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | PWR | data_center_power_cooling | 642.87 |  | 642.375 | 0.0771 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | DELL | ai_server_oem | 443.82 |  | 442.6487 | 0.2646 | 435.98 | 415.79 | 3.9813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 705.6 |  | 707.2993 | -0.2403 | 705.86 | 703.63 | 0.0085 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 70.36 |  | 70.8289 | -0.662 | 70.43 | 69.81 | 0.0142 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 211.91 |  | 211.8035 | 0.0503 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 389.91 |  | 389.6377 | 0.0699 | 400.89 | 392.26 | 0.2488 | below_opening_15m_low | below_opening_15m_low |
| AAPL | mega_cap_platform | 326.14 |  | 324.9966 | 0.3518 | 328.865 | 325.74 | 0.0123 | watch_only | none |
| GOOGL | cloud_ai_capex | 342.81 |  | 346.7336 | -1.1316 | 348.76 | 346.23 | 0.0292 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 551.7 |  | 553.5575 | -0.3356 | 548.755 | 526.6 | 0.377 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 421.66 |  | 421.2973 | 0.0861 | 419.42 | 414.87 | 0.0356 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 555.205 |  | 554.8982 | 0.0553 | 551.02 | 540.105 | 0.036 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 586.57 |  | 586.8492 | -0.0476 | 581.9 | 572.01 | 0.0239 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 396.9 |  | 393.2189 | 0.9361 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 959.57 |  | 968.867 | -0.9596 | 963.41 | 936.99 | 1.211 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 210.81 |  | 211.58 | -0.3639 | 207.06 | 202.18 | 1.7267 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 443.82 |  | 442.6487 | 0.2646 | 435.98 | 415.79 | 3.9813 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 48.33 |  | 48.861 | -1.0868 | 48.96 | 47.01 | 0.0207 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 30.545 |  | 31.1081 | -1.8101 | 30.66 | 28.52 | 0.0327 | below_vwap | below_vwap |
| SPY | market_regime | 747.76 |  | 748.3664 | -0.081 | 747.68 | 746.425 | 0.0254 | below_vwap | below_vwap |
| IWM | market_regime | 293.8 |  | 294.6803 | -0.2987 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.815 |  | 126.4128 | -0.4729 | 128.79 | 125.83 | 2.2652 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 82.86 |  | 83.312 | -0.5426 | 83.22 | 79.6 | 0.2172 | below_vwap | below_vwap |
| VRT | data_center_power_cooling | 301.89 |  | 300.2015 | 0.5624 | 297.69 | 293.905 | 0.0861 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.835 |  | 407.6267 | -0.1942 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 642.87 |  | 642.375 | 0.0771 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 991.24 |  | 1002.6457 | -1.1376 | 1036.605 | 998.94 | 0.3672 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.425 |  | 473.9141 | 0.1078 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 142.67 |  | 142.7941 | -0.0869 | 143.27 | 141.04 | 0.028 | below_vwap | below_vwap |
| ANET | ai_networking_optical | 175.1 |  | 175.0443 | 0.0318 | 175.265 | 171.06 | 0.2684 | watch_only | none |
| COHR | ai_networking_optical | 312.765 |  | 315.6056 | -0.9001 | 317.93 | 306.89 | 3.485 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 828.55 |  | 834.619 | -0.7272 | 840.47 | 814.62 | 1.6185 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 398.51 |  | 403.834 | -1.3184 | 407.12 | 397.835 | 0.123 | below_vwap | below_vwap |
| AAOI | ai_networking_optical | 110.55 |  | 113.6244 | -2.7058 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.36 |  | 330.0469 | 0.0949 | 322.67 | 307.545 | 4.7373 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1801.75 |  | 1800.0406 | 0.095 | 1786.525 | 1767.54 | 0.0244 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 553.21 |  | 558.5826 | -0.9618 | 559.22 | 544.305 | 0.1301 | below_vwap | below_vwap |
| LRCX | semiconductor_equipment | 318.99 |  | 319.631 | -0.2005 | 317.72 | 311.31 |  | below_vwap | below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 214.185 |  | 215.9765 | -0.8295 | 215.465 | 210.975 | 0.0374 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 369.445 |  | 371.4467 | -0.5389 | 369.53 | 365 |  | below_vwap | below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 294.505 |  | 295.389 | -0.2993 | 298.42 | 288.335 | 4.9507 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 66.825 |  | 67.4058 | -0.8616 | 66.73 | 64.98 | 2.9181 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 54.98 |  | 55.4248 | -0.8026 | 56.2 | 54.45 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 137.53 |  | 138.682 | -0.8307 | 140.09 | 135.555 | 4.8789 | below_vwap | below_vwap,spread_too_wide |
| MKSI | semiconductor_materials | 345.01 |  | 345.5764 | -0.1639 | 345.675 | 331.945 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 509.28 |  | 507.7398 | 0.3033 | 507.545 | 505.59 | 4.5339 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.05 |  | 297.5526 | -0.1689 | 300.24 | 297.585 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.17 |  | 30.6133 | -1.4481 | 30.78 | 29.46 | 0.0994 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.115 |  | 42.3168 | -2.8401 | 42.29 | 40.305 | 0.0486 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.545 |  | 23.927 | -1.5966 | 24.255 | 23.58 | 0.0425 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1590.55 |  | 1585.7123 | 0.3051 | 1558.88 | 1518.99 | 4.7072 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 556.16 |  | 556.6841 | -0.0941 | 548.14 | 526.22 |  | below_vwap | below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 907.77 |  | 909.6887 | -0.2109 | 899.59 | 860.605 | 0.8945 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 244.96 |  | 244.3009 | 0.2698 | 248.43 | 244.47 | 0.0122 | watch_only | none |
| META | cloud_ai_capex | 628.64 |  | 629.5111 | -0.1384 | 647.02 | 632.77 | 2.1777 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 283.74 |  | 285.4952 | -0.6148 | 286.39 | 280.275 |  | below_vwap | below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 165.27 |  | 166.7108 | -0.8643 | 166.63 | 162.08 | 1.2767 | below_vwap | below_vwap,spread_too_wide |
