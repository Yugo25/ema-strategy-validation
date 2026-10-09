# Advanced Analytics

_Project: 5/19 Day-trading EMA_  
_Generated: 2026-10-09 15:34 UTC_  
_Trades analysed: 64_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 64 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $41.24 _(net profit divided by the number of closed trades)_
- **Total PnL:** $2,639.18
- **Drawdown:** $677.22 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $12,639.18
- **Balance:** $12,639.18
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 51.56%
- **Avg Result / Trade:** $41.24
- **Profit Factor:** 1.80
- **Profitability:** 26.39% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-08 | 10000 |
| 2024-01-09 | 10334.05 |
| 2024-02-23 | 9775.65 |
| 2024-03-04 | 10028.11 |
| 2024-04-12 | 10838.63 |
| 2024-05-13 | 11017.37 |
| 2024-06-03 | 10585.75 |
| 2024-06-18 | 10578.39 |
| 2024-06-26 | 11164.04 |
| 2024-09-12 | 10903.87 |
| 2024-09-24 | 11276.98 |
| 2024-10-27 | 11591.28 |
| 2024-11-28 | 11177.93 |
| 2025-01-10 | 11763.34 |
| 2025-01-27 | 12500.01 |
| 2025-01-30 | 12178.58 |
| 2025-02-26 | 12508.1 |
| 2025-03-24 | 13259.12 |
| 2025-04-08 | 12949.74 |
| 2025-05-02 | 12639.18 |

_20 of 65 points, shape-preserving; min $9,775.65 (2024-02-23), max $13,259.12 (2025-03-24), final $12,639.18 (2025-05-02)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-08 | 0 |
| 2024-01-09 | 334.05 |
| 2024-02-23 | -224.35 |
| 2024-03-04 | 28.11 |
| 2024-04-12 | 838.63 |
| 2024-05-13 | 1017.37 |
| 2024-06-03 | 585.75 |
| 2024-06-18 | 578.39 |
| 2024-06-26 | 1164.04 |
| 2024-09-12 | 903.87 |
| 2024-09-24 | 1276.98 |
| 2024-10-27 | 1591.28 |
| 2024-11-28 | 1177.93 |
| 2025-01-10 | 1763.34 |
| 2025-01-27 | 2500.01 |
| 2025-01-30 | 2178.58 |
| 2025-02-26 | 2508.1 |
| 2025-03-24 | 3259.12 |
| 2025-04-08 | 2949.74 |
| 2025-05-02 | 2639.18 |

_20 of 65 points, shape-preserving; min -$224.35 (2024-02-23), max $3,259.12 (2025-03-24), final $2,639.18 (2025-05-02)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-08 | 0 |
| 2024-01-23 | -105.6 |
| 2024-02-23 | -558.4 |
| 2024-03-04 | -305.94 |
| 2024-03-28 | -9.22 |
| 2024-05-13 | 0 |
| 2024-06-03 | -431.62 |
| 2024-06-18 | -438.98 |
| 2024-06-26 | 0 |
| 2024-09-12 | -326.58 |
| 2024-09-24 | 0 |
| 2024-10-27 | 0 |
| 2024-11-28 | -413.35 |
| 2024-12-23 | -86.67 |
| 2025-01-27 | 0 |
| 2025-01-30 | -321.43 |
| 2025-02-14 | -50.85 |
| 2025-03-24 | 0 |
| 2025-04-08 | -309.38 |
| 2025-05-02 | -619.94 |

_20 of 65 points, shape-preserving; min -$619.94 (2025-05-02), max $0.00 (2024-01-08), final -$619.94 (2025-05-02)._

## 2. Analytics Insights

#### Overview

- **Net profit:** $2,639.18
- **Trades analysed:** 64
- **Score:** 13 of 40 points
- **Tests:** 13 passed, 7 failed
- **Total potential improvement:** $1,641.83 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 4h 38m
- **Trading period:** 1 year, 3 months, 22 days

#### Behavioural strengths

- Effective Risk Management
- Effective Stress Management
- Cost Conscious

#### Behavioural weaknesses

