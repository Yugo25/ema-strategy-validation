# Advanced Analytics

_Project: 6/16 200EMA_  
_Generated: 2026-10-09 15:44 UTC_  
_Trades analysed: 25_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 25 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $38.37 _(net profit divided by the number of closed trades)_
- **Total PnL:** $959.20
- **Drawdown:** $258.41 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $10,959.20
- **Balance:** $10,959.20
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 56.00%
- **Avg Result / Trade:** $38.37
- **Profit Factor:** 1.80
- **Profitability:** 9.59% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-23 | 10000 |
| 2024-01-24 | 9891.76 |
| 2024-02-08 | 10026.4 |
| 2024-03-01 | 10197.3 |
| 2024-04-15 | 10199.12 |
| 2024-04-19 | 10088.05 |
| 2024-07-11 | 9866.48 |
| 2024-07-23 | 10072.66 |
| 2024-07-24 | 10225.72 |
| 2024-08-27 | 10270.15 |
| 2024-08-30 | 10155.78 |
| 2024-09-10 | 10275.55 |
| 2024-10-21 | 10611.8 |
| 2024-10-22 | 10505.53 |
| 2024-10-30 | 10397.64 |
| 2024-12-23 | 10575.57 |
| 2025-01-13 | 10469.98 |
| 2025-01-23 | 10650.23 |
| 2025-03-17 | 11066.99 |
| 2025-03-18 | 10959.2 |

_20 of 26 points, shape-preserving; min $9,866.48 (2024-07-11), max $11,066.99 (2025-03-17), final $10,959.20 (2025-03-18)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-23 | 0 |
| 2024-01-24 | -108.24 |
| 2024-02-08 | 26.4 |
| 2024-03-01 | 197.3 |
| 2024-04-15 | 199.12 |
| 2024-04-19 | 88.05 |
| 2024-07-11 | -133.52 |
| 2024-07-23 | 72.66 |
| 2024-07-24 | 225.72 |
| 2024-08-27 | 270.15 |
| 2024-08-30 | 155.78 |
| 2024-09-10 | 275.55 |
| 2024-10-21 | 611.8 |
| 2024-10-22 | 505.53 |
| 2024-10-30 | 397.64 |
| 2024-12-23 | 575.57 |
| 2025-01-13 | 469.98 |
| 2025-01-23 | 650.23 |
| 2025-03-17 | 1066.99 |
| 2025-03-18 | 959.2 |

_20 of 26 points, shape-preserving; min -$133.52 (2024-07-11), max $1,066.99 (2025-03-17), final $959.20 (2025-03-18)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-23 | 0 |
| 2024-01-24 | -108.24 |
| 2024-02-08 | 0 |
| 2024-03-18 | -106.38 |
| 2024-04-15 | 0 |
| 2024-04-19 | -111.07 |
| 2024-07-11 | -332.64 |
| 2024-07-23 | -126.46 |
| 2024-07-24 | 0 |
| 2024-08-27 | 0 |
| 2024-08-30 | -114.37 |
| 2024-09-10 | 0 |
| 2024-10-21 | 0 |
| 2024-10-22 | -106.27 |
| 2024-10-30 | -214.16 |
| 2024-12-23 | -36.23 |
| 2025-01-13 | -141.83 |
| 2025-01-23 | 0 |
| 2025-03-17 | 0 |
| 2025-03-18 | -107.79 |

_20 of 26 points, shape-preserving; min -$332.64 (2024-07-11), max $0.00 (2024-01-23), final -$107.79 (2025-03-18)._

## 2. Analytics Insights

_You need at least 30 trades for more precise recommendations. Keep testing — the more data we have, the smarter your analytics become._

#### Overview

- **Net profit:** $959.20
- **Trades analysed:** 25
- **Score:** 14 of 40 points
- **Tests:** 14 passed, 6 failed
- **Total potential improvement:** $211.43 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 8h 10m
- **Trading period:** 1 year, 1 month, 22 days

#### Behavioural strengths

- Effective Risk Management
- Effective Stress Management
- Emotional Control

#### Behavioural weaknesses

- Poor Strategic Planning
- Lack Of Discipline
- Inconsistent Execution

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Try keeping risk below 2% per trade

