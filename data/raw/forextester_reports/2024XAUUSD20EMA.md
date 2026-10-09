# Advanced Analytics

_Project: 6/1 20EMA_  
_Generated: 2026-10-09 15:42 UTC_  
_Trades analysed: 36_  
_Account currency: USD_  
_Time basis: closeTime_  
_Filters: none_  
_Detail: compact (long tables are cut to their head, per-section copies carry everything)._  

## 1. Performance Over Time

- **Total trades:** 36 _(closed buys and sells, breakeven ones included)_
- **Average trade:** $30.03 _(net profit divided by the number of closed trades)_
- **Total PnL:** $1,081.11
- **Drawdown:** $185.05 _(the largest decline from a peak: highest closed balance less equity, checked at every tick with open positions included; the drawdown curve below reads equity at trade closes, and Drawdown Anatomy measures from the equity peak rather than the closed-balance peak and states its own sampling in its section note, so each of the three can differ from the others; they are three readings of one history, not a contradiction)_
- **Equity:** $11,081.11
- **Balance:** $11,081.11
- **Starting Balance:** $10,000.00
- **Total Deposits:** $10,000.00
- **Total Withdrawals:** $0.00
- **Winrate:** 52.78%
- **Avg Result / Trade:** $30.03
- **Profit Factor:** 1.66
- **Profitability:** 10.81% _(net result as a share of the starting balance)_

#### Equity over time

| Date | Equity (USD) |
| --- | --- |
| 2024-01-01 | 10000 |
| 2024-01-02 | 10112.99 |
| 2024-01-10 | 9914.75 |
| 2024-01-24 | 9921.78 |
| 2024-01-24 | 10170.71 |
| 2024-01-31 | 10434.19 |
| 2024-02-27 | 10533.73 |
| 2024-04-05 | 10344.94 |
| 2024-04-09 | 10517.95 |
| 2024-04-24 | 10233.9 |
| 2024-05-14 | 10135.22 |
| 2024-05-29 | 10373.7 |
| 2024-06-04 | 10279.38 |
| 2024-06-11 | 10288.79 |
| 2024-07-01 | 10778.95 |
| 2024-07-18 | 10681.8 |
| 2024-10-01 | 10991.45 |
| 2024-10-24 | 10911.23 |
| 2024-11-13 | 11175.31 |
| 2024-12-24 | 11081.1 |

_20 of 37 points, shape-preserving; min $9,914.75 (2024-01-10), max $11,175.31 (2024-11-13), final $11,081.11 (2024-12-24)._

#### Total PnL over time

| Date | Total PnL (USD) |
| --- | --- |
| 2024-01-01 | 0 |
| 2024-01-02 | 112.99 |
| 2024-01-10 | -85.25 |
| 2024-01-24 | -78.22 |
| 2024-01-24 | 170.71 |
| 2024-01-31 | 434.19 |
| 2024-02-27 | 533.73 |
| 2024-04-05 | 344.94 |
| 2024-04-09 | 517.95 |
| 2024-04-24 | 233.89 |
| 2024-05-14 | 135.22 |
| 2024-05-29 | 373.7 |
| 2024-06-04 | 279.38 |
| 2024-06-11 | 288.79 |
| 2024-07-01 | 778.95 |
| 2024-07-18 | 681.8 |
| 2024-10-01 | 991.45 |
| 2024-10-24 | 911.23 |
| 2024-11-13 | 1175.31 |
| 2024-12-24 | 1081.11 |

_20 of 37 points, shape-preserving; min -$85.25 (2024-01-10), max $1,175.31 (2024-11-13), final $1,081.11 (2024-12-24)._

#### Drawdown over time

| Date | Drawdown from the running peak (zero or negative) (USD) |
| --- | --- |
| 2024-01-01 | 0 |
| 2024-01-02 | 0 |
| 2024-01-10 | -198.24 |
| 2024-01-24 | -191.21 |
| 2024-01-24 | 0 |
| 2024-02-08 | -99.18 |
| 2024-02-27 | 0 |
| 2024-04-05 | -188.79 |
| 2024-04-09 | -15.78 |
| 2024-04-24 | -299.83 |
| 2024-05-14 | -398.51 |
| 2024-05-29 | -160.03 |
| 2024-06-04 | -254.35 |
| 2024-06-11 | -244.94 |
| 2024-06-25 | 0 |
| 2024-07-18 | -97.15 |
| 2024-10-01 | 0 |
| 2024-10-24 | -95.34 |
| 2024-11-01 | 0 |
| 2024-12-24 | -94.2 |

_20 of 37 points, shape-preserving; min -$398.51 (2024-05-14), max $0.00 (2024-01-01), final -$94.20 (2024-12-24)._

