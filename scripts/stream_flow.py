"""Stream new options flow prints with the official Tradytics Python client.

Usage:
    export TRADYTICS_API_KEY="tdy_..."
    python scripts/stream_flow.py --min-premium 250000
"""

from __future__ import annotations

import argparse
from tradytics import Client


def main() -> None:
    parser = argparse.ArgumentParser(description="Stream live options flow via Tradytics API.")
    parser.add_argument("--symbol", help="Optional ticker filter (e.g. NVDA)")
    parser.add_argument("--min-premium", type=int, default=250_000, help="Minimum premium in USD")
    args = parser.parse_args()

    client = Client()  # reads TRADYTICS_API_KEY
    params = {"min_premium": args.min_premium}
    if args.symbol:
        params["symbol"] = args.symbol.upper()

    print(f"Streaming options flow ({params})... Press Ctrl+C to stop.")
    try:
        for print_row in client.stream(client.options.flow, **params):
            prem = print_row.get("premium_usd") or 0
            print(
                f"{print_row.get('time', '')[:19]}  "
                f"{print_row.get('symbol', ''):6} "
                f"{str(print_row.get('type', '')).upper():4} "
                f"{print_row.get('strike', ''):>7} "
                f"{print_row.get('expiration', '')}  "
                f"side={print_row.get('side', '-'):4}  "
                f"${prem:,.0f}"
            )
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
