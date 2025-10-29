from .meta_convert import MetaConverter as MetaConverter
from shudaodao_core import AsyncSession as AsyncSession
from shudaodao_meta.generate.entity_table.meta_column import (
    MetaColumn as MetaColumn,
    MetaColumnCreate as MetaColumnCreate,
)
from shudaodao_meta.generate.entity_table.meta_schema import MetaSchema as MetaSchema
from shudaodao_meta.generate.entity_table.meta_table import (
    MetaTable as MetaTable,
    MetaTableCreate as MetaTableCreate,
    MetaTableUpdate as MetaTableUpdate,
)
from shudaodao_meta.generate.entity_table.meta_view import (
    MetaView as MetaView,
    MetaViewCreate as MetaViewCreate,
    MetaViewUpdate as MetaViewUpdate,
)
from shudaodao_meta.generate.entity_table.source_schema import (
    SourceSchema as SourceSchema,
)

class MetaStore:
    auto_commit: bool
    def __init__(self, *, db: AsyncSession = None, schema_name: str = None) -> None: ...
    async def save_sqlmodel(self, db: AsyncSession = None, schema_name: str = None): ...