## 2. Analytics Insights

#### Overview

- **Net profit:** $1,081.11
- **Trades analysed:** 36
- **Score:** 15 of 40 points
- **Tests:** 15 passed, 5 failed
- **Total potential improvement:** $49.68 _(sum over the failed tests; the tests overlap, so it is a ceiling, not a forecast)_
- **Trading style:** Likely Intraday
- **Median holding duration:** 3h 6m
- **Trading period:** 0 years, 11 months, 22 days

#### Behavioural strengths

- Adaptable
- Emotional Control
- Effective Stress Management

#### Behavioural weaknesses

- Greed Driven Decisions
- Poor Strategic Planning
- Inconsistent Execution

#### Failed tests

Each one below is a mistake the history shows, with what fixing it would have been worth and what to change. The amount beside a test is the improvement the test estimates, not profit observed.

#### ❌ Consider cautiously increasing position size after winning streaks (potential improvement +$49.68)

You sometimes increase risk after winning streaks, but analysis suggests a more strategic approach (what-if scenarios) could improve results.

Recommendations:
- Historical analysis shows you could improve net profit by $49.68 (4.6%) by doubling position size for just one trade after 2 consecutive wins. Note: This significantly increases risk.
- Another check flags positions far above your typical size, so these two tips point in opposite directions. The choice is yours: a larger size after a streak chases the missed profit, while consistent sizing protects your account.

Trades behind this verdict: 6.

#### ❌ Try using time-based exit rules or trailing stops

You have trades held significantly longer than your average.

Recommendations:
- Implement time-based exit rules or trailing stops to prevent holding trades beyond their optimal duration. Consider setting maximum holding periods based on your typical profitable trade duration.

#### ❌ Try maintaining consistent position sizes

We've detected trades with position sizes significantly larger than your typical size. Such inconsistencies can lead to oversized losses and often suggest emotional decision-making.

Recommendations:
- Develop and stick to a position sizing formula based on your account risk percentage. Avoid emotional trading that leads to sudden position size increases.
- Another check shows profit missed by not increasing your lot after a winning streak, so these two tips point in opposite directions. The choice is yours: consistent sizing protects your account, while a larger size after a streak chases the missed profit.

#### ❌ Try aiming for better Reward:Risk ratios

Your Reward:Risk ratios need improvement.

Recommendations:
- Set your take profit targets at least twice as far from entry as your stop loss. This ensures favorable risk-reward even with lower win rates.
- Manage open positions to achieve better reward:risk outcomes. Let winners run to target and cut losses at predetermined stops rather than closing early.

#### ❌ Try to reduce your maximum drawdown

Your worst drawdown relative to profit is 175.45%, which is too high. Your deepest drawdown in money ($398.51) happened at a different time.

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
- ✅ Consistent Loss Management
- ✅ Appropriate stop loss placement
- ✅ Direction bias analysis
- ✅ Return over Maximum Drawdown (RoMaD)

## 3. Exit Optimizer

_The optimizer ranks by net profit only; win rate and profit factor are shown, not optimized._

#### XAUUSD: best exit parameters (based on 36 trades)

- **Stop loss:** 6055.8 pips _(average loss as traded: 560.3 pips)_
- **Take profit:** 5985.0 pips _(average profit as traded: 714.8 pips)_
- **Max holding:** 3d 17h 8m _(median holding as traded: 3h 6m)_

#### XAUUSD: with the best exits vs as traded

| Metric | With the best exits | As traded |
| --- | --- | --- |
| Net profit | $5,020.74 | $1,081.11 |
| Profit factor | 2.25 | 1.66 |
| Win rate | 62.5% | 52.78% |
| Expected value per trade | $313.80 | $30.03 |
| Net result in display units | 26118.9 pips | 4056.2 pips |

_Same entries, exits re-simulated; distances are in the symbol’s display unit._

#### XAUUSD: the 10 best stop loss × take profit × holding combinations

