# Advanced Analytics

_Project: 6/1 200EMA_  
_Generated: 2026-10-09 15:41 UTC_  
_Trades analysed: 43_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 43 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $35.80 _(net profit divided by the number of closed trades)_
- **Total PnL:** $1,539.33
- **Drawdown:** $98.53 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $11,539.33
- **Balance:** $11,539.33
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 51.16%
- **Avg Result / Trade:** $35.80
- **Profit Factor:** 1.77
- **Profitability:** 15.39% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-04 | 10000 |
| 2024-01-05 | 10152.13 |
| 2024-01-30 | 10314.06 |
| 2024-02-21 | 10118.37 |
| 2024-02-29 | 9826.01 |
| 2024-03-20 | 9944.73 |
| 2024-05-03 | 9660.16 |
| 2024-07-24 | 9756.02 |
| 2024-09-12 | 9561.23 |
| 2024-10-17 | 10036.81 |
| 2024-11-20 | 10062.58 |
| 2024-12-10 | 10457.18 |
| 2024-12-27 | 10724.14 |
| 2025-01-29 | 10752.17 |
| 2025-02-13 | 11002.92 |
| 2025-04-28 | 10730.09 |
| 2025-05-14 | 10887.83 |
| 2025-07-08 | 11054.34 |
| 2025-08-14 | 11530.77 |
| 2025-10-29 | 11539.33 |

_20 of 44 points, shape-preserving; min $9,561.23 (2024-09-12), max $11,625.57 (2025-09-29), final $11,539.33 (2025-10-29)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-04 | 0 |
| 2024-01-05 | 152.13 |
| 2024-01-30 | 314.06 |
| 2024-02-21 | 118.37 |
| 2024-02-29 | -173.99 |
| 2024-03-20 | -55.28 |
| 2024-05-03 | -339.84 |
| 2024-07-24 | -243.98 |
| 2024-09-12 | -438.77 |
| 2024-10-17 | 36.81 |
| 2024-11-20 | 62.58 |
| 2024-12-10 | 457.18 |
| 2024-12-27 | 724.14 |
| 2025-01-29 | 752.17 |
| 2025-02-13 | 1002.92 |
| 2025-04-28 | 730.09 |
| 2025-05-14 | 887.83 |
| 2025-07-08 | 1054.34 |
| 2025-08-14 | 1530.77 |
| 2025-10-29 | 1539.33 |

_20 of 44 points, shape-preserving; min -$438.77 (2024-09-12), max $1,625.56 (2025-09-29), final $1,539.33 (2025-10-29)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-04 | 0 |
| 2024-01-16 | -96.25 |
| 2024-01-30 | 0 |
| 2024-02-21 | -195.69 |
| 2024-02-29 | -488.05 |
| 2024-03-20 | -369.33 |
| 2024-05-03 | -653.9 |
| 2024-07-24 | -558.04 |
| 2024-09-12 | -752.83 |
| 2024-10-17 | -277.25 |
| 2024-11-20 | -251.47 |
| 2024-12-10 | 0 |
| 2024-12-31 | -97.04 |
| 2025-01-29 | -99.11 |
| 2025-02-13 | 0 |
| 2025-04-28 | -272.83 |
| 2025-05-14 | -115.09 |
| 2025-06-25 | 0 |
| 2025-09-29 | 0 |
| 2025-10-29 | -86.23 |

_20 of 44 points, shape-preserving; min -$752.83 (2024-09-12), max $0.00 (2024-01-04), final -$86.23 (2025-10-29)._

## 2. Analytics Insights

#### Overview

- **Net profit:** $1,539.33
- **Trades analysed:** 43
- **Score:** 15 of 40 points
- **Tests:** 15 passed, 5 failed
- **Total potential improvement:** $438.86 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 4h 2m
- **Trading period:** 1 year, 9 months, 24 days

#### Behavioural strengths

- Effective Risk Management
- Effective Stress Management
- Cost Conscious

#### Behavioural weaknesses

- Lack Of Discipline
- Poor Strategic Planning
- Inconsistent Execution

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Try avoiding very low-risk trades (risk < 0.75%) (potential improvement +$166.79)

2 very low-risk trades cost you $166.79 in earnings.

Recommendations:
- Backtest suggests improving results by $166.79 if you avoid trades where potential risk is less than 0.75% of balance. Likely reason: such trades may be taken less seriously and planned less carefully, leading to lower quality decisions.

