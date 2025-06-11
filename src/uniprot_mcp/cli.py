import logging
import sys
from typing import cast

import typer

from uniprot_mcp.server import UniprotMCP
from uniprot_mcp.settings import settings


logger = logging.getLogger(__name__)
app = typer.Typer()


@app.command()
def run(
    server_name: str | None = None,
    host: str | None = None,
    port: int | None = None,
    transport: str | None = typer.Option(
        None,
        help="Transport mode for MCP server; can be 'stdio' or 'streamable-http'",
    ),
) -> None:
    """Run the MCP server."""
    try:
        server = UniprotMCP(name=server_name or settings.SERVER_NAME)
        transport = transport or settings.TRANSPORT

        if transport == "stdio":
            server.run(transport=transport)
        elif transport == "streamable-http":
            server.run(
                transport=cast(str, transport),
                host=host or settings.SERVER_HOST,
                port=port or settings.SERVER_PORT,
            )
        else:
            raise typer.BadParameter(f"Invalid transport: {transport}")
    except Exception as e:
        logger.error(f"Error running MCP server from typer app: {e}")
        sys.exit(1)


__all__ = ["app"]