| # | Stop loss | Take profit | Max holding | Net profit | Win rate | Profit factor |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 6055.8 pips | 5985.0 pips | 3d 17h 8m | $5,020.74 | 62.5% | 2.25 |
| 2 | 10402.0 pips | 5985.0 pips | 3d 17h 8m | $4,986.51 | 62.5% | 2.23 |
| 3 | none | 5985.0 pips | 3d 17h 8m | $4,986.51 | 62.5% | 2.23 |
| 4 | 6730.3 pips | 5985.0 pips | 3d 17h 8m | $4,946.55 | 62.5% | 2.21 |
| 5 | 7425.7 pips | 5985.0 pips | 3d 17h 8m | $4,870.05 | 62.5% | 2.17 |
| 6 | 8141.3 pips | 5985.0 pips | 3d 17h 8m | $4,791.34 | 62.5% | 2.13 |
| 7 | 8876.3 pips | 5985.0 pips | 3d 17h 8m | $4,710.49 | 62.5% | 2.09 |
| 8 | 9630.0 pips | 5985.0 pips | 3d 17h 8m | $4,627.58 | 62.5% | 2.05 |
| 9 | 6055.8 pips | 5392.1 pips | 3d 17h 8m | $4,597.37 | 62.5% | 2.14 |
| 10 | 10402.0 pips | 5392.1 pips | 3d 17h 8m | $4,563.14 | 62.5% | 2.12 |

_Ranked by net profit, the figure the optimizer maximises. "none" means the level was disabled._

#### XAUUSD: net profit vs stop loss (TP fixed at 5985.0 pips, holding at 3d 17h 8m — the best values)

| stop loss (pips) | Net profit (USD) |
| --- | --- |
| 171.5 | 222.14 |
| 433.3 | 2477.86 |
| 760.1 | 1569.35 |
| 1138 | 3857.55 |
| 1559 | 3578.36 |
| 2017.8 | 2729.58 |
| 2510.8 | 3431.74 |
| 3035 | 2561.56 |
| 3588 | 3912.64 |
| 4168.2 | 3829.26 |
| 4773.7 | 3320.64 |
| 5403.3 | 3795.33 |
| 6055.8 | 5020.74 |
| 6730.3 | 4946.55 |
| 7425.7 | 4870.05 |
| 8141.3 | 4791.34 |
| 8876.3 | 4710.49 |
| 9630 | 4627.58 |
| 10402 | 4986.51 |

_min $222.14 (171.5), max $5,020.74 (6055.8), final $4,986.51 (10402)._

#### XAUUSD: net profit vs take profit (SL fixed at 6055.8 pips, holding at 3d 17h 8m — the best values)

| take profit (pips) | Net profit (USD) |
| --- | --- |
| 219.6 | -1221.16 |
| 449.7 | -459.53 |
| 737 | 191.11 |
| 1069.2 | 453.79 |
| 1439.2 | -48.45 |
| 1842.6 | 362.1 |
| 2275.9 | 985.02 |
| 2736.7 | 1883.58 |
| 3222.9 | 2831.67 |
| 3732.8 | 2669.57 |
| 4265.1 | 3211.16 |
| 4818.5 | 3891.84 |
| 5392.1 | 4597.37 |
| 5985 | 5020.74 |
| 6596.2 | 3553.99 |
| 7225.2 | 3852.35 |
| 7871.3 | 3082.16 |
| 8533.9 | 3208.06 |
| 9212.5 | 2232.11 |

_min -$1,221.16 (219.6), max $5,020.74 (5985), final $2,232.11 (9212.5)._

#### XAUUSD: net profit vs max holding (SL fixed at 6055.8 pips, TP fixed at 5985.0 pips — the best values)

| max holding (duration) | Net profit (USD) |
| --- | --- |
| 4h 27m | -11.41 |
| 5h 42m | -79.55 |
| 7h 50m | 591.73 |
| 10h 30m | 203.25 |
| 13h 34m | 509.21 |
| 17h | -121.91 |
| 20h 44m | -97.13 |
| 1d 45m | 1202.37 |
| 1d 5h 2m | 489.64 |
| 1d 9h 32m | 681.18 |
| 1d 14h 16m | 329.28 |
| 1d 19h 13m | 1130.82 |
| 2d 21m | 2452.01 |
| 2d 5h 40m | 1636.35 |
| 2d 11h 10m | -71.02 |
| 2d 16h 51m | 1444.77 |
| 2d 22h 41m | 2967.19 |
| 3d 4h 41m | 3714.6 |
| 3d 10h 50m | 3547.54 |
| 3d 17h 8m | 5020.74 |

_min -$121.91 (17h), max $5,020.74 (3d 17h 8m), final $5,020.74 (3d 17h 8m)._

## 4. Entry / Exit Efficiency

_34 of 36 filtered trade rows are included. 2 filtered trade rows were excluded._

#### Favorable move captured

- **Median capture:** 60.0% _(realized result as a share of the best move in the trade’s favour, all trades)_
- **Winning-trade median:** 91.1%
- **Money-weighted capture:** 24.4% _(total money earned over total money the best favourable moves offered)_
- **Average open loss on winners:** $30.33 _(deepest open loss sat through before a winner closed)_
- **Average open loss on losers:** $110.02
- **Winners with open loss above profit:** 0.0%

#### E-ratio in the first bars after entry

