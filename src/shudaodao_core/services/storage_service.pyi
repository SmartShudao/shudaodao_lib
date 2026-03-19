from ..config.app_config import AppConfig as AppConfig
from ..engine.object_engine import ObjectEngine as ObjectEngine
from ..exception.service_exception import ServiceError as ServiceError
from ..logger.logging_ import logging as logging
from ..tools.rustfs_checker import RustfsChecker as RustfsChecker
from botocore.client import BaseClient as BaseClient

class AsyncStorageService:
    def __new__(cls):
        """线程安全单例构造器"""
    def get_s3_client(self, *, name: str = None, schema_name: str = None): ...
    def list_buckets(self, *, name: str = None, s3_client: BaseClient = None): ...
    def create_buckets(
        self, *, buckets: list[str], name: str = None, schema_name: str = None
    ): ...
    def generate_signed_url(
        self,
        *,
        schema_name: str,
        store_key: str,
        method: str,
        s3_client: BaseClient = None,
        expiration: int = 3600,
    ) -> list: ...
    def __del__(self) -> None:
        """析构函数"""
