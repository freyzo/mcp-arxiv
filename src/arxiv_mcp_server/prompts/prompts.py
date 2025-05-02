"""Prompt definitions for arXiv MCP server."""

from mcp.types import Prompt, PromptArgument

# Define available prompts
PROMPTS = {
    "deep-paper-analysis": Prompt(
        name="deep-paper-analysis",
        description="Analyze a specific paper in detail",
        arguments=[
            PromptArgument(
                name="paper_id", description="arXiv paper ID", required=True
            ),
        ],
    ),
}
