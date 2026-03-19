from ..config_remote.source_database import DatabaseConfigSource as DatabaseConfigSource
from ..enums.config import RemoteConfigSourceName as RemoteConfigSourceName
from .base import RemoteConfigSource as RemoteConfigSource

class RemoteConfigManager:
    """
    统一管理多个远程配置源
    """

    source: RemoteConfigSource | None
    def __init__(self) -> None: ...
    def load(self) -> dict: ...