Trades behind this verdict: 2.

#### ❌ Consider cautiously increasing position size after winning streaks (potential improvement +$272.07)

You sometimes increase risk after winning streaks, but analysis suggests a more strategic approach (what-if scenarios) could improve results.

Recommendations:
- Historical analysis shows you could improve net profit by $272.07 (17.7%) by doubling position size for just one trade after 2 consecutive wins. Note: This significantly increases risk.

Trades behind this verdict: 9.

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

Your maximum drawdown is 239.71% of your peak cumulative profit — that is too high.

Recommendations:
- Review trades during drawdown periods to identify patterns. Consider reducing position sizes when certain drawdown level is reached, implementing portfolio heat limits, or using systematic risk reduction during losing streaks.

Trades behind this verdict: 15.

#### Passed tests

- ✅ Daily loss limit analysis
- ✅ Trading session analysis
- ✅ Revenge trades
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

#### XAUUSD: best exit parameters (based on 43 trades)

- **Stop loss:** none (no stop loss) _(average loss as traded: 1034.2 pips)_
- **Take profit:** 7262.3 pips _(average profit as traded: 1331.0 pips)_
- **Max holding:** 3d 13h 50m _(median holding as traded: 4h 2m)_

#### XAUUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $4,076.15 | $1,539.33 |
| Profit factor | 6.14 | 1.77 |
| Win rate | 72.73% | 51.16% |
| Expected value per trade | $370.56 | $35.80 |
| Net result in display units | 33426.4 pips | 7563.7 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### XAUUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | none | 7262.3 pips | 3d 13h 50m | $4,076.15 | 72.73% | 6.14 |
| 2 | none | 7262.3 pips | 3d 22h 4m | $4,054.76 | 72.73% | 5.23 |
| 3 | 5395.2 pips | 7262.3 pips | 3d 13h 50m | $4,043.68 | 72.73% | 5.9 |
| 4 | 5847.7 pips | 7262.3 pips | 3d 13h 50m | $4,034.63 | 72.73% | 5.83 |
| 5 | 6311.0 pips | 7262.3 pips | 3d 13h 50m | $4,025.36 | 72.73% | 5.77 |
| 6 | 5395.2 pips | 7262.3 pips | 3d 22h 4m | $4,022.29 | 72.73% | 5.06 |
| 7 | 5847.7 pips | 7262.3 pips | 3d 22h 4m | $4,013.24 | 72.73% | 5.01 |
| 8 | 6311.0 pips | 7262.3 pips | 3d 22h 4m | $4,003.97 | 72.73% | 4.97 |
| 9 | 3702.3 pips | 7262.3 pips | 5d 9h 18m | $3,829.86 | 63.64% | 3.3 |
| 10 | none | 7262.3 pips | 2d 22h 8m | $3,722.62 | 72.73% | 5.66 |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### XAUUSD: net profit vs stop loss (TP fixed at 7262.3 pips, holding at 3d 13h 50m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 170.2 | 287.1 |
| 327.3 | 1069.52 |
| 523.5 | 839.97 |
| 750.3 | 574.61 |
| 1003 | 688.68 |
| 1278.4 | 1697.14 |
| 1574.3 | 1448.59 |
| 1889 | 1184.24 |
| 2221 | 1378.27 |
| 2569.2 | 1141.5 |
| 2932.6 | 2321.67 |
| 3310.6 | 2520.27 |
| 3702.3 | 3373.9 |
| 4107.1 | 3272.7 |
| 4524.5 | 3168.35 |
| 4954 | 3060.98 |
| 5395.2 | 4043.68 |
| 5847.7 | 4034.63 |
| 6311 | 4025.36 |

_min $287.10 (170.2), max $4,043.68 (5395.2), final $4,025.36 (6311). The best stop loss is none (the level disabled), which is not on this axis; with it disabled net profit is $4,076.15.._

#### XAUUSD: net profit vs take profit (SL fixed at none (no stop loss), holding at 3d 13h 50m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 88.5 | 121.25 |
| 253.9 | 347.84 |
| 533.6 | 731.03 |
| 882.9 | 1209.57 |
| 1286.6 | 1762.64 |
| 1736.5 | 1677.54 |
| 2226.8 | 1284.24 |
| 2753.6 | 1398.46 |
| 3313.7 | 1773.73 |
| 3904.7 | 2128.74 |
| 4524.5 | 2488.23 |
| 5171.6 | 2863.54 |
| 5844.4 | 3253.77 |
| 6541.6 | 3658.14 |
| 7262.3 | 4076.15 |
| 8005.4 | 1770.53 |
| 8770 | 1824.05 |
| 9555.4 | 1879.03 |
| 10360.9 | 1935.42 |
| 11185.7 | 1316.2 |

