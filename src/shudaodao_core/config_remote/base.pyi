from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any

class RemoteConfigSource:
    """
    远程配置源抽象基类
    """

    configs: Incomplete
    def __init__(self, configs: Mapping[str, Any] | None = None) -> None: ...
    def load(self) -> dict[str, Any]:
        """
        拉取并返回完整远程配置（扁平 or 嵌套）
        """
