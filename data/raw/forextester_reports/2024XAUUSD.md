# Advanced Analytics

_Project: 20EMA-5m_  
_Generated: 2026-10-09 15:24 UTC_  
_Trades analysed: 22_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 22 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $76.46 _(net profit divided by the number of closed trades)_
- **Total PnL:** $1,682.21
- **Drawdown:** $230.89 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $11,682.21
- **Balance:** $11,682.22
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 59.09%
- **Avg Result / Trade:** $76.46
- **Profit Factor:** 2.91
- **Profitability:** 16.82% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-02 | 10000 |
| 2024-01-03 | 10124.08 |
| 2024-01-05 | 10026.57 |
| 2024-01-08 | 10277.82 |
| 2024-01-11 | 10488.52 |
| 2024-01-23 | 10389.71 |
| 2024-01-29 | 10291.8 |
| 2024-02-20 | 10764.06 |
| 2024-02-22 | 10664.66 |
| 2024-03-13 | 11016.83 |
| 2024-03-19 | 11223.8 |
| 2024-03-26 | 11125.86 |
| 2024-04-09 | 10932.13 |
| 2024-04-30 | 11135.61 |
| 2024-05-06 | 11335.43 |
| 2024-05-07 | 11238.36 |
| 2024-05-17 | 11354.84 |
| 2024-05-29 | 11551.8 |
| 2024-06-06 | 11779.46 |
| 2024-06-11 | 11682.22 |

_20 of 23 points, shape-preserving; min $10,000.00 (2024-01-02), max $11,779.46 (2024-06-06), final $11,682.22 (2024-06-11)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-02 | 0 |
| 2024-01-03 | 124.08 |
| 2024-01-05 | 26.57 |
| 2024-01-08 | 277.82 |
| 2024-01-11 | 488.52 |
| 2024-01-23 | 389.71 |
| 2024-01-29 | 291.8 |
| 2024-02-20 | 764.06 |
| 2024-02-22 | 664.66 |
| 2024-03-13 | 1016.83 |
| 2024-03-19 | 1223.8 |
| 2024-03-26 | 1125.86 |
| 2024-04-09 | 932.13 |
| 2024-04-30 | 1135.61 |
| 2024-05-06 | 1335.43 |
| 2024-05-07 | 1238.36 |
| 2024-05-17 | 1354.84 |
| 2024-05-29 | 1551.8 |
| 2024-06-06 | 1779.46 |
| 2024-06-11 | 1682.22 |

_20 of 23 points, shape-preserving; min $0.00 (2024-01-02), max $1,779.46 (2024-06-06), final $1,682.22 (2024-06-11)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-02 | 0 |
| 2024-01-03 | 0 |
| 2024-01-05 | -97.51 |
| 2024-01-08 | 0 |
| 2024-01-11 | 0 |
| 2024-01-23 | -98.81 |
| 2024-01-29 | -196.72 |
| 2024-02-20 | 0 |
| 2024-02-22 | -99.41 |
| 2024-03-13 | 0 |
| 2024-03-19 | 0 |
| 2024-03-26 | -97.94 |
| 2024-04-09 | -291.67 |
| 2024-04-30 | -88.19 |
| 2024-05-06 | 0 |
| 2024-05-07 | -97.07 |
| 2024-05-17 | 0 |
| 2024-05-29 | 0 |
| 2024-06-06 | 0 |
| 2024-06-11 | -97.24 |

_20 of 23 points, shape-preserving; min -$291.67 (2024-04-09), max $0.00 (2024-01-02), final -$97.24 (2024-06-11)._

## 2. Analytics Insights

_You need at least 30 trades for more precise recommendations. Keep testing — the more data we have, the smarter your analytics become._

#### Overview

- **Net profit:** $1,682.22
- **Trades analysed:** 22
- **Score:** 14 of 40 points
- **Tests:** 14 passed, 6 failed
- **Total potential improvement:** $115.91 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 1h 52m
- **Trading period:** 0 years, 5 months, 7 days

#### Behavioural strengths

- Effective Risk Management
- Adaptable
- Emotional Control

#### Behavioural weaknesses

- Overconfidence Bias
- Poor Strategic Planning
- Loss Aversion Bias

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Make your position sizing consistent first

Your risk per trade is below 1% of your balance, but this history also has positions far above your typical size. That is a risk to the account, so the advice to increase your lot waits until your position sizing is consistent.

Recommendations:
- First, use one consistent formula for your position sizes (see the position sizing check). Once the oversized trades are gone, consider raising your risk per trade toward 1%.

#### ❌ Consider keeping position size after winning streaks (potential improvement +$115.91)