_min $121.25 (88.5), max $4,076.15 (7262.3), final $1,316.20 (11185.7)._

#### XAUUSD: net profit vs max holding (SL fixed at none (no stop loss), TP fixed at 7262.3 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 6h 27m | 459.61 |
| 8h 17m | 594.11 |
| 11h 22m | -194.31 |
| 15h 14m | -335.96 |
| 19h 41m | -302.62 |
| 1d 40m | 136.71 |
| 1d 6h 5m | -387.63 |
| 1d 11h 55m | 380.15 |
| 1d 18h 7m | 1444.52 |
| 2d 39m | 1751.29 |
| 2d 7h 31m | 1955.77 |
| 2d 14h 41m | 2620.91 |
| 2d 22h 8m | 3722.62 |
| 3d 5h 51m | 3712.53 |
| 3d 13h 50m | 4076.15 |
| 3d 22h 4m | 4054.76 |
| 4d 6h 32m | 3359.75 |
| 4d 15h 14m | 3089.36 |
| 5d 9m | 3264.97 |
| 5d 9h 18m | 3338.62 |

_min -$387.63 (1d 6h 5m), max $4,076.15 (3d 13h 50m), final $3,338.62 (5d 9h 18m)._

## 4. Entry / Exit Efficiency

_38 of 43 filtered trade rows are included. 5 filtered trade rows were excluded._

#### Favorable move captured

- **Median capture:** 75.5% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 93.4%
- **Money-weighted capture:** 35.8% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $36.44 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $129.30
- **Winners with open loss above profit:** 0.0%

#### E-ratio in the first bars after entry