Your risk management shows frequent moderate risk with 44.0% of trades exceeding the 1% threshold.

Recommendations:
- A significant portion of your trades (44.0%) risked more than the recommended 1% of your capital. To ensure long-term sustainability, consider consistently reducing your position sizes.
- To better manage risk, consider recalibrating your standard position size to ensure your risk per trade consistently remains below the ideal 1% threshold.

Trades behind this verdict: 11.

#### ❌ Try adding more trade filters to increase win ratio or increase timeframe

Trading costs are significant relative to your average trade profit.

Recommendations:
- Your trading costs are consuming 26.1% of your average trade profit. Try to reduce the impact of trading costs on your profits to enhance your net results.

#### ❌ Try using time-based exit rules or trailing stops

You have trades held significantly longer than your average.

Recommendations:
- Implement time-based exit rules or trailing stops to prevent holding trades beyond their optimal duration. Consider setting maximum holding periods based on your typical profitable trade duration.

#### ❌ Try aiming for better Reward:Risk ratios

Your Reward:Risk ratios need improvement.

Recommendations:
- Set your take profit targets at least twice as far from entry as your stop loss. This ensures favorable risk-reward even with lower win rates.
- Manage open positions to achieve better reward:risk outcomes. Let winners run to target and cut losses at predetermined stops rather than closing early.

#### ❌ Reduce lot size on unprofitable symbol-direction combinations (potential improvement +$234.19)

At least one instrument shows profit imbalance between Long and Short directions.

Recommendations:
- Temporarily avoid or reduce position sizes for symbol-direction combinations showing consistent losses. Estimated improvement: $234.19. Consider using trend indicators on a higher timeframe to align entries with the dominant direction.

#### ❌ Try to reduce your maximum drawdown

Your maximum drawdown is 167.05% of your peak cumulative profit — that is too high.

Recommendations:
- Review trades during drawdown periods to identify patterns. Consider reducing position sizes when certain drawdown level is reached, implementing portfolio heat limits, or using systematic risk reduction during losing streaks.

Trades behind this verdict: 4.

#### Passed tests

- ✅ Daily loss limit analysis
- ✅ Trading session analysis
- ✅ Consecutive winners
- ✅ Revenge trades
- ✅ Trading during news events
- ✅ News reaction trading
- ✅ Position averaging
- ✅ Netting opportunities
- ✅ Timeframe analysis
- ✅ Trading without stops
- ✅ Consistent Loss Management
- ✅ Appropriate stop loss placement
- ✅ Consistent position sizing
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### USDCAD: best exit parameters (based on 25 trades)

- **Stop loss:** 5.8 pips _(average loss as traded: 15.7 pips)_
- **Take profit:** 79.5 pips _(average profit as traded: 24.0 pips)_
- **Max holding:** 2d 18h 35m _(median holding as traded: 8h 10m)_

#### USDCAD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $1,165.02 | $959.20 |
| Profit factor | 4.61 | 1.8 |
| Win rate | 30% | 56% |
| Expected value per trade | $116.50 | $38.37 |
| Net result in display units | 197.9 pips | 163.9 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### USDCAD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 5.8 pips | 79.5 pips | 2d 18h 35m | $1,165.02 | 30% | 4.61 |
| 2 | 5.8 pips | 79.5 pips | 3d 35m | $1,165.02 | 30% | 4.61 |
| 3 | 5.8 pips | 79.5 pips | 3d 6h 45m | $1,165.02 | 30% | 4.61 |
| 4 | 5.8 pips | 79.5 pips | 3d 13h 4m | $1,165.02 | 30% | 4.61 |
| 5 | 5.8 pips | 79.5 pips | 3d 19h 32m | $1,165.02 | 30% | 4.61 |
| 6 | 5.8 pips | 79.5 pips | 2d 12h 46m | $1,100.45 | 30% | 4.41 |
| 7 | 7.7 pips | 79.5 pips | 2d 18h 35m | $1,079.71 | 30% | 3.64 |
| 8 | 7.7 pips | 79.5 pips | 3d 35m | $1,079.71 | 30% | 3.64 |
| 9 | 7.7 pips | 79.5 pips | 3d 6h 45m | $1,079.71 | 30% | 3.64 |
| 10 | 7.7 pips | 79.5 pips | 3d 13h 4m | $1,079.71 | 30% | 3.64 |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### USDCAD: net profit vs stop loss (TP fixed at 79.5 pips, holding at 2d 18h 35m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 2 | -217 |
| 2.8 | -268.16 |
| 4.1 | -351.3 |
| 5.8 | 1165.02 |
| 7.7 | 1079.71 |
| 9.9 | 980.93 |
| 12.2 | 877.65 |
| 14.8 | 760.91 |
| 17.4 | 644.17 |
| 20.3 | 513.96 |
| 23.2 | 383.75 |
| 26.3 | 420.33 |
| 29.6 | 661.48 |
| 32.9 | 549.25 |
| 36.3 | 433.63 |
| 39.9 | 311.2 |
| 43.6 | 185.37 |
| 47.3 | 59.54 |
| 51.2 | -73.09 |
| 55.1 | -205.72 |

