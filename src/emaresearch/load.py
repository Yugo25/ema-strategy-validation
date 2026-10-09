"""Load Forex Tester trade-history exports into a single tidy DataFrame."""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TRADES_DIR = ROOT / "data" / "raw" / "trades"
MANIFEST = ROOT / "data" / "manifest.csv"

# Forex Tester writes Excel-style "zero dates" when a timestamp is missing.
_INVALID_DATE_BEFORE = pd.Timestamp("1990-01-01")


def read_forextester_csv(path):
    """Parse one Forex Tester export and return its closed BUY/SELL trades.

    The file starts with a ``sep=,`` hint and a ``Trade History`` title line
    before the real header. Deposits and withdrawals are dropped.
    """
    df = pd.read_csv(path, skiprows=2, dtype=str, keep_default_na=False)
    df = df[df["type"].isin(["BUY", "SELL"])].copy()

    for col in [
        "lots",
        "lotSize",
        "openPrice",
        "closePrice",
        "sl",
        "tp",
        "swap",
        "commision",
        "points",
        "profit",
    ]:
        df[col] = pd.to_numeric(df[col])
    for col in ["openTime", "closeTime"]:
        ts = pd.to_datetime(df[col])
        df[col] = ts.where(ts >= _INVALID_DATE_BEFORE)

    out = pd.DataFrame(
        {
            "trade_no": df["id"].astype(int),
            "symbol": df["symbol"],
            "side": df["type"].str.lower().map({"buy": "long", "sell": "short"}),
            "open_time": df["openTime"],
            "close_time": df["closeTime"],
            "open_price": df["openPrice"],
            "close_price": df["closePrice"],
            "sl": df["sl"],
            "tp": df["tp"],
            "lots": df["lots"],
            "commission": df["commision"],
            "swap": df["swap"],
            "profit": df["profit"],
        }
    )
    out["r_multiple"] = r_multiple(out)
    out["r_net"] = r_net(out)
    out["hold_hours"] = (out["close_time"] - out["open_time"]).dt.total_seconds() / 3600
    return out.sort_values("close_time", kind="stable").reset_index(drop=True)


def r_multiple(trades):
    """Result of each trade in units of its initial risk (entry-to-stop distance).

    ``R = direction * (close - open) / |open - sl|``. A full stop-out is -1R.
    Price-based, so it is independent of position size and account currency.
    """
    direction = np.where(trades["side"] == "long", 1.0, -1.0)
    risk = (trades["open_price"] - trades["sl"]).abs()
    r = direction * (trades["close_price"] - trades["open_price"]) / risk
    return r.where(risk > 0)


def r_net(trades):
    """R after commission and swap, using the trade's own dollar value of 1R.

    ``gross = profit + commission - swap`` (Forex Tester deducts commission from
    ``profit``), so ``dollars_per_r = gross / r_multiple`` and ``r_net = profit / dollars_per_r``.
    """
    gross = trades["profit"] + trades["commission"] - trades["swap"]
    dollars_per_r = gross / trades["r_multiple"]
    return trades["profit"] / dollars_per_r


def load_manifest(path=MANIFEST):
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def load_all(trades_dir=TRADES_DIR, manifest_path=MANIFEST):
    """All trades from every test listed in the manifest, with test metadata."""
    manifest = load_manifest(manifest_path)
    frames = []
    for row in manifest.itertuples(index=False):
        t = read_forextester_csv(Path(trades_dir) / row.file)
        t.insert(0, "test_id", row.test_id)
        t.insert(1, "strategy", row.strategy)
        t.insert(2, "timeframe", row.timeframe)
        frames.append(t)
    return pd.concat(frames, ignore_index=True)
