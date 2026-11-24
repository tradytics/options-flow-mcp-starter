# Intraday 0DTE Dealer Gamma & Flow Check

Paste into Claude, ChatGPT, or Cursor during the session:

```text
Check intraday 0DTE positioning on SPY, SPX, and QQQ using Tradytics MCP:

1. Call get_dealer_positioning for SPY, SPX, and QQQ to report spot price, gamma flip, call wall, put wall, and net dealer gamma regime.
2. Call get_volatility for expected daily range and IV vs realized context.
3. Call get_flow_summary and get_options_flow for SPY and QQQ to see whether intraday call/put net flow aligns with or diverges from price.

Present one side-by-side table for SPY, SPX, and QQQ, then note key inflection levels to watch.
```
