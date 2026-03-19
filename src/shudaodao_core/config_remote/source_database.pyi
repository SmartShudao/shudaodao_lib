from .base import RemoteConfigSource as RemoteConfigSource
from .schema.database.app import ConfigApp as ConfigApp
from .schema.database.item import ConfigItem as ConfigItem
from .schema.database.namespace import ConfigNamespace as ConfigNamespace
from typing import Any

class DatabaseConfigSource(RemoteConfigSource):
    """
    从数据库中获取配置信息
    """

    remote_configs: dict[str, Any]
    def __init__(self) -> None: ...
    def load(self) -> dict[str, Any]: ...

def create_config_engine(url: str): ...