Your results indicate that increasing lot size after winning streaks has been harmful historically.

Recommendations:
- Historical analysis shows you could improve net profit by $115.91 (6.9%) by keeping your position size unchanged after winning streaks.

Trades behind this verdict: 6.

#### ❌ Try using time-based exit rules or trailing stops

You have trades held significantly longer than your average.

Recommendations:
- Implement time-based exit rules or trailing stops to prevent holding trades beyond their optimal duration. Consider setting maximum holding periods based on your typical profitable trade duration.

#### ❌ Try maintaining consistent position sizes

We've detected trades with position sizes significantly larger than your typical size. Such inconsistencies can lead to oversized losses and often suggest emotional decision-making.

Recommendations:
- Develop and stick to a position sizing formula based on your account risk percentage. Avoid emotional trading that leads to sudden position size increases.

#### ❌ Try setting initial Reward:Risk above 2:1

Your Reward:Risk ratios need improvement.

Recommendations:
- Set your take profit targets at least twice as far from entry as your stop loss. This ensures favorable risk-reward even with lower win rates.

#### ❌ Try to reduce your maximum drawdown

Your worst drawdown relative to profit is 78.58%, which is too high. Your deepest drawdown in money ($291.67) happened at a different time.

Recommendations:
- Review trades during drawdown periods to identify patterns. Consider reducing position sizes when certain drawdown level is reached, implementing portfolio heat limits, or using systematic risk reduction during losing streaks.

Trades behind this verdict: 2.

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
- ✅ Direction bias analysis
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### XAUUSD: best exit parameters (based on 22 trades)

- **Stop loss:** 2404.1 pips _(average loss as traded: 369.1 pips)_
- **Take profit:** 1195.4 pips _(average profit as traded: 722.2 pips)_
- **Max holding:** 13h 10m _(median holding as traded: 1h 52m)_

#### XAUUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $1,576.58 | $1,682.22 |
| Profit factor | 6.97 | 2.91 |
| Win rate | 83.33% | 59.09% |
| Expected value per trade | $262.76 | $76.46 |
| Net result in display units | 5176.3 pips | 6066.7 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### XAUUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2404.1 pips | 1195.4 pips | 13h 10m | $1,576.58 | 83.33% | 6.97 |
| 2 | none | 1195.4 pips | 13h 10m | $1,576.58 | 83.33% | 6.97 |
| 3 | 2404.1 pips | 1072.7 pips | 13h 10m | $1,387.63 | 83.33% | 6.25 |
| 4 | none | 1072.7 pips | 13h 10m | $1,387.63 | 83.33% | 6.25 |
| 5 | 2404.1 pips | 1195.4 pips | 14h 10m | $1,385.51 | 83.33% | 4.04 |
| 6 | none | 1195.4 pips | 14h 10m | $1,385.51 | 83.33% | 4.04 |
| 7 | 2404.1 pips | 954.2 pips | 13h 10m | $1,205.14 | 83.33% | 5.56 |
| 8 | none | 954.2 pips | 13h 10m | $1,205.14 | 83.33% | 5.56 |
| 9 | 2404.1 pips | 1453.0 pips | 13h 10m | $1,203.61 | 66.67% | 2.79 |
| 10 | none | 1453.0 pips | 13h 10m | $1,203.61 | 66.67% | 2.79 |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### XAUUSD: net profit vs stop loss (TP fixed at 1195.4 pips, holding at 13h 10m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 47.6 | -89.11 |
| 107.9 | -201.87 |
| 183.2 | 911.84 |
| 270.2 | 828.32 |
| 367.2 | 735.2 |
| 472.9 | 633.73 |
| 586.4 | 1005.86 |
| 707.1 | 922.57 |
| 834.5 | 834.67 |
| 968.2 | 742.41 |
| 1107.7 | 646.16 |
| 1252.7 | 546.11 |
| 1403 | 442.4 |
| 1558.3 | 335.25 |
| 1718.5 | 224.71 |
| 1883.3 | 468.25 |
| 2052.7 | 407.27 |
| 2226.3 | 344.77 |
| 2404.1 | 1576.58 |

_min -$201.87 (107.9), max $1,576.58 (2404.1), final $1,576.58 (2404.1)._

