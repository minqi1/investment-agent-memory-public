# Intraday State

- Generated at: `2026-07-22T01:52:03+08:00`
- Market time ET: `2026-07-21T13:52:04-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 20, 'watch_only': 8, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 1, 'below_vwap': 5, 'below_opening_15m_low': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.99 |  | 706.8079 | 0.4502 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 554.64 |  | 548.8282 | 1.0589 | 550.77 | 545.11 | 0.0451 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.57 |  | 580.7053 | 0.8377 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.85 |  | 746.9931 | 0.2486 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.295 |  | 419.9737 | 1.0289 | 418.76 | 415.025 | 0.1013 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.57 |  | 580.7053 | 0.8377 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.64 |  | 548.8282 | 1.0589 | 550.77 | 545.11 | 0.0451 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.99 |  | 706.8079 | 0.4502 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 544.09 |  | 533.9352 | 1.9019 | 532.365 | 524.72 | 0.2702 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 748.85 |  | 746.9931 | 0.2486 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1812.85 |  | 1810.2537 | 0.1434 | 1804.54 | 1786.51 | 0.0359 | buy_precheck_manual_confirm | none |
| 8 | CIEN | ai_networking_optical | 410.675 |  | 405.5166 | 1.2721 | 401.91 | 397.18 | 0.1169 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 568.26 |  | 564.438 | 0.6771 | 564.91 | 552.71 | 0.1742 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 306.17 |  | 301.5812 | 1.5216 | 305.09 | 299.13 | 0.0915 | buy_precheck_manual_confirm | none |
| 11 | IWM | market_regime | 296.11 |  | 294.5525 | 0.5288 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.75 |  | 46.5299 | 0.4731 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 13 | WDC | memory_hbm_storage | 550.63 |  | 540.048 | 1.9595 | 533.56 | 517.335 | 0.138 | buy_precheck_manual_confirm | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.35 |  | 23.9885 | 1.5071 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 15 | IREN | high_beta_ai_infrastructure | 42.15 |  | 41.8752 | 0.6562 | 41.65 | 40.435 | 0.0474 | buy_precheck_manual_confirm | none |
| 16 | ORCL | cloud_ai_capex | 126.755 |  | 125.5126 | 0.9898 | 126.01 | 122.48 | 0.1815 | buy_precheck_manual_confirm | none |
| 17 | AMKR | semiconductor_test_packaging | 66.85 |  | 66.0667 | 1.1857 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 25.345 |  | 24.8884 | 1.8346 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.69 |  | 30.2738 | 1.3747 | 29.735 | 28.785 | 0.0978 | buy_precheck_manual_confirm | none |
| 20 | TQQQ | leveraged_tool | 71.7 |  | 70.7714 | 1.3122 | 70.84 | 70.09 | 0.0139 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 748.85 |  | 746.9931 | 0.2486 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 2 | ASML | semiconductor_equipment | 1812.85 |  | 1810.2537 | 0.1434 | 1804.54 | 1786.51 | 0.0359 | buy_precheck_manual_confirm | none |
| 3 | HPE | ai_server_oem | 46.75 |  | 46.5299 | 0.4731 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.99 |  | 706.8079 | 0.4502 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | IWM | market_regime | 296.11 |  | 294.5525 | 0.5288 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 6 | GOOGL | cloud_ai_capex | 349.18 |  | 349.1773 | 0.0008 | 350.985 | 347.69 | 0.0401 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 399.35 |  | 399.1623 | 0.047 | 401.45 | 396.36 | 0.02 | watch_only | none |
| 8 | AMAT | semiconductor_equipment | 568.26 |  | 564.438 | 0.6771 | 564.91 | 552.71 | 0.1742 | buy_precheck_manual_confirm | none |
| 9 | TT | data_center_power_cooling | 470.99 |  | 469.805 | 0.2522 | 475.98 | 467.01 | 0.1762 | watch_only | none |
| 10 | IREN | high_beta_ai_infrastructure | 42.15 |  | 41.8752 | 0.6562 | 41.65 | 40.435 | 0.0474 | buy_precheck_manual_confirm | none |
| 11 | NVDA | ai_accelerator | 206.77 |  | 206.0218 | 0.3632 | 208.61 | 206.275 | 0.0097 | watch_only | none |
| 12 | AVGO | custom_silicon_networking | 386.85 |  | 384.8097 | 0.5302 | 390.11 | 382.13 | 0.1112 | watch_only | none |
| 13 | KLAC | semiconductor_equipment | 218.22 |  | 216.7759 | 0.6662 | 220.76 | 214.41 | 0.0183 | watch_only | none |
| 14 | AMZN | cloud_ai_capex | 248.79 |  | 247.7899 | 0.4036 | 248.915 | 247.32 | 0.0121 | watch_only | none |
| 15 | SMH | semiconductor_index | 585.57 |  | 580.7053 | 0.8377 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 16 | SOXX | semiconductor_index | 554.64 |  | 548.8282 | 1.0589 | 550.77 | 545.11 | 0.0451 | buy_precheck_manual_confirm | none |
| 17 | PWR | data_center_power_cooling | 642.45 |  | 638.4534 | 0.626 | 645.815 | 635.91 | 0.2428 | watch_only | none |
| 18 | TSM | foundry | 424.295 |  | 419.9737 | 1.0289 | 418.76 | 415.025 | 0.1013 | buy_precheck_manual_confirm | none |
| 19 | AMKR | semiconductor_test_packaging | 66.85 |  | 66.0667 | 1.1857 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 20 | ORCL | cloud_ai_capex | 126.755 |  | 125.5126 | 0.9898 | 126.01 | 122.48 | 0.1815 | buy_precheck_manual_confirm | none |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | TSM | foundry | 424.295 |  | 419.9737 | 1.0289 | 418.76 | 415.025 | 0.1013 | buy_precheck_manual_confirm | none |
| 2 | SMH | semiconductor_index | 585.57 |  | 580.7053 | 0.8377 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| 3 | SOXX | semiconductor_index | 554.64 |  | 548.8282 | 1.0589 | 550.77 | 545.11 | 0.0451 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 709.99 |  | 706.8079 | 0.4502 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| 5 | AMD | ai_accelerator | 544.09 |  | 533.9352 | 1.9019 | 532.365 | 524.72 | 0.2702 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 748.85 |  | 746.9931 | 0.2486 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| 7 | ASML | semiconductor_equipment | 1812.85 |  | 1810.2537 | 0.1434 | 1804.54 | 1786.51 | 0.0359 | buy_precheck_manual_confirm | none |
| 8 | CIEN | ai_networking_optical | 410.675 |  | 405.5166 | 1.2721 | 401.91 | 397.18 | 0.1169 | buy_precheck_manual_confirm | none |
| 9 | AMAT | semiconductor_equipment | 568.26 |  | 564.438 | 0.6771 | 564.91 | 552.71 | 0.1742 | buy_precheck_manual_confirm | none |
| 10 | VRT | data_center_power_cooling | 306.17 |  | 301.5812 | 1.5216 | 305.09 | 299.13 | 0.0915 | buy_precheck_manual_confirm | none |
| 11 | IWM | market_regime | 296.11 |  | 294.5525 | 0.5288 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| 12 | HPE | ai_server_oem | 46.75 |  | 46.5299 | 0.4731 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| 13 | WDC | memory_hbm_storage | 550.63 |  | 540.048 | 1.9595 | 533.56 | 517.335 | 0.138 | buy_precheck_manual_confirm | none |
| 14 | CORZ | high_beta_ai_infrastructure | 24.35 |  | 23.9885 | 1.5071 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| 15 | IREN | high_beta_ai_infrastructure | 42.15 |  | 41.8752 | 0.6562 | 41.65 | 40.435 | 0.0474 | buy_precheck_manual_confirm | none |
| 16 | ORCL | cloud_ai_capex | 126.755 |  | 125.5126 | 0.9898 | 126.01 | 122.48 | 0.1815 | buy_precheck_manual_confirm | none |
| 17 | AMKR | semiconductor_test_packaging | 66.85 |  | 66.0667 | 1.1857 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| 18 | SMCI | ai_server_oem | 25.345 |  | 24.8884 | 1.8346 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| 19 | APLD | high_beta_ai_infrastructure | 30.69 |  | 30.2738 | 1.3747 | 29.735 | 28.785 | 0.0978 | buy_precheck_manual_confirm | none |
| 20 | TQQQ | leveraged_tool | 71.7 |  | 70.7714 | 1.3122 | 70.84 | 70.09 | 0.0139 | buy_precheck_manual_confirm | none |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 709.99 |  | 706.8079 | 0.4502 | 707.09 | 704.52 | 0.0042 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.7 |  | 70.7714 | 1.3122 | 70.84 | 70.09 | 0.0139 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 206.77 |  | 206.0218 | 0.3632 | 208.61 | 206.275 | 0.0097 | watch_only | none |
| MSFT | cloud_ai_capex | 399.35 |  | 399.1623 | 0.047 | 401.45 | 396.36 | 0.02 | watch_only | none |
| AAPL | mega_cap_platform | 327.34 |  | 326.1944 | 0.3512 | 325.59 | 322.63 | 0.3819 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GOOGL | cloud_ai_capex | 349.18 |  | 349.1773 | 0.0008 | 350.985 | 347.69 | 0.0401 | watch_only | none |
| AMD | ai_accelerator | 544.09 |  | 533.9352 | 1.9019 | 532.365 | 524.72 | 0.2702 | buy_precheck_manual_confirm | none |
| TSM | foundry | 424.295 |  | 419.9737 | 1.0289 | 418.76 | 415.025 | 0.1013 | buy_precheck_manual_confirm | none |
| 000660.KS | memory_hbm_storage | 1836000 |  | 1880296.2757 | -2.3558 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 554.64 |  | 548.8282 | 1.0589 | 550.77 | 545.11 | 0.0451 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 585.57 |  | 580.7053 | 0.8377 | 582.03 | 576.57 | 0.0342 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 386.85 |  | 384.8097 | 0.5302 | 390.11 | 382.13 | 0.1112 | watch_only | none |
| MU | memory_hbm_storage | 975.79 |  | 950.2662 | 2.686 | 944.99 | 923 | 0.7748 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 209.53 |  | 207.6387 | 0.9109 | 208.61 | 205.31 | 1.2075 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| DELL | ai_server_oem | 403 |  | 403.5327 | -0.132 | 405.78 | 397.185 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.75 |  | 46.5299 | 0.4731 | 46.685 | 45.835 | 0.0428 | buy_precheck_manual_confirm | none |
| SMCI | ai_server_oem | 25.345 |  | 24.8884 | 1.8346 | 24.77 | 24.34 | 0.0395 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 748.85 |  | 746.9931 | 0.2486 | 746.6 | 744.3 | 0.0027 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.11 |  | 294.5525 | 0.5288 | 294.51 | 292.72 | 0.0068 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.755 |  | 125.5126 | 0.9898 | 126.01 | 122.48 | 0.1815 | buy_precheck_manual_confirm | none |
| CRWV | gpu_cloud_ai_factory | 80.03 |  | 78.4377 | 2.0301 | 76.615 | 74.55 | 4.1859 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| VRT | data_center_power_cooling | 306.17 |  | 301.5812 | 1.5216 | 305.09 | 299.13 | 0.0915 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 406.22 |  | 406.0782 | 0.0349 | 411.01 | 404.21 | 2.0654 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| PWR | data_center_power_cooling | 642.45 |  | 638.4534 | 0.626 | 645.815 | 635.91 | 0.2428 | watch_only | none |
| GEV | data_center_power_cooling | 1088.705 |  | 1096.4976 | -0.7107 | 1140.63 | 1103.815 | 0.8212 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 470.99 |  | 469.805 | 0.2522 | 475.98 | 467.01 | 0.1762 | watch_only | none |
| JCI | data_center_power_cooling | 142.37 |  | 141.8127 | 0.393 | 142.15 | 140.105 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 175.005 |  | 175.1705 | -0.0945 | 176.06 | 172.32 |  | below_vwap | below_vwap,spread_unavailable |
| COHR | ai_networking_optical | 319.06 |  | 311.9544 | 2.2778 | 309.72 | 302.3 | 1.2035 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LITE | ai_networking_optical | 841.8 |  | 823.9696 | 2.164 | 823.31 | 800.37 | 1.0739 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| CIEN | ai_networking_optical | 410.675 |  | 405.5166 | 1.2721 | 401.91 | 397.18 | 0.1169 | buy_precheck_manual_confirm | none |
| AAOI | ai_networking_optical | 119.86 |  | 116.0788 | 3.2574 | 109.39 | 107.58 | 1.0846 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ALAB | ai_networking_optical | 325.425 |  | 325.9177 | -0.1512 | 329.97 | 323.92 | 0.1444 | below_vwap | below_vwap |
| ASML | semiconductor_equipment | 1812.85 |  | 1810.2537 | 0.1434 | 1804.54 | 1786.51 | 0.0359 | buy_precheck_manual_confirm | none |
| AMAT | semiconductor_equipment | 568.26 |  | 564.438 | 0.6771 | 564.91 | 552.71 | 0.1742 | buy_precheck_manual_confirm | none |
| LRCX | semiconductor_equipment | 322.095 |  | 320.4357 | 0.5178 | 328.135 | 317.17 | 5.0296 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| KLAC | semiconductor_equipment | 218.22 |  | 216.7759 | 0.6662 | 220.76 | 214.41 | 0.0183 | watch_only | none |
| TER | semiconductor_test_packaging | 379.01 |  | 370.0947 | 2.4089 | 365.97 | 356.39 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 301.82 |  | 296.9653 | 1.6348 | 296.68 | 291.36 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 66.85 |  | 66.0667 | 1.1857 | 66.54 | 65 | 0.0898 | buy_precheck_manual_confirm | none |
| COHU | semiconductor_test_packaging | 56.2 |  | 55.0283 | 2.1292 | 54.53 | 54.03 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 142.43 |  | 141.5454 | 0.625 | 142.09 | 139.41 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 345.92 |  | 339.8491 | 1.7864 | 340.205 | 336.3 | 4.1455 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LIN | industrial_gases | 507.09 |  | 506.3682 | 0.1425 | 512.83 | 507.675 | 0.0631 | below_opening_15m_low | below_opening_15m_low |
| APD | industrial_gases | 299.525 |  | 299.2542 | 0.0905 | 301.84 | 296.5 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 30.69 |  | 30.2738 | 1.3747 | 29.735 | 28.785 | 0.0978 | buy_precheck_manual_confirm | none |
| IREN | high_beta_ai_infrastructure | 42.15 |  | 41.8752 | 0.6562 | 41.65 | 40.435 | 0.0474 | buy_precheck_manual_confirm | none |
| CORZ | high_beta_ai_infrastructure | 24.35 |  | 23.9885 | 1.5071 | 23.32 | 22.79 | 0.0411 | buy_precheck_manual_confirm | none |
| SNDK | memory_hbm_storage | 1569.22 |  | 1541.1263 | 1.8229 | 1540.85 | 1490.29 | 2.0634 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| WDC | memory_hbm_storage | 550.63 |  | 540.048 | 1.9595 | 533.56 | 517.335 | 0.138 | buy_precheck_manual_confirm | none |
| STX | memory_hbm_storage | 896.93 |  | 877.0571 | 2.2659 | 866.73 | 845.78 | 2.1418 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 248.79 |  | 247.7899 | 0.4036 | 248.915 | 247.32 | 0.0121 | watch_only | none |
| META | cloud_ai_capex | 647.24 |  | 647.4184 | -0.0276 | 655.425 | 643.54 | 0.3554 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 292.71 |  | 286.3978 | 2.204 | 286.39 | 275.86 | 2.5588 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 171.13 |  | 166.1926 | 2.9709 | 165.88 | 160.77 | 2.2614 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