- **5 bars of 5m:** 1.00 _(38 eligible, 0 unavailable)_
- **10 bars of 5m:** 1.39 _(38 eligible, 0 unavailable)_
- **20 bars of 5m:** 1.79 _(38 eligible, 0 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 7.62%
- **Maximum drawdown, money:** $786.15 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 9.9 mo
- **Average recovery:** 47d 17h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 3.01%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-04 | 0 |
| 2024-01-05 | -0.55 |
| 2024-01-12 | -0.01 |
| 2024-01-16 | -1.58 |
| 2024-02-13 | -0.22 |
| 2024-02-26 | -3.79 |
| 2024-02-29 | -4.73 |
| 2024-03-20 | -3.58 |
| 2024-05-13 | -7.21 |
| 2024-10-09 | -7.62 |
| 2024-10-17 | -2.69 |
| 2024-11-13 | -3.21 |
| 2024-11-20 | -0.1 |
| 2024-12-31 | -1.46 |
| 2025-01-24 | 0 |
| 2025-03-05 | 0 |
| 2025-04-28 | -2.65 |
| 2025-06-25 | 0 |
| 2025-09-29 | 0 |
| 2025-10-29 | -0.74 |

_20 of 126 points, shape-preserving; min -7.62% (2024-10-09), max 0.00% (2024-01-04), final -0.74% (2025-10-29)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7.62% | $786.15 | 12 Feb 2024 17:00 | 09 Oct 2024 09:00 | 10 Dec 2024 09:00 | 9.9 mo | 2.0 mo | 21 | — |
| 2.65% | $292.38 | 05 Mar 2025 09:00 | 28 Apr 2025 13:00 | 25 Jun 2025 09:00 | 3.7 mo | 57d 20h | 4 | — |
| 1.58% | $160.98 | 15 Jan 2024 17:00 | 16 Jan 2024 05:00 | 30 Jan 2024 09:00 | 14d 16h | 14d 4h | 2 | — |
| 1.46% | $157.88 | 31 Dec 2024 05:00 | 31 Dec 2024 05:00 | 23 Jan 2025 21:00 | 23d 16h | 23d 16h | 1 | — |
| 0.94% | $101.67 | 29 Jan 2025 09:00 | 29 Jan 2025 09:00 | 07 Feb 2025 05:00 | 8d 20h | 8d 20h | 1 | — |

_Showing the 5 deepest of 11 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 43
- **Winnings:** 22/43 (51.16%)
- **Losing:** 21/43 (48.84%)
- **Long trades:** 30/43 (69.77%)
- **Short trades:** 13/43 (30.23%)
- **Profit on longs:** $682.75
- **Profit on shorts:** $856.58

## 7. Rolling Performance

_Measured over 43 closed trades matching the filters, in close-time order._

#### Last 30 trades vs overall

- **Average trade, last 30 trades:** $59.46 _(+$23.67 vs overall)_
- **Average trade, overall:** $35.8
- **Win rate, last 30 trades:** 60% _(+8.84 pp vs overall)_
- **Win rate, overall:** 51.16%

#### Verdict

- Average trade over the last 30 trades is $59.46, above the overall $35.8. Counted as above or below once the gap exceeds 20% of the overall value.
- Win rate over the last 30 trades is 60%, above the overall 51.16%. Counted as above or below overall once the gap exceeds 5 percentage points.

#### Average trade over the last 30 trades, window by window

| Trade number (close-time order) | Average trade (USD) |
| --- | --- |
| 30 | 25.07 |
| 31 | 23.73 |
| 32 | 31.57 |
| 33 | 23.69 |
| 34 | 17.19 |
| 35 | 17.06 |
| 36 | 25.65 |
| 37 | 32.93 |
| 38 | 41.02 |
| 39 | 40.94 |
| 40 | 52.1 |
| 41 | 52.87 |
| 42 | 59.17 |
| 43 | 59.46 |

_min $17.06 (trade 35), max $59.46 (trade 43), final $59.46 (trade 43); overall $35.8._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XAUUSD | 43 | 22 | 21 | 51.16% | 6.1 | $3,537.77 | $1,998.44 | $1,539.33 | 1.77 | 63.90% / 36.10% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 1 | 2.33% | -$80.56 | -$80.56 | 0.0% | 0.00 |
| London Session | 08:00-17:00 London time | 21 | 48.84% | $876.29 | $41.73 | 52.4% | 1.92 |
| Asian Session | 09:00-18:00 Tokyo time | 13 | 30.23% | $458.93 | $35.30 | 53.8% | 1.81 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 4 | 9.30% | $42.41 | $10.60 | 50.0% | 1.22 |
| New York Session | 08:00-17:00 New York time | 16 | 37.21% | $629.91 | $39.37 | 50.0% | 1.83 |
| Outside sessions | — | 3 | 6.98% | -$76.61 | -$25.54 | — | — |

_Shares are of the 43 trades analysed. Sessions overlap: 43 trades are counted 55 times in total, because a trade opened while two sessions run counts in both. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

#### Risk and outcome summary

- **Average trade result:** $35.80
- **Median ending balance:** $11,516.87
- **Average ending balance:** $11,526.89
- **Where most endings landed (middle 90%):** $10,137.05 - $12,964.58
- **Chance of profit:** 96.70% ± 0.56%
- **Chance of ruin (below 50%):** 0.00% ± 0.00% _(ruin level $5,000.00)_
- **Worst-case drawdown:** $955.18 (8.81%) _(The amount and the percentage are ranked separately, so they may come from different paths.)_
- **Median maximum drawdown:** $478.83 (4.42%) _(The amount and the percentage are ranked separately, so they may come from different paths.)_
- **Average of worst 5% endings:** $9,861.78

- Ended above the starting balance in 96.70% of runs.
- The balance fell to $5,000.00 or below in 0.00% of simulations.
- Your 43 real trades would end at $11,539.33 from this starting balance. Deposits and withdrawals are excluded, as in the simulation.

#### Simulation parameters

- **Starting balance:** $10,000.00
- **Trades per simulation:** 43
- **Number of simulations:** 1000
- **Trade order:** Random picks
- **Trade size:** Same money amounts

#### Simulated outcomes: Median

| Trade number | Balance (USD) |
| --- | --- |
| 0 | 10000 |
| 1 | 9919.44 |
| 3 | 10122.43 |
| 5 | 10171.09 |
| 8 | 10259.59 |
| 11 | 10364.6 |
| 12 | 10432.47 |
| 15 | 10543.43 |
| 17 | 10574.36 |
| 20 | 10685.77 |
| 22 | 10767.57 |
| 24 | 10870.56 |
| 26 | 10904.63 |
| 30 | 11076.44 |
| 32 | 11156.62 |
| 35 | 11237.46 |
| 37 | 11327.69 |
| 39 | 11400.85 |
| 40 | 11408.2 |
| 43 | 11516.87 |

_20 of 44 points, shape-preserving; min $9,919.44 (Trade 1), max $11,516.87 (Trade 43), final $11,516.87 (Trade 43)._

#### Maximum drawdowns

| Maximum drawdown | Simulations | Share of simulations | At or below |
| --- | --- | --- | --- |
| 0.00% - 1.50% | 3 | 0.30% | 0.30% |
| 1.50% - 3.00% | 206 | 20.60% | 20.90% |
| 3.00% - 4.50% | 314 | 31.40% | 52.30% |
| 4.50% - 6.00% | 241 | 24.10% | 76.40% |
| 6.00% - 7.50% | 133 | 13.30% | 89.70% |
| 7.50% - 9.00% | 60 | 6.00% | 95.70% |
| 9.00% - 10.50% | 27 | 2.70% | 98.40% |
| 10.50% - 12.00% | 12 | 1.20% | 99.60% |
| 12.00% - 13.50% | 3 | 0.30% | 99.90% |
| 13.50% - 14.50% | 1 | 0.10% | 100.00% |

_Median maximum drawdown: 4.42%. Worst-case drawdown (only 1 in 20 paths went deeper): 8.81%. Largest seen: 14.07%. Random picks break up your streaks, which can hide larger drawdowns. Use 'Keep streaks' for a more realistic view._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $1,539.33
- **Average trade:** $35.8
- **Gross profit:** $3,537.77
- **Gross loss:** $1,998.44
- **Profit / month:** $70.1
- **Average profit:** $160.81
- **Average loss:** $95.16
- **Max drawdown:** $98.53
- **Max current day loss %:** 0%
- **Profit factor:** 1.77
- **Return %:** 15.39%

#### Trades

- **Total trades:** 43
- **Trading days:** 43
- **Profit trades:** 22
- **Loss trades:** 21
- **Max consecutive profit trades:** 4
- **Max consecutive loss trades:** 6
- **Trades / day:** 0.06
- **Trades / month:** 1.96
- **Profit trades / month:** 1
- **Loss trades / month:** 0.96
- **Max profit trade:** $282.62
- **Max loss trade:** $99.93
- **Total volume traded:** $1.5m
- **Average order size:** $35.6k

#### Time

- **Days processed:** 668.34
- **Months processed:** 21.96

#### Other

- **Max lot used:** 0.3
- **Restoration factor:** 15.62
- **Reliability factor:** 0.71
- **Win rate %:** 51.16%
- **Loss rate %:** 48.84%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 0.58
- **Average win/loss ratio 1:3:** 1.33
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.0662
- **Monthly Sharpe Ratio:** 0.3129
- **Daily Sortino Ratio:** 0.1136
- **Monthly Sortino Ratio:** 0.5452

## 13. Drawdown luck check

How this works: your trades are shuffled 2,000 times and your real drawdown is compared with the shuffled ones. If your drawdown is ordinary for these trades, nothing special happened. If it is deeper than almost all shuffles, your losses bunched together in time — a bad month, a market change, tilt — rather than falling randomly.

#### Close to the deep edge of ordinary

Your deepest fall of $752.83 is just outside the middle 90% of shuffles ($292.18 - $750.94, median $470.97): 5% of the 2,000 shuffles fell as deep or deeper. The edge itself is only known to within a point or two with this many shuffles, so read this as a hint, not a finding. With 43 trades, one trade more or less can move these shares noticeably — read them as rough, not exact. This was not one long row of losses: your longest losing run was 6 trades and did not exceed the usual ceiling of 7. The fall came from which losses came close together, not from how many came in a row. Your deepest fall is counted on closed results in the order they happened, so it matches the drawdown curve in Performance Over Time; the Drawdown card can show a deeper fall when its caption says it checks every tick. What to do: Worth a look, not an alarm: Rolling Performance shows where the losses gathered. Plan for a $750.94 fall either way.

#### Longest losing run

| Your run | Middle 90% of shuffles | Shuffles shorter | Shuffles same | Shuffles longer | Reading |
| --- | --- | --- | --- | --- | --- |
| 6 | 3 - 7 | 82% | 11% | 7% | Normal for a 51% win rate over 43 trades: 3 - 7 (median 4). |

_What to do: Put any "stop for the day" or "cut size" rule above 7 so a normal run does not trigger it._

- **Eligible trades:** 43 _(22 wins, 21 losses, 0 breakevens)_
- **Shuffles:** 2000

#### What it cannot tell you

Whether the trades are good — a losing strategy can have a perfectly ordinary sequence. It ignores deposits, balance and margin, uses only the trades you filtered, and one history in ten lands outside the middle range by pure chance. With fewer than about 50 trades one trade can move the share noticeably. 2,000 shuffles are an estimate: each share shown is usually within one or two points.

## 14. Prop Challenge pass probability

_Based on 43 usable closed trades across 663 calendar days. Advanced Analytics filters affect this estimate._

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

- **Estimated pass chance within 90 days:** 1.4% _(95%: 0.8–2.3%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Not decided within the horizon:** 98.6% _(95%: 97.7–99.2%)_
- **Median calendar days to pass (passed attempts only):** 73
- **Median trades to pass (passed attempts only):** 8

#### Simulated account balance, Day 90

- **Median attempt:** 1.67%
- **Low outcome (5%):** -3.08%
- **High outcome (95%):** 7.87%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 24 | 0 |
| 26 | 0 |
| 32 | 0.22 |
| 37 | 0.3 |
| 44 | 0.59 |
| 47 | 0.61 |
| 53 | 0.79 |
| 55 | 0.95 |
| 62 | 1.19 |
| 68 | 1.2 |
| 72 | 1.23 |
| 75 | 1.34 |
| 83 | 1.55 |
| 88 | 1.67 |
| 90 | 1.67 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 1.67% (Day 90), final 1.67% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-4)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 43
- **Hours with trades:** 34

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Tuesday | 07:00-08:00 | $282.62 | 1 | 100.00% |
| Friday | 09:00-10:00 | $266.95 | 1 | 100.00% |
| Monday | 07:00-08:00 | $240.06 | 1 | 100.00% |
| Thursday | 12:00-13:00 | $236.37 | 1 | 100.00% |
| Wednesday | 14:00-15:00 | $213.34 | 1 | 100.00% |
| Wednesday | 04:00-05:00 | $199.71 | 1 | 100.00% |
| Wednesday | 09:00-10:00 | $166.32 | 2 | 100.00% |
| Monday | 08:00-09:00 | $143.76 | 1 | 100.00% |
| Wednesday | 22:00-23:00 | $138.76 | 1 | 100.00% |
| Wednesday | 12:00-13:00 | $122.08 | 1 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Thursday | 08:00-09:00 | -$99.92 | 1 | 0.00% |
| Monday | 10:00-11:00 | -$99.79 | 1 | 0.00% |
| Wednesday | 21:00-22:00 | -$98.08 | 1 | 0.00% |
| Tuesday | 02:00-03:00 | -$97.04 | 1 | 0.00% |
| Tuesday | 04:00-05:00 | -$96.76 | 3 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 1 | $94.8 | $94.8 | No loss | 100.00% |
| Monday | 5 | $99.38 | $19.88 | 1.35 | 40.00% |
| Tuesday | 9 | -$267.4 | -$29.71 | 0.60 | 22.22% |
| Wednesday | 14 | $924.28 | $66.02 | 2.90 | 64.29% |
| Thursday | 8 | $234.67 | $29.33 | 1.63 | 50.00% |
| Friday | 6 | $453.6 | $75.6 | 3.39 | 66.67% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 4 | $314.06 | 4 | 3 / 1 |
| February 2024 | 5 | -$488.05 | 5 | 0 / 5 |
| March 2024 | 2 | $118.72 | 2 | 1 / 1 |
| April 2024 | 2 | -$189.33 | 2 | 0 / 2 |
| May 2024 | 2 | -$184.48 | 2 | 0 / 2 |
| June 2024 | 0 | — | 0 | 0 / 0 |
| July 2024 | 1 | $185.10 | 1 | 1 / 0 |
| August 2024 | 1 | -$98.08 | 1 | 0 / 1 |
| September 2024 | 1 | -$96.71 | 1 | 0 / 1 |
| October 2024 | 3 | $475.58 | 3 | 3 / 0 |
| November 2024 | 3 | $137.76 | 3 | 2 / 1 |
| December 2024 | 3 | $452.53 | 3 | 2 / 1 |
| January 2025 | 3 | $125.07 | 3 | 2 / 1 |
| February 2025 | 2 | $250.75 | 2 | 2 / 0 |
| March 2025 | 1 | -$92.49 | 1 | 0 / 1 |
| April 2025 | 2 | -$180.34 | 2 | 0 / 2 |
| May 2025 | 1 | $157.74 | 1 | 1 / 0 |
| June 2025 | 2 | $265.93 | 2 | 2 / 0 |
| July 2025 | 2 | $140.65 | 2 | 1 / 1 |
| August 2025 | 1 | $236.37 | 1 | 1 / 0 |
| September 2025 | 1 | $94.80 | 1 | 1 / 0 |
| October 2025 | 1 | -$86.23 | 1 | 0 / 1 |

_A month with 0 trades had none in the filtered history._

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-4)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 0 | 0 | 0 |
| 01 | 1 | 2 | -1 |
| 02 | 1 | 1 | 0 |
| 03 | 0 | 1 | -1 |
| 04 | 2 | 3 | -1 |
| 05 | 0 | 0 | 0 |
| 06 | 1 | 1 | 0 |
| 07 | 2 | 1 | +1 |
| 08 | 3 | 5 | -2 |
| 09 | 4 | 1 | +3 |
| 10 | 1 | 3 | -2 |
| 11 | 0 | 1 | -1 |
| 12 | 2 | 0 | +2 |
| 13 | 0 | 0 | 0 |
| 14 | 1 | 0 | +1 |
| 15 | 0 | 0 | 0 |
| 16 | 1 | 0 | +1 |
| 17 | 0 | 0 | 0 |
| 18 | 0 | 0 | 0 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 1 | -1 |
| 21 | 1 | 1 | 0 |
| 22 | 2 | 0 | +2 |
| 23 | 0 | 0 | 0 |