#### XAUUSD: net profit vs take profit (SL fixed at 2404.1 pips, holding at 13h 10m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 59.6 | 111.35 |
| 88.7 | 165.77 |
| 137.9 | 257.77 |
| 199.4 | 372.78 |
| 270.4 | 505.55 |
| 349.6 | 653.65 |
| 435.9 | 406.95 |
| 528.6 | 549.71 |
| 627.2 | 701.56 |
| 731.2 | 861.72 |
| 840.4 | 1029.88 |
| 954.2 | 1205.14 |
| 1072.7 | 1387.63 |
| 1195.4 | 1576.58 |
| 1322.2 | 1034.88 |
| 1453 | 1203.61 |
| 1587.6 | 953.29 |
| 1725.9 | 833.13 |
| 1867.6 | 358.78 |
| 2012.8 | 397.98 |

_min $111.35 (59.6), max $1,576.58 (1195.4), final $397.98 (2012.8)._

#### XAUUSD: net profit vs max holding (SL fixed at 2404.1 pips, TP fixed at 1195.4 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 42m | 29.47 |
| 54m | -1.02 |
| 1h 14m | 244.24 |
| 1h 40m | 195.54 |
| 2h 9m | 144.62 |
| 2h 42m | 65.89 |
| 3h 17m | -33.88 |
| 3h 56m | -173.21 |
| 4h 37m | 41.1 |
| 5h 20m | 271.61 |
| 6h 5m | 185.68 |
| 6h 52m | 429.5 |
| 7h 41m | 221.4 |
| 8h 32m | 71.54 |
| 9h 24m | 282.45 |
| 10h 18m | 573.89 |
| 11h 14m | 381.06 |
| 12h 11m | 1151.7 |
| 13h 10m | 1576.58 |
| 14h 10m | 1385.51 |

_min -$173.21 (3h 56m), max $1,576.58 (13h 10m), final $1,385.51 (14h 10m)._

## 4. Entry / Exit Efficiency

_22 of 22 filtered trade rows are included._

#### Favorable move captured

- **Median capture:** 76.9% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 92.5%
- **Money-weighted capture:** 53.9% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $46.36 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $98.68
- **Winners with open loss above profit:** 0.0%

#### Caveats on capture

- Measured over 20 trade(s), fewer than the 30 this section treats as enough to call a figure typical.
- 2 trade(s) never moved in their favour and were left out of capture.

#### E-ratio in the first bars after entry

