import numpy as np
import pandas as pd
import pytest

from emaresearch import stats
from emaresearch.load import r_multiple, r_net
from emaresearch.metrics import longest_streak, max_drawdown, summarize


def make_trades(r_values, dollars_per_r=100.0, commission=0.0):
    r = np.asarray(r_values, dtype=float)
    profit = r * dollars_per_r - commission
    return pd.DataFrame(
        {
            "r_multiple": r,
            "r_net": profit / dollars_per_r,
            "profit": profit,
            "hold_hours": np.ones(len(r)),
        }
    )


def test_r_multiple_long_and_short():
    trades = pd.DataFrame(
        {
            "side": ["long", "long", "short", "short"],
            "open_price": [100.0, 100.0, 50.0, 50.0],
            "close_price": [104.0, 98.0, 47.0, 51.0],
            "sl": [98.0, 98.0, 51.0, 51.0],
        }
    )
    assert r_multiple(trades).tolist() == pytest.approx([2.0, -1.0, 3.0, -1.0])


def test_r_multiple_zero_risk_is_missing():
    trades = pd.DataFrame({"side": ["long"], "open_price": [1.0], "close_price": [1.1], "sl": [1.0]})
    assert r_multiple(trades).isna().all()


def test_r_net_deducts_commission_in_r_units():
    # 1R = $100. A +2R trade with $10 commission nets $190 -> 1.9R.
    trades = pd.DataFrame(
        {"r_multiple": [2.0, -1.0], "profit": [190.0, -110.0], "commission": [10.0, 10.0], "swap": [0.0, 0.0]}
    )
    assert r_net(trades).tolist() == pytest.approx([1.9, -1.1])


def test_max_drawdown_counts_from_starting_zero():
    assert max_drawdown([-1, -2, 1, 3, 1]) == pytest.approx(2.0)
    assert max_drawdown([1, 2, 3]) == 0.0
    assert max_drawdown([2, 1, 0, -1, 4]) == pytest.approx(3.0)


def test_longest_streak():
    assert longest_streak([True, True, False, True, True, True, False]) == 3
    assert longest_streak([False, False]) == 0


def test_summarize_known_answer():
    s = summarize(make_trades([2, -1, 2, -1, -1, 3]))
    assert s["trades"] == 6
    assert s["win_rate"] == pytest.approx(0.5)
    assert s["avg_win_r"] == pytest.approx(7 / 3)
    assert s["avg_loss_r"] == pytest.approx(1.0)
    assert s["breakeven_win_rate"] == pytest.approx(1 / (1 + 7 / 3))
    assert s["profit_factor"] == pytest.approx(7 / 3)
    assert s["expectancy_r"] == pytest.approx(4 / 6)
    assert s["total_r"] == pytest.approx(4.0)
    assert s["max_dd_r"] == pytest.approx(2.0)
    assert s["max_losing_streak"] == 2
    assert s["net_return_pct"] == pytest.approx(4.0)


def test_summarize_reports_cost_drag():
    s = summarize(make_trades([2, -1], commission=10.0))
    assert s["expectancy_r_gross"] == pytest.approx(0.5)
    assert s["expectancy_r"] == pytest.approx(0.4)


def test_bootstrap_ci_brackets_mean_and_is_deterministic():
    r = np.array([2, -1, 1.5, -1, 2.5, -1, 1.2, -1, 1.8, 2.0])
    a, b = stats.bootstrap_mean(r), stats.bootstrap_mean(r)
    assert a == b
    assert a["ci_low"] < r.mean() < a["ci_high"]


def test_permutation_identical_samples_is_not_significant():
    r = np.array([2, -1, 1.5, -1, 2.5, -1] * 5)
    assert stats.permutation_diff(r, r.copy(), n_perm=2_000)["p_value"] > 0.9


def test_monte_carlo_all_losses():
    mc = stats.monte_carlo(np.array([-1.0]), horizon=10, n_sims=50)
    assert (mc["total_r"] == -10).all()
    assert (mc["max_dd_r"] == 10).all()
    assert (mc["max_losing_streak"] == 10).all()
