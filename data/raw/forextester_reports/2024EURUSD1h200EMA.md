# Advanced Analytics

_Project: 4/21 EMA swing strategy_  
_Generated: 2026-10-09 15:31 UTC_  
_Trades analysed: 5_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 5 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $107.72 _(net profit divided by the number of closed trades)_
- **Total PnL:** $538.61
- **Drawdown:** $137.08 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $10,538.61
- **Balance:** $10,538.61
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 80.00%
- **Avg Result / Trade:** $107.72
- **Profit Factor:** 6.42
- **Profitability:** 5.39% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-16 | 10000 |
| 2024-01-17 | 10145.01 |
| 2024-03-07 | 10242.96 |
| 2024-03-20 | 10143.6 |
| 2024-04-02 | 10365.09 |
| 2024-04-26 | 10538.61 |

_min $10,000.00 (2024-01-16), max $10,538.61 (2024-04-26), final $10,538.61 (2024-04-26)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-16 | 0 |
| 2024-01-17 | 145.01 |
| 2024-03-07 | 242.96 |
| 2024-03-20 | 143.6 |
| 2024-04-02 | 365.09 |
| 2024-04-26 | 538.61 |

_min $0.00 (2024-01-16), max $538.61 (2024-04-26), final $538.61 (2024-04-26)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-16 | 0 |
| 2024-01-17 | 0 |
| 2024-03-07 | 0 |
| 2024-03-20 | -99.36 |
| 2024-04-02 | 0 |
| 2024-04-26 | 0 |

_min -$99.36 (2024-03-20), max $0.00 (2024-01-16), final $0.00 (2024-04-26)._

## 2. Analytics Insights

_You need at least 30 trades for more precise recommendations. Keep testing — the more data we have, the smarter your analytics become._

#### Overview

- **Net profit:** $538.61
- **Trades analysed:** 5
- **Score:** 16 of 40 points
- **Tests:** 16 passed, 4 failed
- **Total potential improvement:** $49.55 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Swing
- **Median holding duration:** 3d 3h 37m
- **Trading period:** 0 years, 3 months, 16 days

#### Behavioural strengths

- Effective Risk Management
- Disciplined Approach
- Prudent Position Sizing

#### Behavioural weaknesses

- Poor Strategic Planning
- Overconfidence Bias
- Inconsistent Execution

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Consider increasing lot size to reach 1% risk per trade (potential improvement +$5.39)

Your maximum risk per trade is 0.99%, which is below the recommended 1%. Increasing lot size by 1.01x to target 1% risk could improve your returns, provided you keep risk controls in place.

Recommendations:
- Your trades risk less than 1% of balance (measured on trades where the risk was defined). Consider increasing your lot size by 1.01x so the maximum risk per trade reaches about 1%. This could increase profits while keeping risk conservative.

#### ❌ Consider keeping position size after winning streaks (potential improvement +$44.16)

Your results indicate that increasing lot size after winning streaks has been harmful historically.

Recommendations:
- Historical analysis shows you could improve net profit by $44.16 (8.2%) by keeping your position size unchanged after winning streaks.

Trades behind this verdict: 1.

#### ❌ Try aiming for better Reward:Risk ratios

Your Reward:Risk ratios need improvement.

Recommendations:
- Set your take profit targets at least twice as far from entry as your stop loss. This ensures favorable risk-reward even with lower win rates.
- Manage open positions to achieve better reward:risk outcomes. Let winners run to target and cut losses at predetermined stops rather than closing early.

#### ❌ Try to reduce your maximum drawdown

Your maximum drawdown is 40.90% of your peak cumulative profit — that is too high.

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
- ✅ Consistent trade holding times
- ✅ Consistent Loss Management
- ✅ Appropriate stop loss placement
- ✅ Consistent position sizing
- ✅ Direction bias analysis
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### EURUSD: best exit parameters (based on 5 trades)

- **Stop loss:** 72.2 pips _(average loss as traded: 35.8 pips)_
- **Take profit:** 112.2 pips _(average profit as traded: 74.8 pips)_
- **Max holding:** 11d 5h 30m _(median holding as traded: 3d 3h 37m)_

#### EURUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $918.44 | $538.61 |
| Profit factor | — | 6.42 |
| Win rate | 100% | 80% |
| Expected value per trade | $183.69 | $107.72 |
| Net result in display units | 446.0 pips | 263.3 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### EURUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 72.2 pips | 112.2 pips | 11d 5h 30m | $918.44 | 100% | — |
| 2 | none | 112.2 pips | 11d 5h 30m | $918.44 | 100% | — |
| 3 | 72.2 pips | 101.1 pips | 11d 5h 30m | $852.95 | 100% | — |
| 4 | none | 101.1 pips | 11d 5h 30m | $852.95 | 100% | — |
| 5 | 72.2 pips | 123.6 pips | 11d 5h 30m | $847.32 | 100% | — |
| 6 | none | 123.6 pips | 11d 5h 30m | $847.32 | 100% | — |
| 7 | 72.2 pips | 90.4 pips | 8d 4h 3m | $775.56 | 100% | — |
| 8 | 72.2 pips | 90.4 pips | 8d 21h 43m | $775.56 | 100% | — |
| 9 | 72.2 pips | 90.4 pips | 9d 15h 51m | $775.56 | 100% | — |
| 10 | 72.2 pips | 90.4 pips | 10d 10h 27m | $775.56 | 100% | — |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### EURUSD: net profit vs stop loss (TP fixed at 112.2 pips, holding at 11d 5h 30m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 2 | -35.4 |
| 3 | -47.2 |
| 4.8 | -68.44 |
| 7 | -94.4 |
| 9.6 | -125.08 |
| 12.4 | -158.12 |
| 15.5 | -194.7 |
| 18.9 | -38.17 |
| 22.4 | -74.22 |
| 26.1 | 27.71 |
| 30.1 | 0.91 |
| 34.2 | -26.56 |
| 38.4 | -54.7 |
| 42.8 | -84.18 |
| 47.4 | -115 |
| 52.1 | -146.49 |
| 56.9 | 108.82 |
| 61.9 | 83.82 |
| 67 | 434.6 |
| 72.2 | 918.44 |

_min -$194.70 (15.5), max $918.44 (72.2), final $918.44 (72.2)._

#### EURUSD: net profit vs take profit (SL fixed at 72.2 pips, holding at 11d 5h 30m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 2 | 11.8 |
| 4.5 | 41.3 |
| 8.8 | 92.04 |
| 14.2 | 155.76 |
| 20.4 | 228.92 |
| 27.3 | 310.34 |
| 34.9 | 400.02 |
| 42.9 | 494.42 |
| 51.6 | 457.4 |
| 60.6 | 531.2 |
| 70.2 | 609.92 |
| 80.1 | 691.1 |
| 90.4 | 775.56 |
| 101.1 | 852.95 |
| 112.2 | 918.44 |
| 123.6 | 847.32 |
| 135.4 | 689.28 |
| 147.5 | 721.95 |
| 159.8 | 590.19 |
| 172.5 | 590.19 |

_min $11.80 (2), max $918.44 (112.2), final $590.19 (172.5)._

#### EURUSD: net profit vs max holding (SL fixed at 72.2 pips, TP fixed at 112.2 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 13h 28m | 57.35 |
| 17h 16m | 186.27 |
| 23h 42m | 113.29 |
| 1d 7h 45m | 150.06 |
| 1d 17h 3m | 64.59 |
| 2d 3h 25m | -25.65 |
| 2d 14h 43m | -74.03 |
| 3d 2h 52m | 150.99 |
| 3d 15h 47m | 479.28 |
| 4d 5h 25m | 587.71 |
| 4d 19h 43m | 489.48 |
| 5d 10h 39m | 491.96 |
| 6d 2h 10m | 396.34 |
| 6d 18h 16m | 358.19 |
| 7d 10h 54m | 449.78 |
| 8d 4h 3m | 509.46 |
| 8d 21h 43m | 382.89 |
| 9d 15h 51m | 466.29 |
| 10d 10h 27m | 623.12 |
| 11d 5h 30m | 918.44 |

_min -$74.03 (2d 14h 43m), max $918.44 (11d 5h 30m), final $918.44 (11d 5h 30m)._

## 4. Entry / Exit Efficiency

_5 of 5 filtered trade rows are included._

#### Favorable move captured

- **Median capture:** 97.4% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 98.0%
- **Money-weighted capture:** 71.7% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $61.58 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $122.04
- **Winners with open loss above profit:** 0.0%

#### Caveats on capture

- Measured over 5 trade(s), fewer than the 30 this section treats as enough to call a figure typical.

#### E-ratio in the first bars after entry