- Lack Of Discipline
- Emotional Reactivity
- Poor Strategic Planning

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Try stopping for the day after the first loss to improve profits (potential improvement +$208.28)

You would have made more profit by stopping trading for the day after your first losing trade.

Recommendations:
- Implement a rule to stop trading after your first losing trade of the day. Historical analysis shows this would have improved your net profit by $208.28.

#### ❌ Try avoiding very low-risk trades (risk < 0.75%) (potential improvement +$100.48)

1 very low-risk trades cost you $100.48 in earnings.

Recommendations:
- Backtest suggests improving results by $100.48 if you avoid trades where potential risk is less than 0.75% of balance. Likely reason: such trades may be taken less seriously and planned less carefully, leading to lower quality decisions.

Trades behind this verdict: 1.

#### ❌ Consider cautiously increasing position size after winning streaks (potential improvement +$1,121.29)

You sometimes increase risk after winning streaks, but analysis suggests a more strategic approach (what-if scenarios) could improve results.

Recommendations:
- Historical analysis shows you could improve net profit by $1,121.29 (42.5%) by doubling position size after 2 consecutive wins until the next loss. Note: This significantly increases risk.

Trades behind this verdict: 14.

#### ❌ Try taking breaks after losing trades to improve profits (potential improvement +$211.78)

You have a high percentage (3.1%) of revenge trades.

Recommendations:
- Try avoiding re-entries within 2x of previous trade duration after a loss. Estimated improvement: $211.78.

#### ❌ Try using time-based exit rules or trailing stops

You have trades held significantly longer than your average.

Recommendations:
- Implement time-based exit rules or trailing stops to prevent holding trades beyond their optimal duration. Consider setting maximum holding periods based on your typical profitable trade duration.

#### ❌ Try aiming for better Reward:Risk ratios

Your Reward:Risk ratios need improvement.

Recommendations:
- Set your take profit targets at least twice as far from entry as your stop loss. This ensures favorable risk-reward even with lower win rates.
- Manage open positions to achieve better reward:risk outcomes. Let winners run to target and cut losses at predetermined stops rather than closing early.

#### ❌ Try to reduce your maximum drawdown

Your worst drawdown relative to profit is 167.16%, which is too high. Your deepest drawdown in money ($619.94) happened at a different time.

Recommendations:
- Review trades during drawdown periods to identify patterns. Consider reducing position sizes when certain drawdown level is reached, implementing portfolio heat limits, or using systematic risk reduction during losing streaks.

Trades behind this verdict: 6.

#### Passed tests

- ✅ Trading session analysis
- ✅ Trading during news events
- ✅ News reaction trading
- ✅ Position averaging
- ✅ Netting opportunities
- ✅ Average trade vs. trading costs
- ✅ Timeframe analysis
- ✅ Trading without stops
- ✅ Consistent Loss Management
- ✅ Appropriate stop loss placement
- ✅ Consistent position sizing
- ✅ Direction bias analysis
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### EURUSD: best exit parameters (based on 64 trades)

- **Stop loss:** 127.2 pips _(average loss as traded: 16.0 pips)_
- **Take profit:** 22.3 pips _(average profit as traded: 23.7 pips)_
- **Max holding:** 3d 21h 52m _(median holding as traded: 4h 38m)_

#### EURUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $4,155.86 | $2,639.18 |
| Profit factor | 45.45 | 1.8 |
| Win rate | 92.86% | 51.56% |
| Expected value per trade | $148.42 | $41.24 |
| Net result in display units | 567.3 pips | 286.8 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### EURUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 127.2 pips | 22.3 pips | 3d 21h 52m | $4,155.86 | 92.86% | 45.45 |
| 2 | 137.2 pips | 22.3 pips | 3d 21h 52m | $4,155.86 | 92.86% | 45.45 |
| 3 | none | 22.3 pips | 3d 21h 52m | $4,155.86 | 92.86% | 45.45 |
| 4 | 127.2 pips | 22.3 pips | 4d 15h | $4,031.30 | 92.86% | 19.49 |
| 5 | 137.2 pips | 22.3 pips | 4d 15h | $4,031.30 | 92.86% | 19.49 |
| 6 | none | 22.3 pips | 4d 15h | $4,031.30 | 92.86% | 19.49 |
| 7 | 127.2 pips | 22.3 pips | 4d 6h 19m | $4,019.11 | 92.86% | 18.46 |
| 8 | 137.2 pips | 22.3 pips | 4d 6h 19m | $4,019.11 | 92.86% | 18.46 |
| 9 | none | 22.3 pips | 4d 6h 19m | $4,019.11 | 92.86% | 18.46 |
| 10 | 127.2 pips | 22.3 pips | 5d 9h 1m | $3,972.47 | 92.86% | 15.35 |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### EURUSD: net profit vs stop loss (TP fixed at 22.3 pips, holding at 3d 21h 52m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 2 | -241.14 |
| 4 | 646.24 |
| 7.4 | 1347 |
| 11.7 | 1192.08 |
| 16.6 | 889.38 |
| 22.1 | 377.88 |
| 28.1 | 1528.44 |
| 34.5 | 1150.2 |
| 41.3 | 1059.96 |
| 48.5 | 1738.8 |
| 56.1 | 1857.16 |
| 64 | 2427.25 |
| 72.2 | 2229.63 |
| 80.6 | 2335.89 |
| 89.4 | 2764.56 |
| 98.5 | 3646.52 |
| 107.8 | 3597.23 |
| 117.4 | 3546.35 |
| 127.2 | 4155.86 |
| 137.2 | 4155.86 |

_min -$241.14 (2), max $4,155.86 (127.2), final $4,155.86 (137.2)._

#### EURUSD: net profit vs take profit (SL fixed at 127.2 pips, holding at 3d 21h 52m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 2 | 211.6 |
| 9.5 | 1798.6 |
| 22.3 | 4155.86 |
| 38.1 | -1095.07 |
| 56.5 | -2355.14 |
| 77 | -2423.76 |
| 99.3 | -2066.62 |
| 123.3 | -1630.12 |
| 148.7 | -1605.45 |
| 175.6 | -1193.88 |
| 203.8 | -762.42 |
| 233.3 | -739.06 |
| 263.9 | -393.28 |
| 295.6 | -35.07 |
| 328.4 | 335.57 |
| 362.2 | 717.51 |
| 397 | 1110.75 |
| 432.7 | 1514.16 |
| 469.4 | 1928.87 |
| 506.9 | 1833.97 |

_min -$2,423.76 (77), max $4,155.86 (22.3), final $1,833.97 (506.9)._

#### EURUSD: net profit vs max holding (SL fixed at 127.2 pips, TP fixed at 22.3 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 6h 27m | 785.47 |
| 8h 16m | 497.86 |
| 11h 21m | 485.69 |
| 15h 12m | 998.1 |
| 19h 39m | 1295.78 |
| 1d 37m | 1539.68 |
| 1d 6h 1m | 1371.43 |
| 1d 11h 50m | 2182.1 |
| 1d 18h 1m | 2944.78 |
| 2d 33m | 3141.13 |
| 2d 7h 24m | 3283.18 |
| 2d 14h 33m | 3189.29 |
| 2d 21h 59m | 3535.72 |
| 3d 5h 41m | 3364.15 |
| 3d 13h 39m | 3825.13 |
| 3d 21h 52m | 4155.86 |
| 4d 6h 19m | 4019.11 |
| 4d 15h | 4031.3 |
| 4d 23h 54m | 3923.72 |
| 5d 9h 1m | 3972.47 |

_min $485.69 (11h 21m), max $4,155.86 (3d 21h 52m), final $3,972.47 (5d 9h 1m)._

## 4. Entry / Exit Efficiency

_51 of 64 filtered trade rows are included. 13 filtered trade rows were excluded._

#### Favorable move captured

- **Median capture:** 70.8% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 93.2%
- **Money-weighted capture:** 44.4% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $29.76 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $112.58
- **Winners with open loss above profit:** 0.0%

#### Caveats on capture

- 4 trade(s) never moved in their favour and were left out of capture.

#### E-ratio in the first bars after entry

