"""Rebuild every table and figure in reports/ from the raw Forex Tester exports.

Usage:  python scripts/build_report.py
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emaresearch import plots, stats  # noqa: E402
from emaresearch.load import load_all, load_manifest  # noqa: E402
from emaresearch.metrics import summarize, summarize_by  # noqa: E402

REPORTS = ROOT / "reports"
FIGURES = REPORTS / "figures"
TABLES = REPORTS / "tables"
STRATEGIES = ["200EMA", "20EMA", "Hybrid"]
# Each test is its own $10k account, so $-equity metrics are meaningless once tests are pooled.
ACCOUNT_LEVEL = ["net_profit", "net_return_pct", "max_dd_pct"]
MC_HORIZON = 100


def with_bootstrap(summary, groups):
    """Attach bootstrap CI, P(mean<=0) and t-stat for each group's R sample."""
    rows = []
    for key in summary.index:
        r = groups[key]
        b = stats.bootstrap_mean(r)
        rows.append(
            {
                "ci_low": b["ci_low"],
                "ci_high": b["ci_high"],
                "p_le_zero": b["p_le_zero"],
                "t_stat": stats.t_stat(r),
            }
        )
    return pd.concat([summary, pd.DataFrame(rows, index=summary.index)], axis=1)


def per_test_table(trades, manifest):
    s = summarize_by(trades, "test_id")
    groups = {k: g["r_net"].to_numpy() for k, g in trades.groupby("test_id")}
    s = with_bootstrap(s, groups)
    meta = manifest.set_index("test_id")[["strategy", "symbol", "timeframe", "research_date"]]
    return meta.join(s).loc[manifest["test_id"]]


def by_strategy_table(trades):
    s = summarize_by(trades, "strategy").loc[STRATEGIES]
    groups = {k: g["r_net"].to_numpy() for k, g in trades.groupby("strategy")}
    s = with_bootstrap(s, groups)
    everything = summarize(trades.sort_values("close_time")).to_frame("All").T
    everything = with_bootstrap(everything, {"All": trades["r_net"].to_numpy()})
    return pd.concat([s, everything]).drop(columns=ACCOUNT_LEVEL)


FORMATTERS = {
    "int": lambda v: f"{int(v)}",
    "pct": lambda v: f"{100 * v:.1f}%",
    "pct_raw": lambda v: f"{v:.1f}%",
    "r": lambda v: f"{v:+.2f}",
    "r_abs": lambda v: f"{v:.1f}",
    "x": lambda v: f"{v:.2f}",
    "p": lambda v: f"{v:.3f}" if v >= 0.001 else "<0.001",
    "h": lambda v: f"{v:.1f}",
}


def fmt(value, kind):
    return "–" if pd.isna(value) else FORMATTERS[kind](value)


def md_table(df, columns):
    """Render selected columns as a GitHub markdown table. columns: [(col, header, kind)]."""
    lines = [
        "| " + " | ".join(h for _, h, _ in columns) + " |",
        "|" + "|".join("---" if k == "text" else "---:" for _, _, k in columns) + "|",
    ]
    for idx, row in df.iterrows():
        cells = []
        for col, _, kind in columns:
            value = idx if col == "index" else row[col]
            cells.append(str(value) if kind == "text" else fmt(value, kind))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def forest_rows(per_test, by_strategy):
    """Rows for the forest plot: per strategy, the pooled row first, then tests by expectancy."""
    cols = ["expectancy_r", "ci_low", "ci_high", "trades"]
    tests = per_test[["strategy", *cols]].assign(label=per_test.index, pooled=False)
    pooled = by_strategy.loc[STRATEGIES, cols].assign(
        strategy=STRATEGIES, label=[f"{s} (pooled)" for s in STRATEGIES], pooled=True
    )
    rows = pd.concat([pooled, tests], ignore_index=True).rename(columns={"expectancy_r": "mean"})
    rows["order"] = rows["strategy"].map({s: i for i, s in enumerate(STRATEGIES)})
    rows = rows.sort_values(["order", "pooled", "mean"], ascending=[True, False, False])
    return rows.drop(columns="order").reset_index(drop=True)


