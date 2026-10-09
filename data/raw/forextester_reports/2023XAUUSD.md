# Advanced Analytics

_Project: 5/12 200EMA-5m_  
_Generated: 2026-10-09 15:32 UTC_  
_Trades analysed: 24_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 24 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $41.24 _(net profit divided by the number of closed trades)_
- **Total PnL:** $989.76
- **Drawdown:** $54.48 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $10,989.76
- **Balance:** $10,989.77
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 50.00%
- **Avg Result / Trade:** $41.24
- **Profit Factor:** 1.90
- **Profitability:** 9.90% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2023-01-02 | 10000 |
| 2023-01-03 | 9901.37 |
| 2023-01-12 | 10009.95 |
| 2023-01-25 | 10212.2 |
| 2023-04-06 | 10013.83 |
| 2023-04-06 | 10263.11 |
| 2023-04-28 | 10166.57 |
| 2023-05-01 | 10069.87 |
| 2023-05-09 | 10191.66 |
| 2023-06-01 | 9995.26 |
| 2023-06-02 | 9899.6 |
| 2023-07-04 | 10155.64 |
| 2023-07-12 | 10339.64 |
| 2023-07-27 | 10242.38 |
| 2023-08-08 | 10438.3 |
| 2023-08-29 | 10312.77 |
| 2023-09-12 | 10514.05 |
| 2023-09-25 | 10415.06 |
| 2023-10-05 | 10621.43 |
| 2023-10-18 | 10989.77 |

_20 of 25 points, shape-preserving; min $9,899.60 (2023-06-02), max $10,989.77 (2023-10-18), final $10,989.77 (2023-10-18)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2023-01-02 | 0 |
| 2023-01-03 | -98.63 |
| 2023-01-12 | 9.95 |
| 2023-01-25 | 212.2 |
| 2023-04-06 | 13.83 |
| 2023-04-06 | 263.11 |
| 2023-04-28 | 166.57 |
| 2023-05-01 | 69.87 |
| 2023-05-09 | 191.66 |
| 2023-06-01 | -4.74 |
| 2023-06-02 | -100.4 |
| 2023-07-04 | 155.64 |
| 2023-07-12 | 339.64 |
| 2023-07-27 | 242.38 |
| 2023-08-08 | 438.3 |
| 2023-08-29 | 312.77 |
| 2023-09-12 | 514.05 |
| 2023-09-25 | 415.06 |
| 2023-10-05 | 621.43 |
| 2023-10-18 | 989.77 |

_20 of 25 points, shape-preserving; min -$100.40 (2023-06-02), max $989.77 (2023-10-18), final $989.77 (2023-10-18)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2023-01-02 | 0 |
| 2023-01-03 | -98.63 |
| 2023-01-12 | 0 |
| 2023-01-25 | 0 |
| 2023-04-06 | -198.37 |
| 2023-04-06 | 0 |
| 2023-04-28 | -96.54 |
| 2023-05-01 | -193.24 |
| 2023-05-09 | -71.45 |
| 2023-06-01 | -267.85 |
| 2023-06-02 | -363.51 |
| 2023-07-04 | -107.47 |
| 2023-07-12 | 0 |
| 2023-07-27 | -97.27 |
| 2023-08-08 | 0 |
| 2023-08-29 | -125.53 |
| 2023-09-12 | 0 |
| 2023-09-25 | -98.99 |
| 2023-10-05 | 0 |
| 2023-10-18 | 0 |

_20 of 25 points, shape-preserving; min -$363.51 (2023-06-02), max $0.00 (2023-01-02), final $0.00 (2023-10-18)._

## 2. Analytics Insights

_You need at least 30 trades for more precise recommendations. Keep testing — the more data we have, the smarter your analytics become._

#### Overview

- **Net profit:** $989.77
- **Trades analysed:** 24
- **Score:** 15 of 40 points
- **Tests:** 15 passed, 5 failed
- **Total potential improvement:** $287.72 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 3h 59m
- **Trading period:** 0 years, 9 months, 14 days

