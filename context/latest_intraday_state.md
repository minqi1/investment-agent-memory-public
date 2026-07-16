# Intraday State

- Generated at: `2026-07-16T23:04:20+08:00`
- Market time ET: `2026-07-16T11:04:22-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `55`
- stale_count: `1`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'watch_only': 5, 'below_opening_15m_low': 12, 'manual_confirm_candidate': 3, 'spread_too_wide_or_missing': 21, 'price_stale_or_missing': 1, 'below_vwap': 14}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.62 |  | 710.6053 | 0.1428 | 713.55 | 708.25 | 0.0337 | watch_only | none |
| SOXX | semiconductor_index | 537.43 |  | 538.1758 | -0.1386 | 543.4 | 535.47 | 0.08 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.14 |  | 576.117 | -0.1696 | 580.31 | 572.21 | 0.0522 | below_vwap | below_vwap |
| SPY | market_regime | 754.05 |  | 752.6706 | 0.1833 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.05 |  | 752.6706 | 0.1833 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.84 |  | 296.5763 | 0.0889 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.35 |  | 329.2337 | 0.3391 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.05 |  | 752.6706 | 0.1833 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.84 |  | 296.5763 | 0.0889 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.35 |  | 329.2337 | 0.3391 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |
| 4 | QQQ | market_regime | 711.62 |  | 710.6053 | 0.1428 | 713.55 | 708.25 | 0.0337 | watch_only | none |
| 5 | GOOGL | cloud_ai_capex | 372.535 |  | 372.0507 | 0.1302 | 375.18 | 369.2 | 0.1476 | watch_only | none |
| 6 | MU | memory_hbm_storage | 868.84 |  | 866.5483 | 0.2645 | 887.1 | 866.765 | 0.1554 | watch_only | none |
| 7 | MSFT | cloud_ai_capex | 397.26 |  | 395.4194 | 0.4655 | 398.69 | 392.2 | 0.0327 | watch_only | none |
| 8 | CIEN | ai_networking_optical | 399.315 |  | 399.1514 | 0.041 | 410 | 397.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | LITE | ai_networking_optical | 721.575 |  | 721.3202 | 0.0353 | 737.175 | 720.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 10 | LIN | industrial_gases | 514.87 |  | 513.4273 | 0.281 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | JCI | data_center_power_cooling | 141.32 |  | 140.6704 | 0.4618 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | TT | data_center_power_cooling | 475.96 |  | 474.0851 | 0.3955 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 13 | VRT | data_center_power_cooling | 297.04 |  | 296.7449 | 0.0994 | 300.385 | 293.64 | 3.8581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 512.08 |  | 510.8448 | 0.2418 | 518.33 | 507.62 | 1.1736 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | PWR | data_center_power_cooling | 635.31 |  | 633.6276 | 0.2655 | 640.25 | 631.005 | 1.5174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | ONTO | semiconductor_test_packaging | 291.86 |  | 290.6013 | 0.4332 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | KLAC | semiconductor_equipment | 223.03 |  | 222.9657 | 0.0288 | 222.19 | 218.09 | 2.3136 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | MKSI | semiconductor_materials | 343.2 |  | 341.2996 | 0.5568 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | APD | industrial_gases | 293.725 |  | 292.2833 | 0.4933 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | ENTG | semiconductor_materials | 136.84 |  | 136.0884 | 0.5523 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | SPY | market_regime | 754.05 |  | 752.6706 | 0.1833 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| 2 | IWM | market_regime | 296.84 |  | 296.5763 | 0.0889 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| 3 | AAPL | mega_cap_platform | 330.35 |  | 329.2337 | 0.3391 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |
| 4 | ASML | semiconductor_equipment | 1823.96 |  | 1827.1002 | -0.1719 | 1823.13 | 1796.26 | 0.7094 | below_vwap | below_vwap,spread_too_wide |
| 5 | TT | data_center_power_cooling | 475.96 |  | 474.0851 | 0.3955 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 6 | JCI | data_center_power_cooling | 141.32 |  | 140.6704 | 0.4618 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 7 | GEV | data_center_power_cooling | 1043.43 |  | 1031.393 | 1.1671 | 1035.07 | 1021.09 | 4.5916 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 8 | AMAT | semiconductor_equipment | 578.25 |  | 575.6817 | 0.4461 | 572.69 | 562.32 | 3.035 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 9 | KLAC | semiconductor_equipment | 223.03 |  | 222.9657 | 0.0288 | 222.19 | 218.09 | 2.3136 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 10 | COHU | semiconductor_test_packaging | 53.2 |  | 52.6614 | 1.0228 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 11 | TER | semiconductor_test_packaging | 332.62 |  | 328.8745 | 1.1389 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 12 | QQQ | market_regime | 711.62 |  | 710.6053 | 0.1428 | 713.55 | 708.25 | 0.0337 | watch_only | none |
| 13 | MU | memory_hbm_storage | 868.84 |  | 866.5483 | 0.2645 | 887.1 | 866.765 | 0.1554 | watch_only | none |
| 14 | MSFT | cloud_ai_capex | 397.26 |  | 395.4194 | 0.4655 | 398.69 | 392.2 | 0.0327 | watch_only | none |
| 15 | GOOGL | cloud_ai_capex | 372.535 |  | 372.0507 | 0.1302 | 375.18 | 369.2 | 0.1476 | watch_only | none |
| 16 | TQQQ | leveraged_tool | 72.48 |  | 72.2155 | 0.3662 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| 17 | ANET | ai_networking_optical | 165.7 |  | 166.3406 | -0.3851 | 169.91 | 165.6 | 1.213 | below_vwap | below_vwap,spread_too_wide |
| 18 | SOXX | semiconductor_index | 537.43 |  | 538.1758 | -0.1386 | 543.4 | 535.47 | 0.08 | below_vwap | below_vwap |
| 19 | AVGO | custom_silicon_networking | 382.105 |  | 382.1264 | -0.0056 | 386.58 | 378.53 | 0.5025 | below_vwap | below_vwap,spread_too_wide |
| 20 | LRCX | semiconductor_equipment | 326.975 |  | 327.7187 | -0.2269 | 328.96 | 324.11 | 4.1655 | below_vwap | below_vwap,spread_too_wide |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 711.62 |  | 710.6053 | 0.1428 | 713.55 | 708.25 | 0.0337 | watch_only | none |
| TQQQ | leveraged_tool | 72.48 |  | 72.2155 | 0.3662 | 73.09 | 71.45 | 0.0276 | watch_only | none |
| NVDA | ai_accelerator | 206.66 |  | 208.0482 | -0.6672 | 211.03 | 207.49 | 0.0097 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| MSFT | cloud_ai_capex | 397.26 |  | 395.4194 | 0.4655 | 398.69 | 392.2 | 0.0327 | watch_only | none |
| AAPL | mega_cap_platform | 330.35 |  | 329.2337 | 0.3391 | 328.98 | 326.885 | 0.0696 | buy_precheck_manual_confirm | none |
| GOOGL | cloud_ai_capex | 372.535 |  | 372.0507 | 0.1302 | 375.18 | 369.2 | 0.1476 | watch_only | none |
| AMD | ai_accelerator | 512.08 |  | 510.8448 | 0.2418 | 518.33 | 507.62 | 1.1736 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 413.45 |  | 411.5108 | 0.4712 | 414.385 | 406.61 | 2.467 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1842000 |  | 1958272.8955 | -5.9375 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 537.43 |  | 538.1758 | -0.1386 | 543.4 | 535.47 | 0.08 | below_vwap | below_vwap |
| SMH | semiconductor_index | 575.14 |  | 576.117 | -0.1696 | 580.31 | 572.21 | 0.0522 | below_vwap | below_vwap |
| AVGO | custom_silicon_networking | 382.105 |  | 382.1264 | -0.0056 | 386.58 | 378.53 | 0.5025 | below_vwap | below_vwap,spread_too_wide |
| MU | memory_hbm_storage | 868.84 |  | 866.5483 | 0.2645 | 887.1 | 866.765 | 0.1554 | watch_only | none |
| MRVL | custom_silicon_networking | 193.3 |  | 194.858 | -0.7996 | 201.61 | 194.19 | 0.8226 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| DELL | ai_server_oem | 404.355 |  | 405.4961 | -0.2814 | 411.65 | 400.635 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 46.06 |  | 46.597 | -1.1524 | 47.65 | 46.165 | 0.0651 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SMCI | ai_server_oem | 25.6 |  | 25.867 | -1.0323 | 26.71 | 25.74 | 0.0781 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SPY | market_regime | 754.05 |  | 752.6706 | 0.1833 | 753.51 | 751.13 | 0.004 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 296.84 |  | 296.5763 | 0.0889 | 296.28 | 294.65 | 0.0067 | buy_precheck_manual_confirm | none |
| ORCL | cloud_ai_capex | 126.83 |  | 127.1831 | -0.2776 | 131.36 | 126.665 | 2.5231 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 73.68 |  | 74.0543 | -0.5054 | 75.54 | 73.985 | 0.8958 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 297.04 |  | 296.7449 | 0.0994 | 300.385 | 293.64 | 3.8581 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ETN | data_center_power_cooling | 397.87 |  | 402.1173 | -1.0562 | 406.24 | 399.495 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 635.31 |  | 633.6276 | 0.2655 | 640.25 | 631.005 | 1.5174 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| GEV | data_center_power_cooling | 1043.43 |  | 1031.393 | 1.1671 | 1035.07 | 1021.09 | 4.5916 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TT | data_center_power_cooling | 475.96 |  | 474.0851 | 0.3955 | 474.085 | 467.64 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 141.32 |  | 140.6704 | 0.4618 | 140.83 | 139.43 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ANET | ai_networking_optical | 165.7 |  | 166.3406 | -0.3851 | 169.91 | 165.6 | 1.213 | below_vwap | below_vwap,spread_too_wide |
| COHR | ai_networking_optical | 280.94 |  | 284.6276 | -1.2956 | 288.48 | 280.67 | 4.0436 | below_vwap | below_vwap,spread_too_wide |
| LITE | ai_networking_optical | 721.575 |  | 721.3202 | 0.0353 | 737.175 | 720.21 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| CIEN | ai_networking_optical | 399.315 |  | 399.1514 | 0.041 | 410 | 397.68 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AAOI | ai_networking_optical | 102.57 |  | 103.6153 | -1.0088 | 106.975 | 102.85 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 330.83 |  | 329.3548 | 0.4479 | 337.59 | 326.16 | 0.4443 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ASML | semiconductor_equipment | 1823.96 |  | 1827.1002 | -0.1719 | 1823.13 | 1796.26 | 0.7094 | below_vwap | below_vwap,spread_too_wide |
| AMAT | semiconductor_equipment | 578.25 |  | 575.6817 | 0.4461 | 572.69 | 562.32 | 3.035 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 326.975 |  | 327.7187 | -0.2269 | 328.96 | 324.11 | 4.1655 | below_vwap | below_vwap,spread_too_wide |
| KLAC | semiconductor_equipment | 223.03 |  | 222.9657 | 0.0288 | 222.19 | 218.09 | 2.3136 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 332.62 |  | 328.8745 | 1.1389 | 332.49 | 326.685 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 291.86 |  | 290.6013 | 0.4332 | 295.83 | 285.02 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMKR | semiconductor_test_packaging | 64.5 |  | 64.7257 | -0.3487 | 66.19 | 63.93 |  | below_vwap | below_vwap,spread_unavailable |
| COHU | semiconductor_test_packaging | 53.2 |  | 52.6614 | 1.0228 | 52.72 | 51.735 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ENTG | semiconductor_materials | 136.84 |  | 136.0884 | 0.5523 | 138.07 | 133.73 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MKSI | semiconductor_materials | 343.2 |  | 341.2996 | 0.5568 | 346.26 | 338 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 514.87 |  | 513.4273 | 0.281 | 515.825 | 512.23 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 293.725 |  | 292.2833 | 0.4933 | 293.89 | 291.35 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APLD | high_beta_ai_infrastructure | 27.2 |  | 27.4827 | -1.0286 | 28.05 | 27.6 | 0.0735 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| IREN | high_beta_ai_infrastructure | 35.83 |  | 36.2267 | -1.0951 | 37.365 | 36.4 | 0.0558 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| CORZ | high_beta_ai_infrastructure | 21.44 |  | 21.5932 | -0.7094 | 22.18 | 21.78 | 0.1399 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| SNDK | memory_hbm_storage | 1490.055 |  | 1498.3705 | -0.555 | 1549.47 | 1482.06 | 3.3556 | below_vwap | below_vwap,spread_too_wide |
| WDC | memory_hbm_storage | 482.79 |  | 484.0436 | -0.259 | 498.04 | 480.14 | 0.611 | below_vwap | below_vwap,spread_too_wide |
| STX | memory_hbm_storage | 782.59 |  | 778.3033 | 0.5508 | 797.155 | 768.7 | 3.2559 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMZN | cloud_ai_capex | 255.02 |  | 255.1822 | -0.0635 | 258.07 | 252.62 | 0.1098 | below_vwap | below_vwap |
| META | cloud_ai_capex | 679.89 |  | 674.5405 | 0.7931 | 680.09 | 667.1 | 0.8178 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| ARM | ai_accelerator | 257.2 |  | 259.2079 | -0.7746 | 265.96 | 258.1 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| SKHY | memory_hbm_storage | 161.98 |  | 164.4579 | -1.5067 | 168.11 | 162.41 | 0.5001 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
