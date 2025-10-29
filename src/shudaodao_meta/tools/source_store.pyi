from .meta_convert import MetaConverter as MetaConverter
from .source_inspect import SourceInspect as SourceInspect
from shudaodao_core import AsyncSession as AsyncSession
from shudaodao_meta.generate.entity_table.source_column import (
    SourceColumn as SourceColumn,
)
from shudaodao_meta.generate.entity_table.source_foreign_key import (
    SourceForeignKey as SourceForeignKey,
)
from shudaodao_meta.generate.entity_table.source_index import SourceIndex as SourceIndex
from shudaodao_meta.generate.entity_table.source_primary_key import (
    SourcePrimaryKey as SourcePrimaryKey,
)
from shudaodao_meta.generate.entity_table.source_referencing_foreign_key import (
    SourceReferencingForeignKey as SourceReferencingForeignKey,
)
from shudaodao_meta.generate.entity_table.source_schema import (
    SourceSchema as SourceSchema,
)
from shudaodao_meta.generate.entity_table.source_table import SourceTable as SourceTable
from shudaodao_meta.generate.entity_table.source_view import SourceView as SourceView

class SourceStore:
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