#### Behavioural strengths

- Effective Risk Management
- Effective Stress Management
- Cost Conscious

#### Behavioural weaknesses

- Greed Driven Decisions
- Inconsistent Execution
- Fear Driven Decisions

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Consider cautiously increasing position size after winning streaks (potential improvement +$287.72)

You sometimes increase risk after winning streaks, but analysis suggests a more strategic approach (what-if scenarios) could improve results.

Recommendations:
- Historical analysis shows you could improve net profit by $287.72 (29.1%) by doubling position size for just one trade after 2 consecutive wins. Note: This significantly increases risk.
- Another check flags positions far above your typical size, so these two tips point in opposite directions. The choice is yours: a larger size after a streak chases the missed profit, while consistent sizing protects your account.

Trades behind this verdict: 4.

#### ❌ Try using time-based exit rules or trailing stops

You have trades held significantly longer than your average.

Recommendations:
- Implement time-based exit rules or trailing stops to prevent holding trades beyond their optimal duration. Consider setting maximum holding periods based on your typical profitable trade duration.

#### ❌ Try maintaining consistent position sizes

We've detected trades with position sizes significantly larger than your typical size. Such inconsistencies can lead to oversized losses and often suggest emotional decision-making.

Recommendations:
- Develop and stick to a position sizing formula based on your account risk percentage. Avoid emotional trading that leads to sudden position size increases.
- Another check shows profit missed by not increasing your lot after a winning streak, so these two tips point in opposite directions. The choice is yours: consistent sizing protects your account, while a larger size after a streak chases the missed profit.

#### ❌ Try managing trades to achieve 2:1 Reward:Risk

Your Reward:Risk ratios need improvement.

Recommendations:
- Manage open positions to achieve better reward:risk outcomes. Let winners run to target and cut losses at predetermined stops rather than closing early.

#### ❌ Try to reduce your maximum drawdown

Your maximum drawdown is 138.16% of your peak cumulative profit — that is too high.

Recommendations:
- Review trades during drawdown periods to identify patterns. Consider reducing position sizes when certain drawdown level is reached, implementing portfolio heat limits, or using systematic risk reduction during losing streaks.

Trades behind this verdict: 7.

#### Passed tests

- ✅ Daily loss limit analysis
- ✅ Trading session analysis
- ✅ Risk per trade analysis
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
- ✅ Direction bias analysis
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### XAUUSD: best exit parameters (based on 24 trades)

- **Stop loss:** 192.6 pips _(average loss as traded: 439.8 pips)_
- **Take profit:** 6163.3 pips _(average profit as traded: 656.7 pips)_
- **Max holding:** 2d 23h 34m _(median holding as traded: 3h 59m)_

#### XAUUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $2,794.30 | $989.77 |
| Profit factor | 10.67 | 1.9 |
| Win rate | 22.22% | 50% |
| Expected value per trade | $310.48 | $41.24 |
| Net result in display units | 6560.4 pips | 2603.1 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### XAUUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 192.6 pips | 6163.3 pips | 2d 23h 34m | $2,794.30 | 22.22% | 10.67 |
| 2 | 192.6 pips | 6163.3 pips | 3d 5h 39m | $2,794.30 | 22.22% | 10.67 |
| 3 | 192.6 pips | 6163.3 pips | 3d 11h 52m | $2,794.30 | 22.22% | 10.67 |
| 4 | 192.6 pips | 6163.3 pips | 3d 18h 15m | $2,794.30 | 22.22% | 10.67 |
| 5 | 1244.8 pips | 6163.3 pips | 3d 11h 52m | $2,790.42 | 44.44% | 2.95 |
| 6 | 192.6 pips | none | 2d 23h 34m | $2,766.04 | 22.22% | 10.57 |
| 7 | 192.6 pips | none | 3d 18h 15m | $2,735.10 | 22.22% | 10.47 |
| 8 | 192.6 pips | none | 3d 5h 39m | $2,725.74 | 22.22% | 10.43 |
| 9 | 192.6 pips | 6163.3 pips | 2d 17h 39m | $2,696.51 | 22.22% | 10.33 |
| 10 | 192.6 pips | none | 2d 17h 39m | $2,696.51 | 22.22% | 10.33 |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### XAUUSD: net profit vs stop loss (TP fixed at 6163.3 pips, holding at 2d 23h 34m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 86.7 | -202.07 |
| 192.6 | 2794.3 |
| 324.8 | 2596 |
| 477.6 | 2366.8 |
| 647.9 | 2111.35 |
| 833.4 | 2419.05 |
| 1032.8 | 2163.82 |
| 1244.8 | 2388.12 |
| 1468.5 | 2130.87 |
| 1703.1 | 1861.08 |
| 1948 | 1579.44 |
| 2202.6 | 1513.2 |
| 2466.5 | 1257.22 |
| 2739.3 | 992.6 |
| 3020.5 | 1221.05 |
| 3309.9 | 1307.75 |
| 3607.2 | 1144.24 |
| 3912 | 976.6 |
| 4224.2 | 1282.13 |

