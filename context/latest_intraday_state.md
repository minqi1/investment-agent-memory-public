# Intraday State

- Generated at: `2026-07-23T01:29:50+08:00`
- Market time ET: `2026-07-22T13:29:51-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 11, 'below_opening_15m_low': 7, 'below_vwap': 10, 'spread_too_wide_or_missing': 26, 'price_stale_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.03 |  | 707.4565 | 0.2224 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.86 |  | 552.9675 | 1.2465 | 551.02 | 540.105 | 0.0482 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.49 |  | 585.3362 | 1.0513 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.21 |  | 748.5035 | 0.0944 | 747.68 | 746.425 | 0.0133 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.76 |  | 211.156 | 1.2332 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.86 |  | 552.9675 | 1.2465 | 551.02 | 540.105 | 0.0482 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 591.49 |  | 585.3362 | 1.0513 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.03 |  | 707.4565 | 0.2224 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 749.21 |  | 748.5035 | 0.0944 | 747.68 | 746.425 | 0.0133 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1811.28 |  | 1797.5857 | 0.7618 | 1786.525 | 1767.54 | 0.0414 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 560.08 |  | 558.4515 | 0.2916 | 559.22 | 544.305 | 0.1589 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 301.55 |  | 298.98 | 0.8596 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.37 |  | 31.1797 | 0.6102 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| 10 | CRWV | gpu_cloud_ai_factory | 83.68 |  | 83.5251 | 0.1854 | 83.22 | 79.6 | 0.0837 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.31 |  | 70.847 | 0.6535 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.21 |  | 748.5035 | 0.0944 | 747.68 | 746.425 | 0.0133 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 709.03 |  | 707.4565 | 0.2224 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 3 | AMAT | semiconductor_equipment | 560.08 |  | 558.4515 | 0.2916 | 559.22 | 544.305 | 0.1589 | buy_precheck_manual_confirm | none |
| 4 | CRWV | gpu_cloud_ai_factory | 83.68 |  | 83.5251 | 0.1854 | 83.22 | 79.6 | 0.0837 | buy_precheck_manual_confirm | none |
| 5 | ASML | semiconductor_equipment | 1811.28 |  | 1797.5857 | 0.7618 | 1786.525 | 1767.54 | 0.0414 | buy_precheck_manual_confirm | none |
| 6 | SMCI | ai_server_oem | 31.37 |  | 31.1797 | 0.6102 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.55 |  | 298.98 | 0.8596 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| 8 | NVDA | ai_accelerator | 213.76 |  | 211.156 | 1.2332 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 9 | JCI | data_center_power_cooling | 143.04 |  | 142.9019 | 0.0967 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | ETN | data_center_power_cooling | 408.62 |  | 407.9331 | 0.1684 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 296.18 |  | 295.3548 | 0.2794 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | APD | industrial_gases | 297.825 |  | 297.7602 | 0.0218 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | SOXX | semiconductor_index | 559.86 |  | 552.9675 | 1.2465 | 551.02 | 540.105 | 0.0482 | buy_precheck_manual_confirm | none |
| 14 | SMH | semiconductor_index | 591.49 |  | 585.3362 | 1.0513 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| 15 | TT | data_center_power_cooling | 475.745 |  | 473.5906 | 0.4549 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ARM | ai_accelerator | 286.36 |  | 285.6461 | 0.2499 | 286.39 | 280.275 | 2.4654 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | KLAC | semiconductor_equipment | 216.57 |  | 216.0926 | 0.2209 | 215.465 | 210.975 | 4.1788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | LIN | industrial_gases | 509.44 |  | 507.2507 | 0.4316 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | PWR | data_center_power_cooling | 643.75 |  | 640.5126 | 0.5054 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | DELL | ai_server_oem | 443.14 |  | 442.7154 | 0.0959 | 435.98 | 415.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.76 |  | 211.156 | 1.2332 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.86 |  | 552.9675 | 1.2465 | 551.02 | 540.105 | 0.0482 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 591.49 |  | 585.3362 | 1.0513 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.03 |  | 707.4565 | 0.2224 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 749.21 |  | 748.5035 | 0.0944 | 747.68 | 746.425 | 0.0133 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1811.28 |  | 1797.5857 | 0.7618 | 1786.525 | 1767.54 | 0.0414 | buy_precheck_manual_confirm | none |
| 7 | AMAT | semiconductor_equipment | 560.08 |  | 558.4515 | 0.2916 | 559.22 | 544.305 | 0.1589 | buy_precheck_manual_confirm | none |
| 8 | VRT | data_center_power_cooling | 301.55 |  | 298.98 | 0.8596 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| 9 | SMCI | ai_server_oem | 31.37 |  | 31.1797 | 0.6102 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| 10 | CRWV | gpu_cloud_ai_factory | 83.68 |  | 83.5251 | 0.1854 | 83.22 | 79.6 | 0.0837 | buy_precheck_manual_confirm | none |
| 11 | TQQQ | leveraged_tool | 71.31 |  | 70.847 | 0.6535 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 12 | MU | memory_hbm_storage | 981.29 |  | 967.7639 | 1.3977 | 963.41 | 936.99 | 0.5218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 422.705 |  | 420.7316 | 0.469 | 419.42 | 414.87 | 0.9013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 557.34 |  | 551.4892 | 1.0609 | 548.755 | 526.6 | 2.4168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.745 |  | 473.5906 | 0.4549 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1624.27 |  | 1578.1882 | 2.9199 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 562.51 |  | 555.8285 | 1.2021 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | STX | memory_hbm_storage | 918.14 |  | 908.7788 | 1.0301 | 899.59 | 860.605 | 0.5021 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | MRVL | custom_silicon_networking | 213.855 |  | 211.2008 | 1.2567 | 207.06 | 202.18 | 0.4676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TER | semiconductor_test_packaging | 372.85 |  | 371.5622 | 0.3466 | 369.53 | 365 | 4.8572 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.03 |  | 707.4565 | 0.2224 | 705.86 | 703.63 | 0.0071 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.31 |  | 70.847 | 0.6535 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.76 |  | 211.156 | 1.2332 | 207.4 | 205.01 | 0.0094 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.985 |  | 390.2987 | -0.5928 | 400.89 | 392.26 | 0.0335 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.68 |  | 325.151 | -0.4524 | 328.865 | 325.74 | 0.0278 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.95 |  | 347.9585 | -0.0024 | 348.76 | 346.23 | 0.0546 | below_vwap | below_vwap |
| AMD | ai_accelerator | 557.34 |  | 551.4892 | 1.0609 | 548.755 | 526.6 | 2.4168 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.705 |  | 420.7316 | 0.469 | 419.42 | 414.87 | 0.9013 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.86 |  | 552.9675 | 1.2465 | 551.02 | 540.105 | 0.0482 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 591.49 |  | 585.3362 | 1.0513 | 581.9 | 572.01 | 0.0524 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 396.57 |  | 390.0774 | 1.6644 | 387.635 | 380.205 | 0.8447 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 981.29 |  | 967.7639 | 1.3977 | 963.41 | 936.99 | 0.5218 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213.855 |  | 211.2008 | 1.2567 | 207.06 | 202.18 | 0.4676 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 443.14 |  | 442.7154 | 0.0959 | 435.98 | 415.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 48.925 |  | 49.0292 | -0.2125 | 48.96 | 47.01 | 0.0409 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.37 |  | 31.1797 | 0.6102 | 30.66 | 28.52 | 0.0319 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.21 |  | 748.5035 | 0.0944 | 747.68 | 746.425 | 0.0133 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.465 |  | 295.1362 | -0.2274 | 296.39 | 295.22 | 0.0068 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.255 |  | 126.6734 | -0.3303 | 128.79 | 125.83 | 0.5544 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.68 |  | 83.5251 | 0.1854 | 83.22 | 79.6 | 0.0837 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 301.55 |  | 298.98 | 0.8596 | 297.69 | 293.905 | 0.1061 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 408.62 |  | 407.9331 | 0.1684 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.75 |  | 640.5126 | 0.5054 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 994.61 |  | 1007.5156 | -1.2809 | 1036.605 | 998.94 | 3.0796 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.745 |  | 473.5906 | 0.4549 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.04 |  | 142.9019 | 0.0967 | 143.27 | 141.04 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.52 |  | 174.8636 | 0.3754 | 175.265 | 171.06 | 2.6265 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 315.58 |  | 316.1639 | -0.1847 | 317.93 | 306.89 | 2.5794 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 832.27 |  | 840.4484 | -0.9731 | 840.47 | 814.62 | 3.476 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.36 |  | 405.7847 | -0.844 | 407.12 | 397.835 | 4.9508 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.655 |  | 114.4811 | -2.4686 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 333.59 |  | 329.411 | 1.2686 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1811.28 |  | 1797.5857 | 0.7618 | 1786.525 | 1767.54 | 0.0414 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 560.08 |  | 558.4515 | 0.2916 | 559.22 | 544.305 | 0.1589 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 321.09 |  | 319.0229 | 0.6479 | 317.72 | 311.31 | 4.0643 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 216.57 |  | 216.0926 | 0.2209 | 215.465 | 210.975 | 4.1788 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372.85 |  | 371.5622 | 0.3466 | 369.53 | 365 | 4.8572 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ONTO | semiconductor_test_packaging | 296.18 |  | 295.3548 | 0.2794 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.72 |  | 67.4769 | 0.3603 | 66.73 | 64.98 | 1.772 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.85 |  | 55.6969 | 0.2749 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.4 |  | 138.7527 | 0.4665 | 140.09 | 135.555 | 4.5265 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 347.39 |  | 343.9997 | 0.9856 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.44 |  | 507.2507 | 0.4316 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 297.825 |  | 297.7602 | 0.0218 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.38 |  | 30.7696 | -1.2663 | 30.78 | 29.46 | 0.0987 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.23 |  | 42.66 | -1.0081 | 42.29 | 40.305 | 0.0474 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.9 |  | 24.1263 | -0.9379 | 24.255 | 23.58 | 0.1255 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1624.27 |  | 1578.1882 | 2.9199 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 562.51 |  | 555.8285 | 1.2021 | 548.14 | 526.22 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| STX | memory_hbm_storage | 918.14 |  | 908.7788 | 1.0301 | 899.59 | 860.605 | 0.5021 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 243.1 |  | 244.4427 | -0.5493 | 248.43 | 244.47 | 0.0617 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 628.68 |  | 631.1577 | -0.3926 | 647.02 | 632.77 | 0.0652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 286.36 |  | 285.6461 | 0.2499 | 286.39 | 280.275 | 2.4654 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 167.67 |  | 166.7999 | 0.5217 | 166.63 | 162.08 | 2.9582 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
