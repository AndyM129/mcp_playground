from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server
mcp = FastMCP("request-url", log_level="ERROR")


# 注册工具的装饰器，可以很方便的把一个函数注册为工具
@mcp.tool()
async def request_example_url() -> dict[str, Any] | None:
    """
    请求示例 URL。当用户要求请求示例URL时，调用此工具
    """

    url = "https://httpbin.org/get"
    headers = {
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10.0)
            response.raise_for_status()
            # 格式化物流信息
            result = f"请求结果如下：\n```json\n{response.text}\n```\n"
            return result
        except Exception as e:
            result = f"请求示例 URL 失败：{e}"
            return result


def main():
    print("Hello from request-url!")


if __name__ == "__main__":
    main()
