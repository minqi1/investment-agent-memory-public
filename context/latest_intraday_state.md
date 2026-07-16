# Intraday State

- Generated at: `2026-07-16T23:56:33+08:00`
- Market time ET: `2026-07-16T11:56:34-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_vwap': 21, 'manual_confirm_candidate': 2, 'price_stale_or_missing': 1, 'below_opening_15m_low': 24, 'spread_too_wide_or_missing': 6, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.09 |  | 710.5172 | -0.0601 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| SOXX | semiconductor_index | 534.74 |  | 537.3594 | -0.4875 | 543.4 | 535.47 | 0.0823 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.92 |  | 575.1872 | -0.3942 | 580.31 | 572.21 | 0.0943 | below_vwap | below_vwap |
| SPY | market_regime | 753.46 |  | 752.8645 | 0.0791 | 753.51 | 751.13 | 0.004 | watch_only | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.435 |  | 396.1128 | 0.8387 | 398.69 | 392.2 | 0.1051 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.75 |  | 329.6647 | 0.6325 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 753.46 |  | 752.8645 | 0.0791 | 753.51 | 751.13 | 0.004 | watch_only | none |
| 2 | AMZN | cloud_ai_capex | 256.03 |  | 255.2776 | 0.2947 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| 3 | AAPL | mega_cap_platform | 331.75 |  | 329.6647 | 0.6325 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 399.435 |  | 396.1128 | 0.8387 | 398.69 | 392.2 | 0.1051 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 475.28 |  | 474.4185 | 0.1816 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | LIN | industrial_gases | 516.85 |  | 514.6037 | 0.4365 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ANET | ai_networking_optical | 167.29 |  | 166.2949 | 0.5984 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | AVGO | custom_silicon_networking | 381.87 |  | 381.8591 | 0.0028 | 386.58 | 378.53 | 1.3355 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | APD | industrial_gases | 295.98 |  | 294.544 | 0.4875 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | META | cloud_ai_capex | 675.32 |  | 675.0634 | 0.038 | 680.09 | 667.1 | 1.4097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 11 | IWM | market_regime | 296.4 |  | 296.62 | -0.0742 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 12 | QQQ | market_regime | 710.09 |  | 710.5172 | -0.0601 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| 13 | ASML | semiconductor_equipment | 1820.81 |  | 1825.5939 | -0.262 | 1823.13 | 1796.26 | 0.1433 | below_vwap | below_vwap |
| 14 | SMH | semiconductor_index | 572.92 |  | 575.1872 | -0.3942 | 580.31 | 572.21 | 0.0943 | below_vwap | below_vwap |
| 15 | GOOGL | cloud_ai_capex | 371.75 |  | 371.9968 | -0.0663 | 375.18 | 369.2 | 0.0753 | below_vwap | below_vwap |
| 16 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 17 | NVDA | ai_accelerator | 207.565 |  | 207.6275 | -0.0301 | 211.03 | 207.49 | 0.2457 | below_vwap | below_vwap |
| 18 | PWR | data_center_power_cooling | 632.34 |  | 633.1542 | -0.1286 | 640.25 | 631.005 | 0.1676 | below_vwap | below_vwap |
| 19 | JCI | data_center_power_cooling | 140.47 |  | 140.6973 | -0.1615 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | ONTO | semiconductor_test_packaging | 290.64 |  | 290.6455 | -0.0019 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | MSFT | cloud_ai_capex | 399.435 |  | 396.1128 | 0.8387 | 398.69 | 392.2 | 0.1051 | buy_precheck_manual_confirm | none |
| 2 | AAPL | mega_cap_platform | 331.75 |  | 329.6647 | 0.6325 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |
| 3 | IWM | market_regime | 296.4 |  | 296.62 | -0.0742 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| 4 | TT | data_center_power_cooling | 475.28 |  | 474.4185 | 0.1816 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 5 | LIN | industrial_gases | 516.85 |  | 514.6037 | 0.4365 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | APD | industrial_gases | 295.98 |  | 294.544 | 0.4875 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | SPY | market_regime | 753.46 |  | 752.8645 | 0.0791 | 753.51 | 751.13 | 0.004 | watch_only | none |
| 8 | AMZN | cloud_ai_capex | 256.03 |  | 255.2776 | 0.2947 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| 9 | TSM | foundry | 408.96 |  | 411.2889 | -0.5662 | 414.385 | 406.61 | 2.7533 | below_vwap | below_vwap,spread_too_wide |
| 10 | QQQ | market_regime | 710.09 |  | 710.5172 | -0.0601 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| 11 | NVDA | ai_accelerator | 207.565 |  | 207.6275 | -0.0301 | 211.03 | 207.49 | 0.2457 | below_vwap | below_vwap |
| 12 | JCI | data_center_power_cooling | 140.47 |  | 140.6973 | -0.1615 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| 13 | AMD | ai_accelerator | 508.27 |  | 510.2304 | -0.3842 | 518.33 | 507.62 | 1.2611 | below_vwap | below_vwap,spread_too_wide |
| 14 | PWR | data_center_power_cooling | 632.34 |  | 633.1542 | -0.1286 | 640.25 | 631.005 | 0.1676 | below_vwap | below_vwap |
| 15 | GEV | data_center_power_cooling | 1031.19 |  | 1032.5677 | -0.1334 | 1035.07 | 1021.09 | 3.846 | below_vwap | below_vwap,spread_too_wide |
| 16 | ASML | semiconductor_equipment | 1820.81 |  | 1825.5939 | -0.262 | 1823.13 | 1796.26 | 0.1433 | below_vwap | below_vwap |
| 17 | AMAT | semiconductor_equipment | 571.13 |  | 574.8432 | -0.6459 | 572.69 | 562.32 | 3.5719 | below_vwap | below_vwap,spread_too_wide |
| 18 | ONTO | semiconductor_test_packaging | 290.64 |  | 290.6455 | -0.0019 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| 19 | KLAC | semiconductor_equipment | 221.18 |  | 222.7232 | -0.6929 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| 20 | SMH | semiconductor_index | 572.92 |  | 575.1872 | -0.3942 | 580.31 | 572.21 | 0.0943 | below_vwap | below_vwap |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 710.09 |  | 710.5172 | -0.0601 | 713.55 | 708.25 | 0.0155 | below_vwap | below_vwap |
| TQQQ | leveraged_tool | 72 |  | 72.1991 | -0.2757 | 73.09 | 71.45 | 0.0139 | below_vwap | below_vwap |
| NVDA | ai_accelerator | 207.565 |  | 207.6275 | -0.0301 | 211.03 | 207.49 | 0.2457 | below_vwap | below_vwap |
| MSFT | cloud_ai_capex | 399.435 |  | 396.1128 | 0.8387 | 398.69 | 392.2 | 0.1051 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 331.75 |  | 329.6647 | 0.6325 | 328.98 | 326.885 | 0.0814 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 371.75 |  | 371.9968 | -0.0663 | 375.18 | 369.2 | 0.0753 | below_vwap | below_vwap |
| AMD | ai_accelerator | 508.27 |  | 510.2304 | -0.3842 | 518.33 | 507.62 | 1.2611 | below_vwap | below_vwap,spread_too_wide |
| TSM | foundry | 408.96 |  | 411.2889 | -0.5662 | 414.385 | 406.61 | 2.7533 | below_vwap | below_vwap,spread_too_wide |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 534.74 |  | 537.3594 | -0.4875 | 543.4 | 535.47 | 0.0823 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 572.92 |  | 575.1872 | -0.3942 | 580.31 | 572.21 | 0.0943 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 381.87 |  | 381.8591 | 0.0028 | 386.58 | 378.53 | 1.3355 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MU | memory_hbm_storage | 853 |  | 863.7588 | -1.2456 | 887.1 | 866.765 | 0.2825 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MRVL | custom_silicon_networking | 190.135 |  | 193.6568 | -1.8186 | 201.61 | 194.19 | 0.9467 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 399.95 |  | 404.6687 | -1.1661 | 411.65 | 400.635 | 4.5706 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| HPE | ai_server_oem | 45.48 |  | 46.2238 | -1.6092 | 47.65 | 46.165 | 0.044 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.21 |  | 25.6781 | -1.8229 | 26.71 | 25.74 | 0.0397 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 753.46 |  | 752.8645 | 0.0791 | 753.51 | 751.13 | 0.004 | watch_only | none |
| IWM | market_regime | 296.4 |  | 296.62 | -0.0742 | 296.28 | 294.65 | 0.0067 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 126.12 |  | 127.0359 | -0.7209 | 131.36 | 126.665 | 0.3092 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CRWV | gpu_cloud_ai_factory | 72.75 |  | 73.7591 | -1.3681 | 75.54 | 73.985 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| VRT | data_center_power_cooling | 293.5 |  | 296.1847 | -0.9064 | 300.385 | 293.64 | 0.2215 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ETN | data_center_power_cooling | 395.91 |  | 401.3891 | -1.365 | 406.24 | 399.495 | 4.2131 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| PWR | data_center_power_cooling | 632.34 |  | 633.1542 | -0.1286 | 640.25 | 631.005 | 0.1676 | below_vwap | below_vwap |
| GEV | data_center_power_cooling | 1031.19 |  | 1032.5677 | -0.1334 | 1035.07 | 1021.09 | 3.846 | below_vwap | below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.28 |  | 474.4185 | 0.1816 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.47 |  | 140.6973 | -0.1615 | 140.83 | 139.43 |  | below_vwap | below_vwap,spread_unavailable |
| ANET | ai_networking_optical | 167.29 |  | 166.2949 | 0.5984 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 278.58 |  | 283.639 | -1.7836 | 288.48 | 280.67 | 2.222 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 702.445 |  | 715.4621 | -1.8194 | 737.175 | 720.21 | 2.4386 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 394.12 |  | 397.9708 | -0.9676 | 410 | 397.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AAOI | ai_networking_optical | 100.97 |  | 103.0578 | -2.0259 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 320.17 |  | 327.1359 | -2.1294 | 337.59 | 326.16 | 3.9854 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ASML | semiconductor_equipment | 1820.81 |  | 1825.5939 | -0.262 | 1823.13 | 1796.26 | 0.1433 | below_vwap | below_vwap |
| AMAT | semiconductor_equipment | 571.13 |  | 574.8432 | -0.6459 | 572.69 | 562.32 | 3.5719 | below_vwap | below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 323.48 |  | 326.9693 | -1.0672 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 221.18 |  | 222.7232 | -0.6929 | 222.19 | 218.09 |  | below_vwap | below_vwap,spread_unavailable |
| TER | semiconductor_test_packaging | 326.94 |  | 328.9155 | -0.6006 | 332.49 | 326.685 | 0.5475 | below_vwap | below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 290.64 |  | 290.6455 | -0.0019 | 295.83 | 285.02 |  | below_vwap | below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.34 |  | 64.5846 | -0.3788 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 52.25 |  | 52.6601 | -0.7788 | 52.72 | 51.735 |  | below_vwap | below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 135.54 |  | 135.9611 | -0.3097 | 138.07 | 133.73 |  | below_vwap | below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 339.08 |  | 341.059 | -0.5803 | 346.26 | 338 |  | below_vwap | below_vwap,spread_unavailable |
| LIN | industrial_gases | 516.85 |  | 514.6037 | 0.4365 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 295.98 |  | 294.544 | 0.4875 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 26.54 |  | 27.3016 | -2.7897 | 28.05 | 27.6 | 0.0754 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.065 |  | 35.9727 | -2.5232 | 37.365 | 36.4 | 0.0285 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.09 |  | 21.5298 | -2.0426 | 22.18 | 21.78 | 0.0474 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1444.38 |  | 1485.8705 | -2.7923 | 1549.47 | 1482.06 | 4.98 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 468.325 |  | 481.7229 | -2.7812 | 498.04 | 480.14 | 2.4662 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 756.55 |  | 774.7421 | -2.3481 | 797.155 | 768.7 | 0.2868 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMZN | cloud_ai_capex | 256.03 |  | 255.2776 | 0.2947 | 258.07 | 252.62 | 0.0195 | watch_only | none |
| META | cloud_ai_capex | 675.32 |  | 675.0634 | 0.038 | 680.09 | 667.1 | 1.4097 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 256.45 |  | 258.4777 | -0.7845 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.105 |  | 163.6331 | -1.545 | 168.11 | 162.41 | 2.787 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