- **5 bars:** — _(fewer than 30 measurable trades, so no ratio is shown; 0 eligible, 22 unavailable)_
- **10 bars:** — _(fewer than 30 measurable trades, so no ratio is shown; 0 eligible, 22 unavailable)_
- **20 bars:** — _(fewer than 30 measurable trades, so no ratio is shown; 0 eligible, 22 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 2.60%
- **Maximum drawdown, money:** $291.67 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 41d 4h
- **Average recovery:** 13d 20h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 1.03%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-03 | 0 |
| 2024-01-05 | -0.96 |
| 2024-01-08 | -0.01 |
| 2024-01-11 | -0.4 |
| 2024-01-23 | -0.13 |
| 2024-01-29 | -1.88 |
| 2024-01-31 | -0.64 |
| 2024-01-31 | 0 |
| 2024-02-22 | -0.92 |
| 2024-03-13 | -1.19 |
| 2024-03-19 | 0 |
| 2024-03-26 | -0.87 |
| 2024-04-09 | -2.6 |
| 2024-04-29 | -2.6 |
| 2024-04-30 | -0.79 |
| 2024-05-06 | 0 |
| 2024-05-17 | 0 |
| 2024-05-29 | 0 |
| 2024-06-06 | 0 |
| 2024-06-11 | -0.83 |

_20 of 39 points, shape-preserving; min -2.60% (2024-04-09), max 0.00% (2024-01-03), final -0.83% (2024-06-11)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.60% | $291.67 | 26 Mar 2024 01:00 | 09 Apr 2024 17:00 | 06 May 2024 05:00 | 41d 4h | 26d 12h | 4 | — |
| 1.88% | $196.72 | 23 Jan 2024 17:00 | 29 Jan 2024 13:00 | 31 Jan 2024 13:00 | 7d 20h | 2d | 3 | — |
| 1.19% | $128.37 | 22 Feb 2024 01:00 | 13 Mar 2024 09:00 | 13 Mar 2024 13:00 | 20d 11h | 4h | 0 | — |
| 0.96% | $97.51 | 05 Jan 2024 01:00 | 05 Jan 2024 01:00 | 08 Jan 2024 09:00 | 3d 8h | 3d 8h | 1 | — |
| 0.86% | $97.07 | 07 May 2024 05:00 | 07 May 2024 05:00 | 17 May 2024 09:00 | 10d 4h | 10d 4h | 0 | — |

_Showing the 5 deepest of 7 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 22
- **Winnings:** 13/22 (59.09%)
- **Losing:** 9/22 (40.91%)
- **Long trades:** 12/22 (54.55%)
- **Short trades:** 10/22 (45.45%)
- **Profit on longs:** $1,185.00
- **Profit on shorts:** $497.22

## 7. Rolling Performance

_Nothing to report for the current trades and filters._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XAUUSD | 22 | 13 | 9 | 59.09% | 7.1 | $2,561.83 | $879.61 | $1,682.22 | 2.91 | 74.44% / 25.56% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 4 | 18.18% | $516.19 | $129.05 | 75.0% | 6.32 |
| London Session | 08:00-17:00 London time | 9 | 40.91% | $904.46 | $100.50 | 66.7% | 4.08 |
| Asian Session | 09:00-18:00 Tokyo time | 14 | 63.64% | $1,284.63 | $91.76 | 64.3% | 3.63 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 1 | 4.55% | $115.90 | $115.90 | 100.0% | --- |
| New York Session | 08:00-17:00 New York time | 6 | 27.27% | $379.48 | $63.25 | 50.0% | 2.30 |
| Outside sessions | — | 0 | 0.00% | $0.00 | — | — | — |

_Shares are of the 22 trades analysed. Sessions overlap: 22 trades are counted 34 times in total, because a trade opened while two sessions run counts in both. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

_Nothing to report for the current trades and filters._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $1,682.22
- **Average trade:** $76.46
- **Gross profit:** $2,561.83
- **Gross loss:** $879.61
- **Profit / month:** $302.43
- **Average profit:** $197.06
- **Average loss:** $97.73
- **Max drawdown:** $230.89
- **Max current day loss %:** 0%
- **Profit factor:** 2.91
- **Return %:** 16.82%

#### Trades

- **Total trades:** 22
- **Trading days:** 22
- **Profit trades:** 13
- **Loss trades:** 9
- **Max consecutive profit trades:** 4
- **Max consecutive loss trades:** 3
- **Trades / day:** 0.13
- **Trades / month:** 3.96
- **Profit trades / month:** 2.34
- **Loss trades / month:** 1.62
- **Max profit trade:** $352.18
- **Max loss trade:** $99.41
- **Total volume traded:** $1.5m
- **Average order size:** $69.1k

#### Time

- **Days processed:** 169.3
- **Months processed:** 5.56

#### Other

- **Max lot used:** 0.68
- **Restoration factor:** 7.29
- **Reliability factor:** 1.31
- **Win rate %:** 59.09%
- **Loss rate %:** 40.91%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 1.5
- **Average win/loss ratio 1:3:** 2
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.1866
- **Monthly Sharpe Ratio:** 1.2569
- **Daily Sortino Ratio:** 0.4756
- **Monthly Sortino Ratio:** N/A

## 13. Drawdown luck check

_Nothing to report for the current trades and filters._

## 14. Prop Challenge pass probability

_Based on 22 usable closed trades across 161 calendar days. Advanced Analytics filters affect this estimate._

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

- **Estimated pass chance within 90 days:** 48.6% _(95%: 45.5–51.7%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Not decided within the horizon:** 51.4% _(95%: 48.3–54.5%)_
- **Median calendar days to pass (passed attempts only):** 64
- **Median trades to pass (passed attempts only):** 9

#### Simulated account balance, Day 90

- **Median attempt:** 9.53%
- **Low outcome (5%):** 1.72%
- **High outcome (95%):** 12.04%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 4 | 0 |
| 8 | 0.07 |
| 10 | 0.76 |
| 18 | 1.73 |
| 22 | 1.88 |
| 25 | 2.15 |
| 33 | 3.08 |
| 36 | 3.63 |
| 41 | 4.06 |
| 45 | 4.74 |
| 53 | 5.37 |
| 58 | 6.06 |
| 62 | 6.34 |
| 66 | 6.71 |
| 70 | 7.26 |
| 79 | 8.01 |
| 83 | 8.65 |
| 86 | 8.94 |
| 90 | 9.53 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 9.53% (Day 90), final 9.53% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-4)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 22
- **Hours with trades:** 21

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Wednesday | 13:00-14:00 | $352.18 | 1 | 100.00% |
| Wednesday | 09:00-10:00 | $292.22 | 1 | 100.00% |
| Monday | 06:00-07:00 | $251.24 | 1 | 100.00% |
| Thursday | 08:00-09:00 | $210.7 | 1 | 100.00% |
| Tuesday | 04:00-05:00 | $206.96 | 1 | 100.00% |
| Monday | 22:00-23:00 | $203.48 | 1 | 100.00% |
| Monday | 03:00-04:00 | $199.82 | 1 | 100.00% |
| Wednesday | 05:00-06:00 | $196.97 | 1 | 100.00% |
| Tuesday | 01:00-02:00 | $180.04 | 1 | 100.00% |
| Wednesday | 04:00-05:00 | $124.08 | 1 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Wednesday | 22:00-23:00 | -$99.41 | 1 | 0.00% |
| Tuesday | 18:00-19:00 | -$98.81 | 1 | 0.00% |
| Friday | 08:00-09:00 | -$98.38 | 1 | 0.00% |
| Monday | 23:00-00:00 | -$97.94 | 1 | 0.00% |
| Monday | 11:00-12:00 | -$97.91 | 1 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 0 | $0 | — | N/A | N/A |
| Monday | 5 | $458.7 | $91.74 | 3.34 | 60.00% |
| Tuesday | 6 | -$1.46 | -$0.24 | 1.00 | 33.33% |
| Wednesday | 6 | $977.79 | $162.97 | 10.84 | 83.33% |
| Thursday | 3 | $229.09 | $76.36 | 3.35 | 66.67% |
| Friday | 2 | $18.11 | $9.05 | 1.18 | 50.00% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 7 | $584.02 | 7 | 4 / 3 |
| February 2024 | 2 | $80.64 | 2 | 1 / 1 |
| March 2024 | 3 | $461.20 | 3 | 2 / 1 |
| April 2024 | 3 | $9.75 | 3 | 1 / 2 |
| May 2024 | 4 | $416.20 | 4 | 3 / 1 |
| June 2024 | 3 | $130.41 | 3 | 2 / 1 |

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-4)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 1 | 0 | +1 |
| 01 | 1 | 0 | +1 |
| 02 | 0 | 0 | 0 |
| 03 | 1 | 2 | -1 |
| 04 | 2 | 0 | +2 |
| 05 | 1 | 0 | +1 |
| 06 | 1 | 0 | +1 |
| 07 | 0 | 0 | 0 |
| 08 | 1 | 1 | 0 |
| 09 | 2 | 0 | +2 |
| 10 | 0 | 0 | 0 |
| 11 | 1 | 1 | 0 |
| 12 | 0 | 0 | 0 |
| 13 | 1 | 1 | 0 |
| 14 | 0 | 0 | 0 |
| 15 | 0 | 0 | 0 |
| 16 | 0 | 0 | 0 |
| 17 | 0 | 0 | 0 |
| 18 | 0 | 1 | -1 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |
| 21 | 0 | 0 | 0 |
| 22 | 1 | 2 | -1 |
| 23 | 0 | 1 | -1 |

