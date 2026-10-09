# Methodology

## 1. How the backtests were run

| Item | Setting |
|---|---|
| Platform | [Forex Tester](https://forextester.com/) — bar-by-bar manual replay of historical data |
| Execution | Discretionary: each trade was taken by hand by following the written rules ([200EMA](strategy-200ema.md), [20EMA](strategy-20ema.md)) |
| Account | $10,000 starting balance per test, USD |
| Risk | Fixed fractional, ≈1% of balance per trade (median $ value of 1R across all trades: ≈$99) |
| Orders | Stop-loss always set at entry; take-profit at the planned target or a manual exit |
| Costs | Commission as configured in Forex Tester (non-zero for FX pairs, ≈0 for XAUUSD); no swap was charged |
| Instruments | XAUUSD, EURUSD, AUDUSD, EURAUD, USDCAD, GBPUSD |
| Timeframes | 5m execution (most tests), 1h execution (two tests) — see [`data/manifest.csv`](../data/manifest.csv) |
| Period | Trades closed between 2023-01 and 2025-12 |

Each Forex Tester project produced two exports, both kept unmodified in `data/raw/`:

- `trades/*.csv`: the trade history (entry, exit, stop, target, lots, commission, P&L).
- `forextester_reports/*.md`: Forex Tester's "Advanced Analytics" report.

**Only the trade CSVs feed the analysis.** The reports are kept as an independent check:
`tests/test_load.py` asserts that the parser reproduces each report's trade count, win rate,
profit factor and net P&L.

## 2. Unit of measurement: R

Results are measured in **R**, i.e. multiples of the risk taken on the trade:

```
R_gross = direction × (exit − entry) / |entry − stop|          direction = +1 long, −1 short
R_net   = profit_$ / ($ value of 1R),   $ value of 1R = gross_profit_$ / R_gross
```

- R is independent of position size, account currency and instrument, so tests on gold and
  on FX pairs can be pooled.
- No loss exceeds −1R gross: 183 of 185 losing trades are exact stop-outs, and the other 2
  were closed early (−0.28R, −0.52R). (R uses the stop recorded at exit, so a stop moved
  before exit cannot be detected from this export.)
- **Net R is used for every headline number.** Commission costs 0.08–0.10R per trade on the
  5m FX tests, i.e. 15–30 % of their gross edge, so ignoring it would overstate results.
- With ≈1 % risk per trade, cumulative R ≈ non-compounded % return.

## 3. Metrics

| Metric | Definition |
|---|---|
| Win rate | share of trades with R > 0 |
| Payoff | average winning R / average losing R |
| Breakeven win rate | `1 / (1 + payoff)`: the win rate at which expectancy is zero |
| Profit factor | gross winning R / gross losing R (the $ version is shown for cross-checking) |
| Expectancy, E[R] | mean R per trade |
| Max drawdown (R) | largest peak-to-trough fall of cumulative R, starting from 0 |
| Max drawdown (%) | same, on the $ equity curve, as % of the running peak |
| Losing streak | longest run of consecutive losing trades |

## 4. Statistical tests

All resampling uses a fixed seed (42), so `make report` is byte-for-byte reproducible;
CI enforces this.

- **Bootstrap CI of expectancy.** 20,000 resamples of the trades with replacement; percentile
  95 % interval. `P(E ≤ 0)` is the share of resampled means at or below zero, a direct
  answer to "how likely is it that this edge is zero or negative?"
- **t statistic** of mean R against zero (in the tables CSV), as a parametric cross-check.
- **Permutation test** for differences between strategies. The strategy labels are shuffled
  20,000 times, and the p-value is the share of shuffles with an absolute difference in mean R
  at least as large as observed.
- **Monte Carlo.** 10,000 synthetic sequences of 100 trades drawn from each strategy's
  observed R distribution. It gives the drawdown, losing streak and outcome range to expect
  if future trades resemble past ones.

## 5. Data cleaning

| Issue | Handling |
|---|---|
| Header lines `sep=,` and `Trade History` before the column names | skipped |
| `DEPOSIT` rows | dropped (not trades) |
| One open time exported as `1899-12-30` (AUDUSD-200EMA, trade #5) | set to missing; affects hold time only. This is why Forex Tester reports a "125-year" trading period for that test |
| Forex Tester's drawdown figure (e.g. $0.52 for a test with a 4.6R losing run) | not used; drawdown is recomputed from the trade sequence |
| File names start with a year, but several tests run into 2025 | the year in the name is the start year; analysis uses the actual close timestamps |

## 6. Limitations

Please read results with these in mind:

1. **Manual, discretionary backtests.** Replay hides the future, but the tester still knows
   the general market history (e.g. that gold trended up in 2024–25), and rule application
   involves judgement. This is the single biggest source of optimism bias.
2. **Not out-of-sample.** The rules were refined *while* these tests were run (see the
   [research log](research-log.md)). There is no untouched hold-out period yet.
3. **Small samples per test.** 5–64 trades per test. Most single-test confidence intervals
   include zero; only the pooled results are statistically conclusive.
4. **Execution costs.** Commission is included and spread is in the replayed prices, but
   slippage, requotes and latency are not modelled. A 5m strategy with tight stops is
   sensitive to these.
5. **Independence assumption.** The bootstrap and Monte Carlo treat trades as independent
   and identically distributed. Regime changes (trend vs range) violate this, so tail
   estimates (95th-percentile drawdown) are likely understated.
6. **Pooling across instruments** assumes R is comparable across markets, which is
   reasonable for a fixed-risk process but hides instrument-specific behaviour.

The planned next step is a forward test (demo, then small live size) under the frozen rules,
with results added to this repository using the same pipeline.
