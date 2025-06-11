import logging
import signal
import sys
from contextlib import contextmanager
from typing import Literal 

from fastmcp import FastMCP

from uniprot_mcp.prompts.prompts import get_prompt
from uniprot_mcp.tools.search_uniprot import search_uniprot

logger = logging.getLogger(__name__)


class UniprotMCP:
    def __init__(self, name: str | None = None):
        self.app: FastMCP = FastMCP(name=name)
        # self._register_tools()
        # self._register_prompts()
        self._shutdown_requested: bool = False
    
    def _register_tools(self):
        self.app.add_tool(search_uniprot)

    def _register_prompts(self):
        self.app.add_prompt(get_prompt)
    
    def _handle_shutdown(self):
        """Handle shutdown signals gracefully.

        Args:
            signum: Signal number
            frame: Current stack frame
        """
        logger.info("")
        self._shutdown_requested = True
        sys.exit(0)
    
    @contextmanager
    def _setup_signal_handlers(self):
        """Set up signal handlers for graceful shutdown."""
        previous_sigint = signal.getsignal(signal.SIGINT)
        previous_sigterm = signal.getsignal(signal.SIGTERM)

        # set up our handlers
        signal.signal(signal.SIGINT, self._handle_shutdown)
        signal.signal(signal.SIGTERM, self._handle_shutdown)

        try:
            yield
        finally:
            # Restore previous signal handlers
            signal.signal(signal.SIGINT, previous_sigint)
            signal.signal(signal.SIGTERM, previous_sigterm)

    def run(
        self,
        transport: Literal["stdio", "streamable-http"],
        host: str | None = None,
        port: int | None = None,
    ):
        """Run the MCP server.

        Args:
            transport: Transport to use for MCP communication
            host: Host to bind the server to (only used with streamable-http transport)
            port: Port to bind the server to (only used with streamable-http transport)
        """
        with self._setup_signal_handlers():
            try:
                if transport == "stdio":
                    self.app.run(transport=transport)
                elif transport == "streamable-http":
                    if host is None or port is None:
                        raise ValueError("host and port are required for streamable-http transport")

                    self.app.run(
                        host=host, 
                        port=port, 
                        transport=transport,
                        path="/mcp/",
                    )
            except Exception as e:
                logger.error(f"Error running MCP server: {e}")
                sys.exit(1)
