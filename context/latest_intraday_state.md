# Intraday State

- Generated at: `2026-07-23T01:53:48+08:00`
- Market time ET: `2026-07-22T13:53:49-04:00`
- Session open: `True`
- Execution limit: `L3_MANUAL_CONFIRM_REQUIRED`
- Rows: `56`

## Data Quality

- total_rows: `56`
- fresh_count: `54`
- stale_count: `2`
- coverage_price: `55`
- coverage_vwap: `55`
- caution_counts: `{'manual_confirm_candidate': 8, 'below_opening_15m_low': 7, 'below_vwap': 17, 'spread_too_wide_or_missing': 20, 'price_stale_or_missing': 2, 'watch_only': 2}`
- current_max_execution_level: `L3_MANUAL_CONFIRM_REQUIRED`
- data_source_note: `ALPACA_IEX_ONLY/proxy data supports research and manual confirmation only.`

## Market Regime

- Codex hint: intraday raw state only; GPT should form the investment committee summary from the tables below.

## Indices

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.95 |  | 707.5067 | 0.0627 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| SOXX | semiconductor_index | 559.23 |  | 553.1821 | 1.0933 | 551.02 | 540.105 | 0.0644 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.85 |  | 585.6862 | 0.8817 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| SPY | market_regime | 749.01 |  | 748.537 | 0.0632 | 747.68 | 746.425 | 0.0254 | buy_precheck_manual_confirm | none |

## Buy Precheck Candidates

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.88 |  | 211.3348 | 1.2044 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.23 |  | 553.1821 | 1.0933 | 551.02 | 540.105 | 0.0644 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.85 |  | 585.6862 | 0.8817 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 213 |  | 211.3169 | 0.7965 | 207.06 | 202.18 | 0.1455 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 707.95 |  | 707.5067 | 0.0627 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.01 |  | 748.537 | 0.0632 | 747.68 | 746.425 | 0.0254 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.535 |  | 299.1446 | 0.7991 | 297.69 | 293.905 | 0.2255 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 71.07 |  | 70.8621 | 0.2933 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |

## Comfortable Entry Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | QQQ | market_regime | 707.95 |  | 707.5067 | 0.0627 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 2 | SPY | market_regime | 749.01 |  | 748.537 | 0.0632 | 747.68 | 746.425 | 0.0254 | buy_precheck_manual_confirm | none |
| 3 | JCI | data_center_power_cooling | 143.17 |  | 142.9108 | 0.1813 | 143.27 | 141.04 | 0.0419 | watch_only | none |
| 4 | ENTG | semiconductor_materials | 139.2 |  | 138.8511 | 0.2513 | 140.09 | 135.555 | 0.1437 | watch_only | none |
| 5 | MRVL | custom_silicon_networking | 213 |  | 211.3169 | 0.7965 | 207.06 | 202.18 | 0.1455 | buy_precheck_manual_confirm | none |
| 6 | VRT | data_center_power_cooling | 301.535 |  | 299.1446 | 0.7991 | 297.69 | 293.905 | 0.2255 | buy_precheck_manual_confirm | none |
| 7 | SOXX | semiconductor_index | 559.23 |  | 553.1821 | 1.0933 | 551.02 | 540.105 | 0.0644 | buy_precheck_manual_confirm | none |
| 8 | TER | semiconductor_test_packaging | 372 |  | 371.6263 | 0.1006 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 9 | NVDA | ai_accelerator | 213.88 |  | 211.3348 | 1.2044 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 10 | SMH | semiconductor_index | 590.85 |  | 585.6862 | 0.8817 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| 11 | AMAT | semiconductor_equipment | 559.75 |  | 558.5323 | 0.218 | 559.22 | 544.305 | 3.1764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 12 | ANET | ai_networking_optical | 175.265 |  | 174.8855 | 0.217 | 175.265 | 171.06 | 2.6645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 422.02 |  | 420.8015 | 0.2896 | 419.42 | 414.87 | 1.0663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | TT | data_center_power_cooling | 475.87 |  | 473.7254 | 0.4527 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 15 | ARM | ai_accelerator | 285.78 |  | 285.6597 | 0.0421 | 286.39 | 280.275 | 2.8239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 16 | KLAC | semiconductor_equipment | 216.435 |  | 216.1096 | 0.1506 | 215.465 | 210.975 | 4.3246 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 17 | LIN | industrial_gases | 509.81 |  | 507.2836 | 0.498 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 18 | PWR | data_center_power_cooling | 643.69 |  | 640.8432 | 0.4442 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | APD | industrial_gases | 298.09 |  | 297.804 | 0.096 | 300.24 | 297.585 | 4.3309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 20 | STX | memory_hbm_storage | 912.88 |  | 909.189 | 0.406 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Dynamic Leaderboard