## 18. Duration & Profitability

- **Analyzed trades:** 22
- **Net profit:** $1,682.22
- **Holding-time ranges:** 4
- **Median holding time:** 1h 52m

#### Key insights

- **Winner vs loser holding time:** The median winning trade was held 3.7x longer than the median losing trade. Winner median: 3h 49m; loser median: 1h 1m.
- **Profit concentration:** Your top 5% of trades generated 25.2% of your total winning profit.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 4 | 0 | 4 | 0 | 0.0% | -$390.43 | -$97.61 | -$97.71 |
| 1h-4h | 13 | 8 | 5 | 0 | 61.5% | $762.83 | $58.68 | $115.9 |
| 4h-8h | 4 | 4 | 0 | 0 | 100.0% | $1,099.12 | $274.78 | $271.73 |
| 8h-1d | 1 | 1 | 0 | 0 | 100.0% | $210.7 | $210.7 | $210.7 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$400 | 0 |
| -$400 to -$300 | 0 |
| -$300 to -$200 | 0 |
| -$200 to -$100 | 0 |
| -$100 to $0 | 9 |
| $0 to $100 | 0 |
| $100 to $200 | 7 |
| $200 to $300 | 5 |
| $300 to $400 | 1 |
| >$400 | 0 |

_Average $76.46; median $116.19_

#### Holding time by outcome

| Holding time | Loss | Win | Big win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 100.0% (4) | 0.0% (0) | 0.0% (0) | 4 | 0.0% | -$97.61 | -$390.43 | $2,072.65 (18) |
| 1h-4h | 38.5% (5) | 61.5% (8) | 0.0% (0) | 13 | 61.5% | $58.68 | $762.83 | $1,309.82 (5) |
| 4h-8h | 0.0% (0) | 75.0% (3) | 25.0% (1) | 4 | 100.0% | $274.78 | $1,099.12 | $210.7 (1) |
| 8h-1d | 0.0% (0) | 100.0% (1) | 0.0% (0) | 1 | 100.0% | $210.7 | $210.7 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
