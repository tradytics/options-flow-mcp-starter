# Single-Ticker Institutional Tape Deep Dive

Replace `NVDA` with any US stock or ETF and paste into Claude, ChatGPT, or Cursor:

```text
Run an institutional tape check on NVDA using Tradytics MCP:

1. Price & snapshot: get_stock_snapshot for spot price, session change, and volume.
2. Options flow: get_options_flow and get_flow_summary for NVDA to summarize call vs put net premium, aggressive opening orders, and the largest contracts.
3. Dealer positioning & vol: get_dealer_positioning and get_volatility for gamma flip, call wall, put wall, IV rank, skew, and expected move.
4. Dark pool context: get_dark_pool for NVDA's highest-ranked block prints and top dollar-volume price levels.
5. Catalysts & disclosures: get_calendar, get_news, and get_disclosures for upcoming earnings, headlines, and insider or institutional moves.

Output a clean one-page desk note with exact numbers and levels.
```
