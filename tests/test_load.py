"""Smoke tests against the real exports: the parser must reproduce Forex Tester's own headline numbers."""

import re

import pytest

from emaresearch.load import ROOT, load_all, load_manifest

REPORTS = ROOT / "data" / "raw" / "forextester_reports"


def forextester_header(md_path):
    text = md_path.read_text()

    def grab(label):
        return re.search(rf"\*\*{label}:\*\* \$?([\d,.]+)", text).group(1).replace(",", "")

    return {
        "trades": int(grab("Total trades")),
        "win_rate": float(grab("Winrate")) / 100,
        "profit_factor": float(grab("Profit Factor")),
        "net": float(grab("Total PnL")),
    }


@pytest.fixture(scope="module")
def trades():
    return load_all()


def test_every_manifest_file_loads(trades):
    assert set(trades["test_id"]) == set(load_manifest()["test_id"])
    assert trades["r_multiple"].notna().all()
    assert trades["close_time"].notna().all()


def test_stop_outs_are_minus_one_r(trades):
    assert trades["r_multiple"].min() == pytest.approx(-1.0)


@pytest.mark.parametrize("row", load_manifest().to_dict("records"), ids=lambda r: r["test_id"])
def test_matches_forextester_report(trades, row):
    expected = forextester_header(REPORTS / row["file"].replace(".csv", ".md"))
    t = trades[trades["test_id"] == row["test_id"]]
    pnl = t["profit"]
    assert len(t) == expected["trades"]
    assert (pnl > 0).mean() == pytest.approx(expected["win_rate"], abs=1e-4)
    assert pnl[pnl > 0].sum() / -pnl[pnl < 0].sum() == pytest.approx(expected["profit_factor"], abs=0.01)
    assert pnl.sum() == pytest.approx(expected["net"], abs=0.05)
