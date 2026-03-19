from ..generate.entity_table.meta_schema import (
    MetaSchema as MetaSchema,
    MetaSchemaResponse as MetaSchemaResponse,
)
from shudaodao_core import AsyncSession as AsyncSession

class EnumQuery:
    @classmethod
    async def query_schema(cls, *, schema_name, db: AsyncSession): ...
    @classmethod
    async def query_field(cls, *, db: AsyncSession, schema_name, field_name): ...
