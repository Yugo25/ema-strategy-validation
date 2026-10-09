# Research log

How the work progressed, in the order the Forex Tester projects were created. Dates are the
labels I gave each project. The two unlabelled tests were early explorations; their exact
order is not recorded.

| Order | Project label | Test | Strategy | What it was for |
|---|---|---|---|---|
| — | `20EMA-5m` | XAUUSD-5m-20EMA-early | 20EMA | Early exploration of the 20EMA idea on gold |
| — | `20EMA-swing` | GBPUSD-20EMA-swing | 20EMA | Same idea held for days on 1h |
| 1 | `4/21 EMA swing strategy` | EURUSD-1h-200EMA | 200EMA | First structured test of the 200EMA method, on 1h |
| 2 | `5/12 200EMA-5m` | XAUUSD-5m-200EMA-2023 | 200EMA | Move the 200EMA method to 5m execution |
| 3 | `5/19 Day-trading EMA` | EURUSD-5m-hybrid-1 | Hybrid | Trade both setups side by side on one pair |
| 4 | `5/25 200EMA` / `5/25 20EMA` | AUDUSD-200EMA, AUDUSD-20EMA | both | Same pair, same period, each strategy separately: a head-to-head comparison |
| 5 | `6/1 200EMA` / `6/1 20EMA` | XAUUSD-200EMA, XAUUSD-20EMA | both | Repeat the head-to-head on gold |
| 6 | `6/8 200EMA` | EURAUD-200EMA | 200EMA | Test on a cross pair |
| 7 | `6/16 200EMA` | USDCAD-200EMA | 200EMA | Test on a USD-base pair (different trend character) |
| 8 | `6/22 EMA` | EURUSD-5m-hybrid-2 | Hybrid | Hybrid again, over a longer EURUSD period |

## Rule changes driven by the data

**200EMA: higher-timeframe slope filter (STEP 0).**
Reviewing losing trades showed they clustered in phases where I had traded the EMA cross
while the higher-timeframe 200EMA was flat, i.e. a range. The 200EMA tests' only losing
quarter is 2024 Q2 (−2.7R over 18 trades). A cross says *where to look*; it doesn't say the
market is trending. I added a separate pass/fail gate requiring the 200EMA on two higher
timeframes to slope in the trade direction.

**200EMA: what counts as a valid trendline.**
Several stop-outs came from "breaks" of lines drawn through slow drifts or tight ranges.
These are build-up, not pullbacks. The rule now requires the line to connect swings price
actually reacted to, forming a recognisable reversal structure. It also adds explicit skip
heuristics (line through the middle of a cluster; three equally valid lines).

**20EMA: revised entry conditions.**
The revised version adds two preconditions before a 20EMA touch qualifies: a visible
broken trend structure on the left, and a completed first wave. It also requires the target
to come from inside that broken structure.

**Process: from judgement to a rubric.**
To reduce "close enough" decisions, every candidate setup is now graded against a fixed
multi-factor rubric, with numbers computed from market data instead of eyeballed from the
chart. The rubric itself is kept private.

## What the numbers say about the process

- The earliest, smallest tests show the highest expectancy (+0.76R to +1.09R). As tests got
  larger (36+ trades), results settled in a **+0.2R to +0.45R** band. That is consistent with early
  small-sample luck and/or looser early judgement. I treat the large tests as the realistic
  estimate.
- In both head-to-head comparisons the 200EMA version came out ahead (AUDUSD +0.43R vs
  +0.22R, XAUUSD +0.36R vs +0.31R net). Both gaps are well inside the noise, though. Pooled
  over all tests, the 20EMA is slightly *ahead*, and the permutation test finds no
  detectable difference (p ≈ 0.86).

## Next

1. Freeze the current rules and the rubric version.
2. Forward test on demo, logged with the same export format, and add it as a true out-of-sample set.
3. Track rule adherence per trade, so results can be split by "rubric-compliant" vs "not".