_min -$351.30 (4.1), max $1,165.02 (5.8), final -$205.72 (55.1)._

#### USDCAD: net profit vs take profit (SL fixed at 5.8 pips, holding at 2d 18h 35m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 2.1 | -229.46 |
| 3.7 | -182.77 |
| 6.5 | -101.05 |
| 9.9 | -94.44 |
| 13.8 | -3.63 |
| 18.2 | -2.8 |
| 23 | 88.65 |
| 28.2 | 187.71 |
| 33.6 | 290.58 |
| 39.4 | 401.08 |
| 45.5 | 517.29 |
| 51.8 | 637.31 |
| 58.4 | 763.05 |
| 65.2 | 892.59 |
| 72.2 | 1025.95 |
| 79.5 | 1165.02 |
| 87 | 782.73 |
| 94.6 | 861.3 |
| 102.5 | 909.78 |
| 110.6 | 489.42 |

_min -$229.46 (2.1), max $1,165.02 (79.5), final $489.42 (110.6)._

#### USDCAD: net profit vs max holding (SL fixed at 5.8 pips, TP fixed at 79.5 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 4h 34m | -58.96 |
| 5h 52m | -52.93 |
| 8h 3m | 116.68 |
| 10h 47m | 421.09 |
| 13h 56m | 477.58 |
| 17h 28m | 368.05 |
| 21h 18m | 619.02 |
| 1d 1h 25m | 739.87 |
| 1d 5h 49m | 805.17 |
| 1d 10h 27m | 895.86 |
| 1d 15h 18m | 892.95 |
| 1d 20h 22m | 896.58 |
| 2d 1h 39m | 1019.19 |
| 2d 7h 7m | 1027.17 |
| 2d 12h 46m | 1100.45 |
| 2d 18h 35m | 1165.02 |
| 3d 35m | 1165.02 |
| 3d 6h 45m | 1165.02 |
| 3d 13h 4m | 1165.02 |
| 3d 19h 32m | 1165.02 |

_min -$58.96 (4h 34m), max $1,165.02 (2d 18h 35m), final $1,165.02 (3d 19h 32m)._

## 4. Entry / Exit Efficiency

_21 of 25 filtered trade rows are included. 4 filtered trade rows were excluded._

#### Favorable move captured

- **Median capture:** 82.8% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 94.6%
- **Money-weighted capture:** 27.1% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $28.79 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $108.65
- **Winners with open loss above profit:** 0.0%

#### Caveats on capture

- Measured over 21 trade(s), fewer than the 30 this section treats as enough to call a figure typical.

#### E-ratio in the first bars after entry

- **5 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 21 eligible, 0 unavailable)_
- **10 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 21 eligible, 0 unavailable)_
- **20 bars of 5m:** — _(fewer than 30 measurable trades, so no ratio is shown; 21 eligible, 0 unavailable)_

## 5. Drawdown Anatomy

_Measured on equity at each bar close, so drawdowns while trades were open are included._

