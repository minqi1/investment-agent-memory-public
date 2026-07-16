# Intraday State

- Generated at: `2026-07-17T03:27:21+08:00`
- Market time ET: `2026-07-16T15:27:22-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'below_opening_15m_low': 45, 'manual_confirm_candidate': 4, 'price_stale_or_missing': 1, 'below_vwap': 2, 'spread_too_wide_or_missing': 4}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.66 |  | 708.875 | -0.7357 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SOXX | semiconductor_index | 526.54 |  | 533.4085 | -1.2877 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.32 |  | 571.419 | -1.0673 | 580.31 | 572.21 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.08 |  | 751.9904 | -0.387 | 753.51 | 751.13 | 0.016 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.58 |  | 515.4564 | 0.606 | 515.825 | 512.23 | 0.0887 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.55 |  | 295.0946 | 0.4932 | 293.89 | 291.35 | 0.1281 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 402.425 |  | 400.0588 | 0.5915 | 398.69 | 392.2 | 0.1665 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 333.51 |  | 331.3532 | 0.6509 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.58 |  | 515.4564 | 0.606 | 515.825 | 512.23 | 0.0887 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.55 |  | 295.0946 | 0.4932 | 293.89 | 291.35 | 0.1281 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 333.51 |  | 331.3532 | 0.6509 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 4 | MSFT | cloud_ai_capex | 402.425 |  | 400.0588 | 0.5915 | 398.69 | 392.2 | 0.1665 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 474.76 |  | 474.229 | 0.112 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.87 |  | 140.5684 | 0.2145 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | ANET | ai_networking_optical | 167.135 |  | 166.6023 | 0.3198 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 8 | GEV | data_center_power_cooling | 1029.43 |  | 1027.1602 | 0.221 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | IWM | market_regime | 294.7 |  | 295.9948 | -0.4375 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 10 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 11 | SOXX | semiconductor_index | 526.54 |  | 533.4085 | -1.2877 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 12 | TSM | foundry | 405.77 |  | 408.5622 | -0.6834 | 414.385 | 406.61 | 0.0789 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 13 | QQQ | market_regime | 703.66 |  | 708.875 | -0.7357 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 14 | NVDA | ai_accelerator | 206.23 |  | 207.3298 | -0.5304 | 211.03 | 207.49 | 0.1164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | SMH | semiconductor_index | 565.32 |  | 571.419 | -1.0673 | 580.31 | 572.21 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 16 | SPY | market_regime | 749.08 |  | 751.9904 | -0.387 | 753.51 | 751.13 | 0.016 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 17 | HPE | ai_server_oem | 45.25 |  | 45.7377 | -1.0663 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 18 | GOOGL | cloud_ai_capex | 353.495 |  | 366.1176 | -3.4477 | 375.18 | 369.2 | 0.0934 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | SMCI | ai_server_oem | 24.91 |  | 25.2864 | -1.4886 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | AMZN | cloud_ai_capex | 251.84 |  | 254.7873 | -1.1568 | 258.07 | 252.62 | 0.0278 | below_opening_15m_low | below_opening_15m_low,below_vwap |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | LIN | industrial_gases | 518.58 |  | 515.4564 | 0.606 | 515.825 | 512.23 | 0.0887 | buy_precheck_manual_confirm | none |
| 2 | APD | industrial_gases | 296.55 |  | 295.0946 | 0.4932 | 293.89 | 291.35 | 0.1281 | buy_precheck_manual_confirm | none |
| 3 | MSFT | cloud_ai_capex | 402.425 |  | 400.0588 | 0.5915 | 398.69 | 392.2 | 0.1665 | buy_precheck_manual_confirm | none |
| 4 | AAPL | mega_cap_platform | 333.51 |  | 331.3532 | 0.6509 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| 5 | TT | data_center_power_cooling | 474.76 |  | 474.229 | 0.112 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 140.87 |  | 140.5684 | 0.2145 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | IWM | market_regime | 294.7 |  | 295.9948 | -0.4375 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| 8 | ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| 9 | ANET | ai_networking_optical | 167.135 |  | 166.6023 | 0.3198 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | GEV | data_center_power_cooling | 1029.43 |  | 1027.1602 | 0.221 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | SOXX | semiconductor_index | 526.54 |  | 533.4085 | -1.2877 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 12 | TSM | foundry | 405.77 |  | 408.5622 | -0.6834 | 414.385 | 406.61 | 0.0789 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 13 | CIEN | ai_networking_optical | 387.6 |  | 393.4532 | -1.4876 | 410 | 397.68 | 1.0501 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 14 | QQQ | market_regime | 703.66 |  | 708.875 | -0.7357 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 15 | AVGO | custom_silicon_networking | 375.605 |  | 379.4079 | -1.0023 | 386.58 | 378.53 | 0.3914 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 16 | MU | memory_hbm_storage | 843 |  | 855.8469 | -1.5011 | 887.1 | 866.765 | 0.4152 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| 17 | VRT | data_center_power_cooling | 290.525 |  | 293.0245 | -0.853 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| 18 | NVDA | ai_accelerator | 206.23 |  | 207.3298 | -0.5304 | 211.03 | 207.49 | 0.1164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 19 | AMD | ai_accelerator | 494.36 |  | 502.812 | -1.681 | 518.33 | 507.62 | 0.3378 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 20 | PWR | data_center_power_cooling | 628.88 |  | 631.1026 | -0.3522 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 703.66 |  | 708.875 | -0.7357 | 713.55 | 708.25 | 0.0085 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TQQQ | leveraged_tool | 70.03 |  | 71.6914 | -2.3174 | 73.09 | 71.45 | 0.0143 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| NVDA | ai_accelerator | 206.23 |  | 207.3298 | -0.5304 | 211.03 | 207.49 | 0.1164 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 402.425 |  | 400.0588 | 0.5915 | 398.69 | 392.2 | 0.1665 | buy_precheck_manual_confirm | none |
| AAPL | mega_cap_platform | 333.51 |  | 331.3532 | 0.6509 | 328.98 | 326.885 | 0.012 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 353.495 |  | 366.1176 | -3.4477 | 375.18 | 369.2 | 0.0934 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMD | ai_accelerator | 494.36 |  | 502.812 | -1.681 | 518.33 | 507.62 | 0.3378 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TSM | foundry | 405.77 |  | 408.5622 | -0.6834 | 414.385 | 406.61 | 0.0789 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 526.54 |  | 533.4085 | -1.2877 | 543.4 | 535.47 | 0.0741 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMH | semiconductor_index | 565.32 |  | 571.419 | -1.0673 | 580.31 | 572.21 | 0.0354 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AVGO | custom_silicon_networking | 375.605 |  | 379.4079 | -1.0023 | 386.58 | 378.53 | 0.3914 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 843 |  | 855.8469 | -1.5011 | 887.1 | 866.765 | 0.4152 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| MRVL | custom_silicon_networking | 187.22 |  | 190.5886 | -1.7675 | 201.61 | 194.19 | 0.3045 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| DELL | ai_server_oem | 394.09 |  | 401.4991 | -1.8453 | 411.65 | 400.635 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| HPE | ai_server_oem | 45.25 |  | 45.7377 | -1.0663 | 47.65 | 46.165 | 0.0221 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 24.91 |  | 25.2864 | -1.4886 | 26.71 | 25.74 | 0.0401 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 749.08 |  | 751.9904 | -0.387 | 753.51 | 751.13 | 0.016 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IWM | market_regime | 294.7 |  | 295.9948 | -0.4375 | 296.28 | 294.65 | 0.0034 | below_vwap | below_vwap |
| ORCL | cloud_ai_capex | 124.2 |  | 126.4487 | -1.7784 | 131.36 | 126.665 | 4.6779 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.215 |  | 73.2943 | -0.1082 | 75.54 | 73.985 | 1.2839 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 290.525 |  | 293.0245 | -0.853 | 300.385 | 293.64 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ETN | data_center_power_cooling | 396.9 |  | 399.175 | -0.5699 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 628.88 |  | 631.1026 | -0.3522 | 640.25 | 631.005 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| GEV | data_center_power_cooling | 1029.43 |  | 1027.1602 | 0.221 | 1035.07 | 1021.09 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| TT | data_center_power_cooling | 474.76 |  | 474.229 | 0.112 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 140.87 |  | 140.5684 | 0.2145 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 167.135 |  | 166.6023 | 0.3198 | 169.91 | 165.6 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| COHR | ai_networking_optical | 275.41 |  | 280.4513 | -1.7976 | 288.48 | 280.67 | 1.0675 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 699.185 |  | 707.268 | -1.1429 | 737.175 | 720.21 | 4.1477 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 387.6 |  | 393.4532 | -1.4876 | 410 | 397.68 | 1.0501 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 99.585 |  | 101.1071 | -1.5055 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 316.37 |  | 322.8648 | -2.0116 | 337.59 | 326.16 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ASML | semiconductor_equipment | 1784.55 |  | 1814.874 | -1.6709 | 1823.13 | 1796.26 | 0.1552 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AMAT | semiconductor_equipment | 561.05 |  | 569.0774 | -1.4106 | 572.69 | 562.32 | 2.9445 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| LRCX | semiconductor_equipment | 317.95 |  | 322.4219 | -1.387 | 328.96 | 324.11 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| KLAC | semiconductor_equipment | 217.87 |  | 220.7866 | -1.321 | 222.19 | 218.09 | 0.1652 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| TER | semiconductor_test_packaging | 320.58 |  | 326.0847 | -1.6881 | 332.49 | 326.685 | 4.9878 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ONTO | semiconductor_test_packaging | 280.01 |  | 285.5866 | -1.9527 | 295.83 | 285.02 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| AMKR | semiconductor_test_packaging | 62.87 |  | 63.8154 | -1.4814 | 66.19 | 63.93 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 50.93 |  | 51.7199 | -1.5272 | 52.72 | 51.735 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ENTG | semiconductor_materials | 132.99 |  | 134.5808 | -1.1821 | 138.07 | 133.73 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| MKSI | semiconductor_materials | 329.82 |  | 333.8749 | -1.2145 | 346.26 | 338 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| LIN | industrial_gases | 518.58 |  | 515.4564 | 0.606 | 515.825 | 512.23 | 0.0887 | buy_precheck_manual_confirm | none |
| APD | industrial_gases | 296.55 |  | 295.0946 | 0.4932 | 293.89 | 291.35 | 0.1281 | buy_precheck_manual_confirm | none |
| APLD | high_beta_ai_infrastructure | 26.245 |  | 26.7591 | -1.9211 | 28.05 | 27.6 | 0.0381 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.265 |  | 35.5 | -0.6619 | 37.365 | 36.4 | 0.0567 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 20.94 |  | 21.1943 | -1.1999 | 22.18 | 21.78 | 0.0478 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1396.02 |  | 1454.8942 | -4.0466 | 1549.47 | 1482.06 | 4.0795 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 459.095 |  | 472.2949 | -2.7949 | 498.04 | 480.14 | 0.8713 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 741.815 |  | 762.1119 | -2.6632 | 797.155 | 768.7 | 4.3164 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| AMZN | cloud_ai_capex | 251.84 |  | 254.7873 | -1.1568 | 258.07 | 252.62 | 0.0278 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 662.62 |  | 670.6317 | -1.1946 | 680.09 | 667.1 | 3.4303 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| ARM | ai_accelerator | 255.99 |  | 257.2472 | -0.4887 | 265.96 | 258.1 | 3.9064 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| SKHY | memory_hbm_storage | 155.345 |  | 161.2796 | -3.6797 | 168.11 | 162.41 | 1.1458 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
