from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os

load_dotenv()

mcp: FastMCP = FastMCP(
    name="ynu-mcp",
    host=os.getenv("MCP_SERVER_HOST", "0.0.0.0"),
    port=int(os.getenv("MCP_SERVER_PORT", 8000)),
    log_level="DEBUG"
)
