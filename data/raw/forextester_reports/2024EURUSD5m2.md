# Advanced Analytics

_Project: 6/22 EMA_  
_Generated: 2026-10-09 15:44 UTC_  
_Trades analysed: 19_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 19 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $60.75 _(net profit divided by the number of closed trades)_
- **Total PnL:** $1,154.19
- **Drawdown:** $154.12 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $11,154.19
- **Balance:** $11,154.19
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 63.16%
- **Avg Result / Trade:** $60.75
- **Profit Factor:** 2.57
- **Profitability:** 11.54% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-08 | 10000 |
| 2024-01-09 | 10132.48 |
| 2024-03-28 | 10242.73 |
| 2024-04-12 | 10524.97 |
| 2024-04-25 | 10651.23 |
| 2024-05-23 | 10544.73 |
| 2024-08-08 | 10658.21 |
| 2024-08-09 | 10545.33 |
| 2024-09-24 | 10746.34 |
| 2024-11-07 | 10645.35 |
| 2025-01-13 | 10543.7 |
| 2025-02-14 | 10699.13 |
| 2025-02-26 | 10597.07 |
| 2025-03-04 | 10716.14 |
| 2025-03-17 | 10887.08 |
| 2025-05-08 | 11077.46 |
| 2025-06-02 | 11237.62 |
| 2025-06-26 | 11135.02 |
| 2025-09-17 | 11027.14 |
| 2025-10-06 | 11154.19 |

_min $10,000.00 (2024-01-08), max $11,237.62 (2025-06-02), final $11,154.19 (2025-10-06)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-08 | 0 |
| 2024-01-09 | 132.48 |
| 2024-03-28 | 242.73 |
| 2024-04-12 | 524.97 |
| 2024-04-25 | 651.23 |
| 2024-05-23 | 544.73 |
| 2024-08-08 | 658.21 |
| 2024-08-09 | 545.33 |
| 2024-09-24 | 746.34 |
| 2024-11-07 | 645.35 |
| 2025-01-13 | 543.7 |
| 2025-02-14 | 699.13 |
| 2025-02-26 | 597.07 |
| 2025-03-04 | 716.14 |
| 2025-03-17 | 887.08 |
| 2025-05-08 | 1077.46 |
| 2025-06-02 | 1237.62 |
| 2025-06-26 | 1135.02 |
| 2025-09-17 | 1027.14 |
| 2025-10-06 | 1154.19 |

_min $0.00 (2024-01-08), max $1,237.62 (2025-06-02), final $1,154.19 (2025-10-06)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-08 | 0 |
| 2024-01-09 | 0 |
| 2024-03-28 | 0 |
| 2024-04-12 | 0 |
| 2024-04-25 | 0 |
| 2024-05-23 | -106.5 |
| 2024-08-08 | 0 |
| 2024-08-09 | -112.88 |
| 2024-09-24 | 0 |
| 2024-11-07 | -100.98 |
| 2025-01-13 | -202.64 |
| 2025-02-14 | -47.2 |
| 2025-02-26 | -149.26 |
| 2025-03-04 | -30.2 |
| 2025-03-17 | 0 |
| 2025-05-08 | 0 |
| 2025-06-02 | 0 |
| 2025-06-26 | -102.61 |
| 2025-09-17 | -210.49 |
| 2025-10-06 | -83.44 |

_min -$210.49 (2025-09-17), max $0.00 (2024-01-08), final -$83.44 (2025-10-06)._

## 2. Analytics Insights

_You need at least 30 trades for more precise recommendations. Keep testing — the more data we have, the smarter your analytics become._

#### Overview

- **Net profit:** $1,154.19
- **Trades analysed:** 19
- **Score:** 15 of 40 points
- **Tests:** 15 passed, 5 failed
- **Total potential improvement:** $549.93 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 5h 55m
- **Trading period:** 1 year, 8 months, 26 days

#### Behavioural strengths

- Adaptable
- Emotional Control
- Effective Stress Management

#### Behavioural weaknesses