- **5 bars:** — _(fewer than 30 measurable trades, so no ratio is shown; 0 eligible, 34 unavailable)_
- **10 bars:** — _(fewer than 30 measurable trades, so no ratio is shown; 0 eligible, 34 unavailable)_
- **20 bars:** — _(fewer than 30 measurable trades, so no ratio is shown; 0 eligible, 34 unavailable)_

## 5. Drawdown Anatomy

_Trade-close estimate: it does not see what happened while trades were open, so the real drawdown can be deeper. Loading full equity now._

- **Maximum drawdown:** 3.78%
- **Maximum drawdown, money:** $398.51 _(Largest drop below a previous peak, in money, across all drawdowns. It can differ from the percent card and from the table: each drawdown is measured against its own peak, so a larger account can lose more money in a shallower fall. Until full equity has loaded it is measured only at trade closes, so it does not see falls while trades were open and can be smaller than the Drawdown card, whose caption says how often that card checks.)_
- **Longest underwater:** 3.8 mo
- **Average recovery:** 39d 9h _(Average time from falling below a peak to making a new one, for drawdowns that recovered. A dash means none have recovered yet.)_
- **Ulcer Index:** 1.49%

#### Underwater equity

| Date | Below the high-water mark (%) |
| --- | --- |
| 2024-01-02 | 0 |
| 2024-01-08 | -0.98 |
| 2024-01-10 | -1.96 |
| 2024-01-24 | -1.89 |
| 2024-01-30 | 0 |
| 2024-02-08 | -0.95 |
| 2024-02-27 | 0 |
| 2024-04-09 | -0.15 |
| 2024-04-10 | -1.05 |
| 2024-05-14 | -3.78 |
| 2024-05-17 | -2.61 |
| 2024-05-27 | -3.55 |
| 2024-06-06 | -1.38 |
| 2024-06-11 | -2.33 |
| 2024-06-25 | 0 |
| 2024-07-18 | -0.9 |
| 2024-10-01 | 0 |
| 2024-10-24 | -0.87 |
| 2024-11-01 | 0 |
| 2024-12-24 | -0.84 |

_20 of 36 points, shape-preserving; min -3.78% (2024-05-14), max 0.00% (2024-01-02), final -0.84% (2024-12-24)._

#### The 5 deepest drawdowns in percent, deepest first.

| Depth | Depth, money | Start | Trough | Recovery | Duration | Trough to recovery | Trades | Cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.78% | $398.51 | 29 Feb 2024 06:32 | 14 May 2024 08:30 | 24 Jun 2024 21:46 | 3.8 mo | 41d 13h | 15 | — |
| 1.96% | $198.24 | 08 Jan 2024 18:45 | 09 Jan 2024 20:50 | 24 Jan 2024 08:06 | 15d 13h | 14d 11h | 5 | — |
| 0.95% | $99.18 | 07 Feb 2024 21:54 | 07 Feb 2024 21:54 | 27 Feb 2024 02:23 | 19d 4h | 19d 4h | 3 | — |
| 0.90% | $97.15 | 18 Jul 2024 06:19 | 18 Jul 2024 06:19 | 23 Sep 2024 09:42 | 2.2 mo | 2.2 mo | 2 | — |
| 0.88% | $96.55 | 07 Oct 2024 08:31 | 07 Oct 2024 08:31 | 16 Oct 2024 22:03 | 9d 14h | 9d 14h | 2 | — |

_Showing the 5 deepest of 7 drawdowns, sorted by depth in percent._

## 6. Win/Loss & Long/Short Breakdown

- **Total trades:** 36
- **Winnings:** 19/36 (52.78%)
- **Losing:** 17/36 (47.22%)
- **Long trades:** 24/36 (66.67%)
- **Short trades:** 12/36 (33.33%)
- **Profit on longs:** $1,039.36
- **Profit on shorts:** $41.75

## 7. Rolling Performance

_Measured over 36 closed trades matching the filters, in close-time order._

#### Last 30 trades vs overall

- **Average trade, last 30 trades:** $30.35 _(+$0.32 vs overall)_
- **Average trade, overall:** $30.03
- **Win rate, last 30 trades:** 53.33% _(+0.56 pp vs overall)_
- **Win rate, overall:** 52.78%

#### Verdict

- Average trade over the last 30 trades is $30.35, in line with the overall $30.03. Counted as above or below once the gap exceeds 20% of the overall value.
- Win rate over the last 30 trades is 53.33%, in line with the overall 52.78%. Counted as above or below overall once the gap exceeds 5 percentage points.

#### Average trade over the last 30 trades, window by window

