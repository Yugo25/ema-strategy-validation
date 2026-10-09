"""Resampling statistics: is the edge distinguishable from zero, and how bad can it get?"""

import numpy as np

from .metrics import longest_streak, max_drawdown

SEED = 42


def bootstrap_mean(r, n_boot=20_000, ci=0.95, seed=SEED):
    """Percentile bootstrap CI for the mean R, plus the share of resamples with mean <= 0."""
    r = np.asarray(r, dtype=float)
    rng = np.random.default_rng(seed)
    means = rng.choice(r, size=(n_boot, len(r)), replace=True).mean(axis=1)
    lo, hi = np.quantile(means, [(1 - ci) / 2, 1 - (1 - ci) / 2])
    return {"mean": r.mean(), "ci_low": lo, "ci_high": hi, "p_le_zero": (means <= 0).mean()}


def t_stat(r):
    """One-sample t statistic of mean R against zero."""
    r = np.asarray(r, dtype=float)
    return r.mean() / (r.std(ddof=1) / np.sqrt(len(r)))


def permutation_diff(a, b, n_perm=20_000, seed=SEED):
    """Two-sided permutation test for a difference in mean R between two samples."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    observed = a.mean() - b.mean()
    pooled = np.concatenate([a, b])
    rng = np.random.default_rng(seed)
    diffs = np.empty(n_perm)
    for i in range(n_perm):
        rng.shuffle(pooled)
        diffs[i] = pooled[: len(a)].mean() - pooled[len(a) :].mean()
    return {"diff": observed, "p_value": (np.abs(diffs) >= abs(observed)).mean()}


def monte_carlo(r, horizon=100, n_sims=10_000, seed=SEED):
    """Simulate future trade sequences by resampling observed R with replacement.

    Returns per-simulation total R, max drawdown (R) and longest losing streak
    over ``horizon`` trades.
    """
    r = np.asarray(r, dtype=float)
    rng = np.random.default_rng(seed)
    paths = rng.choice(r, size=(n_sims, horizon), replace=True)
    return {
        "total_r": paths.sum(axis=1),
        "max_dd_r": np.array([max_drawdown(np.cumsum(p)) for p in paths]),
        "max_losing_streak": np.array([longest_streak(p <= 0) for p in paths]),
    }