- Poor Strategic Planning
- Lack Of Discipline
- Inconsistent Execution

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Consider cautiously increasing position size after winning streaks (potential improvement +$549.93)

You sometimes increase risk after winning streaks, but analysis suggests a more strategic approach (what-if scenarios) could improve results.

Recommendations:
- Historical analysis shows you could improve net profit by $549.93 (47.6%) by doubling position size after 2 consecutive wins until the next loss. Note: This significantly increases risk.

Trades behind this verdict: 4.

#### ❌ Try using time-based exit rules or trailing stops

You have trades held significantly longer than your average.

Recommendations:
- Implement time-based exit rules or trailing stops to prevent holding trades beyond their optimal duration. Consider setting maximum holding periods based on your typical profitable trade duration.

#### ❌ Try risking the same amount on every trade

You have trades with abnormally large losses.

Recommendations:
- We've identified trades with losses significantly larger than your typical losing trade. Implement stricter risk management rules including maximum loss limits per trade, volatility-based position sizing to ensure that no single trade can disproportionately damage your account balance.

Trades behind this verdict: 1.

#### ❌ Try aiming for better Reward:Risk ratios

Your Reward:Risk ratios need improvement.

Recommendations:
- Set your take profit targets at least twice as far from entry as your stop loss. This ensures favorable risk-reward even with lower win rates.
- Manage open positions to achieve better reward:risk outcomes. Let winners run to target and cut losses at predetermined stops rather than closing early.

#### ❌ Try to reduce your maximum drawdown

Your worst drawdown relative to profit is 27.15%, which is too high. Your deepest drawdown in money ($210.49) happened at a different time.

Recommendations:
- Review trades during drawdown periods to identify patterns. Consider reducing position sizes when certain drawdown level is reached, implementing portfolio heat limits, or using systematic risk reduction during losing streaks.

Trades behind this verdict: 3.

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
- ✅ Appropriate stop loss placement
- ✅ Consistent position sizing
- ✅ Direction bias analysis
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### EURUSD: best exit parameters (based on 19 trades)

- **Stop loss:** 13.9 pips _(average loss as traded: 20.8 pips)_
- **Take profit:** 357.1 pips _(average profit as traded: 29.1 pips)_
- **Max holding:** 3d 6h 40m _(median holding as traded: 5h 55m)_

#### EURUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $3,522.06 | $1,154.19 |
| Profit factor | — | 2.57 |
| Win rate | 100% | 63.16% |
| Expected value per trade | $880.51 | $60.75 |
| Net result in display units | 723.3 pips | 202.8 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### EURUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 13.9 pips | 357.1 pips | 3d 6h 40m | $3,522.06 | 100% | — |
| 2 | 14.7 pips | 357.1 pips | 3d 6h 40m | $3,522.06 | 100% | — |
| 3 | none | 357.1 pips | 3d 6h 40m | $3,522.06 | 100% | — |
| 4 | 13.9 pips | 330.7 pips | 3d 6h 40m | $3,450.78 | 100% | — |
| 5 | 14.7 pips | 330.7 pips | 3d 6h 40m | $3,450.78 | 100% | — |
| 6 | none | 330.7 pips | 3d 6h 40m | $3,450.78 | 100% | — |
| 7 | 13.9 pips | 124.1 pips | 3d 13h 45m | $3,422.18 | 100% | — |
| 8 | 13.9 pips | 124.1 pips | 3d 21h 2m | $3,422.18 | 100% | — |
| 9 | 13.9 pips | 124.1 pips | 4d 4h 29m | $3,422.18 | 100% | — |
| 10 | 13.9 pips | 124.1 pips | 4d 12h 8m | $3,422.18 | 100% | — |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### EURUSD: net profit vs stop loss (TP fixed at 357.1 pips, holding at 3d 6h 40m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 3.3 | -119.54 |
| 3.5 | -125.1 |
| 3.8 | -133.44 |
| 4.2 | -144.56 |
| 4.6 | -155.68 |
| 5 | -166.8 |
| 5.5 | 798.32 |
| 6.1 | 1589.24 |
| 6.6 | 2119.9 |
| 7.3 | 2110.38 |
| 7.9 | 2102.22 |
| 8.6 | 2092.7 |
| 9.2 | 2084.54 |
| 10 | 2073.66 |
| 10.7 | 2064.14 |
| 11.5 | 2053.26 |
| 12.3 | 2042.38 |
| 13.1 | 2031.5 |
| 13.9 | 3522.06 |
| 14.7 | 3522.06 |