| Trade number (close-time order) | Average trade (USD) |
| --- | --- |
| 30 | 33.05 |
| 31 | 26.06 |
| 32 | 33.1 |
| 33 | 33.22 |
| 34 | 34.32 |
| 35 | 41.78 |
| 36 | 30.35 |

_min $26.06 (trade 31), max $41.78 (trade 35), final $30.35 (trade 36); overall $30.03._

## 8. Tag Analytics

_Nothing to report for the current trades and filters._

## 9. Symbol Analysis

#### Trades Breakdown by Symbol

| Symbol | Trades | Wins | Losses | Win rate | Lots | Profit | Loss | Net profit | Profit factor | Profit / loss share of turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XAUUSD | 36 | 19 | 17 | 52.78% | 7.8 | $2,723.84 | $1,642.73 | $1,081.10 | 1.66 | 62.38% / 37.62% |

_Win rate counts break-even trades in the total but on neither side, as the bars do._

## 10. Performance by Session

#### Trade Activity by Session

| Session | Hours | Trades | Share of analysed trades | Net Profit | Avg. Profit per Trade | Win Rate | Profit Factor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| London Silver Bullet | 08:00-09:00 London time | 4 | 11.11% | $760.38 | $190.09 | 100.0% | --- |
| London Session | 08:00-17:00 London time | 21 | 58.33% | $1,003.14 | $47.77 | 57.1% | 2.17 |
| Asian Session | 09:00-18:00 Tokyo time | 13 | 36.11% | $931.74 | $71.67 | 69.2% | 3.38 |
| New York AM Silver Bullet | 10:00-11:00 New York time | 1 | 2.78% | $108.70 | $108.70 | 100.0% | --- |
| New York Session | 08:00-17:00 New York time | 14 | 38.89% | $270.63 | $19.33 | 50.0% | 1.40 |
| Outside sessions | — | 2 | 5.56% | $30.06 | $15.03 | — | — |

_Shares are of the 36 trades analysed. Sessions overlap: 36 trades are counted 53 times in total, because a trade opened while two sessions run counts in both. Outside sessions: These trades were opened when none of the five session windows was active. The windows follow city hours and do not cover the whole day._

The session test's verdict and recommendations are in Analytics Insights, under "✅ Trading session analysis".

## 11. Monte Carlo Simulation

#### Risk and outcome summary

- **Average trade result:** $30.03
- **Median ending balance:** $11,021.93
- **Average ending balance:** $11,034.72
- **Where most endings landed (middle 90%):** $9,825.89 - $12,312.31
- **Chance of profit:** 91.60% ± 0.88%
- **Chance of ruin (below 50%):** 0.00% ± 0.00% _(ruin level $5,000.00)_
- **Worst-case drawdown:** $883.60 (8.57%) _(The amount and the percentage are ranked separately, so they may come from different paths.)_
- **Median maximum drawdown:** $458.02 (4.18%) _(The amount and the percentage are ranked separately, so they may come from different paths.)_
- **Average of worst 5% endings:** $9,519.84

- Ended above the starting balance in 91.60% of runs.
- The balance fell to $5,000.00 or below in 0.00% of simulations.
- Your 36 real trades would end at $11,081.11 from this starting balance. Deposits and withdrawals are excluded, as in the simulation.

#### Simulation parameters

- **Starting balance:** $10,000.00
- **Trades per simulation:** 36
- **Number of simulations:** 1000
- **Trade order:** Random picks
- **Trade size:** Same money amounts

#### Simulated outcomes: Median

| Trade number | Balance (USD) |
| --- | --- |
| 0 | 10000 |
| 1 | 10098.88 |
| 2 | 10039.7 |
| 5 | 10158.34 |
| 6 | 10152.66 |
| 9 | 10261.59 |
| 10 | 10272.47 |
| 13 | 10353.98 |
| 15 | 10424.76 |
| 16 | 10457.73 |
| 18 | 10499.22 |
| 20 | 10550.27 |
| 23 | 10626.97 |
| 24 | 10671.76 |
| 26 | 10712.06 |
| 29 | 10837.02 |
| 31 | 10864.86 |
| 32 | 10923.97 |
| 34 | 10985.77 |
| 36 | 11021.93 |

_20 of 37 points, shape-preserving; min $10,000.00 (Trade 0), max $11,021.93 (Trade 36), final $11,021.93 (Trade 36)._

#### Maximum drawdowns