_min -$202.07 (86.7), max $2,794.30 (192.6), final $1,282.13 (4224.2)._

#### XAUUSD: net profit vs take profit (SL fixed at 192.6 pips, holding at 2d 23h 34m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 49.5 | 71.7 |
| 140.6 | 150.94 |
| 294.7 | 330.86 |
| 487.1 | 326.04 |
| 709.6 | 417.29 |
| 957.4 | 655.18 |
| 1227.5 | 914.48 |
| 1517.8 | 970.81 |
| 1826.3 | 1226.87 |
| 2151.9 | 1310.08 |
| 2493.4 | 1436.44 |
| 2849.9 | 1568.34 |
| 3220.6 | 1705.5 |
| 3604.7 | 1847.62 |
| 4001.7 | 1994.51 |
| 4411.1 | 2145.99 |
| 4832.4 | 2301.87 |
| 5265.1 | 2461.97 |
| 5708.8 | 2626.14 |
| 6163.3 | 2794.3 |

_min $71.70 (49.5), max $2,794.30 (6163.3), final $2,794.30 (6163.3)._

#### XAUUSD: net profit vs max holding (SL fixed at 192.6 pips, TP fixed at 6163.3 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 4h 30m | 542.82 |
| 5h 47m | 849.16 |
| 7h 56m | 796.83 |
| 10h 38m | 712.17 |
| 13h 45m | 960.58 |
| 17h 13m | 1022.9 |
| 21h | 1094.86 |
| 1d 1h 4m | 1013.12 |
| 1d 5h 24m | 1149.91 |
| 1d 9h 58m | 1245.11 |
| 1d 14h 45m | 1363.4 |
| 1d 19h 45m | 987.11 |
| 2d 57m | 857.24 |
| 2d 6h 20m | 1010.05 |
| 2d 11h 55m | 1478.1 |
| 2d 17h 39m | 2696.51 |
| 2d 23h 34m | 2794.3 |
| 3d 5h 39m | 2794.3 |
| 3d 11h 52m | 2794.3 |
| 3d 18h 15m | 2794.3 |

_min $542.82 (4h 30m), max $2,794.30 (2d 23h 34m), final $2,794.30 (3d 18h 15m)._

## 4. Entry / Exit Efficiency

_20 of 24 filtered trade rows are included. 4 filtered trade rows were excluded._

#### Favorable move captured

- **Median capture:** 59.8% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 91.0%
- **Money-weighted capture:** 37.4% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $26.52 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $113.22
- **Winners with open loss above profit:** 9.1%

#### Caveats on capture

- Measured over 19 trade(s), fewer than the 30 this section treats as enough to call a figure typical.
- 1 trade(s) never moved in their favour and were left out of capture.

#### E-ratio in the first bars after entry

