"""Pull a quick options flow, dealer gamma, and dark pool summary via the Tradytics SDK.

Usage:
    export TRADYTICS_API_KEY="tdy_..."
    python scripts/morning_brief.py NVDA SPY
"""

from __future__ import annotations

import sys
from tradytics import Client


def fmt_usd(value: float | int | None) -> str:
    if value is None:
        return "-"
    abs_val = abs(value)
    if abs_val >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    if abs_val >= 1_000:
        return f"${value / 1_000:.1f}K"
    return f"${value:,.0f}"


def summarize_ticker(client: Client, symbol: str) -> None:
    print(f"\n=== {symbol} ===")

    flow = client.options.flow(symbol=symbol, limit=5)
    rows = flow.get("data") or []
    print("Top recent options flow:")
    for row in rows[:5]:
        print(
            f"  {row.get('time', '')[:19]}  {str(row.get('type', '')).upper():4} "
            f"${row.get('strike', '')} exp {row.get('expiration', '')}  "
            f"side={row.get('side', '-')}  prem={fmt_usd(row.get('premium_usd'))}"
        )

    gamma = client.options.exposure(symbol=symbol, greek="gamma")
    gdata = gamma.get("data") or {}
    if isinstance(gdata, dict):
        print(
            "Dealer gamma:",
            f"flip={gdata.get('gamma_flip', '-')}",
            f"call_wall={gdata.get('call_wall', '-')}",
            f"put_wall={gdata.get('put_wall', '-')}",
        )

    dp = client.darkpool.prints(symbol=symbol, limit=3)
    drows = dp.get("data") or []
    print("Recent ranked dark pool prints:")
    for row in drows[:3]:
        print(
            f"  {row.get('time', '')[:19]}  price=${row.get('price', '')}  "
            f"size={row.get('size', '')}  val={fmt_usd(row.get('value_usd'))}"
        )


def main() -> None:
    tickers = [arg.upper() for arg in sys.argv[1:]] or ["NVDA", "SPY"]
    client = Client()  # reads TRADYTICS_API_KEY
    for ticker in tickers:
        summarize_ticker(client, ticker)


if __name__ == "__main__":
    main()