| Maximum drawdown | Simulations | Share of simulations | At or below |
| --- | --- | --- | --- |
| 0.00% - 1.50% | 0 | 0.00% | 0.00% |
| 1.50% - 3.00% | 228 | 22.80% | 22.80% |
| 3.00% - 4.50% | 333 | 33.30% | 56.10% |
| 4.50% - 6.00% | 229 | 22.90% | 79.00% |
| 6.00% - 7.50% | 116 | 11.60% | 90.60% |
| 7.50% - 9.00% | 51 | 5.10% | 95.70% |
| 9.00% - 10.50% | 29 | 2.90% | 98.60% |
| 10.50% - 12.00% | 6 | 0.60% | 99.20% |
| 12.00% - 13.50% | 8 | 0.80% | 100.00% |

_Median maximum drawdown: 4.18%. Worst-case drawdown (only 1 in 20 paths went deeper): 8.57%. Largest seen: 13.40%. Random picks break up your streaks, which can hide larger drawdowns. Use 'Keep streaks' for a more realistic view._

## 12. Risk & Performance Metrics

_This section shows full data. Filtering will be added soon._

#### Income

- **Net profit:** $1,081.1
- **Average trade:** $30.03
- **Gross profit:** $2,723.84
- **Gross loss:** $1,642.73
- **Profit / month:** $89.7
- **Average profit:** $143.36
- **Average loss:** $96.63
- **Max drawdown:** $185.05
- **Max current day loss %:** 0%
- **Profit factor:** 1.66
- **Return %:** 10.81%

#### Trades

- **Total trades:** 36
- **Trading days:** 35
- **Profit trades:** 19
- **Loss trades:** 17
- **Max consecutive profit trades:** 3
- **Max consecutive loss trades:** 4
- **Trades / day:** 0.1
- **Trades / month:** 2.99
- **Profit trades / month:** 1.58
- **Loss trades / month:** 1.41
- **Max profit trade:** $248.93
- **Max loss trade:** $99.46
- **Total volume traded:** $1.7m
- **Average order size:** $48.6k

#### Time

- **Days processed:** 366.85
- **Months processed:** 12.05

#### Other

- **Max lot used:** 0.44
- **Restoration factor:** 5.84
- **Reliability factor:** 0.48
- **Win rate %:** 52.78%
- **Loss rate %:** 47.22%
- **Number of times TP or SL was changed:** 0
- **Number of trades without TP or SL:** 0
- **Amount of time to set TP or SL:** 0
- **Average win/loss ratio 1:2:** 0.58
- **Average win/loss ratio 1:3:** 0
- **Average win/loss ratio 1:4:** 0
- **Average win/loss ratio 1:5:** 0
- **Daily Sharpe Ratio:** N/A
- **Monthly Sharpe Ratio:** N/A
- **Daily Sortino Ratio:** N/A
- **Monthly Sortino Ratio:** N/A

## 13. Drawdown luck check

How this works: your trades are shuffled 2,000 times and your real drawdown is compared with the shuffled ones. If your drawdown is ordinary for these trades, nothing special happened. If it is deeper than almost all shuffles, your losses bunched together in time — a bad month, a market change, tilt — rather than falling randomly.

#### Nothing unusual about the sequence of your trades

Your deepest fall of $398.51 is ordinary for these trades: shuffles usually fall $288.31 - $706.51 (median $425.24), and 46% of them were milder than yours. About one ordinary history in ten lands outside this range by chance. With 36 trades, one trade more or less can move these shares noticeably — read them as rough, not exact. Your deepest fall is counted on closed results in the order they happened, so it matches the drawdown curve in Performance Over Time; the Drawdown card can show a deeper fall when its caption says it checks every tick. What to do: Plan for a $706.51 fall, and do not read the drawdown as a verdict on the strategy.

#### Longest losing run

| Your run | Middle 90% of shuffles | Shuffles shorter | Shuffles same | Shuffles longer | Reading |
| --- | --- | --- | --- | --- | --- |
| 4 | 3 - 6 | 34% | 35% | 32% | Normal for a 53% win rate over 36 trades: 3 - 6 (median 4). |

_What to do: Put any "stop for the day" or "cut size" rule above 6 so a normal run does not trigger it._

- **Eligible trades:** 36 _(19 wins, 17 losses, 0 breakevens)_
- **Shuffles:** 2000

#### What it cannot tell you

Whether the trades are good — a losing strategy can have a perfectly ordinary sequence. It ignores deposits, balance and margin, uses only the trades you filtered, and one history in ten lands outside the middle range by pure chance. With fewer than about 50 trades one trade can move the share noticeably. 2,000 shuffles are an estimate: each share shown is usually within one or two points.

## 14. Prop Challenge pass probability

_Based on 36 usable closed trades across 358 calendar days. Advanced Analytics filters affect this estimate._

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