- **5 bars of 5m:** 1.58 _(50 eligible, 1 unavailable)_
- **10 bars of 5m:** 1.87 _(50 eligible, 1 unavailable)_
- **20 bars of 5m:** 1.93 _(50 eligible, 1 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 5.76%
- **Maximum drawdown, money:** $654.18 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 2.3 mo
- **Average recovery:** 18d 6h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 1.89%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-09 | 0 |
| 2024-01-22 | 0 |
| 2024-02-23 | -5.76 |
| 2024-03-28 | -0.47 |
| 2024-04-25 | 0 |
| 2024-05-20 | -0.28 |
| 2024-06-03 | -3.92 |
| 2024-06-26 | 0 |
| 2024-08-23 | -2.79 |
| 2024-09-12 | -3.71 |
| 2024-10-21 | 0 |
| 2024-11-28 | -4.04 |
| 2024-12-17 | -1.04 |
| 2025-01-24 | 0 |
| 2025-01-30 | -2.57 |
| 2025-02-25 | 0 |
| 2025-03-21 | 0 |
| 2025-03-24 | -1.28 |
| 2025-04-16 | -1.43 |
| 2025-05-02 | -4.92 |

_20 of 186 points, shape-preserving; min -5.76% (2024-02-23), max 0.00% (2024-01-09), final -4.92% (2025-05-02)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5.76% | $598.00 | 22 Jan 2024 21:00 | 23 Feb 2024 13:00 | 01 Apr 2024 13:00 | 2.3 mo | 37d 23h | 10 | — |
| 4.92% | $654.18 | 31 Mar 2025 01:00 | 02 May 2025 01:00 | Not recovered | 32d | — | 6 | — |
| 4.04% | $470.05 | 07 Nov 2024 01:00 | 28 Nov 2024 05:00 | 10 Jan 2025 09:00 | 2.1 mo | 43d 4h | 9 | — |
| 3.98% | $438.98 | 13 May 2024 21:00 | 18 Jun 2024 05:00 | 26 Jun 2024 09:00 | 43d 12h | 8d 4h | 7 | — |
| 3.71% | $420.66 | 13 Aug 2024 05:00 | 12 Sep 2024 09:00 | 21 Oct 2024 13:00 | 2.3 mo | 39d 4h | 8 | — |

_Showing the 5 deepest of 18 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 64
- **Winnings:** 33/64 (51.56%)
- **Losing:** 31/64 (48.44%)
- **Long trades:** 33/64 (51.56%)
- **Short trades:** 31/64 (48.44%)
- **Profit on longs:** $1,088.70
- **Profit on shorts:** $1,550.48

## 7. Rolling Performance

_Measured over 64 closed trades matching the filters, in close-time order._

#### Last 30 trades vs overall

- **Average trade, last 30 trades:** $44.87 _(+$3.63 vs overall)_
- **Average trade, overall:** $41.24
- **Win rate, last 30 trades:** 50% _(-1.56 pp vs overall)_
- **Win rate, overall:** 51.56%

#### Verdict

- Average trade over the last 30 trades is $44.87, in line with the overall $41.24. Counted as above or below once the gap exceeds 20% of the overall value.
- Win rate over the last 30 trades is 50%, in line with the overall 51.56%. Counted as above or below overall once the gap exceeds 5 percentage points.

#### Average trade over the last 30 trades, window by window

| Trade number (close-time order) | Average trade (USD) |
| --- | --- |
| 30 | 30.13 |
| 31 | 26.83 |
| 33 | 31.47 |
| 35 | 47.62 |
| 37 | 57.11 |
| 39 | 41.81 |
| 40 | 33.51 |
| 42 | 33.26 |
| 44 | 22.2 |
| 45 | 34.36 |
| 48 | 53.04 |
| 50 | 53.06 |
| 52 | 53.33 |
| 53 | 62.36 |
| 55 | 44.8 |
| 56 | 56.56 |
| 58 | 71.27 |
| 60 | 71.68 |
| 62 | 52.31 |
| 64 | 44.87 |

_20 of 35 points, shape-preserving; min $22.2 (trade 44), max $71.68 (trade 60), final $44.87 (trade 64); overall $41.24._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 64 | 33 | 31 | 51.56% | 54.1 | $5,953.43 | $3,314.25 | $2,639.18 | 1.80 | 64.24% / 35.76% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 2 | 3.13% | $31.60 | $15.80 | 50.0% | 1.30 |
| London Session | 08:00-17:00 London time | 27 | 42.19% | $2,613.16 | $96.78 | 77.8% | 5.12 |
| Asian Session | 09:00-18:00 Tokyo time | 21 | 32.81% | $683.84 | $32.56 | 42.9% | 1.53 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 5 | 7.81% | $705.77 | $141.15 | 100.0% | --- |
| New York Session | 08:00-17:00 New York time | 25 | 39.06% | $664.62 | $26.58 | 48.0% | 1.48 |
| Outside sessions | — | 4 | 6.25% | -$180.90 | -$45.22 | — | — |

_Shares are of the 64 trades analysed. Sessions overlap: 64 trades are counted 80 times in total, because a trade opened while two sessions run counts in both. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

#### Risk and outcome summary

- **Average trade result:** $41.24
- **Median ending balance:** $12,495.01
- **Average ending balance:** $12,546.23
- **Where most endings landed (middle 90%):** $10,594.69 - $14,530.72
- **Chance of profit:** 98.40% ± 0.40%
- **Chance of ruin (below 50%):** 0.00% ± 0.00% _(ruin level $5,000.00)_
- **Worst-case drawdown:** $1,167.39 (10.46%) _(The amount and the percentage are ranked separately, so they may come from different paths.)_
- **Median maximum drawdown:** $631.23 (5.42%) _(The amount and the percentage are ranked separately, so they may come from different paths.)_
- **Average of worst 5% endings:** $10,128.13

- Ended above the starting balance in 98.40% of runs.
- The balance fell to $5,000.00 or below in 0.00% of simulations.
- Your 64 real trades would end at $12,639.18 from this starting balance. Deposits and withdrawals are excluded, as in the simulation.

#### Simulation parameters

- **Starting balance:** $10,000.00
- **Trades per simulation:** 64
- **Number of simulations:** 1000
- **Trade order:** Random picks
- **Trade size:** Same money amounts

#### Simulated outcomes: Median

| Trade number | Balance (USD) |
| --- | --- |
| 0 | 10000 |
| 1 | 10105.01 |
| 4 | 10122.38 |
| 10 | 10409.89 |
| 11 | 10425.83 |
| 17 | 10706.41 |
| 21 | 10829.89 |
| 24 | 10966.06 |
| 27 | 11094.41 |
| 29 | 11141.31 |
| 34 | 11355.15 |
| 38 | 11529.75 |
| 40 | 11561.66 |
| 43 | 11704.42 |
| 47 | 11813.9 |
| 51 | 11995.99 |
| 54 | 12063.64 |
| 58 | 12264.69 |
| 61 | 12358.44 |
| 64 | 12495.01 |

_20 of 65 points, shape-preserving; min $10,000.00 (Trade 0), max $12,495.01 (Trade 64), final $12,495.01 (Trade 64)._

#### Maximum drawdowns

| Maximum drawdown | Simulations | Share of simulations | At or below |
| --- | --- | --- | --- |
| 0.00% - 1.50% | 0 | 0.00% | 0.00% |
| 1.50% - 3.00% | 47 | 4.70% | 4.70% |
| 3.00% - 4.50% | 279 | 27.90% | 32.60% |
| 4.50% - 6.00% | 278 | 27.80% | 60.40% |
| 6.00% - 7.50% | 202 | 20.20% | 80.60% |
| 7.50% - 9.00% | 92 | 9.20% | 89.80% |
| 9.00% - 10.50% | 52 | 5.20% | 95.00% |
| 10.50% - 12.00% | 24 | 2.40% | 97.40% |
| 12.00% - 13.50% | 13 | 1.30% | 98.70% |
| 13.50% - 15.00% | 4 | 0.40% | 99.10% |
| 15.00% - 16.50% | 6 | 0.60% | 99.70% |
| 16.50% - 18.00% | 3 | 0.30% | 100.00% |

_Median maximum drawdown: 5.42%. Worst-case drawdown (only 1 in 20 paths went deeper): 10.46%. Largest seen: 17.78%. Random picks break up your streaks, which can hide larger drawdowns. Use 'Keep streaks' for a more realistic view._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $2,639.18
- **Average trade:** $41.24
- **Gross profit:** $5,953.43
- **Gross loss:** $3,314.25
- **Profit / month:** $163.74
- **Average profit:** $180.41
- **Average loss:** $106.91
- **Max drawdown:** $677.22
- **Max current day loss %:** 0%
- **Profit factor:** 1.8
- **Return %:** 26.39%

#### Trades

- **Total trades:** 64
- **Trading days:** 61
- **Profit trades:** 33
- **Loss trades:** 31
- **Max consecutive profit trades:** 7
- **Max consecutive loss trades:** 6
- **Trades / day:** 0.13
- **Trades / month:** 3.97
- **Profit trades / month:** 2.05
- **Loss trades / month:** 1.92
- **Max profit trade:** $391.53
- **Max loss trade:** $116.61
- **Total volume traded:** $5.8m
- **Average order size:** $91.2k

#### Time

- **Days processed:** 490.57
- **Months processed:** 16.12

#### Other

- **Max lot used:** 1.69
- **Restoration factor:** 3.9
- **Reliability factor:** 0.24
- **Win rate %:** 51.56%
- **Loss rate %:** 48.44%
- **Number of times TP or SL was changed:** 2
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 0.95
- **Average win/loss ratio 1:3:** 1
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.099
- **Monthly Sharpe Ratio:** 0.4651
- **Daily Sortino Ratio:** 0.176
- **Monthly Sortino Ratio:** 1.03

## 13. Drawdown luck check

How this works: your trades are shuffled 2,000 times and your real drawdown is compared with the shuffled ones. If your drawdown is ordinary for these trades, nothing special happened. If it is deeper than almost all shuffles, your losses bunched together in time — a bad month, a market change, tilt — rather than falling randomly.

#### Nothing unusual about the sequence of your trades

Your deepest fall of $619.94 is ordinary for these trades: shuffles usually fall $402.97 - $961.57 (median $594.73), and 55% of them were milder than yours. About one ordinary history in ten lands outside this range by chance. Your deepest fall is counted on closed results in the order they happened, so it matches the drawdown curve in Performance Over Time; the Drawdown card can show a deeper fall when its caption says it checks every tick. What to do: Plan for a $961.57 fall, and do not read the drawdown as a verdict on the strategy.

#### Longest losing run

| Your run | Middle 90% of shuffles | Shuffles shorter | Shuffles same | Shuffles longer | Reading |
| --- | --- | --- | --- | --- | --- |
| 6 | 3 - 8 | 71% | 17% | 13% | Normal for a 52% win rate over 64 trades: 3 - 8 (median 5). |

_What to do: Put any "stop for the day" or "cut size" rule above 8 so a normal run does not trigger it._

- **Eligible trades:** 64 _(33 wins, 31 losses, 0 breakevens)_
- **Shuffles:** 2000

#### What it cannot tell you

Whether the trades are good — a losing strategy can have a perfectly ordinary sequence. It ignores deposits, balance and margin, uses only the trades you filtered, and one history in ten lands outside the middle range by pure chance. With fewer than about 50 trades one trade can move the share noticeably. 2,000 shuffles are an estimate: each share shown is usually within one or two points.

## 14. Prop Challenge pass probability

_Based on 64 usable closed trades across 479 calendar days. Advanced Analytics filters affect this estimate._

Mode: Check my own rules

#### Challenge rules

- **Preset:** Standard example
- **Profit target (%):** 10%
- **Maximum daily loss (%):** 5%
- **Maximum total loss (%):** 10%
- **Total drawdown:** Fixed from starting balance
- **Minimum trading days:** 0
- **Days to analyze:** 90
- **Simulations:** 1000

- **Estimated pass chance within 90 days:** 20.5% _(95%: 18.1–23.1%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.2% _(95%: 0.1–0.7%)_
- **Not decided within the horizon:** 79.3% _(95%: 76.7–81.7%)_
- **Median calendar days to pass (passed attempts only):** 64
- **Median trades to pass (passed attempts only):** 10

#### Simulated account balance, Day 90

- **Median attempt:** 4.11%
- **Low outcome (5%):** -4.08%
- **High outcome (95%):** 11.28%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 9 | 0 |
| 14 | 0.36 |
| 19 | 0.51 |
| 23 | 0.66 |
| 26 | 1.09 |
| 31 | 1.32 |
| 35 | 1.42 |
| 44 | 1.76 |
| 48 | 2.02 |
| 51 | 2.07 |
| 55 | 2.34 |
| 63 | 2.64 |
| 65 | 2.85 |
| 71 | 3.02 |
| 76 | 3.11 |
| 83 | 3.59 |
| 86 | 3.97 |
| 90 | 4.11 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 4.11% (Day 89), final 4.11% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-4)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 64
- **Hours with trades:** 40

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Wednesday | 09:00-10:00 | $367.29 | 1 | 100.00% |
| Monday | 12:00-13:00 | $225.71 | 2 | 100.00% |
| Tuesday | 09:00-10:00 | $218.35 | 1 | 100.00% |
| Tuesday | 11:00-12:00 | $213.06 | 1 | 100.00% |
| Monday | 11:00-12:00 | $201.6 | 1 | 100.00% |
| Tuesday | 10:00-11:00 | $191.03 | 4 | 100.00% |
| Friday | 08:00-09:00 | $182.58 | 3 | 100.00% |
| Tuesday | 08:00-09:00 | $175.1 | 1 | 100.00% |
| Sunday | 17:00-18:00 | $161.01 | 1 | 100.00% |
| Monday | 05:00-06:00 | $154.38 | 1 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Tuesday | 02:00-03:00 | -$112.86 | 3 | 0.00% |
| Friday | 10:00-11:00 | -$111.37 | 1 | 0.00% |
| Wednesday | 02:00-03:00 | -$109.61 | 1 | 0.00% |
| Tuesday | 05:00-06:00 | -$109.44 | 1 | 0.00% |
| Tuesday | 04:00-05:00 | -$108.58 | 1 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 1 | $161.01 | $161.01 | No loss | 100.00% |
| Monday | 14 | $1,190.15 | $85.01 | 3.85 | 71.43% |
| Tuesday | 18 | $395.26 | $21.96 | 1.37 | 44.44% |
| Wednesday | 6 | $485.02 | $80.84 | 3.28 | 66.67% |
| Thursday | 14 | -$429.19 | -$30.66 | 0.59 | 28.57% |
| Friday | 11 | $836.93 | $76.08 | 2.52 | 54.55% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 4 | $118.35 | 3 | 1 / 2 |
| February 2024 | 4 | -$237.84 | 4 | 1 / 3 |
| March 2024 | 3 | $444.31 | 3 | 3 / 0 |
| April 2024 | 5 | $555.81 | 5 | 4 / 1 |
| May 2024 | 4 | -$189.84 | 4 | 1 / 3 |
| June 2024 | 5 | $473.24 | 5 | 3 / 2 |
| July 2024 | 1 | -$110.25 | 1 | 0 / 1 |
| August 2024 | 3 | -$44.70 | 3 | 1 / 2 |
| September 2024 | 4 | $163.49 | 4 | 2 / 2 |
| October 2024 | 3 | $418.71 | 3 | 3 / 0 |
| November 2024 | 4 | -$413.35 | 4 | 0 / 4 |
| December 2024 | 4 | $326.69 | 4 | 3 / 1 |
| January 2025 | 7 | $673.96 | 6 | 4 / 2 |
| February 2025 | 4 | $329.52 | 4 | 3 / 1 |
| March 2025 | 4 | $650.54 | 4 | 3 / 1 |
| April 2025 | 4 | -$412.70 | 3 | 0 / 3 |
| May 2025 | 1 | -$106.76 | 1 | 0 / 1 |

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-4)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 0 | 1 | -1 |
| 01 | 1 | 2 | -1 |
| 02 | 4 | 9 | -5 |
| 03 | 3 | 1 | +2 |
| 04 | 0 | 4 | -4 |
| 05 | 2 | 1 | +1 |
| 06 | 1 | 0 | +1 |
| 07 | 2 | 2 | 0 |
| 08 | 5 | 4 | +1 |
| 09 | 2 | 0 | +2 |
| 10 | 6 | 2 | +4 |
| 11 | 2 | 0 | +2 |
| 12 | 3 | 1 | +2 |
| 13 | 0 | 0 | 0 |
| 14 | 0 | 0 | 0 |
| 15 | 0 | 1 | -1 |
| 16 | 0 | 1 | -1 |
| 17 | 1 | 1 | 0 |
| 18 | 1 | 0 | +1 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |
| 21 | 0 | 0 | 0 |
| 22 | 0 | 0 | 0 |
| 23 | 0 | 1 | -1 |