- **5 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 18 eligible, 2 unavailable)_
- **10 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 18 eligible, 2 unavailable)_
- **20 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 18 eligible, 2 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 3.95%
- **Maximum drawdown, money:** $407.11 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 2.5 mo
- **Average recovery:** 19d 7h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 1.23%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2023-01-03 | 0 |
| 2023-01-03 | -1.18 |
| 2023-01-25 | 0 |
| 2023-04-06 | -1.94 |
| 2023-04-28 | 0 |
| 2023-05-01 | -2.3 |
| 2023-05-29 | -0.49 |
| 2023-06-01 | -2.57 |
| 2023-06-02 | -3.95 |
| 2023-07-04 | -0.74 |
| 2023-07-04 | -1.49 |
| 2023-07-12 | 0 |
| 2023-07-27 | -0.94 |
| 2023-08-08 | 0 |
| 2023-08-29 | -1.2 |
| 2023-09-12 | -0.11 |
| 2023-09-22 | -0.53 |
| 2023-09-25 | -1.07 |
| 2023-10-11 | 0 |
| 2023-10-18 | 0 |

_20 of 63 points, shape-preserving; min -3.95% (2023-06-02), max 0.00% (2023-01-03), final 0.00% (2023-10-18)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.95% | $407.11 | 28 Apr 2023 09:00 | 02 Jun 2023 09:00 | 12 Jul 2023 09:00 | 2.5 mo | 40d | 9 | — |
| 1.94% | $198.37 | 17 Feb 2023 13:00 | 06 Apr 2023 05:00 | 06 Apr 2023 17:00 | 48d 3h | 12h | 2 | — |
| 1.20% | $125.53 | 21 Aug 2023 01:00 | 29 Aug 2023 09:00 | 12 Sep 2023 05:00 | 22d 4h | 13d 20h | 2 | — |
| 1.18% | $117.87 | 03 Jan 2023 13:00 | 03 Jan 2023 13:00 | 25 Jan 2023 13:00 | 22d | 22d | 1 | — |
| 1.07% | $112.58 | 22 Sep 2023 13:00 | 24 Sep 2023 21:00 | 05 Oct 2023 09:00 | 12d 20h | 10d 12h | 2 | — |

_Showing the 5 deepest of 10 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 24
- **Winnings:** 12/24 (50.00%)
- **Losing:** 12/24 (50.00%)
- **Long trades:** 14/24 (58.33%)
- **Short trades:** 10/24 (41.67%)
- **Profit on longs:** $379.42
- **Profit on shorts:** $610.35

## 7. Rolling Performance

_Nothing to report for the current trades and filters._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XAUUSD | 24 | 12 | 12 | 50% | 6.4 | $2,093.85 | $1,104.09 | $989.77 | 1.90 | 65.48% / 34.52% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 0 | 0.00% | --- | --- | --- | --- |
| London Session | 08:00-17:00 London time | 8 | 33.33% | $247.28 | $30.91 | 50.0% | 1.63 |
| Asian Session | 09:00-18:00 Tokyo time | 8 | 33.33% | $181.98 | $22.75 | 50.0% | 1.46 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 0 | 0.00% | --- | --- | --- | --- |
| New York Session | 08:00-17:00 New York time | 7 | 29.17% | $824.08 | $117.73 | 71.4% | 5.18 |
| Outside sessions | — | 5 | 20.83% | -$136.60 | -$27.32 | — | — |

_Shares are of the 24 trades analysed. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

_Nothing to report for the current trades and filters._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $989.77
- **Average trade:** $41.24
- **Gross profit:** $2,093.85
- **Gross loss:** $1,104.09
- **Profit / month:** $103.91
- **Average profit:** $174.49
- **Average loss:** $92.01
- **Max drawdown:** $54.48
- **Max current day loss %:** 0.38%
- **Profit factor:** 1.9
- **Return %:** 9.9%

#### Trades

- **Total trades:** 24
- **Trading days:** 23
- **Profit trades:** 12
- **Loss trades:** 12
- **Max consecutive profit trades:** 3
- **Max consecutive loss trades:** 3
- **Trades / day:** 0.08
- **Trades / month:** 2.52
- **Profit trades / month:** 1.26
- **Loss trades / month:** 1.26
- **Max profit trade:** $249.28
- **Max loss trade:** $99.94
- **Total volume traded:** $1.2m
- **Average order size:** $51.5k

