"""
pip install mcp[cli]
"""
from mcp.server.fastmcp import FastMCP
from pydantic import Field


# Initialize FastMCP server
mcp = FastMCP("query-order", log_level="ERROR")


# 注册工具的装饰器，可以很方便的把一个函数注册为工具
@mcp.tool()
async def query_order(order_id: str = Field(description="订单号")) -> str:
    """查询物流信息。当用户需要根据订单号查询物流信息时，调用此工具

    Args:
        order_id: 订单号

    Returns:
        物流信息的字符串描述
    """
    # 统一的物流信息数据
    tracking_info = [
        {"time": "2024-01-20 10:00:00", "status": "包裹已揽收", "location": "深圳转运中心"},
        {"time": "2024-01-20 15:30:00", "status": "运输中", "location": "深圳市"},
        {"time": "2024-01-21 09:00:00", "status": "到达目的地", "location": "北京市"},
        {"time": "2024-01-21 14:00:00", "status": "派送中", "location": "北京市朝阳区"},
        {"time": "2024-01-21 16:30:00", "status": "已签收", "location": "北京市朝阳区三里屯"}
    ]

    # 格式化物流信息
    result = f"物流单号：{order_id}\n\n物流轨迹：\n"
    for item in tracking_info:
        result += f"[{item['time']}] {item['status']} - {item['location']}\n"

    return result


def main():
    print("Hello from query_order !")


if __name__ == "__main__":
    main()
