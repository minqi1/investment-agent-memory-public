# Intraday State

- Generated at: `2026-07-17T00:28:18+08:00`
- Market time ET: `2026-07-16T12:28:19-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 18, 'below_opening_15m_low': 31, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'spread_too_wide_or_missing': 3, 'watch_only': 1}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.25 |  | 710.2006 | -0.2747 | 713.55 | 708.25 | 0.0212 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 530.92 |  | 536.8493 | -1.1045 | 543.4 | 535.47 | 0.0791 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.31 |  | 574.6666 | -0.9321 | 580.31 | 572.21 | 0.0773 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.11 |  | 752.803 | -0.0921 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.53 |  | 396.6507 | 0.978 | 398.69 | 392.2 | 0.1348 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.33 |  | 329.8774 | 0.4403 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | AAPL | mega_cap_platform | 331.33 |  | 329.8774 | 0.4403 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 2 | AMZN | cloud_ai_capex | 255.82 |  | 255.3918 | 0.1676 | 258.07 | 252.62 | 0.0547 | watch_only | none |
| 3 | MSFT | cloud_ai_capex | 400.53 |  | 396.6507 | 0.978 | 398.69 | 392.2 | 0.1348 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 514.99 |  | 514.7866 | 0.0395 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | ANET | ai_networking_optical | 166.81 |  | 166.3211 | 0.2939 | 169.91 | 165.6 | 3.1773 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 6 | APD | industrial_gases | 296.32 |  | 294.6971 | 0.5507 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | QQQ | market_regime | 708.25 |  | 710.2006 | -0.2747 | 713.55 | 708.25 | 0.0212 | below_vwap | below_vwap |
| 8 | SPY | market_regime | 752.11 |  | 752.803 | -0.0921 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |
| 9 | IWM | market_regime | 295.875 |  | 296.4818 | -0.2047 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ASML | semiconductor_equipment | 1806.2 |  | 1824.0708 | -0.9797 | 1823.13 | 1796.26 | 0.16 | below_vwap | below_vwap |
| 12 | TT | data_center_power_cooling | 473.48 |  | 474.3165 | -0.1764 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | JCI | data_center_power_cooling | 139.81 |  | 140.5942 | -0.5578 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ONTO | semiconductor_test_packaging | 285.47 |  | 289.962 | -1.5492 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ENTG | semiconductor_materials | 134.085 |  | 135.4168 | -0.9834 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 16 | COHU | semiconductor_test_packaging | 51.84 |  | 52.3202 | -0.9177 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| 17 | TSM | foundry | 407.2 |  | 410.7457 | -0.8632 | 414.385 | 406.61 | 0.5206 | below_vwap | below_vwap,spread_too_wide |
| 18 | AVGO | custom_silicon_networking | 380.655 |  | 381.6728 | -0.2667 | 386.58 | 378.53 | 1.3398 | below_vwap | below_vwap,spread_too_wide |
| 19 | AMAT | semiconductor_equipment | 568.11 |  | 573.9024 | -1.0093 | 572.69 | 562.32 | 2.7143 | below_vwap | below_vwap,spread_too_wide |
| 20 | KLAC | semiconductor_equipment | 219.17 |  | 221.9709 | -1.2619 | 222.19 | 218.09 | 4.9049 | below_vwap | below_vwap,spread_too_wide |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 400.53 |  | 396.6507 | 0.978 | 398.69 | 392.2 | 0.1348 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.33 |  | 329.8774 | 0.4403 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| 3 | APD | industrial_gases | 296.32 |  | 294.6971 | 0.5507 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | AMZN | cloud_ai_capex | 255.82 |  | 255.3918 | 0.1676 | 258.07 | 252.62 | 0.0547 | watch_only | none |
| 5 | TSM | foundry | 407.2 |  | 410.7457 | -0.8632 | 414.385 | 406.61 | 0.5206 | below_vwap | below_vwap,spread_too_wide |
| 6 | QQQ | market_regime | 708.25 |  | 710.2006 | -0.2747 | 713.55 | 708.25 | 0.0212 | below_vwap | below_vwap |
| 7 | AVGO | custom_silicon_networking | 380.655 |  | 381.6728 | -0.2667 | 386.58 | 378.53 | 1.3398 | below_vwap | below_vwap,spread_too_wide |
| 8 | TT | data_center_power_cooling | 473.48 |  | 474.3165 | -0.1764 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| 9 | JCI | data_center_power_cooling | 139.81 |  | 140.5942 | -0.5578 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | ASML | semiconductor_equipment | 1806.2 |  | 1824.0708 | -0.9797 | 1823.13 | 1796.26 | 0.16 | below_vwap | below_vwap |
| 11 | AMAT | semiconductor_equipment | 568.11 |  | 573.9024 | -1.0093 | 572.69 | 562.32 | 2.7143 | below_vwap | below_vwap,spread_too_wide |
| 12 | ONTO | semiconductor_test_packaging | 285.47 |  | 289.962 | -1.5492 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | KLAC | semiconductor_equipment | 219.17 |  | 221.9709 | -1.2619 | 222.19 | 218.09 | 4.9049 | below_vwap | below_vwap,spread_too_wide |
| 14 | SPY | market_regime | 752.11 |  | 752.803 | -0.0921 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.875 |  | 296.4818 | -0.2047 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | DELL | ai_server_oem | 401.6 |  | 403.9447 | -0.5804 | 411.65 | 400.635 | 3.9915 | below_vwap | below_vwap,spread_too_wide |
| 18 | ENTG | semiconductor_materials | 134.085 |  | 135.4168 | -0.9834 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | GOOGL | cloud_ai_capex | 371.29 |  | 371.9013 | -0.1644 | 375.18 | 369.2 | 0.4175 | below_vwap | below_vwap,spread_too_wide |
| 20 | COHU | semiconductor_test_packaging | 51.84 |  | 52.3202 | -0.9177 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 708.25 |  | 710.2006 | -0.2747 | 713.55 | 708.25 | 0.0212 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 71.45 |  | 72.1148 | -0.9218 | 73.09 | 71.45 | 0.014 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.185 |  | 207.5557 | -0.1786 | 211.03 | 207.49 | 0.1882 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 400.53 |  | 396.6507 | 0.978 | 398.69 | 392.2 | 0.1348 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.33 |  | 329.8774 | 0.4403 | 328.98 | 326.885 | 0.0121 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.29 |  | 371.9013 | -0.1644 | 375.18 | 369.2 | 0.4175 | below_vwap | below_vwap,spread_too_wide |
| AMD | ai_accelerator | 500.77 |  | 508.6436 | -1.548 | 518.33 | 507.62 | 2.7657 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 407.2 |  | 410.7457 | -0.8632 | 414.385 | 406.61 | 0.5206 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 530.92 |  | 536.8493 | -1.1045 | 543.4 | 535.47 | 0.0791 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 569.31 |  | 574.6666 | -0.9321 | 580.31 | 572.21 | 0.0773 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 380.655 |  | 381.6728 | -0.2667 | 386.58 | 378.53 | 1.3398 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 851 |  | 862.283 | -1.3085 | 887.1 | 866.765 | 1.1257 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 188.475 |  | 192.797 | -2.2417 | 201.61 | 194.19 | 0.8542 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 401.6 |  | 403.9447 | -0.5804 | 411.65 | 400.635 | 3.9915 | below_vwap | below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.52 |  | 46.1239 | -1.3092 | 47.65 | 46.165 | 0.022 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.055 |  | 25.5663 | -2.0001 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.11 |  | 752.803 | -0.0921 | 753.51 | 751.13 | 0.0066 | below_vwap | below_vwap |
| IWM | market_regime | 295.875 |  | 296.4818 | -0.2047 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.27 |  | 126.828 | -0.4399 | 131.36 | 126.665 | 0.1901 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.64 |  | 73.5959 | -1.2988 | 75.54 | 73.985 | 1.7896 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.74 |  | 295.4212 | -1.9231 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 392.61 |  | 400.6216 | -1.9998 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 626.94 |  | 632.6491 | -0.9024 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1018.105 |  | 1031.397 | -1.2887 | 1035.07 | 1021.09 | 0.1729 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TT | data_center_power_cooling | 473.48 |  | 474.3165 | -0.1764 | 474.085 | 467.64 |  | below_vwap | below_vwap,spread_unavailable |
| JCI | data_center_power_cooling | 139.81 |  | 140.5942 | -0.5578 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 166.81 |  | 166.3211 | 0.2939 | 169.91 | 165.6 | 3.1773 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 276.98 |  | 282.916 | -2.0982 | 288.48 | 280.67 | 0.6354 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 702.07 |  | 712.9442 | -1.5253 | 737.175 | 720.21 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| CIEN | ai_networking_optical | 390.99 |  | 397.1378 | -1.548 | 410 | 397.68 | 4.3889 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 99.25 |  | 102.4906 | -3.1618 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 317.27 |  | 325.5512 | -2.5437 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1806.2 |  | 1824.0708 | -0.9797 | 1823.13 | 1796.26 | 0.16 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 568.11 |  | 573.9024 | -1.0093 | 572.69 | 562.32 | 2.7143 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 321.09 |  | 325.74 | -1.4275 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 219.17 |  | 221.9709 | -1.2619 | 222.19 | 218.09 | 4.9049 | below_vwap | below_vwap,spread_too_wide |
| TER | semiconductor_test_packaging | 323 |  | 328.1433 | -1.5674 | 332.49 | 326.685 | 0.6625 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 285.47 |  | 289.962 | -1.5492 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 63.265 |  | 64.4665 | -1.8638 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.84 |  | 52.3202 | -0.9177 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 134.085 |  | 135.4168 | -0.9834 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 335.17 |  | 339.3529 | -1.2326 | 346.26 | 338 | 3.9383 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 514.99 |  | 514.7866 | 0.0395 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.32 |  | 294.6971 | 0.5507 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.38 |  | 27.1543 | -2.8516 | 28.05 | 27.6 | 0.1137 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.975 |  | 35.8054 | -2.3192 | 37.365 | 36.4 | 0.0858 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.955 |  | 21.4473 | -2.2954 | 22.18 | 21.78 | 0.0954 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1442.93 |  | 1479.01 | -2.4395 | 1549.47 | 1482.06 | 1.7326 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 463.47 |  | 479.7595 | -3.3953 | 498.04 | 480.14 | 0.904 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 756.55 |  | 770.1133 | -1.7612 | 797.155 | 768.7 | 4.2522 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 255.82 |  | 255.3918 | 0.1676 | 258.07 | 252.62 | 0.0547 | watch_only | none |
| META | cloud_ai_capex | 669.655 |  | 674.2233 | -0.6776 | 680.09 | 667.1 | 0.6421 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 254.03 |  | 258.0837 | -1.5707 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161 |  | 163.4635 | -1.5071 | 168.11 | 162.41 | 1.8571 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