- **Estimated pass chance within 90 days:** 1.6% _(95%: 1.0–2.6%)_
- **Failed daily-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Failed total-loss rule:** 0.0% _(95%: 0.0–0.4%)_
- **Not decided within the horizon:** 98.4% _(95%: 97.4–99.0%)_
- **Median calendar days to pass (passed attempts only):** 72
- **Median trades to pass (passed attempts only):** 10

#### Simulated account balance, Day 90

- **Median attempt:** 2.79%
- **Low outcome (5%):** -2.33%
- **High outcome (95%):** 8.10%

#### Simulated account balance: Median attempt

| Calendar days | Account change (%) |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 9 | 0 |
| 13 | 0 |
| 15 | 0.04 |
| 24 | 0.39 |
| 26 | 0.56 |
| 30 | 0.63 |
| 37 | 1.13 |
| 43 | 1.2 |
| 47 | 1.41 |
| 51 | 1.48 |
| 57 | 1.65 |
| 61 | 1.86 |
| 65 | 1.92 |
| 73 | 2.22 |
| 79 | 2.29 |
| 84 | 2.59 |
| 87 | 2.64 |
| 90 | 2.79 |

_20 of 91 points, shape-preserving; min 0.00% (Day 0), max 2.79% (Day 90), final 2.79% (Day 90)._

- The testing window runs from your first closed trade to your last; quiet time before or after is not counted.

## 15. Profitability Heatmap

_Trades are grouped by close time in America/New_York (UTC-5)._

- **Coloured by:** Avg PnL
- **Minimum trades per hour:** 1
- **Eligible trades:** 36
- **Hours with trades:** 25

#### Best hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Wednesday | 05:00-06:00 | $213.85 | 1 | 100.00% |
| Monday | 07:00-08:00 | $197.55 | 1 | 100.00% |
| Monday | 09:00-10:00 | $150.77 | 1 | 100.00% |
| Monday | 21:00-22:00 | $138.94 | 1 | 100.00% |
| Friday | 13:00-14:00 | $137.91 | 1 | 100.00% |
| Wednesday | 11:00-12:00 | $126.18 | 1 | 100.00% |
| Friday | 09:00-10:00 | $123.82 | 1 | 100.00% |
| Wednesday | 22:00-23:00 | $111.67 | 1 | 100.00% |
| Thursday | 11:00-12:00 | $108.7 | 1 | 100.00% |
| Tuesday | 02:00-03:00 | $107.83 | 3 | 100.00% |

_Hours with only one or two trades are marked as a small sample. Treat them as noise until more trades build up._

#### Worst hours by Avg PnL

| Weekday | Hour | Avg PnL | Trades | Win rate |
| --- | --- | --- | --- | --- |
| Monday | 18:00-19:00 | -$99.46 | 1 | 0.00% |
| Sunday | 22:00-23:00 | -$99.2 | 1 | 0.00% |
| Tuesday | 20:00-21:00 | -$98.26 | 2 | 0.00% |
| Monday | 08:00-09:00 | -$96.55 | 1 | 0.00% |
| Thursday | 06:00-07:00 | -$96.49 | 2 | 0.00% |

#### Totals by weekday

| Weekday | Trades | Total PnL | Avg PnL | Profit factor | Win rate |
| --- | --- | --- | --- | --- | --- |
| Sunday | 2 | -$193.9 | -$96.95 | 0.00 | 0.00% |
| Monday | 5 | $291.26 | $58.25 | 2.49 | 60.00% |
| Tuesday | 13 | $90.67 | $6.97 | 1.13 | 46.15% |
| Wednesday | 9 | $903.95 | $100.44 | 5.66 | 77.78% |
| Thursday | 4 | -$179.63 | -$44.91 | 0.38 | 25.00% |
| Friday | 3 | $168.76 | $56.25 | 2.82 | 66.67% |
| Saturday | 0 | $0 | — | N/A | N/A |

## 16. Trading Activity Calendar

#### Month by month

| Month | Trades | Net result | Trading days | Profitable / losing days |
| --- | --- | --- | --- | --- |
| January 2024 | 8 | $434.19 | 8 | 5 / 3 |
| February 2024 | 4 | $3.71 | 4 | 2 / 2 |
| March 2024 | 0 | — | 0 | 0 / 0 |
| April 2024 | 5 | -$204.00 | 4 | 1 / 3 |
| May 2024 | 4 | $139.80 | 4 | 2 / 2 |
| June 2024 | 5 | $207.71 | 5 | 3 / 2 |
| July 2024 | 2 | $100.39 | 2 | 1 / 1 |
| August 2024 | 0 | — | 0 | 0 / 0 |
| September 2024 | 1 | $150.77 | 1 | 1 / 0 |
| October 2024 | 4 | $78.66 | 4 | 2 / 2 |
| November 2024 | 2 | $264.09 | 2 | 2 / 0 |
| December 2024 | 1 | -$94.21 | 1 | 0 / 1 |