_min -$166.80 (5), max $3,522.06 (13.9), final $3,522.06 (14.7)._

#### EURUSD: net profit vs take profit (SL fixed at 13.9 pips, holding at 3d 6h 40m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 2 | 27.8 |
| 7.3 | 175.14 |
| 16.2 | 422.56 |
| 27.4 | 733.92 |
| 40.3 | 1092.54 |
| 54.7 | 1492.86 |
| 70.4 | 1929.32 |
| 87.3 | 2399.14 |
| 105.2 | 2577.21 |
| 124.1 | 2581.74 |
| 143.9 | 2710.44 |
| 164.6 | 2844.99 |
| 186.2 | 2985.39 |
| 208.5 | 3130.34 |
| 231.5 | 3279.84 |
| 255.3 | 3247.2 |
| 279.8 | 3313.35 |
| 304.9 | 3381.12 |
| 330.7 | 3450.78 |
| 357.1 | 3522.06 |

_min $27.80 (2), max $3,522.06 (357.1), final $3,522.06 (357.1)._

#### EURUSD: net profit vs max holding (SL fixed at 13.9 pips, TP fixed at 357.1 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 5h 24m | 738.21 |
| 6h 55m | 583.47 |
| 9h 30m | 587.3 |
| 12h 44m | 933.04 |
| 16h 28m | 1213.47 |
| 20h 38m | 1360.55 |
| 1d 1h 10m | 1432.67 |
| 1d 6h 2m | 1408.28 |
| 1d 11h 13m | 1065.38 |
| 1d 16h 41m | 1291.31 |
| 1d 22h 26m | 1464.51 |
| 2d 4h 25m | 1514.27 |
| 2d 10h 39m | 2609.28 |
| 2d 17h 6m | 3146.35 |
| 2d 23h 47m | 3095.13 |
| 3d 6h 40m | 3522.06 |
| 3d 13h 45m | 3237.58 |
| 3d 21h 2m | 3239.04 |
| 4d 4h 29m | 2849.63 |
| 4d 12h 8m | 2360.08 |

_min $583.47 (6h 55m), max $3,522.06 (3d 6h 40m), final $2,360.08 (4d 12h 8m)._

## 4. Entry / Exit Efficiency

_16 of 19 filtered trade rows are included. 3 filtered trade rows were excluded._

#### Favorable move captured

- **Median capture:** 87.2% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 95.1%
- **Money-weighted capture:** 46.3% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $24.23 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $97.91
- **Winners with open loss above profit:** 0.0%

#### Caveats on capture

- Measured over 16 trade(s), fewer than the 30 this section treats as enough to call a figure typical.

#### E-ratio in the first bars after entry

- **5 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 16 eligible, 0 unavailable)_
- **10 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 16 eligible, 0 unavailable)_
- **20 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 16 eligible, 0 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 2.37%
- **Maximum drawdown, money:** $256.10 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 5.5 mo
- **Average recovery:** 59d 20h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 1.01%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-09 | 0 |
| 2024-03-27 | -0.72 |
| 2024-03-28 | -0.01 |
| 2024-04-12 | -0.13 |
| 2024-04-25 | 0 |
| 2024-05-22 | 0 |
| 2024-05-23 | -2.06 |
| 2024-09-24 | -1.53 |
| 2024-11-06 | 0 |
| 2024-11-07 | -1.43 |
| 2025-01-13 | -2.37 |
| 2025-02-26 | -0.44 |
| 2025-02-26 | -1.88 |
| 2025-03-04 | -0.77 |
| 2025-03-17 | -0.97 |
| 2025-03-17 | 0 |
| 2025-05-08 | -0.4 |
| 2025-06-26 | 0 |
| 2025-09-17 | -2.21 |
| 2025-10-06 | -1.08 |

