# arXiv MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=arxiv&inputs=%5B%5D&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22arxiv-mcp-server%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=arxiv&inputs=%5B%5D&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22arxiv-mcp-server%22%5D%7D&quality=insider)

A Model Context Protocol server for searching and reading arXiv papers.

## Features

- **search** - query arXiv with filters (date, category, sort)
- **download** - fetch paper PDF, convert to markdown
- **read** - access stored paper content
- **list** - view all downloaded papers
- **prompts** - deep paper analysis workflow

## Prerequisites

- Python 3.11+

## Installation

```bash
git clone <repo-url>
cd arxiv-mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Configuration

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "arxiv": {
      "command": "/path/to/.venv/bin/python",
      "args": ["-m", "arxiv_mcp_server", "--storage-path", "/path/to/papers"]
    }
  }
}
```

### Cursor

Add to MCP settings:

```json
{
  "mcpServers": {
    "arxiv": {
      "command": "python",
      "args": ["-m", "arxiv_mcp_server"],
      "env": {
        "PYTHONPATH": "/path/to/arxiv-mcp-server/src"
      }
    }
  }
}
```

Default storage: `~/.arxiv-mcp-server/papers`

## Tools

### search_papers

```json
{
  "query": "transformer architecture",
  "max_results": 10,
  "date_from": "2023-01-01",
  "categories": ["cs.AI", "cs.LG"],
  "sort_by": "relevance"
}
```

### download_paper

```json
{
  "paper_id": "2401.12345"
}
```

### list_papers

```json
{}
```

### read_paper

```json
{
  "paper_id": "2401.12345"
}
```

## Prompts

### deep-paper-analysis

Comprehensive paper analysis workflow:

```json
{
  "paper_id": "2401.12345"
}
```

Covers: executive summary, methodology, results, implications, future directions.

## Environment variables

| Variable | Default |
|----------|---------|
| `ARXIV_STORAGE_PATH` | `~/.arxiv-mcp-server/papers` |

## License

MIT
