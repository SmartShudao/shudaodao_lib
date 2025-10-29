from .gen_convert import GenConverter as GenConverter
from shudaodao_core import AsyncSession as AsyncSession
from shudaodao_meta.generate.entity_table.gen_column import (
    GenColumn as GenColumn,
    GenColumnCreate as GenColumnCreate,
)
from shudaodao_meta.generate.entity_table.gen_schema import GenSchema as GenSchema
from shudaodao_meta.generate.entity_table.gen_table import (
    GenTable as GenTable,
    GenTableCreate as GenTableCreate,
    GenTableUpdate as GenTableUpdate,
)
from shudaodao_meta.generate.entity_table.gen_view import (
    GenView as GenView,
    GenViewCreate as GenViewCreate,
    GenViewUpdate as GenViewUpdate,
)
from shudaodao_meta.generate.entity_table.meta_schema import MetaSchema as MetaSchema

class GenStore:
    auto_commit: bool
    def __init__(self, *, db: AsyncSession = None, schema_name: str = None) -> None: ...
    async def save_sqlmodel(self, db: AsyncSession = None, schema_name: str = None): ...