- **Maximum drawdown:** 3.26%
- **Maximum drawdown, money:** $332.64 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. It is measured on your equity at the close of each 4-hour bar, and the peak it is measured from includes open profit, so it can sit a little above or below the Drawdown card, which measures from the highest closed balance and says under its value how often it checks.)_
- **Longest underwater:** 3.2 mo
- **Average recovery:** 37d 9h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 1.27%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-24 | 0 |
| 2024-01-24 | -2.17 |
| 2024-03-01 | 0 |
| 2024-04-15 | 0 |
| 2024-05-07 | -2.15 |
| 2024-07-11 | -3.26 |
| 2024-07-23 | -2.94 |
| 2024-07-24 | 0 |
| 2024-07-29 | -1.29 |
| 2024-09-10 | 0 |
| 2024-10-18 | -0.79 |
| 2024-10-21 | 0 |
| 2024-10-22 | -1 |
| 2024-10-30 | -0.05 |
| 2024-11-11 | -2.01 |
| 2024-12-23 | -0.34 |
| 2025-01-22 | -1.13 |
| 2025-01-23 | 0 |
| 2025-03-18 | 0 |
| 2025-03-18 | -1.95 |

_20 of 74 points, shape-preserving; min -3.26% (2024-07-11), max 0.00% (2024-01-24), final -1.95% (2025-03-18)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.26% | $332.64 | 19 Apr 2024 01:00 | 11 Jul 2024 05:00 | 24 Jul 2024 17:00 | 3.2 mo | 13d 12h | 5 | — |
| 2.17% | $219.38 | 24 Jan 2024 13:00 | 24 Jan 2024 13:00 | 01 Mar 2024 09:00 | 36d 20h | 36d 20h | 1 | — |
| 2.02% | $214.16 | 21 Oct 2024 21:00 | 30 Oct 2024 17:00 | 23 Jan 2025 09:00 | 3.1 mo | 2.8 mo | 6 | — |
| 1.95% | $218.44 | 18 Mar 2025 09:00 | 18 Mar 2025 13:00 | Not recovered | 4h | — | 1 | — |
| 1.29% | $131.72 | 28 Jul 2024 21:00 | 27 Aug 2024 09:00 | 27 Aug 2024 13:00 | 29d 16h | 4h | 1 | — |

_Showing the 5 deepest of 9 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 25
- **Winnings:** 14/25 (56.00%)
- **Losing:** 11/25 (44.00%)
- **Long trades:** 18/25 (72.00%)
- **Short trades:** 7/25 (28.00%)
- **Profit on longs:** $1,193.39
- **Profit on shorts:** -$234.19

## 7. Rolling Performance

_Nothing to report for the current trades and filters._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| USDCAD | 25 | 14 | 11 | 56.00% | 25.1 | $2,157.45 | $1,198.25 | $959.20 | 1.80 | 64.29% / 35.71% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 0 | 0.00% | --- | --- | --- | --- |
| London Session | 08:00-17:00 London time | 7 | 28.00% | $435.30 | $62.19 | 71.4% | 2.96 |
| Asian Session | 09:00-18:00 Tokyo time | 7 | 28.00% | $83.25 | $11.89 | 42.9% | 1.19 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 0 | 0.00% | --- | --- | --- | --- |
| New York Session | 08:00-17:00 New York time | 10 | 40.00% | $496.34 | $49.63 | 60.0% | 2.13 |
| Outside sessions | — | 3 | 12.00% | -$10.42 | -$3.47 | — | — |

_Shares are of the 25 trades analysed. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

_Nothing to report for the current trades and filters._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $959.2
- **Average trade:** $38.37
- **Gross profit:** $2,157.45
- **Gross loss:** $1,198.25
- **Profit / month:** $64.67
- **Average profit:** $154.1
- **Average loss:** $108.93
- **Max drawdown:** $258.41
- **Max current day loss %:** 0%
- **Profit factor:** 1.8
- **Return %:** 9.59%

#### Trades

- **Total trades:** 25
- **Trading days:** 25
- **Profit trades:** 14
- **Loss trades:** 11
- **Max consecutive profit trades:** 3
- **Max consecutive loss trades:** 3
- **Trades / day:** 0.06
- **Trades / month:** 1.69
- **Profit trades / month:** 0.94
- **Loss trades / month:** 0.74
- **Max profit trade:** $252.49
- **Max loss trade:** $114.37
- **Total volume traded:** $2.5m
- **Average order size:** $100.3k

