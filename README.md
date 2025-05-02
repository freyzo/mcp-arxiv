# ArXiv MCP Server

> 🔍 Enable AI assistants to search and access arXiv papers through a simple MCP interface.

The ArXiv MCP Server provides a bridge between AI assistants and arXiv's research repository through the Model Context Protocol (MCP). It allows AI models to search for papers and access their content in a programmatic way.

## ✨ Core Features

- 🔎 **Paper Search**: Query arXiv papers with filters for date ranges and categories
- 📄 **Paper Access**: Download and read paper content
- 📋 **Paper Listing**: View all downloaded papers
- 🗃️ **Local Storage**: Papers are saved locally for faster access
- 📝 **Prompts**: A Set of Research Prompts

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher

### Local Setup

1. **Navigate to project directory**:
```bash
cd /Users/user/Desktop/arxiv-mcp-server-main
```

2. **Create virtual environment**:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

3. **Install dependencies**:
```bash
pip install --upgrade pip
pip install -e .
```

4. **Test the server** (optional):
```bash
python -m arxiv_mcp_server
# Or run tests
python -m pytest
```

**Note**: The server runs via stdio and waits for MCP client connections. Press Ctrl+C to stop when testing manually.

### 🔌 MCP Client Configuration

#### For Claude Desktop

Add this to your Claude Desktop MCP config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
    "mcpServers": {
        "arxiv-mcp-server": {
            "command": "/Users/user/Desktop/arxiv-mcp-server-main/.venv/bin/python",
            "args": [
                "-m",
                "arxiv_mcp_server",
                "--storage-path",
                "/Users/user/Desktop/arxiv-mcp-server-main/papers"
            ]
        }
    }
}
```

**Note**: Update the paths to match your actual project location. Use the full path to the Python interpreter in your `.venv` directory.

#### Using environment variable for storage path

You can also set the storage path via environment variable:

```json
{
    "mcpServers": {
        "arxiv-mcp-server": {
            "command": "python",
            "args": ["-m", "arxiv_mcp_server"],
            "env": {
                "PYTHONPATH": "/Users/user/Desktop/arxiv-mcp-server-main/src",
                "ARXIV_STORAGE_PATH": "/Users/user/Desktop/arxiv-mcp-server-main/papers"
            }
        }
    }
}
```

**Default storage location**: If not specified, papers are stored at `~/.arxiv-mcp-server/papers`

## 💡 Available Tools

The server provides four main tools:

### 1. Paper Search
Search for papers with optional filters:

```python
result = await call_tool("search_papers", {
    "query": "transformer architecture",
    "max_results": 10,
    "date_from": "2023-01-01",
    "categories": ["cs.AI", "cs.LG"]
})
```

### 2. Paper Download
Download a paper by its arXiv ID:

```python
result = await call_tool("download_paper", {
    "paper_id": "2401.12345"
})
```

### 3. List Papers
View all downloaded papers:

```python
result = await call_tool("list_papers", {})
```

### 4. Read Paper
Access the content of a downloaded paper:

```python
result = await call_tool("read_paper", {
    "paper_id": "2401.12345"
})
```

## 📝 Research Prompts

The server offers specialized prompts to help analyze academic papers:

### Paper Analysis Prompt
A comprehensive workflow for analyzing academic papers that only requires a paper ID:

```python
result = await call_prompt("deep-paper-analysis", {
    "paper_id": "2401.12345"
})
```

This prompt includes:
- Detailed instructions for using available tools (list_papers, download_paper, read_paper, search_papers)
- A systematic workflow for paper analysis
- Comprehensive analysis structure covering:
  - Executive summary
  - Research context
  - Methodology analysis
  - Results evaluation
  - Practical and theoretical implications
  - Future research directions
  - Broader impacts

## ⚙️ Configuration

Configure through environment variables:

| Variable | Purpose | Default |
|----------|---------|---------|
| `ARXIV_STORAGE_PATH` | Paper storage location | ~/.arxiv-mcp-server/papers |