_20 of 55 points, shape-preserving; min -2.37% (2025-01-13), max 0.00% (2024-01-09), final -1.08% (2025-10-06)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.37% | $256.10 | 07 Nov 2024 01:00 | 13 Jan 2025 17:00 | 17 Mar 2025 13:00 | 4.3 mo | 2.1 mo | 6 | — |
| 2.21% | $248.93 | 26 Jun 2025 17:00 | 17 Sep 2025 17:00 | Not recovered | 3.3 mo | — | 3 | — |
| 2.06% | $221.99 | 22 May 2024 21:00 | 23 May 2024 09:00 | 06 Nov 2024 17:00 | 5.5 mo | 5.5 mo | 4 | — |
| 0.72% | $72.75 | 27 Mar 2024 17:00 | 27 Mar 2024 17:00 | 28 Mar 2024 05:00 | 12h | 12h | 1 | — |
| 0.40% | $44.08 | 08 May 2025 09:00 | 08 May 2025 09:00 | 08 May 2025 13:00 | 4h | 4h | 1 | — |

_Showing the 5 deepest of 6 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 19
- **Winnings:** 12/19 (63.16%)
- **Losing:** 7/19 (36.84%)
- **Long trades:** 11/19 (57.89%)
- **Short trades:** 8/19 (42.11%)
- **Profit on longs:** $620.92
- **Profit on shorts:** $533.27

## 7. Rolling Performance

_Nothing to report for the current trades and filters._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 19 | 12 | 7 | 63.16% | 12.3 | $1,888.76 | $734.57 | $1,154.19 | 2.57 | 72.00% / 28.00% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 0 | 0.00% | --- | --- | --- | --- |
| London Session | 08:00-17:00 London time | 6 | 31.58% | $677.27 | $112.88 | 83.3% | 7.66 |
| Asian Session | 09:00-18:00 Tokyo time | 6 | 31.58% | $760.44 | $126.74 | 83.3% | 7.74 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 2 | 10.53% | $30.82 | $15.41 | 50.0% | 1.30 |
| New York Session | 08:00-17:00 New York time | 11 | 57.89% | $112.06 | $10.19 | 45.5% | 1.18 |
| Outside sessions | — | 1 | 5.26% | $126.26 | $126.26 | — | — |

_Shares are of the 19 trades analysed. Sessions overlap: 19 trades are counted 25 times in total, because a trade opened while two sessions run counts in both. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

_Nothing to report for the current trades and filters._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $1,154.19
- **Average trade:** $60.75
- **Gross profit:** $1,888.76
- **Gross loss:** $734.57
- **Profit / month:** $48.42
- **Average profit:** $157.4
- **Average loss:** $104.94
- **Max drawdown:** $154.12
- **Max current day loss %:** 0%
- **Profit factor:** 2.57
- **Return %:** 11.54%

#### Trades

- **Total trades:** 19
- **Trading days:** 19
- **Profit trades:** 12
- **Loss trades:** 7
- **Max consecutive profit trades:** 4
- **Max consecutive loss trades:** 2
- **Trades / day:** 0.03
- **Trades / month:** 0.8
- **Profit trades / month:** 0.5
- **Loss trades / month:** 0.29
- **Max profit trade:** $282.24
- **Max loss trade:** $112.88
- **Total volume traded:** $1.3m
- **Average order size:** $71k

#### Time

- **Days processed:** 725.56
- **Months processed:** 23.84

#### Other

- **Max lot used:** 1.36
- **Restoration factor:** 7.49
- **Reliability factor:** 0.31
- **Win rate %:** 63.16%
- **Loss rate %:** 36.84%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 1.67
- **Average win/loss ratio 1:3:** 0
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.0763
- **Monthly Sharpe Ratio:** 0.5442
- **Daily Sortino Ratio:** 0.1449
- **Monthly Sortino Ratio:** 1.5372