#### Time

- **Days processed:** 451.42
- **Months processed:** 14.83

#### Other

- **Max lot used:** 1.76
- **Restoration factor:** 3.71
- **Reliability factor:** 0.25
- **Win rate %:** 56%
- **Loss rate %:** 44%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 0.88
- **Average win/loss ratio 1:3:** 0
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** 0.0669
- **Monthly Sharpe Ratio:** 0.7383
- **Daily Sortino Ratio:** 0.1073
- **Monthly Sortino Ratio:** 1.6174

## 13. Drawdown luck check

_Nothing to report for the current trades and filters._

## 14. Prop Challenge pass probability

_Based on 25 usable closed trades across 420 calendar days. Advanced Analytics filters affect this estimate._

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

- **Estimated pass chance within 90 days:** 2.8% _(95%: 1.9–4.0%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Not decided within the horizon:** 97.2% _(95%: 96.0–98.1%)_
- **Median calendar days to pass (passed attempts only):** 74
- **Median trades to pass (passed attempts only):** 7

#### Simulated account balance, Day 90

- **Median attempt:** 1.99%
- **Low outcome (5%):** -2.10%
- **High outcome (95%):** 7.94%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 5 | 0 |
| 10 | 0 |
| 19 | 0 |
| 22 | 0 |
| 25 | 0.26 |
| 31 | 0.3 |
| 36 | 0.69 |
| 41 | 0.87 |
| 49 | 0.95 |
| 51 | 1.07 |
| 56 | 1.11 |
| 64 | 1.37 |
| 67 | 1.51 |
| 71 | 1.66 |
| 79 | 1.88 |
| 82 | 1.9 |
| 88 | 1.98 |
| 90 | 1.99 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 1.99% (Day 90), final 1.99% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-4)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 25
- **Hours with trades:** 21

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Tuesday | 16:00-17:00 | $206.18 | 1 | 100.00% |
| Wednesday | 08:00-09:00 | $202.23 | 1 | 100.00% |
| Friday | 09:00-10:00 | $170.9 | 1 | 100.00% |
| Thursday | 07:00-08:00 | $157.45 | 2 | 100.00% |
| Tuesday | 10:00-11:00 | $153.51 | 1 | 100.00% |
| Wednesday | 14:00-15:00 | $153.05 | 1 | 100.00% |
| Monday | 02:00-03:00 | $134.02 | 1 | 100.00% |
| Monday | 13:00-14:00 | $108.2 | 1 | 100.00% |
| Monday | 06:00-07:00 | $98.84 | 1 | 100.00% |
| Monday | 05:00-06:00 | $79.1 | 1 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Friday | 08:00-09:00 | -$114.37 | 1 | 0.00% |
| Thursday | 03:00-04:00 | -$112.85 | 1 | 0.00% |
| Friday | 02:00-03:00 | -$111.07 | 1 | 0.00% |
| Sunday | 20:00-21:00 | -$109.08 | 1 | 0.00% |
| Monday | 17:00-18:00 | -$108.72 | 1 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 1 | -$109.08 | -$109.08 | 0.00 | 0.00% |
| Monday | 8 | $263.74 | $32.97 | 1.82 | 62.50% |
| Tuesday | 6 | $517.88 | $86.31 | 3.42 | 66.67% |
| Wednesday | 4 | $139.15 | $34.79 | 1.64 | 50.00% |
| Thursday | 3 | $202.05 | $67.35 | 2.79 | 66.67% |
| Friday | 3 | -$54.54 | -$18.18 | 0.76 | 33.33% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 1 | -$108.24 | 1 | 0 / 1 |
| February 2024 | 1 | $134.64 | 1 | 1 / 0 |
| March 2024 | 2 | $64.52 | 2 | 1 / 1 |
| April 2024 | 2 | -$2.87 | 2 | 1 / 1 |
| May 2024 | 1 | -$108.72 | 1 | 0 / 1 |
| June 2024 | 0 | — | 0 | 0 / 0 |
| July 2024 | 4 | $137.31 | 4 | 2 / 2 |
| August 2024 | 2 | $39.14 | 2 | 1 / 1 |
| September 2024 | 1 | $119.77 | 1 | 1 / 0 |
| October 2024 | 4 | $122.09 | 4 | 2 / 2 |
| November 2024 | 1 | $98.84 | 1 | 1 / 0 |
| December 2024 | 1 | $79.10 | 1 | 1 / 0 |
| January 2025 | 2 | $74.66 | 2 | 1 / 1 |
| February 2025 | 1 | $252.49 | 1 | 1 / 0 |
| March 2025 | 2 | $56.48 | 2 | 1 / 1 |

