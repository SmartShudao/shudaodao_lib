from .gen_convert import GenConverter as GenConverter
from .meta_inspect import MetaInspect as MetaInspect
from shudaodao_core import AsyncSession as AsyncSession
from shudaodao_meta.generate.entity_table.meta_column import MetaColumn as MetaColumn
from shudaodao_meta.generate.entity_table.meta_foreign_key import (
    MetaForeignKey as MetaForeignKey,
)
from shudaodao_meta.generate.entity_table.meta_index import MetaIndex as MetaIndex
from shudaodao_meta.generate.entity_table.meta_primary_key import (
    MetaPrimaryKey as MetaPrimaryKey,
)
from shudaodao_meta.generate.entity_table.meta_referencing_foreign_key import (
    MetaReferencingForeignKey as MetaReferencingForeignKey,
)
from shudaodao_meta.generate.entity_table.meta_schema import MetaSchema as MetaSchema
from shudaodao_meta.generate.entity_table.meta_table import MetaTable as MetaTable
from shudaodao_meta.generate.entity_table.meta_unique_constraint import (
    MetaUniqueConstraint as MetaUniqueConstraint,
)
from shudaodao_meta.generate.entity_table.meta_view import MetaView as MetaView

class MetaStore:
    auto_commit: bool
    def __init__(
        self,
        *,
        db: AsyncSession = None,
        engine_name: str = None,
        schema_name: str = None,
    ) -> None: ...
    def inspect(self, *, engine_name: str = None, schema_name: str = None) -> dict: ...
    async def save_meta(
        self,
        *,
        metadata: dict = None,
        db: AsyncSession = None,
        engine_name: str = None,
        schema_name: str = None,
    ): ...
