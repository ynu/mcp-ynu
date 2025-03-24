# MCP-YNU - FastMCP Server

A dynamic MCP server implementation using FastMCP that automatically loads tools, resources, and prompts from respective directories.

## Features

- Dynamic loading of modules from `tools/`, `resources/`, and `prompts/` directories
- Automatic discovery and registration of modules
- Simple configuration and extensibility
- Type hints for better code clarity and static analysis
- Comprehensive logging for monitoring server activity

## Recent Updates

- Added type hints throughout the codebase
- Improved MCP instance handling
- Added logging functionality
- Added MIT license
- Updated documentation with reference links

## Directory Structure

```
mcp-ynu/
├── tools/          # Directory for tool modules
│   ├── __init__.py
│   ├── example_tool.py
├── resources/      # Directory for resource modules
│   ├── __init__.py
│   ├── example_resource.py
├── prompts/        # Directory for prompt modules
│   ├── __init__.py
│   ├── example_prompt.py
├── main.py         # Main server implementation
├── README.md       # Project documentation
├── LICENSE         # MIT License
└── pyproject.toml  # Project configuration
```

## Usage

1. Create modules in the appropriate directories
2. Implement a `register(mcp: FastMCP)` function in each module
3. Run the server:

```bash
python main.py
```

## Example Modules

### Tools Module Example (tools/example_tool.py)
```python
from mcp.server.fastmcp import FastMCP
from typing import Callable

def register(mcp: FastMCP) -> None:
    @mcp.tool("example_tool")
    def example_tool() -> str:
        return "This is an example tool"
```

### Resources Module Example (resources/example_resource.py)
```python
from mcp.server.fastmcp import FastMCP
from typing import Callable

def register(mcp: FastMCP) -> None:
    @mcp.resource("example_resource")
    def example_resource() -> str:
        return "This is an example resource"
```

### Prompts Module Example (prompts/example_prompt.py)
```python
from mcp.server.fastmcp import FastMCP
from typing import Callable

def register(mcp: FastMCP) -> None:
    @mcp.prompt("example_prompt")
    def example_prompt() -> str:
        return "This is an example prompt"
```

## Configuration

Configure directories in `main.py`:
```python
server = DynamicMCP(
    tools_dir="custom_tools",
    resources_dir="custom_resources",
    prompts_dir="custom_prompts"
)
```

## Debugging

1. Update `MCP_TRANSPORT_TYPE` in `.env`, Execute `python main.py` to start the mcp server
2. Execute `npx @modelcontextprotocol/inspector` to open the [inspect](http://localhost:5173/).
3. Choose `SSE` Transport Type with URL `http://localhost:<mcp_server_port>/sse` or Choose `STDIO` Transport Type with Command `python` and Arguments `/path/to/main.py`

![@modelcontextprotocol/inspector](inspect.png)

## Requirements

- Python >= 3.10
- FastMCP

## Reference Links

- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Core Concepts](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#core-concepts)
- [FastMCP Implementation](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/fastmcp.py)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
