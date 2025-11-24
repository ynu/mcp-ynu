from typing import Any, Dict
from mcp_server import mcp
from coremail import CoremailClient
from logger import get_logger
from dotenv import load_dotenv
from os.path import dirname, join

load_dotenv(dotenv_path=join(dirname(__file__), 'coremail.env'))

# Initialize the client with environment variables or explicit parameters
client = CoremailClient()


@mcp.tool()
def getAttrs(user_at_domain: str, attrs = ["true_name", "cas_name", "user_status"]) -> str | Dict[str, Any]:
    """获取 coremail 用户 user_at_domain 的指定属性（默认为姓名，统一身份认证用户名，用户状态）信息"""
    result = client.getAttrs(user_at_domain, attrs)
    if result["code"] != 0:
      return f"Error: ${result['message']}"
    return result["result"]

@mcp.tool()
def getSmtpAlias(user_at_domain: str) -> str:
    """获取 coremail 用户 user_at_domain 的用户的别名信息"""
    result = client.getSmtpAlias(user_at_domain)
    if result["code"] != 0:
      return f"Error: ${result['message']}"
    return result["result"]
  

@mcp.tool()
def addSmtpAlias(user_at_domain: str, user_alias_at_domain) -> str | bool:
    """添加 coremail 用户 user_at_domain 的别名信息"""
    result = client.addSmtpAlias(user_at_domain, user_alias_at_domain)
    if result["code"] != 0:
      return f"Error: ${result['message']}"
    return True
  

@mcp.tool()
def delSmtpAlias(user_at_domain: str, user_alias_at_domain) -> str | bool:
    """添加 coremail 用户 user_at_domain 的别名信息"""
    result = client.delSmtpAlias(user_at_domain, user_alias_at_domain)
    if result["code"] != 0:
      return f"Error: ${result['message']}"
    return True
  

@mcp.tool()
def userExist2(user_at_domain: str) -> bool:
    """检查 coremail 用户 user_at_domain 是否存在"""
    return client.userExist2(user_at_domain)
  
  

@mcp.tool()
def updatePassword(user_at_domain: str, password) -> str | bool:
    """修改 coremail 用户 user_at_domain 的密码为 password"""
    result = client.changeAttrs(user_at_domain, {"password": password})
    if result["code"] != 0:
      return f"Error: ${result['message']}"
    return True
  

@mcp.tool()
def getUserFromCasName(cas_name: str) -> str | bool:
    """根据 统一身份认证用户 cas_name 查找 coremail 用户"""
    return client.getUserFromCasName(cas_name)