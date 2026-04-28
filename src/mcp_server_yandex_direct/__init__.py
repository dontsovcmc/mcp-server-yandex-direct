"""MCP server for Yandex Direct API v5."""

import sys

__version__ = "0.1.1"


def main():
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        from .cli import main as cli_main
        cli_main()
    elif "--version" in sys.argv:
        print(f"mcp-server-yandex-direct {__version__}")
    else:
        from .server import mcp
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