_A month with 0 trades had none in the filtered history._

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-4)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 0 | 0 | 0 |
| 01 | 0 | 0 | 0 |
| 02 | 1 | 1 | 0 |
| 03 | 0 | 2 | -2 |
| 04 | 0 | 0 | 0 |
| 05 | 1 | 0 | +1 |
| 06 | 1 | 0 | +1 |
| 07 | 2 | 0 | +2 |
| 08 | 2 | 2 | 0 |
| 09 | 2 | 2 | 0 |
| 10 | 1 | 0 | +1 |
| 11 | 1 | 1 | 0 |
| 12 | 0 | 0 | 0 |
| 13 | 1 | 1 | 0 |
| 14 | 1 | 0 | +1 |
| 15 | 0 | 0 | 0 |
| 16 | 1 | 0 | +1 |
| 17 | 0 | 1 | -1 |
| 18 | 0 | 0 | 0 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 1 | -1 |
| 21 | 0 | 0 | 0 |
| 22 | 0 | 0 | 0 |
| 23 | 0 | 0 | 0 |

## 18. Duration & Profitability

- **Analyzed trades:** 25
- **Net profit:** $959.2
- **Holding-time ranges:** 5
- **Median holding time:** 8h 10m

#### Key insights

- **Winner vs loser holding time:** The median losing trade was held 2.1x longer than the median winning trade. Winner median: 4h 23m; loser median: 9h 13m.
- **Profit concentration:** Your top 5% of trades generated 21.3% of your total winning profit.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 1 | 1 | 0 | 0 | 100.0% | $79.1 | $79.1 | $79.1 |
| 1h-4h | 10 | 6 | 4 | 0 | 60.0% | $397.67 | $39.77 | $113.98 |
| 4h-8h | 1 | 1 | 0 | 0 | 100.0% | $164.27 | $164.27 | $164.27 |
| 8h-1d | 10 | 4 | 6 | 0 | 40.0% | $87.04 | $8.7 | -$105.93 |
| 1d-3d | 3 | 2 | 1 | 0 | 66.7% | $231.13 | $77.04 | $134.02 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$250 | 0 |
| -$250 to -$200 | 0 |
| -$200 to -$150 | 0 |
| -$150 to -$100 | 11 |
| -$100 to -$50 | 0 |
| -$50 to $0 | 0 |
| $0 to $50 | 0 |
| $50 to $100 | 2 |
| $100 to $150 | 4 |
| $150 to $200 | 5 |
| $200 to $250 | 2 |
| >$250 | 1 |

_Average $38.37; median $98.84_

#### Holding time by outcome

| Holding time | Loss | Win | Big win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15m-1h | 0.0% (0) | 100.0% (1) | 0.0% (0) | 1 | 100.0% | $79.1 | $79.1 | $880.11 (24) |
| 1h-4h | 40.0% (4) | 60.0% (6) | 0.0% (0) | 10 | 60.0% | $39.77 | $397.67 | $482.44 (14) |
| 4h-8h | 0.0% (0) | 100.0% (1) | 0.0% (0) | 1 | 100.0% | $164.27 | $164.27 | $318.16 (13) |
| 8h-1d | 60.0% (6) | 30.0% (3) | 10.0% (1) | 10 | 40.0% | $8.7 | $87.04 | $231.13 (3) |
| 1d-3d | 33.3% (1) | 66.7% (2) | 0.0% (0) | 3 | 66.7% | $77.04 | $231.13 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
