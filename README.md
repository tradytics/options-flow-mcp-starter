<p align="center">
  <a href="https://tradytics.com/docs/mcp"><img src="https://tradytics.com/api/v2/og/sdk.png?v=4" alt="Tradytics Options Flow & Market Data MCP Starter" width="100%"></a>
</p>

# Options Flow & Market Data MCP Starter

Ready-to-run MCP configs, desk prompts, and Python scripts for connecting **Claude**, **Claude Code**, **ChatGPT**, **Cursor**, **Cline**, and **Codex** to live US market data through [Tradytics](https://tradytics.com/docs/mcp).

[![npm](https://img.shields.io/npm/v/tradytics-mcp?color=168eff&label=tradytics-mcp)](https://www.npmjs.com/package/tradytics-mcp)
[![PyPI](https://img.shields.io/pypi/v/tradytics?color=168eff&label=python%20sdk)](https://pypi.org/project/tradytics/)
[![Docs](https://img.shields.io/badge/docs-tradytics.com-16171a)](https://tradytics.com/docs/mcp)
[![License](https://img.shields.io/badge/license-MIT-16171a)](LICENSE)
[![Tradytics MCP connector](https://glama.ai/mcp/connectors/com.tradytics/market-data/badges/score.svg)](https://glama.ai/mcp/connectors/com.tradytics/market-data)

```bash
# Hosted OAuth MCP (Claude Code)
claude mcp add --transport http tradytics https://tradytics.com/mcp

# Coding-agent skill (Claude Code, Codex, Cursor)
npx skills add tradytics/skills

# Python SDK
pip install tradytics
```

## What is inside

- **Workspace MCP configs**: [`.cursor/mcp.json`](.cursor/mcp.json) and [`.mcp.json`](.mcp.json) pre-wired to `https://tradytics.com/mcp`, ready to clone and open.
- **Desk workflow prompts**: copy-paste prompts in [`prompts/`](prompts/) for morning briefings, single-ticker institutional tape checks, 0DTE dealer gamma, and prediction-market vs options comparisons.
- **Python starter scripts**: zero-dependency scripts in [`scripts/`](scripts/) using `pip install tradytics` to summarize flow, dealer gamma and dark pools or stream new prints live.

## 60-second setup

| Client | Setup |
| :--- | :--- |
| **Claude Code** | `claude mcp add --transport http tradytics https://tradytics.com/mcp`, then `/mcp` to sign in |
| **Cursor** | Clone this repo (includes `.cursor/mcp.json`) and click **Connect** next to `tradytics` |
| **Claude Desktop / Cline / Windsurf** | Run `npx -y tradytics-mcp` or `uvx tradytics-mcp` with `TRADYTICS_API_KEY` ([`tradytics/tradytics-mcp`](https://github.com/tradytics/tradytics-mcp)) |
| **ChatGPT** | `chatgpt.com/plugins` -> **+ -> Add custom MCP server** -> `https://tradytics.com/mcp` (OAuth) |

## Ready-to-run prompts

| Prompt | What it builds |
| :--- | :--- |
| [`prompts/morning-briefing.md`](prompts/morning-briefing.md) | Index snapshot, overnight stock perpetuals, options flow leaders, SPY/QQQ dealer gamma flip and walls, and today's catalysts |
| [`prompts/ticker-deep-dive.md`](prompts/ticker-deep-dive.md) | Single-stock institutional tape note: options flow, dealer gamma/vanna/charm, ranked dark pool levels, expected move, and filings |
| [`prompts/0dte-gamma-check.md`](prompts/0dte-gamma-check.md) | Intraday SPY / SPX / QQQ dealer positioning, gamma flip, call/put walls, and net flow divergence |
| [`prompts/event-odds-vs-options.md`](prompts/event-odds-vs-options.md) | Kalshi and Polymarket finance probabilities alongside options implied moves for macro releases and earnings |

## Python starter scripts

Get a key at [tradytics.com/developer/keys](https://tradytics.com/developer/keys) and run:

```bash
pip install tradytics
export TRADYTICS_API_KEY="tdy_..."

python scripts/morning_brief.py NVDA SPY
python scripts/stream_flow.py --min-premium 250000
```

## More

- [MCP server repo](https://github.com/tradytics/tradytics-mcp) (`npx -y tradytics-mcp` / `uvx tradytics-mcp`)
- [Market data API benchmark](https://github.com/tradytics/market-data-api-benchmark)
- [API documentation](https://tradytics.com/docs) and [rate limits](https://tradytics.com/docs/rate-limits)
- Support: [hello@tradytics.com](mailto:hello@tradytics.com)

MIT License. Not investment advice; all market data is for informational purposes only.
