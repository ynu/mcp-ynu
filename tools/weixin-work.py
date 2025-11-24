from typing import Any, Dict
from mcp_server import mcp
from logger import get_logger
from dotenv import load_dotenv
from os.path import dirname, join
from weixin_work_reborn import WeChatWorkClient, Config

# Initialize the client with configuration
config = Config(env_file=join(dirname(__file__), 'weixin-work.env'))  # Loads from .env file or environment variables
client = WeChatWorkClient(config=config)


@mcp.tool()
def get_user(userid: str) -> str | Dict[str, Any]:
    """根据企微用户id userid 获取企微用户信息"""
    return client.get_user(userid)


@mcp.tool()
def update_user_biz_mail_alias(user_id: str, biz_mail_alias: str) -> Dict[str, Any]:
    """根据企微用户id user_id 及企业邮箱别名 biz_mail_alias 设置其企业邮箱别名  """
    return client.update_user(
        userid=user_id,
        biz_mail_alias={
            "item": [biz_mail_alias]
        },
    )


@mcp.tool()
def get_userid_by_telphone(telphone: str) -> str:
    """根据企微用户电话号码 telphone 获取企微用户id userid 信息"""
    userid_result = client.mobile_to_userid(telphone)
    return userid_result.get('userid')

