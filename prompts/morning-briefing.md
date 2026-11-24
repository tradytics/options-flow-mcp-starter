# Morning Market & Flow Briefing

Paste this into Claude, ChatGPT, or Cursor with the Tradytics MCP server connected:

```text
Using Tradytics MCP, build my morning market briefing in compact tables:

1. Market backdrop: call get_market and get_calendar for today's macro releases and major earnings.
2. Overnight stock perpetuals: call get_perp_markets and highlight the top 5 tickers by session volume and notable funding shifts.
3. Options flow leaders: call get_flow_summary to list the top bullish and bearish single stocks by net premium.
4. Dealer levels: call get_dealer_positioning for SPY and QQQ and summarize gamma flip, call wall, put wall, and whether dealers sit in positive or negative gamma.
5. Dark pool highlights: call get_dark_pool for SPY, QQQ, and the top flow leader to flag top-ranked block prints and nearby price levels.

Keep it concise, cite timestamps, and separate facts from interpretation.
```
