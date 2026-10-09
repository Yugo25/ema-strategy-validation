"""Static figures for the README (PNG, light surface)."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Categorical slots 1-3 of the validated reference palette (passes all-pairs CVD checks).
STRATEGY_COLORS = {"200EMA": "#2a78d6", "20EMA": "#eb6834", "Hybrid": "#1baf7a"}
SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT_2 = "#52514e"
GRID = "#e4e3df"

plt.rcParams.update(
    {
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT_2,
        "axes.titlecolor": TEXT,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "xtick.color": TEXT_2,
        "ytick.color": TEXT_2,
        "font.size": 10,
        "legend.frameon": False,
    }
)


def _save(fig, path):
    fig.savefig(path, dpi=160, bbox_inches="tight")
    plt.close(fig)


def equity_curves(trades, path):
    """Cumulative R per strategy, trades in close-time order."""
    fig, ax = plt.subplots(figsize=(9, 4.6))
    for strategy, color in STRATEGY_COLORS.items():
        r = trades.loc[trades["strategy"] == strategy].sort_values("close_time")["r_net"]
        cum = np.concatenate([[0.0], r.cumsum().to_numpy()])
        ax.plot(np.arange(len(cum)), cum, color=color, linewidth=2, label=strategy)
        ax.annotate(
            f"{strategy}  {cum[-1]:+.0f}R",
            (len(cum) - 1, cum[-1]),
            xytext=(6, 0),
            textcoords="offset points",
            va="center",
            color=TEXT,
            fontsize=10,
            bbox={"facecolor": SURFACE, "edgecolor": "none", "pad": 1},
        )
    ax.axhline(0, color=TEXT_2, linewidth=0.8)
    ax.set_xlabel("Trade number (pooled across tests, ordered by close time)")
    ax.set_ylabel("Cumulative result (R)")
    ax.set_title("Cumulative R by strategy")
    ax.legend(loc="upper left")
    ax.margins(x=0.12)
    _save(fig, path)


def expectancy_forest(rows, path):
    """Expectancy per test and pooled, with 95% bootstrap CIs.

    ``rows`` needs columns: label, strategy, mean, ci_low, ci_high, trades, pooled.
    """
    rows = rows.iloc[::-1].reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(9, 0.38 * len(rows) + 1.2))
    for i, row in rows.iterrows():
        color = STRATEGY_COLORS.get(row["strategy"], TEXT)
        weight = 2.6 if row["pooled"] else 1.6
        ax.hlines(i, row["ci_low"], row["ci_high"], color=color, linewidth=weight)
        ax.plot(
            row["mean"],
            i,
            "o",
            color=color,
            markersize=9 if row["pooled"] else 7,
            markeredgecolor=SURFACE,
            markeredgewidth=2,
        )
        ax.annotate(
            f"{row['mean']:+.2f}R",
            (row["ci_high"], i),
            xytext=(6, 0),
            textcoords="offset points",
            va="center",
            color=TEXT_2,
            fontsize=9,
        )
    ax.axvline(0, color=TEXT, linewidth=1)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([f"{r.label}  (n={int(r.trades)})" for r in rows.itertuples()])
    for tick, pooled in zip(ax.get_yticklabels(), rows["pooled"], strict=True):
        if pooled:
            tick.set_fontweight("bold")
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("Expectancy per trade (R), 95% bootstrap CI")
    ax.set_title("Expectancy by test: every pooled strategy clears zero, single tests often do not")
    ax.margins(x=0.1)
    _save(fig, path)


def r_distributions(trades, path):
    """Histogram of trade outcomes in R, one panel per strategy."""
    strategies = list(STRATEGY_COLORS)
    fig, axes = plt.subplots(1, len(strategies), figsize=(11, 3.4), sharey=True)
    bins = np.arange(-1.25, 4.5, 0.25)
    for ax, strategy in zip(axes, strategies, strict=True):
        r = trades.loc[trades["strategy"] == strategy, "r_net"]
        ax.hist(r, bins=bins, color=STRATEGY_COLORS[strategy], edgecolor=SURFACE, linewidth=2)
        ax.axvline(r.mean(), color=TEXT, linewidth=1.2, linestyle="--")
        ax.set_title(f"{strategy}  (n={len(r)})", fontsize=11)
        ax.text(
            0.97, 0.92, f"mean {r.mean():+.2f}R", transform=ax.transAxes, ha="right", color=TEXT, fontsize=9
        )
        ax.set_xlabel("Trade result (R)")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("Trades")
    fig.suptitle(
        "Outcome distribution: losses cluster at -1R, winners spread out to +4R",
        x=0.01,
        ha="left",
        fontweight="bold",
        color=TEXT,
    )
    fig.tight_layout()
    _save(fig, path)


def monte_carlo_drawdowns(mc_by_strategy, horizon, path):
    """Distribution of simulated max drawdown over ``horizon`` trades."""
    strategies = [s for s in STRATEGY_COLORS if s in mc_by_strategy]
    fig, axes = plt.subplots(1, len(strategies), figsize=(11, 3.4), sharey=True, sharex=True)
    hi = max(np.quantile(mc_by_strategy[s]["max_dd_r"], 0.995) for s in strategies)
    # Losses are exactly -1R, so drawdowns cluster on whole R; use whole-R bins.
    bins = np.arange(0, np.ceil(hi) + 1, 1.0)
    for ax, strategy in zip(axes, strategies, strict=True):
        dd = mc_by_strategy[strategy]["max_dd_r"]
        ax.hist(dd, bins=bins, color=STRATEGY_COLORS[strategy], edgecolor=SURFACE, linewidth=1)
        p50, p95 = np.quantile(dd, [0.5, 0.95])
        for q, ls in [(p50, "-"), (p95, "--")]:
            ax.axvline(q, color=TEXT, linewidth=1.2, linestyle=ls)
        ax.text(
            0.97,
            0.92,
            f"median {p50:.1f}R (solid)\n95th pct {p95:.1f}R (dashed)",
            transform=ax.transAxes,
            ha="right",
            va="top",
            color=TEXT,
            fontsize=9,
            bbox={"facecolor": SURFACE, "edgecolor": "none", "pad": 2},
        )
        ax.set_title(strategy, fontsize=11)
        ax.set_xlabel(f"Max drawdown over {horizon} trades (R)")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("Simulations")
    fig.suptitle(
        f"Monte Carlo: drawdown to expect over the next {horizon} trades",
        x=0.01,
        ha="left",
        fontweight="bold",
        color=TEXT,
    )
    fig.tight_layout()
    _save(fig, path)
