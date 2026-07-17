# Intraday State

- Generated at: `2026-07-17T23:14:29+08:00`
- Market time ET: `2026-07-17T11:14:31-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 7, 'watch_only': 4, 'below_opening_15m_low': 3, 'spread_too_wide_or_missing': 29, 'price_stale_or_missing': 1, 'below_vwap': 12}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.7 |  | 693.1756 | 0.0756 | 693.36 | 686.78 | 0.0721 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 513.95 |  | 512.3681 | 0.3087 | 511.83 | 498.665 | 0.1051 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 550.83 |  | 549.7679 | 0.1932 | 550 | 536.9 | 0.0908 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 744.18 |  | 744.389 | -0.0281 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 550.83 |  | 549.7679 | 0.1932 | 550 | 536.9 | 0.0908 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 484.03 |  | 478.23 | 1.2128 | 482.43 | 461.04 | 0.1405 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 513.95 |  | 512.3681 | 0.3087 | 511.83 | 498.665 | 0.1051 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 852.125 |  | 848.41 | 0.4379 | 835.82 | 804.09 | 0.1432 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 693.7 |  | 693.1756 | 0.0756 | 693.36 | 686.78 | 0.0721 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 248.48 |  | 247.6701 | 0.327 | 247.72 | 243.725 | 0.0966 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 67 |  | 66.6389 | 0.5418 | 66.9 | 64.92 | 0.0299 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 550.83 |  | 549.7679 | 0.1932 | 550 | 536.9 | 0.0908 | buy_precheck_manual_confirm | none |
| 2 | QQQ | market_regime | 693.7 |  | 693.1756 | 0.0756 | 693.36 | 686.78 | 0.0721 | buy_precheck_manual_confirm | none |
| 3 | AMZN | cloud_ai_capex | 248.48 |  | 247.6701 | 0.327 | 247.72 | 243.725 | 0.0966 | buy_precheck_manual_confirm | none |
| 4 | SOXX | semiconductor_index | 513.95 |  | 512.3681 | 0.3087 | 511.83 | 498.665 | 0.1051 | buy_precheck_manual_confirm | none |
| 5 | GOOGL | cloud_ai_capex | 346.08 |  | 345.5781 | 0.1452 | 348.47 | 341.42 | 0.2138 | watch_only | none |
| 6 | NVDA | ai_accelerator | 203.18 |  | 202.0959 | 0.5365 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| 7 | MU | memory_hbm_storage | 852.125 |  | 848.41 | 0.4379 | 835.82 | 804.09 | 0.1432 | buy_precheck_manual_confirm | none |
| 8 | AMD | ai_accelerator | 484.03 |  | 478.23 | 1.2128 | 482.43 | 461.04 | 0.1405 | buy_precheck_manual_confirm | none |
| 9 | AAPL | mega_cap_platform | 333.79 |  | 332.1672 | 0.4886 | 334.98 | 331.295 | 0.0569 | watch_only | none |
| 10 | CORZ | high_beta_ai_infrastructure | 20.4 |  | 20.3211 | 0.3881 | 20.445 | 19.92 | 0.049 | watch_only | none |
| 11 | TT | data_center_power_cooling | 470.28 |  | 468.7022 | 0.3366 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | ORCL | cloud_ai_capex | 125.21 |  | 124.8684 | 0.2735 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | TER | semiconductor_test_packaging | 309.62 |  | 309.3915 | 0.0739 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 14 | AVGO | custom_silicon_networking | 369.17 |  | 367.9161 | 0.3408 | 368.42 | 357.97 | 3.0474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | JCI | data_center_power_cooling | 141.1 |  | 140.3614 | 0.5262 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | CIEN | ai_networking_optical | 375.9 |  | 373.1644 | 0.7331 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | SNDK | memory_hbm_storage | 1405.93 |  | 1401.0642 | 0.3473 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | TSM | foundry | 395.72 |  | 394.8027 | 0.2323 | 394.11 | 386.02 | 1.7816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | ASML | semiconductor_equipment | 1739.84 |  | 1736.0928 | 0.2158 | 1741.99 | 1704.935 | 0.6891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | ONTO | semiconductor_test_packaging | 267.92 |  | 266.8174 | 0.4133 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SMH | semiconductor_index | 550.83 |  | 549.7679 | 0.1932 | 550 | 536.9 | 0.0908 | buy_precheck_manual_confirm | none |
| 2 | AMD | ai_accelerator | 484.03 |  | 478.23 | 1.2128 | 482.43 | 461.04 | 0.1405 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 513.95 |  | 512.3681 | 0.3087 | 511.83 | 498.665 | 0.1051 | buy_precheck_manual_confirm | none |
| 4 | MU | memory_hbm_storage | 852.125 |  | 848.41 | 0.4379 | 835.82 | 804.09 | 0.1432 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 693.7 |  | 693.1756 | 0.0756 | 693.36 | 686.78 | 0.0721 | buy_precheck_manual_confirm | none |
| 6 | AMZN | cloud_ai_capex | 248.48 |  | 247.6701 | 0.327 | 247.72 | 243.725 | 0.0966 | buy_precheck_manual_confirm | none |
| 7 | TQQQ | leveraged_tool | 67 |  | 66.6389 | 0.5418 | 66.9 | 64.92 | 0.0299 | buy_precheck_manual_confirm | none |
| 8 | HPE | ai_server_oem | 45.22 |  | 45.2866 | -0.1472 | 44.92 | 43.715 | 0.0221 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 744.18 |  | 744.389 | -0.0281 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| 10 | SKHY | memory_hbm_storage | 154.26 |  | 154.9867 | -0.4689 | 151.99 | 145.6 | 0.9724 | below_vwap | below_vwap,spread_too_wide |
| 11 | ANET | ai_networking_optical | 164.23 |  | 162.868 | 0.8362 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TSM | foundry | 395.72 |  | 394.8027 | 0.2323 | 394.11 | 386.02 | 1.7816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | AVGO | custom_silicon_networking | 369.17 |  | 367.9161 | 0.3408 | 368.42 | 357.97 | 3.0474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TT | data_center_power_cooling | 470.28 |  | 468.7022 | 0.3366 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | VRT | data_center_power_cooling | 286.03 |  | 282.4219 | 1.2775 | 280.565 | 273.17 | 3.3493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | JCI | data_center_power_cooling | 141.1 |  | 140.3614 | 0.5262 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | CIEN | ai_networking_optical | 375.9 |  | 373.1644 | 0.7331 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | ETN | data_center_power_cooling | 396.805 |  | 395.9415 | 0.2181 | 389.4 | 382.38 | 2.7293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 19 | GEV | data_center_power_cooling | 1038.07 |  | 1026.2222 | 1.1545 | 1001.82 | 982.21 | 0.7919 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | DELL | ai_server_oem | 390.77 |  | 386.6171 | 1.0742 | 384 | 368.28 | 1.5098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 693.7 |  | 693.1756 | 0.0756 | 693.36 | 686.78 | 0.0721 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 67 |  | 66.6389 | 0.5418 | 66.9 | 64.92 | 0.0299 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 203.18 |  | 202.0959 | 0.5365 | 203.41 | 197.98 | 0.0148 | watch_only | none |
| MSFT | cloud_ai_capex | 390.495 |  | 393.6151 | -0.7927 | 398.39 | 393.52 | 0.0794 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 333.79 |  | 332.1672 | 0.4886 | 334.98 | 331.295 | 0.0569 | watch_only | none |
| GOOGL | cloud_ai_capex | 346.08 |  | 345.5781 | 0.1452 | 348.47 | 341.42 | 0.2138 | watch_only | none |
| AMD | ai_accelerator | 484.03 |  | 478.23 | 1.2128 | 482.43 | 461.04 | 0.1405 | buy_precheck_manual_confirm | none |
| TSM | foundry | 395.72 |  | 394.8027 | 0.2323 | 394.11 | 386.02 | 1.7816 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 513.95 |  | 512.3681 | 0.3087 | 511.83 | 498.665 | 0.1051 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 550.83 |  | 549.7679 | 0.1932 | 550 | 536.9 | 0.0908 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 369.17 |  | 367.9161 | 0.3408 | 368.42 | 357.97 | 3.0474 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 852.125 |  | 848.41 | 0.4379 | 835.82 | 804.09 | 0.1432 | buy_precheck_manual_confirm | none |
| MRVL | custom_silicon_networking | 183.54 |  | 184.4904 | -0.5152 | 185.03 | 178.09 | 2.1194 | below_vwap | below_vwap,spread_too_wide |
| DELL | ai_server_oem | 390.77 |  | 386.6171 | 1.0742 | 384 | 368.28 | 1.5098 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| HPE | ai_server_oem | 45.22 |  | 45.2866 | -0.1472 | 44.92 | 43.715 | 0.0221 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 23.91 |  | 24.0137 | -0.432 | 24.3 | 23.46 | 0.0418 | below_vwap | below_vwap |
| SPY | market_regime | 744.18 |  | 744.389 | -0.0281 | 742.66 | 740.8 | 0.0054 | below_vwap | below_vwap |
| IWM | market_regime | 293.88 |  | 294.0945 | -0.0729 | 294.205 | 291.675 | 0.0102 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 125.21 |  | 124.8684 | 0.2735 | 125.02 | 121.79 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CRWV | gpu_cloud_ai_factory | 72.615 |  | 71.2565 | 1.9064 | 71.24 | 68.65 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| VRT | data_center_power_cooling | 286.03 |  | 282.4219 | 1.2775 | 280.565 | 273.17 | 3.3493 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 396.805 |  | 395.9415 | 0.2181 | 389.4 | 382.38 | 2.7293 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 626.365 |  | 623.4909 | 0.461 | 616.75 | 609.05 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 1038.07 |  | 1026.2222 | 1.1545 | 1001.82 | 982.21 | 0.7919 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 470.28 |  | 468.7022 | 0.3366 | 469.08 | 460.78 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.1 |  | 140.3614 | 0.5262 | 140.765 | 137.165 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 164.23 |  | 162.868 | 0.8362 | 163.275 | 157.34 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 273.345 |  | 268.6203 | 1.7589 | 269.59 | 256.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LITE | ai_networking_optical | 712.84 |  | 698.4437 | 2.0612 | 694.98 | 653.305 | 3.9967 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 375.9 |  | 373.1644 | 0.7331 | 375.52 | 359.81 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 99.46 |  | 98.0441 | 1.4442 | 97.585 | 91.92 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ALAB | ai_networking_optical | 299.38 |  | 300.2588 | -0.2927 | 305.21 | 289.97 |  | below_vwap | below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1739.84 |  | 1736.0928 | 0.2158 | 1741.99 | 1704.935 | 0.6891 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 531.37 |  | 528.6478 | 0.5149 | 535.095 | 513.34 | 1.0614 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 310.03 |  | 307.2543 | 0.9034 | 306.51 | 298.89 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 208.915 |  | 210.3045 | -0.6607 | 210.82 | 204.71 | 0.1915 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 309.62 |  | 309.3915 | 0.0739 | 308.03 | 297.18 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 267.92 |  | 266.8174 | 0.4133 | 265.71 | 258.355 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 60.79 |  | 60.2102 | 0.963 | 60.51 | 57.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHU | semiconductor_test_packaging | 49.14 |  | 48.5874 | 1.1373 | 49.35 | 46.44 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 134.11 |  | 132.7071 | 1.0571 | 129.93 | 126.945 | 5.0854 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MKSI | semiconductor_materials | 317.69 |  | 314.8344 | 0.907 | 315.89 | 307.13 | 4.3155 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 522.06 |  | 521.8515 | 0.04 | 526.74 | 522.205 |  | below_opening_15m_low | below_opening_15m_low,spread_unavailable |
| APD | industrial_gases | 301.27 |  | 301.5467 | -0.0918 | 304.36 | 299.62 | 4.4744 | below_vwap | below_vwap,spread_too_wide |
| APLD | high_beta_ai_infrastructure | 24.67 |  | 24.815 | -0.5844 | 25.45 | 24.1 | 0.0405 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 33.31 |  | 33.4215 | -0.3336 | 34 | 32.26 | 0.06 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.4 |  | 20.3211 | 0.3881 | 20.445 | 19.92 | 0.049 | watch_only | none |
| SNDK | memory_hbm_storage | 1405.93 |  | 1401.0642 | 0.3473 | 1393.96 | 1325.48 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 456.265 |  | 451.9246 | 0.9604 | 453.35 | 431.78 | 0.8175 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 746.23 |  | 735.0241 | 1.5246 | 724.57 | 702.24 | 4.3257 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.48 |  | 247.6701 | 0.327 | 247.72 | 243.725 | 0.0966 | buy_precheck_manual_confirm | none |
| META | cloud_ai_capex | 627.73 |  | 636.7117 | -1.4106 | 649.07 | 638.97 | 0.3999 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 258.78 |  | 254.7977 | 1.5629 | 252.95 | 243.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 154.26 |  | 154.9867 | -0.4689 | 151.99 | 145.6 | 0.9724 | below_vwap | below_vwap,spread_too_wide |