- **5 bars of 1H:** — _(fewer than 30 measurable trades, so no ratio is shown; 5 eligible, 0 unavailable)_
- **10 bars of 1H:** — _(fewer than 30 measurable trades, so no ratio is shown; 5 eligible, 0 unavailable)_
- **20 bars of 1H:** — _(fewer than 30 measurable trades, so no ratio is shown; 5 eligible, 0 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 1.89%
- **Maximum drawdown, money:** $195.58 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 12d
- **Average recovery:** 1d 16h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 0.67%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-09 | 0 |
| 2024-01-10 | -0.03 |
| 2024-01-11 | -0.82 |
| 2024-01-11 | -0.15 |
| 2024-01-12 | -0.76 |
| 2024-01-15 | -0.56 |
| 2024-01-16 | 0 |
| 2024-03-04 | 0 |
| 2024-03-05 | -0.17 |
| 2024-03-06 | 0 |
| 2024-03-07 | -0.44 |
| 2024-03-18 | 0 |
| 2024-03-20 | 0 |
| 2024-03-20 | -1.75 |
| 2024-03-27 | -1.83 |
| 2024-03-29 | -0.71 |
| 2024-04-01 | 0 |
| 2024-04-25 | 0 |
| 2024-04-25 | -1.16 |
| 2024-04-26 | 0 |

_20 of 107 points, shape-preserving; min -1.89% (2024-03-27), max 0.00% (2024-01-09), final 0.00% (2024-04-26)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.89% | $195.58 | 20 Mar 2024 13:00 | 27 Mar 2024 01:00 | 01 Apr 2024 13:00 | 12d | 5d 12h | 1 | — |
| 1.16% | $121.32 | 25 Apr 2024 09:00 | 25 Apr 2024 09:00 | 25 Apr 2024 13:00 | 4h | 4h | 0 | — |
| 0.88% | $88.23 | 09 Jan 2024 21:00 | 11 Jan 2024 21:00 | 15 Jan 2024 21:00 | 6d | 4d | 0 | — |
| 0.50% | $51.30 | 19 Mar 2024 09:00 | 20 Mar 2024 01:00 | 20 Mar 2024 09:00 | 1d | 8h | 0 | — |
| 0.44% | $44.85 | 06 Mar 2024 17:00 | 07 Mar 2024 09:00 | 07 Mar 2024 13:00 | 20h | 4h | 1 | — |

_Showing the 5 deepest of 14 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 5
- **Winnings:** 4/5 (80.00%)
- **Losing:** 1/5 (20.00%)
- **Long trades:** 2/5 (40.00%)
- **Short trades:** 3/5 (60.00%)
- **Profit on longs:** $271.47
- **Profit on shorts:** $267.14

## 7. Rolling Performance

_Nothing to report for the current trades and filters._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EURUSD | 5 | 4 | 1 | 80% | 1.2 | $637.97 | $99.36 | $538.61 | 6.42 | 86.52% / 13.48% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 0 | 0.00% | --- | --- | --- | --- |
| London Session | 08:00-17:00 London time | 3 | 60.00% | $143.60 | $47.87 | 66.7% | 2.45 |
| Asian Session | 09:00-18:00 Tokyo time | 2 | 40.00% | $395.01 | $197.50 | 100.0% | --- |
| New York AM Silver Bullet | 10:00-11:00 New York time | 0 | 0.00% | --- | --- | --- | --- |
| New York Session | 08:00-17:00 New York time | 1 | 20.00% | -$99.36 | -$99.36 | 0.0% | 0.00 |
| Outside sessions | — | 0 | 0.00% | $0.00 | — | — | — |

_Shares are of the 5 trades analysed. Sessions overlap: 5 trades are counted 6 times in total, because a trade opened while two sessions run counts in both. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

_Nothing to report for the current trades and filters._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $538.61
- **Average trade:** $107.72
- **Gross profit:** $637.97
- **Gross loss:** $99.36
- **Profit / month:** $140.87
- **Average profit:** $159.49
- **Average loss:** $99.36
- **Max drawdown:** $137.08
- **Max current day loss %:** 0.28%
- **Profit factor:** 6.42
- **Return %:** 5.39%

#### Trades

- **Total trades:** 5
- **Trading days:** 5
- **Profit trades:** 4
- **Loss trades:** 1
- **Max consecutive profit trades:** 2
- **Max consecutive loss trades:** 1
- **Trades / day:** 0.04
- **Trades / month:** 1.31
- **Profit trades / month:** 1.05
- **Loss trades / month:** 0.26
- **Max profit trade:** $221.49
- **Max loss trade:** $99.36
- **Total volume traded:** $127.7k
- **Average order size:** $25.5k

#### Time

- **Days processed:** 116.37
- **Months processed:** 3.82

#### Other

- **Max lot used:** 0.36
- **Restoration factor:** 3.93
- **Reliability factor:** 1.03
- **Win rate %:** 80%
- **Loss rate %:** 20%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 0
- **Average win/loss ratio 1:3:** 0
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.1467
- **Monthly Sharpe Ratio:** 1.7838
- **Daily Sortino Ratio:** 0.2386
- **Monthly Sortino Ratio:** N/A

## 13. Drawdown luck check

_Nothing to report for the current trades and filters._

## 14. Prop Challenge pass probability

_Nothing to report for the current trades and filters._

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-4)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 5
- **Hours with trades:** 5

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Tuesday | 02:00-03:00 | $221.49 | 1 | 100.00% |
| Friday | 04:00-05:00 | $173.52 | 1 | 100.00% |
| Wednesday | 01:00-02:00 | $145.01 | 1 | 100.00% |
| Thursday | 10:00-11:00 | $97.95 | 1 | 100.00% |
| Wednesday | 14:00-15:00 | -$99.36 | 1 | 0.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 0 | $0 | — | N/A | N/A |
| Monday | 0 | $0 | — | N/A | N/A |
| Tuesday | 1 | $221.49 | $221.49 | No loss | 100.00% |
| Wednesday | 2 | $45.65 | $22.82 | 1.46 | 50.00% |
| Thursday | 1 | $97.95 | $97.95 | No loss | 100.00% |
| Friday | 1 | $173.52 | $173.52 | No loss | 100.00% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 1 | $145.01 | 1 | 1 / 0 |
| February 2024 | 0 | — | 0 | 0 / 0 |
| March 2024 | 2 | -$1.41 | 2 | 1 / 1 |
| April 2024 | 2 | $395.01 | 2 | 2 / 0 |