#### Time

- **Days processed:** 289.92
- **Months processed:** 9.53

#### Other

- **Max lot used:** 0.55
- **Restoration factor:** 18.17
- **Reliability factor:** 1.91
- **Win rate %:** 50%
- **Loss rate %:** 50%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 0.78
- **Average win/loss ratio 1:3:** 3
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.0816
- **Monthly Sharpe Ratio:** 0.5964
- **Daily Sortino Ratio:** 0.164
- **Monthly Sortino Ratio:** 2.6873

## 13. Drawdown luck check

_Nothing to report for the current trades and filters._

## 14. Prop Challenge pass probability

_Based on 24 usable closed trades across 288 calendar days. Advanced Analytics filters affect this estimate._

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

- **Estimated pass chance within 90 days:** 4.4% _(95%: 3.3–5.9%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.1% _(95%: 0.0–0.6%)_
- **Not decided within the horizon:** 95.5% _(95%: 94.0–96.6%)_
- **Median calendar days to pass (passed attempts only):** 75
- **Median trades to pass (passed attempts only):** 8

#### Simulated account balance, Day 90

- **Median attempt:** 2.76%
- **Low outcome (5%):** -3.07%
- **High outcome (95%):** 9.46%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 5 | 0 |
| 14 | 0 |
| 18 | 0 |
| 23 | 0.53 |
| 27 | 0.84 |
| 31 | 0.96 |
| 36 | 1.02 |
| 43 | 1.19 |
| 48 | 1.56 |
| 54 | 1.61 |
| 59 | 1.89 |
| 64 | 2.01 |
| 68 | 2.05 |
| 74 | 2.22 |
| 76 | 2.41 |
| 81 | 2.59 |
| 89 | 2.76 |
| 90 | 2.76 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 2.76% (Day 89), final 2.76% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-4)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 24
- **Hours with trades:** 21

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Thursday | 16:00-17:00 | $249.28 | 1 | 100.00% |
| Wednesday | 05:00-06:00 | $247.22 | 1 | 100.00% |
| Wednesday | 15:00-16:00 | $202.25 | 1 | 100.00% |
| Tuesday | 20:00-21:00 | $202.15 | 1 | 100.00% |
| Tuesday | 02:00-03:00 | $201.28 | 1 | 100.00% |
| Tuesday | 08:00-09:00 | $195.92 | 1 | 100.00% |
| Wednesday | 08:00-09:00 | $184 | 1 | 100.00% |
| Wednesday | 03:00-04:00 | $166.18 | 1 | 100.00% |
| Tuesday | 06:00-07:00 | $121.79 | 1 | 100.00% |
| Thursday | 07:00-08:00 | $108.58 | 1 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Thursday | 03:00-04:00 | -$99.94 | 1 | 0.00% |
| Thursday | 02:00-03:00 | -$99.61 | 1 | 0.00% |
| Tuesday | 10:00-11:00 | -$98.63 | 1 | 0.00% |
| Sunday | 22:00-23:00 | -$98.03 | 1 | 0.00% |
| Sunday | 20:00-21:00 | -$97.84 | 2 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 3 | -$293.72 | -$97.91 | 0.00 | 0.00% |
| Monday | 1 | -$96.79 | -$96.79 | 0.00 | 0.00% |
| Tuesday | 7 | $603.83 | $86.26 | 5.79 | 71.43% |
| Wednesday | 4 | $799.65 | $199.91 | No loss | 100.00% |
| Thursday | 6 | $267.42 | $44.57 | 1.90 | 50.00% |
| Friday | 3 | -$290.63 | -$96.88 | 0.00 | 0.00% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2023 | 3 | $212.20 | 3 | 2 / 1 |
| February 2023 | 1 | -$98.43 | 1 | 0 / 1 |
| March 2023 | 0 | — | 0 | 0 / 0 |
| April 2023 | 4 | -$43.89 | 3 | 1 / 2 |
| May 2023 | 2 | $25.00 | 2 | 1 / 1 |
| June 2023 | 3 | $51.95 | 3 | 1 / 2 |
| July 2023 | 3 | $95.56 | 3 | 2 / 1 |
| August 2023 | 3 | $70.40 | 3 | 1 / 2 |
| September 2023 | 2 | $102.29 | 2 | 1 / 1 |
| October 2023 | 3 | $574.71 | 3 | 3 / 0 |