## 18. Duration & Profitability

- **Analyzed trades:** 64
- **Net profit:** $2,639.18
- **Holding-time ranges:** 7
- **Median holding time:** 4h 38m

#### Key insights

- **Winner vs loser holding time:** The median losing trade was held 2.1x longer than the median winning trade. Winner median: 3h 26m; loser median: 7h 15m.
- **Costliest holding-time range:** Trades held 8h-1d produced -$465.15 in total across 16 trades, averaging -$29.07 per trade.
- **Profit concentration:** Your top 5% of trades generated 22.4% of your total winning profit.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5m-15m | 1 | 0 | 1 | 0 | 0.0% | -$104.4 | -$104.4 | -$104.4 |
| 15m-1h | 7 | 5 | 2 | 0 | 71.4% | $416.45 | $59.49 | $106.24 |
| 1h-4h | 23 | 14 | 9 | 0 | 60.9% | $1,463.38 | $63.63 | $132.08 |
| 4h-8h | 10 | 5 | 5 | 0 | 50.0% | $465 | $46.5 | $8.07 |
| 8h-1d | 16 | 4 | 12 | 0 | 25.0% | -$465.15 | -$29.07 | -$104 |
| 1d-3d | 6 | 4 | 2 | 0 | 66.7% | $556.99 | $92.83 | $154.3 |
| 3d-7d | 1 | 1 | 0 | 0 | 100.0% | $306.9 | $306.9 | $306.9 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$400 | 0 |
| -$400 to -$300 | 0 |
| -$300 to -$200 | 0 |
| -$200 to -$100 | 31 |
| -$100 to $0 | 0 |
| $0 to $100 | 0 |
| $100 to $200 | 22 |
| $200 to $300 | 8 |
| $300 to $400 | 3 |
| >$400 | 0 |

_Average $41.24; median $104.94_

#### Holding time by outcome

| Holding time | Loss | Win | Big win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5m-15m | 100.0% (1) | 0.0% (0) | 0.0% (0) | 1 | 0.0% | -$104.4 | -$104.4 | $2,743.58 (63) |
| 15m-1h | 28.6% (2) | 71.4% (5) | 0.0% (0) | 7 | 71.4% | $59.49 | $416.45 | $2,327.13 (56) |
| 1h-4h | 39.1% (9) | 52.2% (12) | 8.7% (2) | 23 | 60.9% | $63.63 | $1,463.38 | $863.75 (33) |
| 4h-8h | 50.0% (5) | 40.0% (4) | 10.0% (1) | 10 | 50.0% | $46.5 | $465 | $398.74 (23) |
| 8h-1d | 75.0% (12) | 18.8% (3) | 6.3% (1) | 16 | 25.0% | -$29.07 | -$465.15 | $863.89 (7) |
| 1d-3d | 33.3% (2) | 50.0% (3) | 16.7% (1) | 6 | 66.7% | $92.83 | $556.99 | $306.9 (1) |
| 3d-7d | 0.0% (0) | 0.0% (0) | 100.0% (1) | 1 | 100.0% | $306.9 | $306.9 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