## 18. Duration & Profitability

- **Analyzed trades:** 43
- **Net profit:** $1,539.33
- **Holding-time ranges:** 6
- **Median holding time:** 4h 2m

#### Key insights

- **Winner vs loser holding time:** The median losing trade was held 1.6x longer than the median winning trade. Winner median: 3h 53m; loser median: 6h 12m.
- **Profit concentration:** Your top 5% of trades generated 22.3% of your total winning profit.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 1 | 1 | 0 | 0 | 100.0% | $157.74 | $157.74 | $157.74 |
| 1h-4h | 20 | 12 | 8 | 0 | 60.0% | $1,102.97 | $55.15 | $109.85 |
| 4h-8h | 9 | 5 | 4 | 0 | 55.6% | $338.64 | $37.63 | $111.98 |
| 8h-1d | 10 | 3 | 7 | 0 | 30.0% | $3.4 | $0.34 | -$95.02 |
| 1d-3d | 2 | 1 | 1 | 0 | 50.0% | $32.84 | $16.42 | $16.42 |
| 3d-7d | 1 | 0 | 1 | 0 | 0.0% | -$96.25 | -$96.25 | -$96.25 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$300 | 0 |
| -$300 to -$200 | 0 |
| -$200 to -$100 | 0 |
| -$100 to $0 | 21 |
| $0 to $100 | 1 |
| $100 to $200 | 16 |
| $200 to $300 | 5 |
| >$300 | 0 |

_Average $35.8; median $94.8_

#### Holding time by outcome

| Holding time | Loss | Win | Big win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 0.0% (0) | 100.0% (1) | 0.0% (0) | 1 | 100.0% | $157.74 | $157.74 | $1,381.59 (42) |
| 1h-4h | 40.0% (8) | 50.0% (10) | 10.0% (2) | 20 | 60.0% | $55.15 | $1,102.97 | $278.63 (22) |
| 4h-8h | 44.4% (4) | 55.6% (5) | 0.0% (0) | 9 | 55.6% | $37.63 | $338.64 | -$60.01 (13) |
| 8h-1d | 70.0% (7) | 10.0% (1) | 20.0% (2) | 10 | 30.0% | $0.34 | $3.4 | -$63.41 (3) |
| 1d-3d | 50.0% (1) | 50.0% (1) | 0.0% (0) | 2 | 50.0% | $16.42 | $32.84 | -$96.25 (1) |
| 3d-7d | 100.0% (1) | 0.0% (0) | 0.0% (0) | 1 | 0.0% | -$96.25 | -$96.25 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