| rank | ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 1 | NVDA | ai_accelerator | 213.88 |  | 211.3348 | 1.2044 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| 2 | SOXX | semiconductor_index | 559.23 |  | 553.1821 | 1.0933 | 551.02 | 540.105 | 0.0644 | buy_precheck_manual_confirm | none |
| 3 | SMH | semiconductor_index | 590.85 |  | 585.6862 | 0.8817 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| 4 | MRVL | custom_silicon_networking | 213 |  | 211.3169 | 0.7965 | 207.06 | 202.18 | 0.1455 | buy_precheck_manual_confirm | none |
| 5 | QQQ | market_regime | 707.95 |  | 707.5067 | 0.0627 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| 6 | SPY | market_regime | 749.01 |  | 748.537 | 0.0632 | 747.68 | 746.425 | 0.0254 | buy_precheck_manual_confirm | none |
| 7 | VRT | data_center_power_cooling | 301.535 |  | 299.1446 | 0.7991 | 297.69 | 293.905 | 0.2255 | buy_precheck_manual_confirm | none |
| 8 | TQQQ | leveraged_tool | 71.07 |  | 70.8621 | 0.2933 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| 9 | DELL | ai_server_oem | 441.08 |  | 442.7215 | -0.3708 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| 10 | AMKR | semiconductor_test_packaging | 67.465 |  | 67.4792 | -0.021 | 66.73 | 64.98 | 2.3123 | below_vwap | below_vwap,spread_too_wide |
| 11 | SMCI | ai_server_oem | 31.02 |  | 31.1799 | -0.513 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| 12 | MU | memory_hbm_storage | 973.315 |  | 968.2123 | 0.527 | 963.41 | 936.99 | 1.0346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 13 | TSM | foundry | 422.02 |  | 420.8015 | 0.2896 | 419.42 | 414.87 | 1.0663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 14 | AMD | ai_accelerator | 556.35 |  | 551.6238 | 0.8568 | 548.755 | 526.6 | 2.7806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 15 | TT | data_center_power_cooling | 475.87 |  | 473.7254 | 0.4527 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 16 | SNDK | memory_hbm_storage | 1605.72 |  | 1579.9054 | 1.6339 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 17 | WDC | memory_hbm_storage | 557.945 |  | 556.0559 | 0.3397 | 548.14 | 526.22 | 1.1686 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 18 | STX | memory_hbm_storage | 912.88 |  | 909.189 | 0.406 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 19 | TER | semiconductor_test_packaging | 372 |  | 371.6263 | 0.1006 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| 20 | AVGO | custom_silicon_networking | 397.07 |  | 391.1204 | 1.5212 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |

## Full Watchlist Rows

