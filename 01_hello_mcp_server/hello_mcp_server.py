from mcp.server.fastmcp import FastMCP
from pydantic import Field


# Initialize FastMCP server
mcp = FastMCP("hello-mcp-server", log_level="ERROR")


# 注册工具的装饰器，可以很方便的把一个函数注册为工具
@mcp.tool()
async def hello_mcp_server(username: str = Field(description="用户名")) -> str:
    """当用户向 MCP 打招呼时，调用此工具

    Args:
        username: 用户名

    Returns:
        回复用户的问好
    """
    return f"Hello, {username}，我是 MCP 示例!"


def main():
    print("Hello from hello-mcp-server!")


if __name__ == "__main__":
    main()
