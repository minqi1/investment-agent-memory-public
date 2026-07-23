# Intraday State

- Generated at: `2026-07-24T03:22:05+08:00`
- Market time ET: `2026-07-23T15:22:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 22, 'watch_only': 4, 'below_vwap': 24, 'price_stale_or_missing': 2, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.21 |  | 692.7776 | -0.3706 | 698.65 | 693.24 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 545.96 |  | 550.6417 | -0.8502 | 557.38 | 545.965 | 0.0604 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.74 |  | 580.4089 | -0.6321 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| SPY | market_regime | 737.275 |  | 738.4574 | -0.1601 | 742.515 | 738.54 | 0.0393 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  | | | | | | | | | | |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | KLAC | semiconductor_equipment | 216.19 |  | 215.5175 | 0.312 | 217.88 | 212.99 | 0.0278 | watch_only | none |
| 2 | AAPL | mega_cap_platform | 321.03 |  | 320.9397 | 0.0281 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| 3 | TT | data_center_power_cooling | 478.24 |  | 476.8943 | 0.2822 | 480 | 472.33 | 0.3157 | watch_only | none |
| 4 | META | cloud_ai_capex | 606.88 |  | 604.6687 | 0.3657 | 614.15 | 605.39 | 0.0511 | watch_only | none |
| 5 | ETN | data_center_power_cooling | 413.545 |  | 413.3438 | 0.0487 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | ARM | ai_accelerator | 279.77 |  | 279.5583 | 0.0757 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | APD | industrial_gases | 295.88 |  | 295.6915 | 0.0638 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | SMH | semiconductor_index | 576.74 |  | 580.4089 | -0.6321 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| 9 | ASML | semiconductor_equipment | 1794.42 |  | 1801.5341 | -0.3949 | 1806.11 | 1780.9 | 0.0373 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 291.48 |  | 291.6082 | -0.044 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 11 | TER | semiconductor_test_packaging | 369 |  | 371.8343 | -0.7622 | 376.78 | 363.37 | 0.1328 | below_vwap | below_vwap |
| 12 | SMCI | ai_server_oem | 31 |  | 31.5731 | -1.8151 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| 13 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 14 | JCI | data_center_power_cooling | 143.35 |  | 143.8012 | -0.3138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | PWR | data_center_power_cooling | 645.66 |  | 651.4416 | -0.8875 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 54.22 |  | 54.4717 | -0.462 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | TSM | foundry | 415.39 |  | 416.3104 | -0.2211 | 420.72 | 412.69 | 0.6524 | below_vwap | below_vwap,spread_too_wide |
| 18 | MU | memory_hbm_storage | 982.65 |  | 990.944 | -0.837 | 999.04 | 964.86 | 1.4827 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMAT | semiconductor_equipment | 557.36 |  | 563.9424 | -1.1672 | 566.18 | 548.47 | 4.1302 | below_vwap | below_vwap,spread_too_wide |
| 20 | ANET | ai_networking_optical | 175.405 |  | 176.6188 | -0.6873 | 177.84 | 173.19 | 3.1356 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GEV | data_center_power_cooling | 1033.71 |  | 1016.8519 | 1.6579 | 1023.33 | 979.08 | 0.6404 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 2 | TT | data_center_power_cooling | 478.24 |  | 476.8943 | 0.2822 | 480 | 472.33 | 0.3157 | watch_only | none |
| 3 | KLAC | semiconductor_equipment | 216.19 |  | 215.5175 | 0.312 | 217.88 | 212.99 | 0.0278 | watch_only | none |
| 4 | META | cloud_ai_capex | 606.88 |  | 604.6687 | 0.3657 | 614.15 | 605.39 | 0.0511 | watch_only | none |
| 5 | AAPL | mega_cap_platform | 321.03 |  | 320.9397 | 0.0281 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| 6 | TSM | foundry | 415.39 |  | 416.3104 | -0.2211 | 420.72 | 412.69 | 0.6524 | below_vwap | below_vwap,spread_too_wide |
| 7 | SMH | semiconductor_index | 576.74 |  | 580.4089 | -0.6321 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| 8 | MU | memory_hbm_storage | 982.65 |  | 990.944 | -0.837 | 999.04 | 964.86 | 1.4827 | below_vwap | below_vwap,spread_too_wide |
| 9 | ASML | semiconductor_equipment | 1794.42 |  | 1801.5341 | -0.3949 | 1806.11 | 1780.9 | 0.0373 | below_vwap | below_vwap |
| 10 | AMAT | semiconductor_equipment | 557.36 |  | 563.9424 | -1.1672 | 566.18 | 548.47 | 4.1302 | below_vwap | below_vwap,spread_too_wide |
| 11 | ANET | ai_networking_optical | 175.405 |  | 176.6188 | -0.6873 | 177.84 | 173.19 | 3.1356 | below_vwap | below_vwap,spread_too_wide |
| 12 | JCI | data_center_power_cooling | 143.35 |  | 143.8012 | -0.3138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | PWR | data_center_power_cooling | 645.66 |  | 651.4416 | -0.8875 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | IWM | market_regime | 291.48 |  | 291.6082 | -0.044 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| 15 | LRCX | semiconductor_equipment | 318.005 |  | 320.1616 | -0.6736 | 322.4 | 317.27 | 4.5785 | below_vwap | below_vwap,spread_too_wide |
| 16 | WDC | memory_hbm_storage | 557.195 |  | 563.9644 | -1.2003 | 576.24 | 556.3 | 2.3654 | below_vwap | below_vwap,spread_too_wide |
| 17 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 18 | LIN | industrial_gases | 505.74 |  | 507.1743 | -0.2828 | 510.71 | 502.72 | 4.9096 | below_vwap | below_vwap,spread_too_wide |
| 19 | COHR | ai_networking_optical | 311.65 |  | 317.1226 | -1.7257 | 320.13 | 307.04 | 4.5981 | below_vwap | below_vwap,spread_too_wide |
| 20 | CIEN | ai_networking_optical | 403.87 |  | 407.8043 | -0.9647 | 408.58 | 397.9 | 5.1081 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 690.21 |  | 692.7776 | -0.3706 | 698.65 | 693.24 | 0.0043 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 65.76 |  | 66.4913 | -1.0999 | 68.245 | 66.7 | 0.0152 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.795 |  | 208.5057 | -0.3408 | 210.85 | 208.49 | 0.0144 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 380.91 |  | 382.4326 | -0.3981 | 391.71 | 387.245 | 0.3255 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 321.03 |  | 320.9397 | 0.0281 | 323.25 | 320.82 | 0.0125 | watch_only | none |
| GOOGL | cloud_ai_capex | 318.085 |  | 319.5007 | -0.4431 | 324.42 | 320.24 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 535.95 |  | 539.8898 | -0.7297 | 556.12 | 542.33 | 0.2761 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 415.39 |  | 416.3104 | -0.2211 | 420.72 | 412.69 | 0.6524 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1919000 |  | 1862907.8116 | 3.011 |  |  |  | price_stale_or_missing | price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 545.96 |  | 550.6417 | -0.8502 | 557.38 | 545.965 | 0.0604 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 576.74 |  | 580.4089 | -0.6321 | 585.98 | 576.635 | 0.0451 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 390.22 |  | 391.9496 | -0.4413 | 397.34 | 390.54 | 1.4402 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 982.65 |  | 990.944 | -0.837 | 999.04 | 964.86 | 1.4827 | below_vwap | below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 206.465 |  | 209.2415 | -1.3269 | 213.785 | 207.665 | 0.1986 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 435.09 |  | 443.2241 | -1.8352 | 450.07 | 438.55 | 0.3792 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 47.52 |  | 48.2333 | -1.4788 | 48.88 | 47.635 | 0.0631 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 31 |  | 31.5731 | -1.8151 | 31.52 | 30.23 | 0.0323 | below_vwap | below_vwap |
| SPY | market_regime | 737.275 |  | 738.4574 | -0.1601 | 742.515 | 738.54 | 0.0393 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 291.48 |  | 291.6082 | -0.044 | 293.01 | 290.365 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 119.96 |  | 121.6551 | -1.3933 | 124.22 | 122.07 | 0.1667 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 80.87 |  | 82.5228 | -2.0029 | 84.415 | 80.64 | 0.8903 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 302.25 |  | 305.7844 | -1.1558 | 311.13 | 303.96 | 1.4888 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 413.545 |  | 413.3438 | 0.0487 | 415.53 | 406.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| PWR | data_center_power_cooling | 645.66 |  | 651.4416 | -0.8875 | 656.38 | 642.37 |  | below_vwap | below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1033.71 |  | 1016.8519 | 1.6579 | 1023.33 | 979.08 | 0.6404 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 478.24 |  | 476.8943 | 0.2822 | 480 | 472.33 | 0.3157 | watch_only | none |
| JCI | data_center_power_cooling | 143.35 |  | 143.8012 | -0.3138 | 145.035 | 141.815 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 175.405 |  | 176.6188 | -0.6873 | 177.84 | 173.19 | 3.1356 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 311.65 |  | 317.1226 | -1.7257 | 320.13 | 307.04 | 4.5981 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 829.465 |  | 854.6059 | -2.9418 | 880.26 | 833 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 403.87 |  | 407.8043 | -0.9647 | 408.58 | 397.9 | 5.1081 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 111.39 |  | 114.3646 | -2.601 | 118.01 | 108.505 | 4.9197 | below_vwap | below_vwap,spread_too_wide |
| ALAB | ai_networking_optical | 320.81 |  | 326.4571 | -1.7298 | 341.68 | 327.43 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1794.42 |  | 1801.5341 | -0.3949 | 1806.11 | 1780.9 | 0.0373 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 557.36 |  | 563.9424 | -1.1672 | 566.18 | 548.47 | 4.1302 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 318.005 |  | 320.1616 | -0.6736 | 322.4 | 317.27 | 4.5785 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 216.19 |  | 215.5175 | 0.312 | 217.88 | 212.99 | 0.0278 | watch_only | none |
| TER | semiconductor_test_packaging | 369 |  | 371.8343 | -0.7622 | 376.78 | 363.37 | 0.1328 | below_vwap | below_vwap |
| ONTO | semiconductor_test_packaging | 289.04 |  | 293.7092 | -1.5897 | 301.305 | 293.685 | 0.4705 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 64.88 |  | 65.1872 | -0.4712 | 67.455 | 65.81 | 4.1924 | price_stale_or_missing | below_opening_15m_low,below_vwap,price_stale_or_missing,spread_too_wide,stale_or_missing |
| COHU | semiconductor_test_packaging | 54.22 |  | 54.4717 | -0.462 | 55.76 | 53.78 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.17 |  | 134.9034 | -0.5436 | 137.81 | 135.66 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 340.45 |  | 342.5917 | -0.6252 | 347.92 | 341.755 | 4.5704 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 505.74 |  | 507.1743 | -0.2828 | 510.71 | 502.72 | 4.9096 | below_vwap | below_vwap,spread_too_wide |
| APD | industrial_gases | 295.88 |  | 295.6915 | 0.0638 | 299.26 | 295.795 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 29.68 |  | 30.0463 | -1.219 | 31.13 | 29.12 | 0.0674 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 40.42 |  | 41.5401 | -2.6964 | 43.21 | 40.51 | 0.0495 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.95 |  | 24.0686 | -0.4929 | 24.46 | 23.265 | 0.0835 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1612.69 |  | 1641.4095 | -1.7497 | 1651.355 | 1560 | 3.7881 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 557.195 |  | 563.9644 | -1.2003 | 576.24 | 556.3 | 2.3654 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 915.35 |  | 923.3929 | -0.871 | 933.5 | 908.955 | 1.2345 | below_vwap | below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 233.86 |  | 234.2943 | -0.1854 | 238.285 | 235.71 | 0.0171 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 606.88 |  | 604.6687 | 0.3657 | 614.15 | 605.39 | 0.0511 | watch_only | none |
| ARM | ai_accelerator | 279.77 |  | 279.5583 | 0.0757 | 283 | 276.24 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| SKHY | memory_hbm_storage | 168.055 |  | 173.1119 | -2.9212 | 177.88 | 168.18 | 4.1713 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
