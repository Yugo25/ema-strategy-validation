# Roadmap: systematic baselines

Phase 1 (this repository today) shows that the **manual** backtests have a positive
expectancy after costs. It cannot say **where that edge comes from**. Phase 2 answers that
by putting the manual trades next to systematic baselines run on the same price data.

## Questions

| # | Question | Why it matters |
|---|---|---|
| Q1 | Did the manual trades follow the higher-timeframe slope filter, and did compliant trades do better? | Tests the rule change in the [research log](research-log.md) with data, not memory |
| Q2 | Would **random entries with the same stop/target structure** produce the same result? | Separates entry skill from the payoff structure (a 1.6 payoff needs only a 39% win rate) |
| Q3 | Does the **trend filter alone** create an edge? | Measures how much comes from "trade with the trend", which is cheap to replicate |
| Q4 | How does a **mechanical version** of each strategy compare with the manual one? | The difference estimates the value of discretionary selection: the "discretion premium" |
| Q5 | Did manual exits help or hurt compared with holding to the planned stop/target? | Measures exit discipline; `tp` and `sl` are already in the exports |

## Data

- **Prices:** Dukascopy historical bid/ask candles, free. 1m bars for trade simulation,
  resampled to 5m, 30m, 1h, 4h and daily for indicators. Instruments: XAUUSD, EURUSD,
  AUDUSD, EURAUD, USDCAD, GBPUSD. Period 2023-01 to 2025-12.
- Raw downloads go to `data/external/` (git-ignored), fetched by `scripts/fetch_prices.py` with
  recorded checksums, so anyone can rebuild the same dataset.
- **Timestamp alignment check (gate before any analysis):** every manual trade's entry price
  must fall inside the matching 1m bar's bid/ask range. This detects timezone or feed offsets
  between Forex Tester and Dukascopy.

## Experiments

**E1 — Rule-adherence audit (Q1).** For every manual entry, compute the 200EMA slope on the
two reference timeframes using closed bars only. Split trades into compliant and
non-compliant, then compare expectancy with bootstrap CIs and a permutation test.
*Cheapest experiment; do it first.*

**E2 — Exit-matched random entries (Q2).** For each manual trade, draw random entry times
from the same instrument and test period. Keep the direction mix, the stop distance (in ATR
units) and the planned target (in R, from `tp`/`sl`). Simulate each to stop or target on 1m
bars; if both are hit inside one bar, assume the stop (conservative). Repeat 1,000 times to
get a null distribution of E[R], then report the percentile of the manual result.

**E3 — Trend-filtered random entries (Q3).** E2, but entries are only allowed in the direction
the slope filter permits. E3 − E2 is the value of the filter; manual − E3 is the value of
everything else (setup + trigger + selection).

**E4 — Mechanical skeleton (Q4).** Code the objective parts of each strategy: slope filter,
EMA cross, EMA touch, a pivot-based structure-break trigger with pivots confirmed with a lag,
swing stop, measured-move target limited to 1:1–1:3. Run it on all data. Report E[R], trade
count, overlap with the manual trades, and the discretion premium with a bootstrap CI.

**E5 — Exit replay (Q5).** Re-simulate each manual entry holding to its planned stop and
target, then compare with the actual manual exits.

## Rules that keep it honest

- **No look-ahead.** Indicators use closed bars only; pivots count only after confirmation.
- **Costs.** Fills use bid/ask, and commission matches the Forex Tester settings.
- **Public definitions only.** The slope filter and trigger use simple, published
  definitions (e.g. EMA slope over N bars scaled by ATR), not the private grading rubric.
  The results measure a public proxy of the strategy, and the docs say so.
- **Parameters fixed before running.** Parameters are written in this file before running.
  Any later change is logged as a separate run, not overwritten.
- **Multiple comparisons.** Five experiments and several splits; conclusions rely on effect
  sizes and CIs, not on any single p-value.

## Code plan

```
src/emaresearch/prices.py      load/resample candles, alignment check
src/emaresearch/indicators.py  EMA, ATR, slope, confirmed pivots
src/emaresearch/simulate.py    bar-by-bar stop/target simulator (bid/ask aware)
src/emaresearch/baselines.py   E1–E5
scripts/fetch_prices.py        reproducible download
scripts/run_baselines.py       → reports/baselines.md + figures
tests/test_simulate.py         synthetic bars with known stop/target hits, same-bar rule, gaps
```

Order of work: E1 → E5 → E2 → E3 → E4, cheapest and most informative first.
