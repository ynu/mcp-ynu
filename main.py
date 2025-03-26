import importlib
import os
from pathlib import Path
from typing import Type, Any
from dotenv import load_dotenv
from mcp_server import mcp
from logger import get_logger

logger = get_logger(__name__)

load_dotenv()

class MCPLoader:
    def __init__(
        self,
        tools_dir: str = "tools",
        resources_dir: str = "resources",
        prompts_dir: str = "prompts",
    ) -> None:
        self.tools_dir: str = tools_dir
        self.resources_dir: str = resources_dir
        self.prompts_dir: str = prompts_dir
        self.load_modules()

    def load_modules(self) -> None:
        """Dynamically load modules from configured directories"""
        self._load_from_directory(self.tools_dir, "tool")
        self._load_from_directory(self.resources_dir, "resource")
        self._load_from_directory(self.prompts_dir, "prompt")

    def _load_from_directory(self, directory: str, module_type: str) -> None:
        """Load modules from a specific directory"""
        base_dir = Path(__file__).parent   
        path = Path(base_dir / directory)
        if not path.exists():
            logger.warning(f"Directory {directory} does not exist")
            return

        for module_file in path.glob("*.py"):
            if module_file.stem == "__init__":
                continue

            module_name: str = f"{directory}.{module_file.stem}"
            try:
                importlib.import_module(module_name)
                logger.info(f"Successfully loaded {module_type}: {module_name}")
            except Exception as e:
                logger.error(f"Failed to load {module_type} {module_name}: {str(e)}")


def main() -> None:
    # Load modules from configured directories
    MCPLoader()
    # Start the MCP server
    logger.info(f"Starting MCP server with transport type: {os.getenv('MCP_TRANSPORT_TYPE')} with host: {os.getenv('MCP_SERVER_HOST')} and port: {os.getenv('MCP_SERVER_PORT')}")
    mcp.run(transport="sse" if os.getenv("MCP_TRANSPORT_TYPE") == "sse" else "stdio")


if __name__ == "__main__":
    main()