## 13. Drawdown luck check

_Nothing to report for the current trades and filters._

## 14. Prop Challenge pass probability

_Based on 19 usable closed trades across 637 calendar days. Advanced Analytics filters affect this estimate._

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

- **Estimated pass chance within 90 days:** 0.0% _(95%: 0.0–0.4%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Not decided within the horizon:** 100.0% _(95%: 99.6–100.0%)_
- **Median calendar days to pass (passed attempts only):** —
- **Median trades to pass (passed attempts only):** —

#### Simulated account balance, Day 90

- **Median attempt:** 1.33%
- **Low outcome (5%):** -1.86%
- **High outcome (95%):** 5.66%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 5 | 0 |
| 10 | 0 |
| 15 | 0 |
| 20 | 0 |
| 25 | 0 |
| 30 | 0 |
| 39 | 0 |
| 44 | 0.01 |
| 48 | 0.18 |
| 51 | 0.46 |
| 58 | 0.63 |
| 60 | 0.78 |
| 66 | 0.82 |
| 71 | 1.09 |
| 77 | 1.09 |
| 83 | 1.13 |
| 89 | 1.24 |
| 90 | 1.33 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 1.33% (Day 90), final 1.33% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-5)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 19
- **Hours with trades:** 17

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Friday | 03:00-04:00 | $282.24 | 1 | 100.00% |
| Tuesday | 10:00-11:00 | $201 | 1 | 100.00% |
| Thursday | 11:00-12:00 | $190.38 | 1 | 100.00% |
| Monday | 11:00-12:00 | $170.94 | 1 | 100.00% |
| Friday | 08:00-09:00 | $155.44 | 1 | 100.00% |
| Monday | 02:00-03:00 | $143.61 | 2 | 100.00% |
| Tuesday | 11:00-12:00 | $132.48 | 1 | 100.00% |
| Thursday | 01:00-02:00 | $126.26 | 1 | 100.00% |
| Tuesday | 13:00-14:00 | $119.07 | 1 | 100.00% |
| Thursday | 03:00-04:00 | $110.25 | 1 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Friday | 04:00-05:00 | -$112.88 | 1 | 0.00% |
| Wednesday | 13:00-14:00 | -$107.88 | 1 | 0.00% |
| Thursday | 07:00-08:00 | -$106.5 | 1 | 0.00% |
| Thursday | 18:00-19:00 | -$102.61 | 1 | 0.00% |
| Wednesday | 07:00-08:00 | -$102.06 | 1 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 0 | $0 | — | N/A | N/A |
| Monday | 4 | $356.5 | $89.12 | 4.51 | 75.00% |
| Tuesday | 3 | $452.55 | $150.85 | No loss | 100.00% |
| Wednesday | 2 | -$209.94 | -$104.97 | 0.00 | 0.00% |
| Thursday | 7 | $230.29 | $32.9 | 1.74 | 57.14% |
| Friday | 3 | $324.79 | $108.26 | 3.88 | 66.67% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 1 | $132.48 | 1 | 1 / 0 |
| February 2024 | 0 | — | 0 | 0 / 0 |
| March 2024 | 1 | $110.25 | 1 | 1 / 0 |
| April 2024 | 2 | $408.49 | 2 | 2 / 0 |
| May 2024 | 1 | -$106.50 | 1 | 0 / 1 |
| June 2024 | 0 | — | 0 | 0 / 0 |
| July 2024 | 0 | — | 0 | 0 / 0 |
| August 2024 | 2 | $0.60 | 2 | 1 / 1 |
| September 2024 | 1 | $201.00 | 1 | 1 / 0 |
| October 2024 | 0 | — | 0 | 0 / 0 |
| November 2024 | 1 | -$100.98 | 1 | 0 / 1 |
| December 2024 | 0 | — | 0 | 0 / 0 |
| January 2025 | 1 | -$101.66 | 1 | 0 / 1 |
| February 2025 | 2 | $53.38 | 2 | 1 / 1 |
| March 2025 | 2 | $290.01 | 2 | 2 / 0 |
| April 2025 | 0 | — | 0 | 0 / 0 |
| May 2025 | 1 | $190.38 | 1 | 1 / 0 |
| June 2025 | 2 | $57.55 | 2 | 1 / 1 |
| July 2025 | 0 | — | 0 | 0 / 0 |
| August 2025 | 0 | — | 0 | 0 / 0 |
| September 2025 | 1 | -$107.88 | 1 | 0 / 1 |
| October 2025 | 1 | $127.05 | 1 | 1 / 0 |

