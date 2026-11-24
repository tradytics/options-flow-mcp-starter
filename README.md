# Options Flow & Market Data MCP Starter

[![Tradytics MCP connector](https://glama.ai/mcp/connectors/com.tradytics/market-data/badges/score.svg)](https://glama.ai/mcp/connectors/com.tradytics/market-data)

Ready-to-run MCP configs, prompts, and Python scripts for connecting **Claude**, **Claude Code**, **ChatGPT**, **Cursor**, and **Codex** to live US market data through [Tradytics](https://tradytics.com/).

- **Hosted MCP Server:** `https://tradytics.com/mcp` (Streamable HTTP + OAuth)
- **Agent Skill:** `npx skills add tradytics/skills`
- **REST API & SDKs:** `pip install tradytics` | `npm install tradytics`
- **Documentation:** [API Docs](https://tradytics.com/docs) | [MCP Setup](https://tradytics.com/docs/mcp) | [Rate Limits](https://tradytics.com/docs/rate-limits)

## What You Can Query

Every dataset shares one MCP server and one REST API:

- **Options flow:** stitched sweeps, blocks, splits, inferred side, strike heatmaps, and unusual contracts (`get_options_flow`, `get_flow_summary`, `get_option_contracts`)
- **Dealer positioning & volatility:** gamma, delta, vanna, charm, call/put walls, gamma flip, and IV skew (`get_dealer_positioning`, `get_volatility`)
- **Dark pools:** ranked block prints and institutional volume levels (`get_dark_pool`)
- **Stock perpetuals:** 24/7 equity perpetual markets, funding, open interest, and prints (`get_perp_markets`, `get_perp_prints`)
- **Prediction markets:** live and settled finance questions across Kalshi and Polymarket (`get_probabilities`)
- **Equities, fundamentals & filings:** quotes, bars, screener, signals, earnings, SEC filings, and disclosures (`get_quotes`, `get_price_bars`, `get_fundamentals`, `get_filings`, `screen_stocks`)

---

## 60-Second Setup

### Claude Code
```bash
claude mcp add --transport http tradytics https://tradytics.com/mcp
```
Then run `/mcp` inside Claude Code to sign in with OAuth.

### Cursor
This repo already includes [`.cursor/mcp.json`](.cursor/mcp.json). Clone the repo, open it in Cursor, and click **Connect** next to `tradytics` in MCP settings:

```json
{
  "mcpServers": {
    "tradytics": {
      "url": "https://tradytics.com/mcp"
    }
  }
}
```

### Claude (Web / Desktop)
1. Open **Customize -> Connectors -> Add custom connector**.
2. Name it `Tradytics`, set the URL to `https://tradytics.com/mcp`, and click **Add**.
3. Click **Connect** and approve access.

### ChatGPT
1. Open `chatgpt.com/plugins`, select **+ -> Add custom MCP server**.
2. Name it `Tradytics`, choose **Public endpoint**, paste `https://tradytics.com/mcp`, and select **OAuth**.
3. Sign in to Tradytics and mention `@Tradytics` in chat.

### Coding Agents Skill (Claude Code, Codex, Cursor)
Give your coding agent every endpoint and parameter automatically:
```bash
npx skills add tradytics/skills
```

---

## Ready-to-Run Prompts

Copy any workflow from [`prompts/`](prompts/) directly into Claude, ChatGPT, or Cursor once Tradytics MCP is connected:

| Prompt | What It Builds |
| :--- | :--- |
| [`prompts/morning-briefing.md`](prompts/morning-briefing.md) | Opening-bell briefing: index snapshot, overnight perpetuals, bullish/bearish options flow leaders, SPY/QQQ dealer gamma levels, and today's catalysts |
| [`prompts/ticker-deep-dive.md`](prompts/ticker-deep-dive.md) | Single-stock institutional tape check: options flow, dealer gamma/vanna/charm, ranked dark pool blocks, expected move, and recent filings |
| [`prompts/0dte-gamma-check.md`](prompts/0dte-gamma-check.md) | Intraday SPY / SPX / QQQ dealer positioning: gamma flip, call wall, put wall, and options net flow |
| [`prompts/event-odds-vs-options.md`](prompts/event-odds-vs-options.md) | Compare Kalshi and Polymarket finance probabilities alongside options implied moves for macro releases and earnings |

---

## Python Starter Scripts

Install the official zero-dependency Python client and set your key from [tradytics.com/developer/keys](https://tradytics.com/developer/keys):

```bash
pip install tradytics
export TRADYTICS_API_KEY="tdy_..."
```

Run the morning briefing or stream live options flow:

```bash
python scripts/morning_brief.py NVDA SPY
python scripts/stream_flow.py --min-premium 250000
```

## License

MIT. Not investment advice; all market data is for informational purposes only.
