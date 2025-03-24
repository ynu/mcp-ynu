from mcp.server.fastmcp import Context, FastMCP
import importlib
import os
import logging
from pathlib import Path
from typing import Type, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DynamicMCP:
    def __init__(self, 
                 tools_dir: str = "tools", 
                 resources_dir: str = "resources", 
                 prompts_dir: str = "prompts") -> None:
        self.mcp: FastMCP = FastMCP()
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
        path = Path(directory)
        if not path.exists():
            logger.warning(f"Directory {directory} does not exist")
            return

        for module_file in path.glob("*.py"):
            if module_file.stem == "__init__":
                continue

            module_name: str = f"{directory}.{module_file.stem}"
            try:
                module: Any = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register(self.mcp)
                    logger.info(f"Successfully loaded {module_type}: {module_name}")
            except Exception as e:
                logger.error(f"Failed to load {module_type} {module_name}: {str(e)}")

    def run(self) -> None:
        """Start the MCP server"""
        logger.info("Starting MCP server")
        self.mcp.run(transport="sse")

def main() -> None:
    server: DynamicMCP = DynamicMCP()
    server.run()

if __name__ == "__main__":
    main()
