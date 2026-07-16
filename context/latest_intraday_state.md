# Intraday State

- Generated at: `2026-07-17T00:52:05+08:00`
- Market time ET: `2026-07-16T12:52:06-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 37, 'manual_confirm_candidate': 2, 'watch_only': 2, 'price_stale_or_missing': 1, 'below_vwap': 12, 'spread_too_wide_or_missing': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.95 |  | 710.0377 | -0.294 | 713.55 | 708.25 | 0.0424 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 529.33 |  | 536.2011 | -1.2814 | 543.4 | 535.47 | 0.0831 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.16 |  | 574.3768 | -1.0824 | 580.31 | 572.21 | 0.0774 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.18 |  | 752.7494 | -0.0756 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.65 |  | 397.1378 | 1.6398 | 398.69 | 392.2 | 0.0867 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.7 |  | 329.9486 | 0.5308 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | GOOGL | cloud_ai_capex | 371.98 |  | 371.88 | 0.0269 | 375.18 | 369.2 | 0.121 | watch_only | none |
| 2 | AMZN | cloud_ai_capex | 256 |  | 255.4239 | 0.2256 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 331.7 |  | 329.9486 | 0.5308 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |
| 4 | LIN | industrial_gases | 516.495 |  | 514.88 | 0.3137 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | MSFT | cloud_ai_capex | 403.65 |  | 397.1378 | 1.6398 | 398.69 | 392.2 | 0.0867 | buy_precheck_manual_confirm | none |
| 6 | APD | industrial_gases | 296.47 |  | 294.7834 | 0.5722 | 293.89 | 291.35 | 3.8621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 7 | ASML | semiconductor_equipment | 1804.43 |  | 1822.8352 | -1.0097 | 1823.13 | 1796.26 | 0.0671 | below_vwap | below_vwap |
| 8 | KLAC | semiconductor_equipment | 218.51 |  | 221.7849 | -1.4766 | 222.19 | 218.09 | 0.1419 | below_vwap | below_vwap |
| 9 | SPY | market_regime | 752.18 |  | 752.7494 | -0.0756 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 10 | IWM | market_regime | 295.73 |  | 296.4155 | -0.2312 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 11 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 12 | AVGO | custom_silicon_networking | 378.78 |  | 381.4887 | -0.71 | 386.58 | 378.53 | 0.3221 | below_vwap | below_vwap |
| 13 | JCI | data_center_power_cooling | 140.25 |  | 140.5248 | -0.1956 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 14 | ENTG | semiconductor_materials | 133.86 |  | 135.1661 | -0.9663 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 15 | ANET | ai_networking_optical | 165.98 |  | 166.3184 | -0.2035 | 169.91 | 165.6 | 4.9825 | below_vwap | below_vwap,spread_too_wide |
| 16 | TT | data_center_power_cooling | 473.48 |  | 473.9687 | -0.1031 | 474.085 | 467.64 | 5.0372 | below_vwap | below_vwap,spread_too_wide |
| 17 | AMAT | semiconductor_equipment | 564.34 |  | 573.3761 | -1.5759 | 572.69 | 562.32 | 0.5245 | below_vwap | below_vwap,spread_too_wide |
| 18 | META | cloud_ai_capex | 670.785 |  | 673.6239 | -0.4214 | 680.09 | 667.1 | 0.3608 | below_vwap | below_vwap,spread_too_wide |
| 19 | SOXX | semiconductor_index | 529.33 |  | 536.2011 | -1.2814 | 543.4 | 535.47 | 0.0831 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | QQQ | market_regime | 707.95 |  | 710.0377 | -0.294 | 713.55 | 708.25 | 0.0424 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 403.65 |  | 397.1378 | 1.6398 | 398.69 | 392.2 | 0.0867 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.7 |  | 329.9486 | 0.5308 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |
| 3 | LIN | industrial_gases | 516.495 |  | 514.88 | 0.3137 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 4 | APD | industrial_gases | 296.47 |  | 294.7834 | 0.5722 | 293.89 | 291.35 | 3.8621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 5 | GOOGL | cloud_ai_capex | 371.98 |  | 371.88 | 0.0269 | 375.18 | 369.2 | 0.121 | watch_only | none |
| 6 | AMZN | cloud_ai_capex | 256 |  | 255.4239 | 0.2256 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| 7 | ANET | ai_networking_optical | 165.98 |  | 166.3184 | -0.2035 | 169.91 | 165.6 | 4.9825 | below_vwap | below_vwap,spread_too_wide |
| 8 | AVGO | custom_silicon_networking | 378.78 |  | 381.4887 | -0.71 | 386.58 | 378.53 | 0.3221 | below_vwap | below_vwap |
| 9 | TT | data_center_power_cooling | 473.48 |  | 473.9687 | -0.1031 | 474.085 | 467.64 | 5.0372 | below_vwap | below_vwap,spread_too_wide |
| 10 | JCI | data_center_power_cooling | 140.25 |  | 140.5248 | -0.1956 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 11 | ASML | semiconductor_equipment | 1804.43 |  | 1822.8352 | -1.0097 | 1823.13 | 1796.26 | 0.0671 | below_vwap | below_vwap |
| 12 | AMAT | semiconductor_equipment | 564.34 |  | 573.3761 | -1.5759 | 572.69 | 562.32 | 0.5245 | below_vwap | below_vwap,spread_too_wide |
| 13 | KLAC | semiconductor_equipment | 218.51 |  | 221.7849 | -1.4766 | 222.19 | 218.09 | 0.1419 | below_vwap | below_vwap |
| 14 | SPY | market_regime | 752.18 |  | 752.7494 | -0.0756 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| 15 | IWM | market_regime | 295.73 |  | 296.4155 | -0.2312 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | ENTG | semiconductor_materials | 133.86 |  | 135.1661 | -0.9663 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| 18 | META | cloud_ai_capex | 670.785 |  | 673.6239 | -0.4214 | 680.09 | 667.1 | 0.3608 | below_vwap | below_vwap,spread_too_wide |
| 19 | SOXX | semiconductor_index | 529.33 |  | 536.2011 | -1.2814 | 543.4 | 535.47 | 0.0831 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | TSM | foundry | 405.665 |  | 410.4319 | -1.1614 | 414.385 | 406.61 | 0.6952 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.95 |  | 710.0377 | -0.294 | 713.55 | 708.25 | 0.0424 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 71.37 |  | 72.0592 | -0.9565 | 73.09 | 71.45 | 0.028 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 207.06 |  | 207.5345 | -0.2286 | 211.03 | 207.49 | 0.0193 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 403.65 |  | 397.1378 | 1.6398 | 398.69 | 392.2 | 0.0867 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.7 |  | 329.9486 | 0.5308 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.98 |  | 371.88 | 0.0269 | 375.18 | 369.2 | 0.121 | watch_only | none |
| AMD | ai_accelerator | 499.56 |  | 507.5347 | -1.5713 | 518.33 | 507.62 | 0.7547 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TSM | foundry | 405.665 |  | 410.4319 | -1.1614 | 414.385 | 406.61 | 0.6952 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 529.33 |  | 536.2011 | -1.2814 | 543.4 | 535.47 | 0.0831 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 568.16 |  | 574.3768 | -1.0824 | 580.31 | 572.21 | 0.0774 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 378.78 |  | 381.4887 | -0.71 | 386.58 | 378.53 | 0.3221 | below_vwap | below_vwap |
| MU | memory_hbm_storage | 848.4 |  | 860.9764 | -1.4607 | 887.1 | 866.765 | 0.8263 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.93 |  | 192.4077 | -2.3272 | 201.61 | 194.19 | 0.1064 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 399.52 |  | 403.5052 | -0.9877 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.265 |  | 46.0718 | -1.7513 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.04 |  | 25.5215 | -1.8866 | 26.71 | 25.74 | 0.0399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 752.18 |  | 752.7494 | -0.0756 | 753.51 | 751.13 | 0.004 | below_vwap | below_vwap |
| IWM | market_regime | 295.73 |  | 296.4155 | -0.2312 | 296.28 | 294.65 | 0.0068 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.42 |  | 126.7627 | -0.2703 | 131.36 | 126.665 | 0.087 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 73.02 |  | 73.5212 | -0.6817 | 75.54 | 73.985 | 2.424 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 289.47 |  | 295.0079 | -1.8772 | 300.385 | 293.64 | 1.9346 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ETN | data_center_power_cooling | 393.11 |  | 400.1672 | -1.7636 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 627.13 |  | 632.3793 | -0.8301 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1018.51 |  | 1029.6672 | -1.0836 | 1035.07 | 1021.09 | 4.7206 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 473.48 |  | 473.9687 | -0.1031 | 474.085 | 467.64 | 5.0372 | below_vwap | below_vwap,spread_too_wide |
| JCI | data_center_power_cooling | 140.25 |  | 140.5248 | -0.1956 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 165.98 |  | 166.3184 | -0.2035 | 169.91 | 165.6 | 4.9825 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 276.77 |  | 282.3235 | -1.9671 | 288.48 | 280.67 | 4.5742 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 697.75 |  | 711.7624 | -1.9687 | 737.175 | 720.21 | 2.8907 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 390.48 |  | 396.6037 | -1.544 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 98.66 |  | 102.2379 | -3.4996 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 318.27 |  | 324.8464 | -2.0245 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1804.43 |  | 1822.8352 | -1.0097 | 1823.13 | 1796.26 | 0.0671 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 564.34 |  | 573.3761 | -1.5759 | 572.69 | 562.32 | 0.5245 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 319.37 |  | 325.3436 | -1.8361 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 218.51 |  | 221.7849 | -1.4766 | 222.19 | 218.09 | 0.1419 | below_vwap | below_vwap |
| TER | semiconductor_test_packaging | 322.48 |  | 327.6668 | -1.5829 | 332.49 | 326.685 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ONTO | semiconductor_test_packaging | 284.225 |  | 289.5625 | -1.8433 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.85 |  | 64.4 | -2.4068 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 51.38 |  | 52.2999 | -1.7589 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 133.86 |  | 135.1661 | -0.9663 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 334.95 |  | 338.895 | -1.1641 | 346.26 | 338 | 3.926 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LIN | industrial_gases | 516.495 |  | 514.88 | 0.3137 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 296.47 |  | 294.7834 | 0.5722 | 293.89 | 291.35 | 3.8621 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 26.26 |  | 27.0554 | -2.94 | 28.05 | 27.6 | 0.0762 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 34.83 |  | 35.7485 | -2.5694 | 37.365 | 36.4 | 0.0574 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.82 |  | 21.3808 | -2.6228 | 22.18 | 21.78 | 0.048 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1432.01 |  | 1476.6443 | -3.0227 | 1549.47 | 1482.06 | 5.0279 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 458.75 |  | 477.7593 | -3.9789 | 498.04 | 480.14 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| STX | memory_hbm_storage | 753.97 |  | 769.4842 | -2.0162 | 797.155 | 768.7 | 4.2203 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 256 |  | 255.4239 | 0.2256 | 258.07 | 252.62 | 0.0234 | watch_only | none |
| META | cloud_ai_capex | 670.785 |  | 673.6239 | -0.4214 | 680.09 | 667.1 | 0.3608 | below_vwap | below_vwap,spread_too_wide |
| ARM | ai_accelerator | 253.52 |  | 257.7773 | -1.6516 | 265.96 | 258.1 | 2.6428 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 159.56 |  | 163.3422 | -2.3155 | 168.11 | 162.41 | 0.8335 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