def main():
    FIGURES.mkdir(parents=True, exist_ok=True)
    TABLES.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest()
    trades = load_all()
    trades.to_csv(TABLES / "trades_clean.csv", index=False)

    per_test = per_test_table(trades, manifest)
    by_strategy = by_strategy_table(trades)
    by_side = with_bootstrap(
        summarize_by(trades, ["strategy", "side"]).loc[STRATEGIES].drop(columns=ACCOUNT_LEVEL),
        {k: g["r_net"].to_numpy() for k, g in trades.groupby(["strategy", "side"])},
    )
    trades["close_year"] = trades["close_time"].dt.year
    by_year = (
        summarize_by(trades, ["strategy", "close_year"])
        .sort_index()
        .loc[STRATEGIES]
        .drop(columns=ACCOUNT_LEVEL)
    )

    r = {s: trades.loc[trades["strategy"] == s, "r_net"].to_numpy() for s in STRATEGIES}
    comparisons = pd.DataFrame(
        [
            {"comparison": f"{a} vs {b}", **stats.permutation_diff(r[a], r[b])}
            for a, b in [("200EMA", "20EMA"), ("200EMA", "Hybrid"), ("20EMA", "Hybrid")]
        ]
    ).set_index("comparison")

    mc = {s: stats.monte_carlo(r[s], horizon=MC_HORIZON) for s in STRATEGIES}
    monte_carlo = pd.DataFrame(
        {
            s: {
                "median_total_r": np.median(m["total_r"]),
                "p05_total_r": np.quantile(m["total_r"], 0.05),
                "p_total_le_zero": (m["total_r"] <= 0).mean(),
                "median_max_dd_r": np.median(m["max_dd_r"]),
                "p95_max_dd_r": np.quantile(m["max_dd_r"], 0.95),
                "median_losing_streak": np.median(m["max_losing_streak"]),
                "p95_losing_streak": np.quantile(m["max_losing_streak"], 0.95),
            }
            for s, m in mc.items()
        }
    ).T

    for name, df in [
        ("per_test", per_test),
        ("by_strategy", by_strategy),
        ("by_side", by_side),
        ("by_year", by_year),
        ("comparisons", comparisons),
        ("monte_carlo", monte_carlo),
    ]:
        df.round(4).to_csv(TABLES / f"{name}.csv")

    # Figures
    plots.equity_curves(trades, FIGURES / "equity_curves.png")
    plots.expectancy_forest(forest_rows(per_test, by_strategy), FIGURES / "expectancy_forest.png")
    plots.r_distributions(trades, FIGURES / "r_distributions.png")
    plots.monte_carlo_drawdowns(mc, MC_HORIZON, FIGURES / "monte_carlo_drawdown.png")

    # Markdown summary
    strategy_cols = [
        ("index", "Strategy", "text"),
        ("trades", "Trades", "int"),
        ("win_rate", "Win rate", "pct"),
        ("payoff", "Avg win / avg loss", "x"),
        ("breakeven_win_rate", "Breakeven win rate", "pct"),
        ("profit_factor", "Profit factor", "x"),
        ("expectancy_r_gross", "E[R] gross", "r"),
        ("expectancy_r", "E[R] net", "r"),
        ("ci_low", "95% CI low", "r"),
        ("ci_high", "95% CI high", "r"),
        ("p_le_zero", "P(E≤0)", "p"),
        ("max_dd_r", "Max DD (R)", "r_abs"),
        ("max_losing_streak", "Max losing streak", "int"),
    ]
    test_cols = [
        ("index", "Test", "text"),
        ("strategy", "Strategy", "text"),
        ("timeframe", "TF", "text"),
        ("trades", "Trades", "int"),
        ("win_rate", "Win rate", "pct"),
        ("profit_factor", "PF (R)", "x"),
        ("profit_factor_usd", "PF ($, net)", "x"),
        ("expectancy_r_gross", "E[R] gross", "r"),
        ("expectancy_r", "E[R] net", "r"),
        ("ci_low", "CI low", "r"),
        ("ci_high", "CI high", "r"),
        ("max_dd_r", "Max DD (R)", "r_abs"),
        ("net_return_pct", "Net return", "pct_raw"),
        ("max_dd_pct", "Max DD (%)", "pct_raw"),
        ("median_hold_hours", "Median hold (h)", "h"),
    ]
    side_df = by_side.copy()
    side_df.index = [f"{s} · {d}" for s, d in side_df.index]
    year_df = by_year.copy()
    year_df.index = [f"{s} · {int(y)}" for s, y in year_df.index]
    year_cols = [
        ("index", "Strategy · close year", "text"),
        ("trades", "Trades", "int"),
        ("win_rate", "Win rate", "pct"),
        ("expectancy_r", "E[R]", "r"),
        ("total_r", "Total R", "r"),
    ]
    mc_cols = [
        ("index", "Strategy", "text"),
        ("median_total_r", "Median total R", "r"),
        ("p05_total_r", "5th pct total R", "r"),
        ("p_total_le_zero", "P(total ≤ 0)", "p"),
        ("median_max_dd_r", "Median max DD (R)", "r_abs"),
        ("p95_max_dd_r", "95th pct max DD (R)", "r_abs"),
        ("p95_losing_streak", "95th pct losing streak", "int"),
    ]
    cmp_cols = [("index", "Comparison", "text"), ("diff", "Δ E[R]", "r"), ("p_value", "p-value", "p")]

    missing_open = int(trades["open_time"].isna().sum())
    summary = f"""# Results summary

_Auto-generated by `scripts/build_report.py`. Do not edit by hand._

- Trades analysed: **{len(trades)}** across **{trades["test_id"].nunique()}** backtests \
and **{trades["symbol"].nunique()}** instruments
- Close dates: {trades["close_time"].min():%Y-%m-%d} to {trades["close_time"].max():%Y-%m-%d}
- R = direction × (close − open) / |open − stop| (gross; every full stop-out is exactly −1R).
  **All tables use net R** (after commission, using each trade's own $ value of 1R) unless labelled gross.
- Bootstrap: 20,000 resamples, percentile 95% CI, seed 42. Monte Carlo: 10,000 paths of {MC_HORIZON} trades.
- Data cleaning: {missing_open} open timestamp recorded as 1899-12-30 (Forex Tester export bug) \
treated as missing; it affects hold time only.

## By strategy (pooled)

{md_table(by_strategy, strategy_cols)}

## By test

{md_table(per_test, test_cols)}

## Long vs short

{md_table(side_df, strategy_cols)}

## By close year

{md_table(year_df, year_cols)}

## Strategy comparisons (permutation test, two-sided)

{md_table(comparisons, cmp_cols)}

## Monte Carlo ({MC_HORIZON} future trades, resampled with replacement)

{md_table(monte_carlo, mc_cols)}
"""
    (REPORTS / "summary.md").write_text(summary)
    print(summary)


if __name__ == "__main__":
    main()
