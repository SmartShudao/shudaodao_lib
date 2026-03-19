from ..config.app_config import AppConfig as AppConfig
from ..logger.logging_ import logging as logging
from botocore.client import BaseClient as BaseClient

class ObjectEngine:
    def __new__(cls) -> ObjectEngine: ...
    def __init__(self) -> None: ...
    def get_s3_client(self, name: str) -> BaseClient:
        """
        获取 S3 客户端的上下文管理器
        :param name: 存储配置的名称
        """
    def close(self) -> None: ...
    def __del__(self) -> None: ...