_A month with 0 trades had none in the filtered history._

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-5)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 0 | 0 | 0 |
| 01 | 1 | 0 | +1 |
| 02 | 3 | 1 | +2 |
| 03 | 2 | 0 | +2 |
| 04 | 0 | 1 | -1 |
| 05 | 0 | 0 | 0 |
| 06 | 0 | 0 | 0 |
| 07 | 0 | 2 | -2 |
| 08 | 1 | 0 | +1 |
| 09 | 0 | 0 | 0 |
| 10 | 1 | 0 | +1 |
| 11 | 3 | 0 | +3 |
| 12 | 0 | 0 | 0 |
| 13 | 1 | 1 | 0 |
| 14 | 0 | 0 | 0 |
| 15 | 0 | 0 | 0 |
| 16 | 0 | 1 | -1 |
| 17 | 0 | 0 | 0 |
| 18 | 0 | 1 | -1 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |
| 21 | 0 | 0 | 0 |
| 22 | 0 | 0 | 0 |
| 23 | 0 | 0 | 0 |

## 18. Duration & Profitability

- **Analyzed trades:** 19
- **Net profit:** $1,154.19
- **Holding-time ranges:** 6
- **Median holding time:** 5h 55m

#### Key insights

- **Winner vs loser holding time:** The median losing trade was held 2.0x longer than the median winning trade. Winner median: 3h 15m; loser median: 6h 29m.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 1 | 1 | 0 | 0 | 100.0% | $132.48 | $132.48 | $132.48 |
| 1h-4h | 7 | 5 | 2 | 0 | 71.4% | $541.96 | $77.42 | $127.05 |
| 4h-8h | 5 | 3 | 2 | 0 | 60.0% | $317.71 | $63.54 | $113.48 |
| 8h-1d | 5 | 2 | 3 | 0 | 40.0% | -$8.9 | -$1.78 | -$100.98 |
| 1d-3d | 0 | 0 | 0 | 0 | N/A | $0 | $0 | N/A |
| 3d-7d | 1 | 1 | 0 | 0 | 100.0% | $170.94 | $170.94 | $170.94 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$300 | 0 |
| -$300 to -$200 | 0 |
| -$200 to -$100 | 7 |
| -$100 to $0 | 0 |
| $0 to $100 | 0 |
| $100 to $200 | 10 |
| $200 to $300 | 2 |
| >$300 | 0 |

_Average $60.75; median $119.07_

#### Holding time by outcome

| Holding time | Loss | Win | Big win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 0.0% (0) | 100.0% (1) | 0.0% (0) | 1 | 100.0% | $132.48 | $132.48 | $1,021.71 (18) |
| 1h-4h | 28.6% (2) | 71.4% (5) | 0.0% (0) | 7 | 71.4% | $77.42 | $541.96 | $479.74 (11) |
| 4h-8h | 40.0% (2) | 40.0% (2) | 20.0% (1) | 5 | 60.0% | $63.54 | $317.71 | $162.03 (6) |
| 8h-1d | 60.0% (3) | 40.0% (2) | 0.0% (0) | 5 | 40.0% | -$1.78 | -$8.9 | $170.94 (1) |
| 1d-3d | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0 | N/A | N/A | $0 | $170.94 (1) |
| 3d-7d | 0.0% (0) | 100.0% (1) | 0.0% (0) | 1 | 100.0% | $170.94 | $170.94 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