_A month with 0 trades had none in the filtered history._

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-4)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 0 | 0 | 0 |
| 01 | 0 | 0 | 0 |
| 02 | 1 | 2 | -1 |
| 03 | 1 | 1 | 0 |
| 04 | 0 | 0 | 0 |
| 05 | 1 | 0 | +1 |
| 06 | 1 | 0 | +1 |
| 07 | 1 | 1 | 0 |
| 08 | 3 | 2 | +1 |
| 09 | 0 | 0 | 0 |
| 10 | 0 | 3 | -3 |
| 11 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 |
| 13 | 1 | 0 | +1 |
| 14 | 0 | 0 | 0 |
| 15 | 1 | 0 | +1 |
| 16 | 1 | 0 | +1 |
| 17 | 0 | 0 | 0 |
| 18 | 0 | 0 | 0 |
| 19 | 0 | 0 | 0 |
| 20 | 1 | 2 | -1 |
| 21 | 0 | 0 | 0 |
| 22 | 0 | 1 | -1 |
| 23 | 0 | 0 | 0 |

## 18. Duration & Profitability

- **Analyzed trades:** 24
- **Net profit:** $989.77
- **Holding-time ranges:** 5
- **Median holding time:** 3h 59m

#### Key insights

- **Winner vs loser holding time:** The median losing trade was held 1.1x longer than the median winning trade. Winner median: 3h 59m; loser median: 4h 27m.
- **Profit concentration:** Your top 5% of trades generated 23.7% of your total winning profit.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 2 | 0 | 2 | 0 | 0.0% | -$198.37 | -$99.19 | -$99.19 |
| 1h-4h | 11 | 7 | 4 | 0 | 63.6% | $948.63 | $86.24 | $121.79 |
| 4h-8h | 3 | 0 | 3 | 0 | 0.0% | -$293.67 | -$97.89 | -$97.27 |
| 8h-1d | 7 | 5 | 2 | 0 | 71.4% | $632.17 | $90.31 | $166.18 |
| 1d-3d | 1 | 0 | 1 | 0 | 0.0% | -$98.99 | -$98.99 | -$98.99 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$250 | 0 |
| -$250 to -$200 | 0 |
| -$200 to -$150 | 0 |
| -$150 to -$100 | 0 |
| -$100 to -$50 | 11 |
| -$50 to $0 | 1 |
| $0 to $50 | 1 |
| $50 to $100 | 0 |
| $100 to $150 | 2 |
| $150 to $200 | 3 |
| $200 to $250 | 6 |
| >$250 | 0 |

_Average $41.24; median -$9.34_

#### Holding time by outcome

| Holding time | Loss | Breakeven | Win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 100.0% (2) | 0.0% (0) | 0.0% (0) | 2 | 0.0% | -$99.19 | -$198.37 | $1,188.14 (22) |
| 1h-4h | 36.4% (4) | 0.0% (0) | 63.6% (7) | 11 | 63.6% | $86.24 | $948.63 | $239.51 (11) |
| 4h-8h | 100.0% (3) | 0.0% (0) | 0.0% (0) | 3 | 0.0% | -$97.89 | -$293.67 | $533.18 (8) |
| 8h-1d | 28.6% (2) | 14.3% (1) | 57.1% (4) | 7 | 71.4% | $90.31 | $632.17 | -$98.99 (1) |
| 1d-3d | 100.0% (1) | 0.0% (0) | 0.0% (0) | 1 | 0.0% | -$98.99 | -$98.99 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