_A month with 0 trades had none in the filtered history._

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-4)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 0 | 0 | 0 |
| 01 | 1 | 0 | +1 |
| 02 | 1 | 0 | +1 |
| 03 | 0 | 0 | 0 |
| 04 | 1 | 0 | +1 |
| 05 | 0 | 0 | 0 |
| 06 | 0 | 0 | 0 |
| 07 | 0 | 0 | 0 |
| 08 | 0 | 0 | 0 |
| 09 | 0 | 0 | 0 |
| 10 | 1 | 0 | +1 |
| 11 | 0 | 0 | 0 |
| 12 | 0 | 0 | 0 |
| 13 | 0 | 0 | 0 |
| 14 | 0 | 1 | -1 |
| 15 | 0 | 0 | 0 |
| 16 | 0 | 0 | 0 |
| 17 | 0 | 0 | 0 |
| 18 | 0 | 0 | 0 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |
| 21 | 0 | 0 | 0 |
| 22 | 0 | 0 | 0 |
| 23 | 0 | 0 | 0 |

## 18. Duration & Profitability

- **Analyzed trades:** 5
- **Net profit:** $538.61
- **Holding-time ranges:** 3
- **Median holding time:** 3d 3h 37m

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1d-3d | 2 | 1 | 1 | 0 | 50.0% | $74.16 | $37.08 | $37.08 |
| 3d-7d | 2 | 2 | 0 | 0 | 100.0% | $319.44 | $159.72 | $159.72 |
| 7d-28d | 1 | 1 | 0 | 0 | 100.0% | $145.01 | $145.01 | $145.01 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$250 | 0 |
| -$250 to -$200 | 0 |
| -$200 to -$150 | 0 |
| -$150 to -$100 | 0 |
| -$100 to -$50 | 1 |
| -$50 to $0 | 0 |
| $0 to $50 | 0 |
| $50 to $100 | 1 |
| $100 to $150 | 1 |
| $150 to $200 | 1 |
| $200 to $250 | 1 |
| >$250 | 0 |

_Average $107.72; median $145.01_

#### Holding time by outcome

| Holding time | Loss | Win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1d-3d | 50.0% (1) | 50.0% (1) | 2 | 50.0% | $37.08 | $74.16 | $464.45 (3) |
| 3d-7d | 0.0% (0) | 100.0% (2) | 2 | 100.0% | $159.72 | $319.44 | $145.01 (1) |
| 7d-28d | 0.0% (0) | 100.0% (1) | 1 | 100.0% | $145.01 | $145.01 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
