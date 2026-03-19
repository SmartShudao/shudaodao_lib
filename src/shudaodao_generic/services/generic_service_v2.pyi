from ..meta.entity_class import EntityClass as EntityClass
from ..meta.service import GenericMetaService as GenericMetaService
from .generic_service import GenericService as GenericService
from shudaodao_core import QueryService as QueryService

class GenericServiceV2(GenericService):
    @classmethod
    async def create(cls, create_models, entity_path, schema_path): ...
    @classmethod
    async def update(cls, *, schema_path, entity_path, update_models): ...
    @classmethod
    async def read(cls, *, schema_path, entity_path, read_models): ...
    @classmethod
    async def delete(cls, *, schema_path, entity_path, delete_models): ...