_A month with 0 trades had none in the filtered history._

## 17. Trading Activity by Hour

_Trades are grouped by close time in America/New_York (UTC-5)._

#### Trading activity by hour

| hour | Profitable trades | Losing trades | Net (profitable - losing) |
| --- | --- | --- | --- |
| 00 | 1 | 1 | 0 |
| 01 | 0 | 0 | 0 |
| 02 | 3 | 0 | +3 |
| 03 | 1 | 1 | 0 |
| 04 | 0 | 0 | 0 |
| 05 | 1 | 0 | +1 |
| 06 | 0 | 2 | -2 |
| 07 | 1 | 0 | +1 |
| 08 | 3 | 5 | -2 |
| 09 | 2 | 1 | +1 |
| 10 | 0 | 0 | 0 |
| 11 | 2 | 0 | +2 |
| 12 | 1 | 0 | +1 |
| 13 | 1 | 0 | +1 |
| 14 | 0 | 0 | 0 |
| 15 | 0 | 0 | 0 |
| 16 | 0 | 0 | 0 |
| 17 | 0 | 0 | 0 |
| 18 | 0 | 2 | -2 |
| 19 | 0 | 0 | 0 |
| 20 | 0 | 2 | -2 |
| 21 | 2 | 2 | 0 |
| 22 | 1 | 1 | 0 |
| 23 | 0 | 0 | 0 |

## 18. Duration & Profitability

- **Analyzed trades:** 36
- **Net profit:** $1,081.11
- **Holding-time ranges:** 6
- **Median holding time:** 3h 6m

#### Key insights

- **Winner vs loser holding time:** The median losing trade was held 1.1x longer than the median winning trade. Winner median: 3h 6m; loser median: 3h 30m.
- **Profit concentration:** Your top 5% of trades generated 17.0% of your total winning profit.

#### Holding time and results

| Holding time | Trades | Winners | Losers | Breakeven | Win rate | Total profit | Average PnL | Median PnL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5m-15m | 2 | 1 | 1 | 0 | 50.0% | $27.51 | $13.75 | $13.75 |
| 15m-1h | 2 | 1 | 1 | 0 | 50.0% | $39.76 | $19.88 | $19.88 |
| 1h-4h | 18 | 10 | 8 | 0 | 55.6% | $591.23 | $32.85 | $101.83 |
| 4h-8h | 6 | 4 | 2 | 0 | 66.7% | $453.87 | $75.65 | $119.28 |
| 8h-1d | 5 | 2 | 3 | 0 | 40.0% | $8.96 | $1.79 | -$94.21 |
| 1d-3d | 3 | 1 | 2 | 0 | 33.3% | -$40.22 | -$13.41 | -$94.7 |

#### Profit distribution

| Net PnL range | Trades |
| --- | --- |
| <-$250 | 0 |
| -$250 to -$200 | 0 |
| -$200 to -$150 | 0 |
| -$150 to -$100 | 0 |
| -$100 to -$50 | 17 |
| -$50 to $0 | 0 |
| $0 to $50 | 0 |
| $50 to $100 | 2 |
| $100 to $150 | 10 |
| $150 to $200 | 5 |
| $200 to $250 | 2 |
| >$250 | 0 |

_Average $30.03; median $99.36_

#### Holding time by outcome

| Holding time | Loss | Win | Big win | Trades | Win rate | Average result | Total profit | Held past this range |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5m-15m | 50.0% (1) | 50.0% (1) | 0.0% (0) | 2 | 50.0% | $13.75 | $27.51 | $1,053.6 (34) |
| 15m-1h | 50.0% (1) | 50.0% (1) | 0.0% (0) | 2 | 50.0% | $19.88 | $39.76 | $1,013.84 (32) |
| 1h-4h | 44.4% (8) | 50.0% (9) | 5.6% (1) | 18 | 55.6% | $32.85 | $591.23 | $422.61 (14) |
| 4h-8h | 33.3% (2) | 50.0% (3) | 16.7% (1) | 6 | 66.7% | $75.65 | $453.87 | -$31.27 (8) |
| 8h-1d | 60.0% (3) | 40.0% (2) | 0.0% (0) | 5 | 40.0% | $1.79 | $8.96 | -$40.22 (3) |
| 1d-3d | 66.7% (2) | 33.3% (1) | 0.0% (0) | 3 | 33.3% | -$13.41 | -$40.22 | $0 (0) |

_Cells: share of the row (trade count). Held longer: total PnL (trades) of the trades held past this range._
