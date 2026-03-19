from ..meta.entity_class import EntityClass as EntityClass
from ..meta.service import GenericMetaService as GenericMetaService
from _typeshed import Incomplete

class GenericService:
    format_mapping: Incomplete
    @staticmethod
    def get_model_list(request_models, model_class): ...
    @staticmethod
    def get_primary_id(data_model, model_class): ...
    @classmethod
    async def query(cls, *, schema_path, entity_path, query_request): ...
