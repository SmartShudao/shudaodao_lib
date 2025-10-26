from ..engine.database_engine import DatabaseEngine as DatabaseEngine
from ..logger.logging_ import logging as logging
from _typeshed import Incomplete

class MetaDataInspector:
    engine: Incomplete
    schema_name: Incomplete
    support_schema: Incomplete
    inspector: Incomplete
    def __init__(self, *, engine_name: str) -> None: ...
    def get_schema(
        self, *, schema_name: str, alias_name: str = "shudaodao_generate"
    ) -> dict: ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