| ticker | chain | price | chg% | vwap | vs_vwap% | 15m_high | 15m_low | spread% | action | risk |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| QQQ | market_regime | 707.95 |  | 707.5067 | 0.0627 | 705.86 | 703.63 | 0.0085 | buy_precheck_manual_confirm | none |
| TQQQ | leveraged_tool | 71.07 |  | 70.8621 | 0.2933 | 70.43 | 69.81 | 0.0141 | buy_precheck_manual_confirm | none |
| NVDA | ai_accelerator | 213.88 |  | 211.3348 | 1.2044 | 207.4 | 205.01 | 0.014 | buy_precheck_manual_confirm | none |
| MSFT | cloud_ai_capex | 387.84 |  | 390.1699 | -0.5972 | 400.89 | 392.26 | 0.1702 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| AAPL | mega_cap_platform | 323.89 |  | 325.0715 | -0.3635 | 328.865 | 325.74 | 0.0093 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| GOOGL | cloud_ai_capex | 347.53 |  | 347.96 | -0.1236 | 348.76 | 346.23 | 0.0633 | below_vwap | below_vwap |
| AMD | ai_accelerator | 556.35 |  | 551.6238 | 0.8568 | 548.755 | 526.6 | 2.7806 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TSM | foundry | 422.02 |  | 420.8015 | 0.2896 | 419.42 | 414.87 | 1.0663 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| 000660.KS | memory_hbm_storage | 1830000 |  | 1911202.1626 | -4.2487 |  |  |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ^SOX | semiconductor_index |  |  |  |  |  |  |  | below_vwap | below_vwap,spread_unavailable |
| SOXX | semiconductor_index | 559.23 |  | 553.1821 | 1.0933 | 551.02 | 540.105 | 0.0644 | buy_precheck_manual_confirm | none |
| SMH | semiconductor_index | 590.85 |  | 585.6862 | 0.8817 | 581.9 | 572.01 | 0.0559 | buy_precheck_manual_confirm | none |
| AVGO | custom_silicon_networking | 397.07 |  | 391.1204 | 1.5212 | 387.635 | 380.205 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| MU | memory_hbm_storage | 973.315 |  | 968.2123 | 0.527 | 963.41 | 936.99 | 1.0346 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| MRVL | custom_silicon_networking | 213 |  | 211.3169 | 0.7965 | 207.06 | 202.18 | 0.1455 | buy_precheck_manual_confirm | none |
| DELL | ai_server_oem | 441.08 |  | 442.7215 | -0.3708 | 435.98 | 415.79 |  | below_vwap | below_vwap,spread_unavailable |
| HPE | ai_server_oem | 48.88 |  | 49.0258 | -0.2974 | 48.96 | 47.01 | 0.0409 | below_vwap | below_vwap |
| SMCI | ai_server_oem | 31.02 |  | 31.1799 | -0.513 | 30.66 | 28.52 | 0.0322 | below_vwap | below_vwap |
| SPY | market_regime | 749.01 |  | 748.537 | 0.0632 | 747.68 | 746.425 | 0.0254 | buy_precheck_manual_confirm | none |
| IWM | market_regime | 294.575 |  | 295.1031 | -0.1789 | 296.39 | 295.22 | 0.0136 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ORCL | cloud_ai_capex | 126.07 |  | 126.6471 | -0.4557 | 128.79 | 125.83 | 2.3162 | below_vwap | below_vwap,spread_too_wide |
| CRWV | gpu_cloud_ai_factory | 83.02 |  | 83.5207 | -0.5995 | 83.22 | 79.6 | 2.5897 | below_vwap | below_vwap,spread_too_wide |
| VRT | data_center_power_cooling | 301.535 |  | 299.1446 | 0.7991 | 297.69 | 293.905 | 0.2255 | buy_precheck_manual_confirm | none |
| ETN | data_center_power_cooling | 407.66 |  | 407.9217 | -0.0642 | 409.095 | 398.16 |  | below_vwap | below_vwap,spread_unavailable |
| PWR | data_center_power_cooling | 643.69 |  | 640.8432 | 0.4442 | 641.19 | 628.17 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| GEV | data_center_power_cooling | 991.1 |  | 1006.6016 | -1.54 | 1036.605 | 998.94 | 2.1269 | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_too_wide |
| TT | data_center_power_cooling | 475.87 |  | 473.7254 | 0.4527 | 473.865 | 466.83 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| JCI | data_center_power_cooling | 143.17 |  | 142.9108 | 0.1813 | 143.27 | 141.04 | 0.0419 | watch_only | none |
| ANET | ai_networking_optical | 175.265 |  | 174.8855 | 0.217 | 175.265 | 171.06 | 2.6645 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| COHR | ai_networking_optical | 314.685 |  | 316.1256 | -0.4557 | 317.93 | 306.89 |  | below_vwap | below_vwap,spread_unavailable |
| LITE | ai_networking_optical | 826.385 |  | 839.6683 | -1.582 | 840.47 | 814.62 | 4.1191 | below_vwap | below_vwap,spread_too_wide |
| CIEN | ai_networking_optical | 402.27 |  | 405.6423 | -0.8313 | 407.12 | 397.835 | 0.5419 | below_vwap | below_vwap,spread_too_wide |
| AAOI | ai_networking_optical | 110.91 |  | 114.3698 | -3.0251 | 117.185 | 113.68 |  | below_opening_15m_low | below_opening_15m_low,below_vwap,spread_unavailable |
| ALAB | ai_networking_optical | 332.95 |  | 329.5868 | 1.0204 | 322.67 | 307.545 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ASML | semiconductor_equipment | 1805.775 |  | 1798.4259 | 0.4086 | 1786.525 | 1767.54 | 0.911 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| AMAT | semiconductor_equipment | 559.75 |  | 558.5323 | 0.218 | 559.22 | 544.305 | 3.1764 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| LRCX | semiconductor_equipment | 321.06 |  | 319.0959 | 0.6155 | 317.72 | 311.31 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| KLAC | semiconductor_equipment | 216.435 |  | 216.1096 | 0.1506 | 215.465 | 210.975 | 4.3246 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| TER | semiconductor_test_packaging | 372 |  | 371.6263 | 0.1006 | 369.53 | 365 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| ONTO | semiconductor_test_packaging | 295.33 |  | 295.3662 | -0.0122 | 298.42 | 288.335 | 4.5542 | below_vwap | below_vwap,spread_too_wide |
| AMKR | semiconductor_test_packaging | 67.465 |  | 67.4792 | -0.021 | 66.73 | 64.98 | 2.3123 | below_vwap | below_vwap,spread_too_wide |
| COHU | semiconductor_test_packaging | 55.665 |  | 55.6941 | -0.0523 | 56.2 | 54.45 |  | price_stale_or_missing | below_vwap,price_stale_or_missing,spread_unavailable,stale_or_missing |
| ENTG | semiconductor_materials | 139.2 |  | 138.8511 | 0.2513 | 140.09 | 135.555 | 0.1437 | watch_only | none |
| MKSI | semiconductor_materials | 347.5 |  | 344.3997 | 0.9002 | 345.675 | 331.945 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| LIN | industrial_gases | 509.81 |  | 507.2836 | 0.498 | 507.545 | 505.59 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| APD | industrial_gases | 298.09 |  | 297.804 | 0.096 | 300.24 | 297.585 | 4.3309 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| APLD | high_beta_ai_infrastructure | 30.25 |  | 30.7545 | -1.6404 | 30.78 | 29.46 | 0.0331 | below_vwap | below_vwap |
| IREN | high_beta_ai_infrastructure | 41.79 |  | 42.6204 | -1.9483 | 42.29 | 40.305 | 0.0239 | below_vwap | below_vwap |
| CORZ | high_beta_ai_infrastructure | 23.76 |  | 24.1057 | -1.4341 | 24.255 | 23.58 | 0.0842 | below_vwap | below_vwap |
| SNDK | memory_hbm_storage | 1605.72 |  | 1579.9054 | 1.6339 | 1558.88 | 1518.99 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| WDC | memory_hbm_storage | 557.945 |  | 556.0559 | 0.3397 | 548.14 | 526.22 | 1.1686 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| STX | memory_hbm_storage | 912.88 |  | 909.189 | 0.406 | 899.59 | 860.605 |  | spread_too_wide_or_missing | spread_too_wide_or_missing,spread_unavailable |
| AMZN | cloud_ai_capex | 242.8 |  | 244.3779 | -0.6457 | 248.43 | 244.47 | 0.0165 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| META | cloud_ai_capex | 626.66 |  | 630.9351 | -0.6776 | 647.02 | 632.77 | 0.0383 | below_opening_15m_low | below_opening_15m_low,below_vwap |
| ARM | ai_accelerator | 285.78 |  | 285.6597 | 0.0421 | 286.39 | 280.275 | 2.8239 | spread_too_wide_or_missing | spread_too_wide,spread_too_wide_or_missing |
| SKHY | memory_hbm_storage | 166.525 |  | 166.8031 | -0.1667 | 166.63 | 162.08 | 2.2819 | below_vwap | below_vwap,spread_too_wide |
