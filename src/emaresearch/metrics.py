"""Performance metrics computed from a sequence of trades.

R metrics use ``r_net`` (after commission); ``expectancy_r_gross`` is reported
alongside so the cost drag is visible.

All R-based metrics assume a fixed fractional risk per trade (~1% in these
backtests), so cumulative R is approximately the non-compounded % return.
"""

import numpy as np
import pandas as pd

STARTING_BALANCE = 10_000.0


def max_drawdown(cum):
    """Largest peak-to-trough decline of a cumulative series (positive number).

    The series is assumed to start from 0 before the first trade.
    """
    cum = np.concatenate([[0.0], np.asarray(cum, dtype=float)])
    peak = np.maximum.accumulate(cum)
    return float((peak - cum).max())


def longest_streak(mask):
    """Length of the longest run of True values."""
    best = run = 0
    for m in mask:
        run = run + 1 if m else 0
        best = max(best, run)
    return best


def summarize(trades):
    """One row of headline metrics for a set of trades ordered by close time."""
    r = trades["r_net"].to_numpy(dtype=float)
    pnl = trades["profit"].to_numpy(dtype=float)
    wins, losses = r[r > 0], r[r <= 0]

    avg_win = wins.mean() if len(wins) else np.nan
    avg_loss = -losses.mean() if len(losses) else np.nan
    payoff = avg_win / avg_loss if len(losses) else np.nan
    equity = STARTING_BALANCE + np.cumsum(pnl)
    equity_peak = np.maximum.accumulate(np.concatenate([[STARTING_BALANCE], equity]))[1:]

    return pd.Series(
        {
            "trades": len(r),
            "win_rate": (r > 0).mean(),
            "avg_win_r": avg_win,
            "avg_loss_r": avg_loss,
            "payoff": payoff,
            "breakeven_win_rate": 1 / (1 + payoff) if np.isfinite(payoff) else np.nan,
            "profit_factor": wins.sum() / -losses.sum() if losses.sum() < 0 else np.nan,
            "profit_factor_usd": pnl[pnl > 0].sum() / -pnl[pnl < 0].sum() if (pnl < 0).any() else np.nan,
            "expectancy_r": r.mean(),
            "expectancy_r_gross": trades["r_multiple"].mean(),
            "total_r": r.sum(),
            "max_dd_r": max_drawdown(np.cumsum(r)),
            "max_losing_streak": longest_streak(r <= 0),
            "net_profit": pnl.sum(),
            "net_return_pct": 100 * pnl.sum() / STARTING_BALANCE,
            "max_dd_pct": 100 * float(((equity_peak - equity) / equity_peak).max()),
            "median_hold_hours": trades["hold_hours"].median(),
        }
    )


def summarize_by(trades, keys):
    """``summarize`` applied per group, trades ordered by close time within each."""
    ordered = trades.sort_values("close_time", kind="stable")
    columns = ["r_multiple", "r_net", "profit", "hold_hours"]
    return ordered.groupby(keys, sort=False)[columns].apply(summarize)
