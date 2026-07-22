# Intraday State

- Generated at: `2026-07-23T00:46:08+08:00`
- Market time ET: `2026-07-22T12:46:09-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `53`
- stale_count: `3`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 9, 'below_opening_15m_low': 7, 'watch_only': 1, 'spread_too_wide_or_missing': 24, 'price_stale_or_missing': 3, 'below_vwap': 12}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.395 |  | 707.1876 | 0.1707 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 558.05 |  | 552.5048 | 1.0036 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0475 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.73 |  | 748.3971 | 0.1781 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.61 |  | 210.7848 | 1.3403 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.05 |  | 552.5048 | 1.0036 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0475 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.395 |  | 707.1876 | 0.1707 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 749.73 |  | 748.3971 | 0.1781 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1800.65 |  | 1796.0919 | 0.2538 | 1786.525 | 1767.54 | 0.0572 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 31.66 |  | 31.1594 | 1.6064 | 30.66 | 28.52 | 0.0632 | buy_precheck_manual_confirm | none |
| 8 | CRWV | gpu_cloud_ai_factory | 83.615 |  | 83.5124 | 0.1229 | 83.22 | 79.6 | 0.0957 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.18 |  | 70.818 | 0.5112 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 749.73 |  | 748.3971 | 0.1781 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 708.395 |  | 707.1876 | 0.1707 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 3 | ASML | semiconductor_equipment | 1800.65 |  | 1796.0919 | 0.2538 | 1786.525 | 1767.54 | 0.0572 | buy_precheck_manual_confirm | none |
| 4 | CRWV | gpu_cloud_ai_factory | 83.615 |  | 83.5124 | 0.1229 | 83.22 | 79.6 | 0.0957 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 348.03 |  | 347.9382 | 0.0264 | 348.76 | 346.23 | 0.2643 | watch_only | none |
| 6 | SOXX | semiconductor_index | 558.05 |  | 552.5048 | 1.0036 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| 7 | SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0475 | buy_precheck_manual_confirm | none |
| 8 | TER | semiconductor_test_packaging | 372.24 |  | 371.4214 | 0.2204 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.61 |  | 210.7848 | 1.3403 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 10 | LRCX | semiconductor_equipment | 319.73 |  | 318.7679 | 0.3018 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | ONTO | semiconductor_test_packaging | 295.96 |  | 295.2598 | 0.2371 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | APD | industrial_gases | 297.81 |  | 297.7596 | 0.0169 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TT | data_center_power_cooling | 475.2 |  | 472.8991 | 0.4866 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | ANET | ai_networking_optical | 175.675 |  | 174.8092 | 0.4953 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ETN | data_center_power_cooling | 409.21 |  | 407.7553 | 0.3567 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | ARM | ai_accelerator | 285.645 |  | 285.6197 | 0.0088 | 286.39 | 280.275 | 2.8672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | PWR | data_center_power_cooling | 643.92 |  | 640.1188 | 0.5938 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | MKSI | semiconductor_materials | 345.37 |  | 343.5443 | 0.5314 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AMKR | semiconductor_test_packaging | 67.59 |  | 67.461 | 0.1912 | 66.73 | 64.98 | 4.3498 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | TSM | foundry | 422.06 |  | 420.5493 | 0.3592 | 419.42 | 414.87 | 0.5923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.61 |  | 210.7848 | 1.3403 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 558.05 |  | 552.5048 | 1.0036 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0475 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 708.395 |  | 707.1876 | 0.1707 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| 5 | SPY | market_regime | 749.73 |  | 748.3971 | 0.1781 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| 6 | ASML | semiconductor_equipment | 1800.65 |  | 1796.0919 | 0.2538 | 1786.525 | 1767.54 | 0.0572 | buy_precheck_manual_confirm | none |
| 7 | SMCI | ai_server_oem | 31.66 |  | 31.1594 | 1.6064 | 30.66 | 28.52 | 0.0632 | buy_precheck_manual_confirm | none |
| 8 | CRWV | gpu_cloud_ai_factory | 83.615 |  | 83.5124 | 0.1229 | 83.22 | 79.6 | 0.0957 | buy_precheck_manual_confirm | none |
| 9 | TQQQ | leveraged_tool | 71.18 |  | 70.818 | 0.5112 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| 10 | MU | memory_hbm_storage | 971.87 |  | 966.6809 | 0.5368 | 963.41 | 936.99 | 0.8232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | TSM | foundry | 422.06 |  | 420.5493 | 0.3592 | 419.42 | 414.87 | 0.5923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | AMD | ai_accelerator | 554.59 |  | 550.9875 | 0.6538 | 548.755 | 526.6 | 1.933 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TT | data_center_power_cooling | 475.2 |  | 472.8991 | 0.4866 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | SNDK | memory_hbm_storage | 1600.575 |  | 1574.2588 | 1.6717 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | WDC | memory_hbm_storage | 559.67 |  | 555.2964 | 0.7876 | 548.14 | 526.22 | 5.078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | STX | memory_hbm_storage | 914.87 |  | 907.8063 | 0.7781 | 899.59 | 860.605 | 0.6526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | MRVL | custom_silicon_networking | 212.8 |  | 210.9865 | 0.8595 | 207.06 | 202.18 | 0.4182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | TER | semiconductor_test_packaging | 372.24 |  | 371.4214 | 0.2204 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | AVGO | custom_silicon_networking | 394.87 |  | 389.2979 | 1.4313 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | SKHY | memory_hbm_storage | 167.56 |  | 166.6896 | 0.5222 | 166.63 | 162.08 | 0.8355 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.395 |  | 707.1876 | 0.1707 | 705.86 | 703.63 | 0.0099 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.18 |  | 70.818 | 0.5112 | 70.43 | 69.81 | 0.014 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.61 |  | 210.7848 | 1.3403 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 388.75 |  | 390.5287 | -0.4555 | 400.89 | 392.26 | 0.0257 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 324.495 |  | 325.3541 | -0.2641 | 328.865 | 325.74 | 0.0185 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 348.03 |  | 347.9382 | 0.0264 | 348.76 | 346.23 | 0.2643 | watch_only | none |
| AMD | ai_accelerator | 554.59 |  | 550.9875 | 0.6538 | 548.755 | 526.6 | 1.933 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.06 |  | 420.5493 | 0.3592 | 419.42 | 414.87 | 0.5923 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1909131.8389 | -4.1449 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 558.05 |  | 552.5048 | 1.0036 | 551.02 | 540.105 | 0.0699 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 589.955 |  | 584.7878 | 0.8836 | 581.9 | 572.01 | 0.0475 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 394.87 |  | 389.2979 | 1.4313 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 971.87 |  | 966.6809 | 0.5368 | 963.41 | 936.99 | 0.8232 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 212.8 |  | 210.9865 | 0.8595 | 207.06 | 202.18 | 0.4182 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 445.04 |  | 442.6726 | 0.5348 | 435.98 | 415.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| HPE | ai_server_oem | 48.84 |  | 49.0418 | -0.4114 | 48.96 | 47.01 | 0.0614 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.66 |  | 31.1594 | 1.6064 | 30.66 | 28.52 | 0.0632 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.73 |  | 748.3971 | 0.1781 | 747.68 | 746.425 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.645 |  | 295.2284 | -0.1976 | 296.39 | 295.22 | 0.0034 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 125.92 |  | 126.7154 | -0.6277 | 128.79 | 125.83 | 0.0635 | below_vwap | below_vwap |
| CRWV | gpu_cloud_ai_factory | 83.615 |  | 83.5124 | 0.1229 | 83.22 | 79.6 | 0.0957 | buy_precheck_manual_confirm | none |
| VRT | data_center_power_cooling | 300.09 |  | 298.7618 | 0.4446 | 297.69 | 293.905 | 0.9897 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 409.21 |  | 407.7553 | 0.3567 | 409.095 | 398.16 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 643.92 |  | 640.1188 | 0.5938 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 994.51 |  | 1008.7224 | -1.409 | 1036.605 | 998.94 | 1.3474 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.2 |  | 472.8991 | 0.4866 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.295 |  | 142.8712 | 0.2966 | 143.27 | 141.04 | 4.8711 | price_stale_or_missing | price_stale_or_missing,spread_too_wide,stale_or_missing |
| ANET | ai_networking_optical | 175.675 |  | 174.8092 | 0.4953 | 175.265 | 171.06 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 315.44 |  | 316.3045 | -0.2733 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 834.66 |  | 841.2167 | -0.7794 | 840.47 | 814.62 |  | below_vwap | below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 403.02 |  | 406.1563 | -0.7722 | 407.12 | 397.835 | 2.3076 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 112.48 |  | 114.7527 | -1.9805 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.55 |  | 328.5482 | 1.218 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1800.65 |  | 1796.0919 | 0.2538 | 1786.525 | 1767.54 | 0.0572 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 557.92 |  | 558.3698 | -0.0806 | 559.22 | 544.305 | 4.9219 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.73 |  | 318.7679 | 0.3018 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 215.42 |  | 216.0805 | -0.3057 | 215.465 | 210.975 | 4.7906 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 372.24 |  | 371.4214 | 0.2204 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.96 |  | 295.2598 | 0.2371 | 298.42 | 288.335 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 67.59 |  | 67.461 | 0.1912 | 66.73 | 64.98 | 4.3498 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHU | semiconductor_test_packaging | 55.93 |  | 55.6774 | 0.4538 | 56.2 | 54.45 |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 138.33 |  | 138.7451 | -0.2992 | 140.09 | 135.555 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 345.37 |  | 343.5443 | 0.5314 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.38 |  | 507.1196 | 0.4457 | 507.545 | 505.59 | 4.4427 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APD | industrial_gases | 297.81 |  | 297.7596 | 0.0169 | 300.24 | 297.585 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.44 |  | 30.8283 | -1.2597 | 30.78 | 29.46 | 0.0657 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 42.15 |  | 42.7406 | -1.3819 | 42.29 | 40.305 | 0.0237 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.86 |  | 24.1415 | -1.1662 | 24.255 | 23.58 | 0.0838 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1600.575 |  | 1574.2588 | 1.6717 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 559.67 |  | 555.2964 | 0.7876 | 548.14 | 526.22 | 5.078 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 914.87 |  | 907.8063 | 0.7781 | 899.59 | 860.605 | 0.6526 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 244.105 |  | 244.5344 | -0.1756 | 248.43 | 244.47 | 0.4424 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| META | cloud_ai_capex | 628.98 |  | 631.3862 | -0.3811 | 647.02 | 632.77 | 0.9539 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 285.645 |  | 285.6197 | 0.0088 | 286.39 | 280.275 | 2.8672 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 167.56 |  | 166.6896 | 0.5222 | 166.63 | 162.08 | 0.8355 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
