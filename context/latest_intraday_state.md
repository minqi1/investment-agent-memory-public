# Intraday State

- Generated at: `2026-07-17T00:14:40+08:00`
- Market time ET: `2026-07-16T12:14:41-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 35, 'manual_confirm_candidate': 2, 'below_vwap': 13, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 4, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.19 |  | 710.3883 | -0.3094 | 713.55 | 708.25 | 0.0593 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.88 |  | 537.0837 | -1.3413 | 543.4 | 535.47 | 0.0944 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.69 |  | 575.0078 | -1.0987 | 580.31 | 572.21 | 0.0334 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.275 |  | 752.8557 | -0.0771 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.295 |  | 396.4838 | 0.9612 | 398.69 | 392.2 | 0.0949 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.115 |  | 329.8305 | 0.3894 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.115 |  | 329.8305 | 0.3894 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 256.23 |  | 255.3515 | 0.344 | 258.07 | 252.62 | 0.039 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 400.295 |  | 396.4838 | 0.9612 | 398.69 | 392.2 | 0.0949 | buy_precheck_manual_confirm | none |
| 4 | ANET | ai_networking_optical | 166.815 |  | 166.3151 | 0.3006 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | TT | data_center_power_cooling | 474.89 |  | 474.3654 | 0.1106 | 474.085 | 467.64 | 4.9064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | LIN | industrial_gases | 517.08 |  | 514.6922 | 0.4639 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | APD | industrial_gases | 296.76 |  | 294.6315 | 0.7224 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | ASML | semiconductor_equipment | 1806.83 |  | 1824.8178 | -0.9857 | 1823.13 | 1796.26 | 0.1112 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 752.275 |  | 752.8557 | -0.0771 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.95 |  | 296.582 | -0.2131 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | KLAC | semiconductor_equipment | 219.36 |  | 222.5678 | -1.4413 | 222.19 | 218.09 | 0.3282 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 140.275 |  | 140.664 | -0.2765 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 285.71 |  | 290.3509 | -1.5984 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | GOOGL | cloud_ai_capex | 371.03 |  | 371.9385 | -0.2443 | 375.18 | 369.2 | 0.2426 | below_vwap | below_vwap |
| 16 | META | cloud_ai_capex | 671.495 |  | 674.8457 | -0.4965 | 680.09 | 667.1 | 0.2621 | below_vwap | below_vwap |
| 17 | COHU | semiconductor_test_packaging | 51.84 |  | 52.4439 | -1.1515 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | AVGO | custom_silicon_networking | 380.24 |  | 381.7937 | -0.4069 | 386.58 | 378.53 | 0.6233 | below_vwap | below_vwap,spread_too_wide |
| 19 | GEV | data_center_power_cooling | 1025.7 |  | 1032.5799 | -0.6663 | 1035.07 | 1021.09 | 4.3716 | below_vwap | below_vwap,spread_too_wide |
| 20 | AMAT | semiconductor_equipment | 566.43 |  | 574.4708 | -1.3997 | 572.69 | 562.32 | 2.7241 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.295 |  | 396.4838 | 0.9612 | 398.69 | 392.2 | 0.0949 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.115 |  | 329.8305 | 0.3894 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 3 | TT | data_center_power_cooling | 474.89 |  | 474.3654 | 0.1106 | 474.085 | 467.64 | 4.9064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 4 | LIN | industrial_gases | 517.08 |  | 514.6922 | 0.4639 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | APD | industrial_gases | 296.76 |  | 294.6315 | 0.7224 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | AMZN | cloud_ai_capex | 256.23 |  | 255.3515 | 0.344 | 258.07 | 252.62 | 0.039 | watch_only | none |
| 7 | AVGO | custom_silicon_networking | 380.24 |  | 381.7937 | -0.4069 | 386.58 | 378.53 | 0.6233 | below_vwap | below_vwap,spread_too_wide |
| 8 | JCI | data_center_power_cooling | 140.275 |  | 140.664 | -0.2765 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | GEV | data_center_power_cooling | 1025.7 |  | 1032.5799 | -0.6663 | 1035.07 | 1021.09 | 4.3716 | below_vwap | below_vwap,spread_too_wide |
| 10 | ASML | semiconductor_equipment | 1806.83 |  | 1824.8178 | -0.9857 | 1823.13 | 1796.26 | 0.1112 | below_vwap | below_vwap |
| 11 | AMAT | semiconductor_equipment | 566.43 |  | 574.4708 | -1.3997 | 572.69 | 562.32 | 2.7241 | below_vwap | below_vwap,spread_too_wide |
| 12 | ONTO | semiconductor_test_packaging | 285.71 |  | 290.3509 | -1.5984 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 219.36 |  | 222.5678 | -1.4413 | 222.19 | 218.09 | 0.3282 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 752.275 |  | 752.8557 | -0.0771 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.95 |  | 296.582 | -0.2131 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | GOOGL | cloud_ai_capex | 371.03 |  | 371.9385 | -0.2443 | 375.18 | 369.2 | 0.2426 | below_vwap | below_vwap |
| 18 | COHU | semiconductor_test_packaging | 51.84 |  | 52.4439 | -1.1515 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | META | cloud_ai_capex | 671.495 |  | 674.8457 | -0.4965 | 680.09 | 667.1 | 0.2621 | below_vwap | below_vwap |
| 20 | ANET | ai_networking_optical | 166.815 |  | 166.3151 | 0.3006 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.19 |  | 710.3883 | -0.3094 | 713.55 | 708.25 | 0.0593 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.42 |  | 72.1648 | -1.0321 | 73.09 | 71.45 | 0.014 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.75 |  | 207.6081 | -0.4133 | 211.03 | 207.49 | 0.3482 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.295 |  | 396.4838 | 0.9612 | 398.69 | 392.2 | 0.0949 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.115 |  | 329.8305 | 0.3894 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.03 |  | 371.9385 | -0.2443 | 375.18 | 369.2 | 0.2426 | below_vwap | below_vwap |
| AMD | ai_accelerator | 501.99 |  | 509.6208 | -1.4973 | 518.33 | 507.62 | 0.2012 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 406.59 |  | 411.0003 | -1.0731 | 414.385 | 406.61 | 0.182 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.88 |  | 537.0837 | -1.3413 | 543.4 | 535.47 | 0.0944 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.69 |  | 575.0078 | -1.0987 | 580.31 | 572.21 | 0.0334 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.24 |  | 381.7937 | -0.4069 | 386.58 | 378.53 | 0.6233 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 848.73 |  | 863.1328 | -1.6687 | 887.1 | 866.765 | 2.003 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.16 |  | 193.1713 | -2.5942 | 201.61 | 194.19 | 0.1222 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 399.12 |  | 404.3852 | -1.302 | 411.65 | 400.635 | 4.5801 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.49 |  | 46.1598 | -1.4511 | 47.65 | 46.165 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.08 |  | 25.6338 | -2.1604 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.275 |  | 752.8557 | -0.0771 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.95 |  | 296.582 | -0.2131 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.02 |  | 126.9039 | -0.6965 | 131.36 | 126.665 | 3.1662 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 72.47 |  | 73.6857 | -1.6498 | 75.54 | 73.985 | 1.6835 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.73 |  | 295.8812 | -2.0789 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 393.38 |  | 400.8573 | -1.8653 | 406.24 | 399.495 | 3.6936 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 628.93 |  | 633.0088 | -0.6444 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1025.7 |  | 1032.5799 | -0.6663 | 1035.07 | 1021.09 | 4.3716 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 474.89 |  | 474.3654 | 0.1106 | 474.085 | 467.64 | 4.9064 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| JCI | data_center_power_cooling | 140.275 |  | 140.664 | -0.2765 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.815 |  | 166.3151 | 0.3006 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 276.82 |  | 283.2008 | -2.2531 | 288.48 | 280.67 | 3.6377 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 701.805 |  | 713.4852 | -1.6371 | 737.175 | 720.21 | 3.2416 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 393.075 |  | 397.6558 | -1.1519 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 99.56 |  | 102.7579 | -3.1121 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.88 |  | 326.2966 | -2.5794 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1806.83 |  | 1824.8178 | -0.9857 | 1823.13 | 1796.26 | 0.1112 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 566.43 |  | 574.4708 | -1.3997 | 572.69 | 562.32 | 2.7241 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 320.7 |  | 326.3212 | -1.7226 | 328.96 | 324.11 | 4.3343 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 219.36 |  | 222.5678 | -1.4413 | 222.19 | 218.09 | 0.3282 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 323.25 |  | 328.589 | -1.6248 | 332.49 | 326.685 | 4.6713 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 285.71 |  | 290.3509 | -1.5984 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.41 |  | 64.5291 | -1.7342 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.84 |  | 52.4439 | -1.1515 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.345 |  | 135.7636 | -1.7815 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.63 |  | 340.0286 | -1.2936 | 346.26 | 338 | 4.2011 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 517.08 |  | 514.6922 | 0.4639 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.76 |  | 294.6315 | 0.7224 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.29 |  | 27.2094 | -3.3791 | 28.05 | 27.6 | 0.0761 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.03 |  | 35.8488 | -2.2841 | 37.365 | 36.4 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21 |  | 21.4801 | -2.2351 | 22.18 | 21.78 | 0.1429 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1432.49 |  | 1483.7339 | -3.4537 | 1549.47 | 1482.06 | 0.8244 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 465.3 |  | 480.7405 | -3.2118 | 498.04 | 480.14 | 0.9048 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 757.925 |  | 771.5373 | -1.7643 | 797.155 | 768.7 | 4.5123 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256.23 |  | 255.3515 | 0.344 | 258.07 | 252.62 | 0.039 | watch_only | none |
| META | cloud_ai_capex | 671.495 |  | 674.8457 | -0.4965 | 680.09 | 667.1 | 0.2621 | below_vwap | below_vwap |
| ARM | ai_accelerator | 254.19 |  | 258.2771 | -1.5824 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.74 |  | 163.5544 | -1.1094 | 168.11 | 162.41 | 0.9274 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
